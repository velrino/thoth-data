# Thoth Community Data

`velrino/thoth-data` is the default official catalog repository for Thoth, an interactive tool for building, animating, and sharing architecture diagrams. This public repository gives people a place to inspect diagram JSON, review changes in Git, and propose additions or corrections. [Open Thoth](https://thoth.velrino.co/)

The catalog includes **Public References**, which explain real systems and cite their sources, and **Studies**, which teach or compare software concepts. A fork can also hold workspaces published by its owner.

## Contribute to the official catalog

1. [Fork this repository](https://github.com/velrino/thoth-data/fork) and create a branch in your fork.
2. Create or update a diagram in Thoth and export the workspace as JSON. Save the exported `workspace` object as `workspace.json` in the appropriate folder under `content/public/`.
3. Keep the workspace folder ID stable when updating an existing diagram. Put card metadata, attribution, and source links in `metadata.json`. If you include a Brazilian Portuguese translation, put it in `locales/pt-BR.json`.
4. Open a pull request against `velrino/thoth-data`. Explain what the diagram teaches or what your change corrects. Reviewed changes become eligible for inclusion in the official catalog.

## Publish workspaces in your own fork

1. [Fork this repository](https://github.com/velrino/thoth-data/fork) into your GitHub account.
2. Export a workspace from Thoth and add its `workspace` object to your fork at `content/workspaces/<workspace-id>/workspace.json`. Commit each version you want to publish. Review the exported file before committing, since anyone can read a public fork.
3. When GitHub linking is available in Thoth, connect that fork to your account. Thoth will use `content/workspaces/` for your public library. The official examples inherited by the fork stay in their own folders.
4. Keep personal workspace changes in your fork. Open an upstream pull request when you want to propose a diagram for the official catalog.

## Content layout

```text
content/
├── public/
│   └── <company-or-topic-id>/<workspace-id>/
│       ├── workspace.json
│       ├── metadata.json
│       └── locales/pt-BR.json
└── workspaces/
    └── <workspace-id>/
        └── workspace.json
```

Every workspace uses the same filename and Thoth's portable JSON format. The workspace contains the blocks, connections, walkthrough steps, and source text in English (`en-US`). Metadata stores fields the workspace format does not already provide, such as the card summary and source links. Optional locale files contain translations keyed by stable IDs. Missing translations fall back to the English text.

Thoth will generate the catalog indexes from these files. Titles and step counts come from the workspace so edits stay in sync with what readers see on the card.

## Catalog sources

Thoth will start with this repository as the default official source. The same layout is intended to work in any compatible repository. If Thoth adds more official catalogs, users will be able to choose which ones to browse. A workspace is identified by its repository and its stable path, so different catalogs can use the same workspace ID. A Git commit SHA identifies the exact version a reader is viewing.

Official catalog selection and personal fork linking serve different purposes. Choosing an official catalog changes what you browse in Explore. Linking your fork identifies where your own public workspaces are published.

## Contribution guides

Use the [contribution guide](CONTRIBUTING.md) for file formats and validation. When using an AI assistant, point it to [AGENTS.md](AGENTS.md) or give it the [catalog contribution skill](.agents/skills/thoth-catalog-contribution/SKILL.md). The instructions work from a regular checkout and require no assistant-specific runtime.

## Project status

The official references and studies are available in this repository. You can fork the content, propose changes by PR, and track public workspace versions in Git today. Thoth can use the catalog snapshot in builds that include the integration. The account connection and publishing flow require a configured GitHub App.
