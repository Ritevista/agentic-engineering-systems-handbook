## Workflow Snapshot

| Field | Value |
|-------|-------|
| Current Phase | G6 Ship & Learn |
| Next Phase | G6 Ship & Learn |
| Task | Centralize the primary running example as backward-compatible API contract change |

## Gate Status

| Gate | Name | Status | Evidence | Skip Reason |
|------|------|--------|----------|-------------|
| G0 | Discovery | Passed | Searched for service rollout, payment retry, idempotency, and running-example references; inspected `src/SUMMARY.md`, `src/nexus-evolution.md`, Chapter 1, `AGENTS.md`, and `skills/write-handbook-chapter/SKILL.md`. | — |
| G1 | Requirements | Passed | Make backward-compatible API contract change the current primary running example and centralize it as a reusable book-level asset. | — |
| G2 | Design | Passed | Add `src/running-example.md` as canonical source; link it from `SUMMARY`; update Nexus evolution, Chapter 1, AGENTS, and chapter-writing skill to reference the canonical asset. | — |
| G3 | POC / Spike | N/A | Markdown-only placeholder update with no implementation unknowns. | — |
| G4 | Implementation | Passed | Added canonical running-example page and updated `SUMMARY`, Nexus evolution, Chapter 1, `AGENTS.md`, and chapter-writing skill guidance. | — |
| G5 | Review | Passed | Targeted scan confirms old examples are secondary or avoid-as-primary terms only; `mdbook build`, `git diff --check`, and `polyagentctl check --strict --project .` passed. | — |
| G6 | Ship & Learn | In Progress | Summarize changed files and recommended next step. | — |
