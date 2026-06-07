# Diagram Authoring

This directory is the source of truth for diagram authoring in the field manual.

## Repository Layout

- `src/` stores diagram source files.
  - Use `.mmd` for simple Mermaid diagrams.
  - Use `.d2` for structured architecture, capability-layer, and progression diagrams where layout control matters.
- `generated/` stores rendered SVG files committed for mdBook publishing.

Published chapters should embed generated SVGs with normal Markdown image syntax:

```md
![Diagram title](diagrams/generated/example.svg)
```

## Authoring Rules

- Prefer Mermaid for simple lifecycle, sequence, and one-idea flow diagrams.
- Prefer D2 for architecture maps, capability-layer diagrams, progression maps, and diagrams that need stable published composition.
- Prefer generated SVG for published diagrams.
- Do not fight Mermaid layout for editorial diagrams; move those diagrams to D2.
- Keep diagrams focused, with short labels and one main idea.
- Avoid complex custom styling unless necessary.
- Store reusable source diagrams under `diagrams/src/`.
- Store generated diagrams under `diagrams/generated/`.

## Regenerating Diagrams

Required tool:

- Mermaid CLI, available as `mmdc`
- D2, available as `d2`

If D2 is not installed, install it from the official D2 release script or package manager before regenerating `.d2` sources. For a temporary local install:

```bash
curl -fsSL https://d2lang.com/install.sh -o /tmp/d2-install.sh
sh /tmp/d2-install.sh --prefix /tmp/d2
export PATH=/tmp/d2/bin:$PATH
```

Run all commands from `src/diagrams/` or adjust paths accordingly.

Regenerate a single diagram:

```bash
mmdc -i src/reference-architecture.mmd -o generated/reference-architecture.svg
d2 src/nexus-capability-layers.d2 generated/nexus-capability-layers.svg
d2 src/steering-layers.d2 generated/steering-layers.svg
```

Regenerate all Mermaid diagrams:

```bash
for source in src/*.mmd; do
  name="$(basename "$source" .mmd)"
  mmdc -i "$source" -o "generated/$name.svg"
done
```

Regenerate all D2 diagrams:

```bash
for source in src/*.d2; do
  name="$(basename "$source" .d2)"
  d2 "$source" "generated/$name.svg"
done
```

Review generated diagrams locally with `mdbook serve` from the repo root. Because `diagrams/` is inside `src/`, mdBook includes the SVGs automatically — no manual copy step is needed.
