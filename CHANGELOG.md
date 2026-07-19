# Changelog

All notable changes to this field manual are recorded here. Versioning follows [Semantic Versioning](https://semver.org/): the major/minor number reflects the book's structural completeness and stability, not a page count.

## [0.1.1] - 2026-07-19

Authoring-infrastructure release. No chapter content changed; this release applies the book's own Chapter 3, 11, and 15 guidance (steering, specs, and repo layout) to the repository's own authoring process, so future work — including work handed to smaller or cheaper models — is easier to scope correctly and to verify mechanically.

### Added

- `agents/implementer.md`, `agents/planner.md`, `agents/reviewer.md` rewritten as real Chapter-5-style role contracts (responsibility, inputs, allowed actions, output contract, escalation, verification), replacing generic placeholders.
- `specs/` directory: a self-contained task-spec template (`specs/TEMPLATE.md`) so a nontrivial authoring task can be handed off as one bounded brief instead of requiring multi-file synthesis of `AGENTS.md`, `docs/book-voice.md`, `src/nexus-evolution.md`, and `src/running-example.md`.
- `docs/decisions/` directory: an ADR template and ADR-0001, documenting this restructuring itself.
- `scripts/check-no-scaffolding.py`: a fence-aware check that fails if `src/` contains planning-scaffold headings or `_Planned:`/`Status: in progress` markers outside of legitimate fenced code examples. Wired into CI as a new `scaffold-guard` job and into `make check` as `scaffold-check`.
- `.github/workflows/scheduled-link-check.yml`: a monthly link check independent of content changes, to catch link rot between chapter edits, matching the new Field Notes review cadence.
- A `Field Notes` section at the bottom of the appendix: a low-bar, dated capture point for observations not yet worth a full chapter revision, with a promotion rule documented in `AGENTS.md`.
- CI status badges in `README.md`.

### Changed

- `AGENTS.md`: added a Quick-start checklist, a Repository Layout table for `specs/`, `docs/decisions/`, `agents/`, and `prompts/codex/`, a "Working with Smaller or Cheaper Models" section, and a Field Notes and Update Cadence section.
- `prompts/codex/write-chapter.md` and `review-chapter.md` now defer to `skills/write-handbook-chapter/SKILL.md` and `skills/review-handbook-chapter/SKILL.md` instead of restating a chapter structure that had drifted from what the skills (and every real chapter) actually specify.
- `skills/write-handbook-chapter/SKILL.md` and `skills/review-handbook-chapter/SKILL.md` tightened into mechanical, checklist-driven procedures with the exact required chapter shape, replacing "where practical" language.

## [0.1.0] - 2026-07-19

Initial complete release.

### Added

- All 21 chapters, the introduction, and the appendix as finished field-manual guidance. Fourteen chapters (Subagents, Slash Commands, Hooks, Specs/Plans/Tasks, Artifacts, Verification, Incident Response and Rollback, Repo Layout, Decision Frameworks, Anti-Patterns, Tooling/MCP, Tool Portability, Metrics/Cost/Spend Governance, Team Maturity Model) moved from in-progress skeletons to complete chapters, each following the book's standard shape: reader problem, design principle, implementation pattern, decision tables, Nexus case study, anti-patterns, and a quick reference.
- Closed two remaining internal planning notes in Chapter 3 (Steering) and Chapter 9 (Permissions, Approvals, and Sandboxing) that referenced not-yet-written content.

### Changed

- `src/SUMMARY.md` no longer marks any chapter `(in progress)`.
- README project status section rewritten to reflect a complete v0.1.0 release instead of an in-progress source tree.

## Prior history

Chapters 1-5, 9, and 10, the introduction, the appendix, and the Nexus running-example infrastructure were written and iteratively revised before this changelog began. See the git history for that detail.
