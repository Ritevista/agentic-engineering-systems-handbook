# ADR-0001: Authoring kit for smaller and cheaper models

## Status

Accepted

## Context

After the v0.1.0 release completed all 21 chapters, a review of the repository's own authoring infrastructure — `AGENTS.md`, `agents/*.md`, `prompts/codex/*.md`, `skills/*` — found it was itself an example of the anti-patterns Chapter 17 catalogs:

- `agents/implementer.md`, `agents/planner.md`, and `agents/reviewer.md` were literal placeholders with no responsibility boundary, no output contract, and no escalation conditions — exactly the unbounded-role failure Chapter 5 warns against.
- `prompts/codex/write-chapter.md` stated a "required chapter structure" that no longer matched the shape every real chapter actually follows (per `docs/book-voice.md` and `skills/write-handbook-chapter/SKILL.md`), and duplicated rather than referenced the skill — a "one concept, one surface" violation.
- There was no bounded task artifact between "an ambiguous request" and "a finished chapter." Every task required synthesizing `AGENTS.md`, `docs/book-voice.md`, `src/nexus-evolution.md`, and `src/running-example.md` from scratch — a burden a smaller or cheaper model handles poorly, since multi-file synthesis under an implicit instruction is exactly where weaker models degrade.
- `skills/write-handbook-chapter/SKILL.md` said to use the target chapter shape "where practical," which is an escape hatch a weaker model is more likely to use to skip a required section than a stronger one is.

## Decision

Apply this book's own Chapter 3 (Steering), Chapter 11 (Specs, Plans, and Tasks), and Chapter 15 (Repo Layout) guidance to the repository itself:

1. Rewrite `agents/implementer.md`, `agents/planner.md`, `agents/reviewer.md` as real role contracts using Chapter 5's shape (responsibility, inputs, allowed actions, output contract, escalation, verification), scoped specifically to book-authoring work.
2. Add `specs/` with `TEMPLATE.md`: a self-contained task-spec format that inlines the required chapter shape and the relevant Nexus continuity fields, so an implementer does not need to open four other files to start.
3. Add `docs/decisions/` for ADRs about the repository itself (this file is the first), separate from `specs/`, which describes in-flight work rather than permanent decisions.
4. Rewrite `prompts/codex/write-chapter.md` and `review-chapter.md` to defer to the corresponding skill file instead of restating a structure that could drift from it.
5. Tighten `skills/write-handbook-chapter/SKILL.md` and `skills/review-handbook-chapter/SKILL.md` into mechanical, checklist-driven procedures with the exact required shape, replacing "where practical" language.
6. Add a Quick-start checklist, a Repository Layout table, and a "Working with Smaller or Cheaper Models" section to `AGENTS.md` itself, plus the Field Notes and Update Cadence process for keeping the book current between full chapter revisions.
7. Add a `Field Notes` section to the appendix as the designated low-bar capture point for observations not yet worth a full chapter change.

## Alternatives considered

- **Leave `AGENTS.md` as a single long prose document and rely on contributors reading all of it carefully.** Rejected: this is exactly the failure mode Chapter 1 describes for prompts — important behavior should not depend on someone reliably holding a large document in working memory. A short, front-loaded checklist plus a self-contained spec per task is more robust to a weaker or more time-constrained contributor.
- **Fragment steering into per-directory `AGENTS.md` files** (e.g. one under `src/`, one under `skills/`). Rejected for now: this repository is a single content tree, not a multi-service monorepo: Chapter 15's layered pattern earns its complexity in multi-repo organizations with real per-repo variation, and adding indirection here would cost more (more files to discover) than it would save.

## Consequences

- Future chapter or structural work should start with a spec in `specs/`, not a bare instruction — this is now stated in `AGENTS.md`'s Quick-start checklist and enforced by the agent role contracts in `agents/`.
- `prompts/codex/write-chapter.md` and `skills/write-handbook-chapter/SKILL.md` must be kept in sync deliberately; the skill is the source of truth if they ever disagree again.
- `docs/decisions/` now exists as a permanent record; future structural changes to this repository (not to chapter content) should add an ADR here rather than only being described in a commit message.
