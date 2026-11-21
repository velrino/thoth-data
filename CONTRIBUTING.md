# Contributing to Thoth Community Data

For the official catalog, fork [velrino/thoth-data](https://github.com/velrino/thoth-data), make your changes on a branch, and open a pull request. For your own public library, commit workspace files under `content/workspaces/` in your fork. The upstream review path applies to official references and studies.

## Prepare the files

Start with a real Thoth export. If the file is a `diagram-export` envelope, save its `workspace` object as `workspace.json`. Use lowercase hyphenated directory IDs. Official entries contain one diagram with its walkthrough steps. Personal workspaces can contain multiple diagrams and folders.

An official entry can use `workspace.excalidraw` as a standalone board with a `title` in its metadata. To add guided Thoth steps, also provide `walkthrough.json` with an empty first step’s `scene.drawing`. Catalog sync imports the board and generates the browser’s `workspace.json`. Use `workspace.json` directly for diagrams authored entirely in Thoth.

Official entries also need `metadata.json` with `schemaVersion: 1`, `type` (`company` or `study`), `groupName`, `pattern`, `summary`, `scope`, and `sources`. Each source has a title and an HTTPS URL. Use the same group name across the workspaces in a company or study group. Credit the original author and cite material that supports specific claims. Keep personal files, credentials, and unreleased information out of public workspaces.

Optional `locales/pt-BR.json` files use `schemaVersion: 1` and can override `title`, `groupName`, `pattern`, `summary`, `scope`, `componentNotes`, and `steps`. Within `steps`, use the exact step ID and include the translated `title`, `description`, or `nodes` and `edges` fields keyed by their IDs. Each translated node or edge can override its `label` and `notes`. Leave unavailable text untranslated so it can fall back to English.

A diagram step can include a `cameraTour` beside `scene`. Add ordered `focus` shots with world coordinates `x` and `z` and a world-unit `span` for framing. Add a `fit` shot to show the complete diagram. Each shot uses `moveMs` for movement and optional `holdMs` for time at the destination. Keep the tour in the source workspace and inspect it in the intended view before publishing.

## Validate and propose a change

```sh
python3 -m pip install -r scripts/requirements.txt
python3 scripts/validate_catalog.py
```

CI runs the data check on pull requests. Open the workspace in Thoth if possible and describe what you verified. The Thoth application also validates the whole candidate when it updates the official snapshot. Provide a small reviewable change, with sources or examples when they help the reviewer.

Contribute original material or material you are authorized to share. Document the applicable terms for any third-party material. A general license for the original catalog content is pending. The repository's public visibility alone does not grant reuse rights.
