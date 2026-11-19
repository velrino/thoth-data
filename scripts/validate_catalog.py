"""Validate catalog source files against the portable Thoth contract."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
MAX_BYTES = 2 * 1024 * 1024
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
TEXT_LIMITS = {
    "title": 100,
    "groupName": 100,
    "pattern": 100,
    "summary": 500,
    "scope": 2000,
    "author": 100,
}


def read_json(path):
    if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_BYTES:
        raise ValueError(f"Invalid or oversized catalog file: {path}")
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def folders(path):
    if not path.exists():
        return []
    if not path.is_dir() or path.is_symlink():
        raise ValueError(f"Invalid catalog directory: {path}")
    result = []
    for child in sorted(path.iterdir()):
        if child.is_symlink():
            raise ValueError(f"Symlinks are not allowed: {child}")
        if child.is_dir():
            if len(child.name) > 80 or not SLUG.fullmatch(child.name):
                raise ValueError(f"Invalid catalog ID: {child}")
            result.append(child)
    return result


def nested_diagrams(entries):
    for entry in entries:
        if entry["kind"] == "folder":
            yield from nested_diagrams(entry["children"])
        else:
            yield entry


def text(fields, field, maximum, required=False):
    if field not in fields and not required:
        return
    value = fields.get(field)
    if not isinstance(value, str) or len(value.encode("utf-16-le")) // 2 > maximum:
        raise ValueError(f"Invalid text field: {field}")
    if field in {"title", "groupName", "pattern", "summary"} and not value.strip():
        raise ValueError(f"Empty text field: {field}")


def keys(value, accepted):
    if not isinstance(value, dict) or not value.keys() <= set(accepted):
        raise ValueError("Unexpected catalog fields")


def notes(value, step_list):
    node_ids = {node["id"] for step in step_list for node in step["scene"]["nodes"]}
    keys(value, node_ids)
    for key in value:
        text(value, key, 1000)


def metadata(path, step_list):
    value = read_json(path)
    allowed = {"schemaVersion", "groupName", "pattern", "summary", "scope", "author",
               "sources", "componentNotes", "showConnectionLabels"}
    keys(value, allowed)
    if value.get("schemaVersion") != 1:
        raise ValueError("Unsupported metadata schemaVersion")
    for field, limit in TEXT_LIMITS.items():
        if field != "title":
            text(value, field, limit, required=field != "author")
    sources = value.get("sources")
    if not isinstance(sources, list) or len(sources) > 25:
        raise ValueError("Invalid source list")
    for item in sources:
        keys(item, {"title", "url"})
        text(item, "title", 100, required=True)
        text(item, "url", 2048, required=True)
        address = urlsplit(item["url"])
        if address.scheme != "https" or not address.hostname:
            raise ValueError("Use HTTPS URLs for sources")
    if "showConnectionLabels" in value and not isinstance(value["showConnectionLabels"], bool):
        raise ValueError("showConnectionLabels must be a boolean")
    notes(value.get("componentNotes", {}), step_list)
    return value["groupName"]


def translation(path, step_list):
    if not path.exists() and not path.is_symlink():
        return
    if path.parent.is_symlink():
        raise ValueError("Locale directories cannot be symlinks")
    value = read_json(path)
    keys(value, (TEXT_LIMITS.keys() - {"author"}) | {"schemaVersion", "componentNotes", "steps"})
    if value.get("schemaVersion") != 1:
        raise ValueError("Unsupported translation schemaVersion")
    for field, limit in TEXT_LIMITS.items():
        text(value, field, limit)
    notes(value.get("componentNotes", {}), step_list)
    steps = {step["id"]: step for step in step_list}
    overrides = value.get("steps", {})
    keys(overrides, steps)
    for step_id, fields in overrides.items():
        keys(fields, {"title", "description", "nodes", "edges"})
        text(fields, "title", 100)
        text(fields, "description", 2000)
        for section, limit in (("nodes", 150), ("edges", 80)):
            labels = fields.get(section, {})
            keys(labels, {item["id"] for item in steps[step_id]["scene"][section]})
            for item in labels.values():
                keys(item, {"label", "notes"})
                text(item, "label", limit)
                text(item, "notes", 1000)


def validate():
    schema = read_json(ROOT / "schemas" / "workspace.schema.json")
    validator = Draft202012Validator(schema)
    checked = 0
    routes = set()
    official = []
    for section in ("public", "studies"):
        for group in folders(CONTENT / section):
            group_name = None
            for folder in folders(group):
                route = ("studies" if section == "studies" else group.name, folder.name)
                if route in routes or (section == "public" and group.name == "studies"):
                    raise ValueError(f"Conflicting official route: {route}")
                routes.add(route)
                official.append((group, folder))
    all_folders = [folder for _, folder in official] + folders(CONTENT / "workspaces")
    official_folders = dict((folder, group) for group, folder in official)
    group_names = {}
    for folder in all_folders:
        try:
            workspace = read_json(folder / "workspace.json")
            error = next(validator.iter_errors(workspace), None)
            if error:
                raise ValueError(f"Workspace schema violation at {error.json_path}")
            diagrams = list(nested_diagrams(workspace["entries"]))
            if not diagrams:
                raise ValueError("A published workspace needs at least one diagram")
            if folder in official_folders:
                if len(diagrams) != 1:
                    raise ValueError("An official workspace needs exactly one diagram")
                steps = diagrams[0]["steps"]
                name = metadata(folder / "metadata.json", steps)
                group = official_folders[folder]
                if group_names.setdefault(group, name) != name:
                    raise ValueError("Inconsistent catalog group name")
                translation(folder / "locales" / "pt-BR.json", steps)
            checked += 1
        except (ValueError, OSError) as error:
            raise ValueError(f"{folder.relative_to(ROOT)}: {error}") from error
    print(f"Validated {checked} workspace files.")


if __name__ == "__main__":
    try:
        validate()
    except (ValueError, OSError) as error:
        print(error, file=sys.stderr)
        sys.exit(1)
