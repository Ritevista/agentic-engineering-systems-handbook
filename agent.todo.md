## Workflow Snapshot

| Field | Value |
|-------|-------|
| Current Phase | G6 Ship & Learn |
| Next Phase | G6 Ship & Learn |
| Task | Remove internal running-example guidance from published book content |

## Gate Status

| Gate | Name | Status | Evidence | Skip Reason |
|------|------|--------|----------|-------------|
| G0 | Discovery | Passed | Searched for service rollout, payment retry, idempotency, and running-example references; inspected `src/SUMMARY.md`, `src/nexus-evolution.md`, Chapter 1, `AGENTS.md`, and `skills/write-handbook-chapter/SKILL.md`. | — |
| G1 | Requirements | Passed | Remove internal avoid-term and maintenance-checklist guidance from published `src/` content while preserving it in repo authoring guidance. | — |
| G2 | Design | Passed | Keep `src/running-example.md` reader-facing; keep operational instructions in `AGENTS.md` and `skills/write-handbook-chapter/SKILL.md`. | — |
| G3 | POC / Spike | N/A | Markdown-only content cleanup with no implementation unknowns. | — |
| G4 | Implementation | Passed | Removed the avoid-term list and maintenance checklist from `src/running-example.md`; removed secondary-example terms from `src/nexus-evolution.md`; reinforced private authoring guidance. | — |
| G5 | Review | Passed | Targeted scan confirms avoid-term phrases now appear only in `AGENTS.md`, not published `src/` content; `git diff --check`, `mdbook build`, and `polyagentctl gate-check agent.todo.md` passed. | — |
| G6 | Ship & Learn | In Progress | Summarize changed files and verification results. | — |
