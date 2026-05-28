# Diagram Authoring

This directory is the source of truth for diagram authoring in the field manual.

## Repository Layout

- `src/` stores Mermaid source files.
- `generated/` stores rendered SVG files committed for mdBook publishing.

Published chapters should embed generated SVGs with normal Markdown image syntax:

```md
![Diagram title](../diagrams/generated/example.svg)
```

## Authoring Rules

- Prefer Mermaid for source diagrams.
- Prefer generated SVG for published diagrams.
- Use `flowchart LR` for evolution and lifecycle diagrams.
- Use `flowchart TB` for architecture and layer diagrams.
- Keep diagrams focused, with short labels and one main idea.
- Avoid complex custom styling unless necessary.
- Store reusable source diagrams under `diagrams/src/`.
- Store generated diagrams under `diagrams/generated/`.

## Regenerating Diagrams

Required tool:

- Mermaid CLI, available as `mmdc`

Regenerate a single diagram:

```bash
mmdc -p diagrams/puppeteer-config.json -i diagrams/src/reference-architecture.mmd -o diagrams/generated/reference-architecture.svg
```

Regenerate all diagrams:

```bash
for source in diagrams/src/*.mmd; do
  name="$(basename "$source" .mmd)"
  mmdc -p diagrams/puppeteer-config.json -i "$source" -o "diagrams/generated/$name.svg"
done
```

After regenerating diagrams, run:

```bash
mdbook build
mkdir -p book/diagrams
cp -R diagrams/generated book/diagrams/
```

The GitHub Pages workflow runs the same copy step after `mdbook build` so generated SVGs are included in the published artifact.
