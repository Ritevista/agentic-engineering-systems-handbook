## Workflow Snapshot

| Field | Value |
|-------|-------|
| Current Phase | G6 Ship & Learn |
| Next Phase | G6 Ship & Learn |
| Task | Remove related-pattern catalog from Chapter 2 and preserve adjacent-concept placement guidance |

## Gate Status

| Gate | Name | Status | Evidence | Skip Reason |
|------|------|--------|----------|-------------|
| G0 | Discovery | Passed | Inspected Chapter 2, existing appendix catalog, `AGENTS.md` related-pattern guidance, git status, and workflow snapshot. | — |
| G1 | Requirements | Passed | Keep Chapter 2 focused on core vocabulary and control surfaces; replace detailed related-pattern catalog with short adjacent-layer guidance; keep detailed pattern handling in the appendix; add authoring guidance for adjacent concepts. | — |
| G2 | Design | Passed | Edit only Chapter 2, `AGENTS.md`, and workflow evidence. Reuse the existing appendix without expanding it. | — |
| G3 | POC / Spike | N/A | Markdown-only editorial cleanup with no technical unknowns. | — |
| G4 | Implementation | Passed | Replaced Chapter 2's detailed related-pattern catalog with short adjacent-layer guidance and added Adjacent Concepts Rule to `AGENTS.md`. | — |
| G5 | Review | Passed | Confirmed Chapter 2 no longer mentions detailed related-pattern terms; `git diff --check` and `mdbook build` passed. | — |
| G6 | Ship & Learn | In Progress | Summarize changed files and recommended next step. | — |
