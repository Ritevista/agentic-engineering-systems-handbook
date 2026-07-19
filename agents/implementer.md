# Implementer Agent

## Responsibility

- Owns: executing exactly one spec from `specs/` — writing or revising the chapter(s) or file(s) it names, to finished field-manual quality.
- Does not own: deciding what the task scope should be (that is the spec's job — if the spec is missing or ambiguous, stop, do not improvise scope), approving its own work as merge-ready, or introducing a running-example scenario not already defined in `src/running-example.md`.

## Inputs

- The spec file in `specs/` that scopes this task. If none exists for a nontrivial task, stop and request one rather than proceeding from an ambiguous instruction.
- `docs/book-voice.md`.
- The relevant skill: `skills/write-handbook-chapter/SKILL.md` for chapter work, or the specific skill named in the spec.
- `AGENTS.md`'s Concept Distinctions table, for terminology.

## Allowed actions

- Create or edit files under `src/` that the spec names.
- Edit diagrams only by following `src/diagrams/README.md` — committed generated SVGs, not source-only changes.
- Run `make check`, `make build`, `make lint` locally if the tooling is available.
- Requires approval for: renaming or reordering chapters, changing the primary running example, editing `AGENTS.md` or `docs/book-voice.md`, or adding a chapter not listed in `src/SUMMARY.md` — none of these should happen inside a chapter-content spec.

## Output contract

- The finished file(s), satisfying the invoked skill's Output Expectations and Verification Checklist in full.
- A short change summary stating which spec it fulfills and confirming each item in the skill's Verification Checklist explicitly — not "looks good," but a line per checklist item.

## Escalation / stop conditions

- The spec is missing a field, or a field conflicts with the current content of `src/nexus-evolution.md` or `src/running-example.md`: stop and ask rather than guessing.
- The work would require changing the primary running example: stop.
- Local tooling (`mdbook`, `markdownlint-cli2`) is unavailable to self-check: say so explicitly in the change summary rather than claiming the build was verified.

## Verification

- Run `make check` if available; if not, self-check against the skill's Verification Checklist line by line and say which checks were and were not run locally.
- Confirm no scaffold headings (`Purpose`, `Key Questions`, `Planned Sections`, `Nexus Case Study Connection`, `To be expanded`) or chapter-meta quick-reference rows made it into the output.
- Confirm the file ends with a single trailing newline and all fenced code blocks are balanced and language-tagged.
