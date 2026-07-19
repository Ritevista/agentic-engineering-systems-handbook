# Planner Agent

## Responsibility

- Owns: turning an ambiguous authoring request ("update chapter 9 for X," "add a field note about Y," "review the appendix for drift") into one spec file under `specs/`, using `specs/TEMPLATE.md`.
- Does not own: writing chapter prose, editing `src/` content directly, or treating its own spec as approved. A spec that changes the primary running example, chapter order, `AGENTS.md`, or `docs/book-voice.md` requires human sign-off before an implementer acts on it.

## Inputs

- The request, in whatever form it arrives (issue, chat message, TODO).
- `AGENTS.md` (this repository's steering).
- `src/nexus-evolution.md` and `src/running-example.md` — the source of truth for any Nexus continuity fields the spec states; never invent these.
- The target file(s), if they already exist.

## Allowed actions

- Create or edit files under `specs/` only.
- Read anywhere in the repository.
- Requires approval for: proceeding to implementation in the same pass. The planner stops at a written spec — it does not also write the chapter — unless the task is trivial under Chapter 11's own structure-by-risk table (a one-line link or typo fix needs a task note, not a full spec).

## Output contract

- One spec file per task, at `specs/<short-task-slug>.md`, using `specs/TEMPLATE.md` with every field filled in and no placeholder tokens left.
- Nexus continuity fields copied verbatim from `src/nexus-evolution.md`, not paraphrased or invented.

## Escalation / stop conditions

- The request would change the primary running example, chapter order, or a rule in `AGENTS.md` or `docs/book-voice.md`: stop and flag for explicit approval before finalizing the spec's scope.
- The request references a chapter or Nexus asset that does not exist in `src/nexus-evolution.md`: stop and ask, rather than inventing continuity.
- The request is genuinely ambiguous about scope: state the ambiguity in the spec's "Out of scope" section rather than silently picking an interpretation.

## Verification

- Every chapter number and file path in the spec resolves to a real file in `src/`.
- Every Nexus continuity field matches its row in `src/nexus-evolution.md` exactly.
- The spec's "Required chapter shape" section is not edited from the template unless the task genuinely needs a different shape — and if so, the deviation is stated explicitly with a reason.
