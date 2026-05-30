# Diagram Authoring

This directory is the source of truth for diagram authoring in the field manual.

## Repository Layout

- `src/` stores diagram source files.
  - Use `.mmd` for simple Mermaid diagrams.
  - Use `.d2` for structured architecture, capability-layer, and progression diagrams where layout control matters.
- `generated/` stores rendered SVG files committed for mdBook publishing.

Published chapters should embed generated SVGs with normal Markdown image syntax:

```md
![Diagram title](../diagrams/generated/example.svg)
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

Regenerate a single diagram:

```bash
mmdc -p diagrams/puppeteer-config.json -i diagrams/src/reference-architecture.mmd -o diagrams/generated/reference-architecture.svg
d2 diagrams/src/nexus-capability-layers.d2 diagrams/generated/nexus-capability-layers.svg
```

Regenerate all Mermaid diagrams:

```bash
for source in diagrams/src/*.mmd; do
  name="$(basename "$source" .mmd)"
  mmdc -p diagrams/puppeteer-config.json -i "$source" -o "diagrams/generated/$name.svg"
done
```

Regenerate all D2 diagrams:

```bash
for source in diagrams/src/*.d2; do
  name="$(basename "$source" .d2)"
  d2 "$source" "diagrams/generated/$name.svg"
done
```

Review generated diagrams locally:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000/diagrams/generated/nexus-chapter-progression.svg
http://localhost:8000/diagrams/generated/nexus-capability-layers.svg
```

After regenerating diagrams, run:

```bash
mdbook build
mkdir -p book/diagrams
cp -R diagrams/generated book/diagrams/
```

The GitHub Pages workflow runs the same copy step after `mdbook build` so generated SVGs are included in the published artifact.
