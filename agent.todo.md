## Workflow Snapshot

| Field | Value |
|-------|-------|
| Current Phase | Complete |
| Next Phase | None |
| Task | Add concrete working-location steering examples to Chapter 3 |

## Gate Status

| Gate | Name | Status | Evidence | Skip Reason |
|------|------|--------|----------|-------------|
| G0 | Discovery | Passed | Inspected the Steering chapter section layout, existing worktree/testbed content, Quick Reference, and current git state. | — |
| G1 | Requirements | Passed | Add targeted examples for repository root, module directory, Git worktree, dev container/local sandbox, testbed, and session prompt steering without rewriting the chapter. | — |
| G2 | Design | Passed | Insert examples into the existing repositories/worktrees/testbeds section, add a placement decision table before Quick Reference content, and extend Quick Reference with working-location and testbed rules. | — |
| G3 | POC / Spike | N/A | Markdown-only chapter patch with no technical unknowns. | — |
| G4 | Implementation | Passed | Added working-location table, starting-directory example, worktree-local example, testbed example, decision table, and Quick Reference rules. | — |
| G5 | Review | Passed | Reviewed inserted sections for fence integrity and no secret examples; `git diff --check`, `mdbook build`, and `polyagentctl gate-check agent.todo.md` passed. | — |
| G6 | Ship & Learn | Passed | Final response summarizes changed files, examples added, assumptions, and recommended next step. | — |
