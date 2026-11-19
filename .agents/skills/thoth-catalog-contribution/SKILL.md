---
name: thoth-catalog-contribution
description: Add, revise, translate, or review Thoth workspace JSON in the official catalog or a personal fork. Use for diagram data, metadata, locale overlays, stable addresses, and contribution preparation.
---

# Contribute to the Thoth catalog

Read [CONTRIBUTING.md](../../../CONTRIBUTING.md) before editing. Confirm whether the destination is the official catalog or the owner's fork.

1. Place an official reference at `content/public/<company>/<workspace>/workspace.json`, a study at `content/studies/<topic>/<workspace>/workspace.json`, or a personal publication at `content/workspaces/<workspace>/workspace.json`. Keep existing folder, lesson, step, node, and edge IDs stable when revising a published diagram.
2. Use the workspace for the English title, steps, scene, and connections. Use adjacent `metadata.json` for the card summary, pattern, provenance, and component explanations. Update its sources for factual claims. Describe simplified behavior as an illustration and label invented metrics accordingly.
3. Put Brazilian Portuguese overrides in adjacent `locales/pt-BR.json`. Translate the affected fields and reference existing step, node, and edge IDs. Keep geometry, roles, and flow configuration in the source workspace.
4. Run `python3 scripts/validate_catalog.py` with the dependency in `scripts/requirements.txt`. Open the workspace in Thoth and inspect the touched steps, arrow directions, labels, and any translations on a narrow viewport when practical. Report which checks ran in the pull request.
5. Submit only the intended workspace files and related metadata or translations. Thoth generates its published indexes from these sources. Repository visibility, GitHub authorization, commits, pushes, and merges follow the contributor's explicit instructions.
