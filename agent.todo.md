## Workflow Snapshot

| Field | Value |
|-------|-------|
| Current Phase | G6 Ship & Learn |
| Next Phase | G6 Ship & Learn |
| Task | Fix mdBook diagram rendering with generated SVGs |

## Gate Status

| Gate | Name | Status | Evidence | Skip Reason |
|------|------|--------|----------|-------------|
| G0 | Discovery | Passed | Generated HTML showed Mermaid fences emitted as `<code class="language-mermaid">` blocks; mdBook had no Mermaid preprocessor or static diagram generation. | — |
| G1 | Requirements | Passed | Diagrams should render visually in the GitHub Pages mdBook and future diagram conventions should have one source of truth. | — |
| G2 | Design | Passed | Use committed SVGs generated from Mermaid sources under `diagrams/src/`; document conventions in `diagrams/README.md`. | — |
| G3 | POC / Spike | N/A | No high-risk implementation unknowns identified. | — |
| G4 | Implementation | Passed | `src/introduction.md`, `src/nexus-evolution.md`, `diagrams/src/`, `diagrams/generated/`, `diagrams/README.md`, `AGENTS.md`, `.github/workflows/pages.yml` | — |
| G5 | Review | Passed | `mmdc`, `mdbook build`, generated asset copy, `git diff --check`, `polyagentctl check --strict --project /home/svc_wsl/dev/projects/agentic-engineering-systems-handbook`, no Mermaid code blocks in built book, generated SVG image links present. | — |
| G6 | Ship & Learn | In Progress | Amend local unpushed commit, push to `main`, sync `master`. | — |
