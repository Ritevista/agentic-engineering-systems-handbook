# Write Chapter Prompt Template

Write or revise exactly one field manual chapter for this repository.

Before using this prompt, a spec should exist at `specs/<task-slug>.md` (see `specs/README.md` and `specs/TEMPLATE.md`). If one does not exist for this task, write it first — do not start from an ambiguous instruction.

Inputs:

- The spec at `specs/<task-slug>.md`.
- Chapter file path: `<chapter-path>`.
- `docs/book-voice.md`.
- `skills/write-handbook-chapter/SKILL.md` — this is the canonical procedure and required shape. This prompt does not restate it; follow the skill directly rather than a paraphrase of it, so the two never drift apart.

Requirements:

- Follow the spec's scope exactly. Do not widen or narrow it without flagging the change.
- Follow `docs/book-voice.md` for tone.
- Use the Nexus Engineering Control Plane case study, with the exact Before/Design decision/Implementation/After/Lesson continuity the spec copied from `src/nexus-evolution.md`.
- Use mdBook-compatible Markdown: blank lines around headings, tables, lists, and fenced code blocks; every fence language-tagged; file ends with one trailing newline.
- Include at least one decision table and one anti-pattern table.
- Include verification and durable-artifact guidance appropriate to the topic.
- Do not publish scaffold headings (`Purpose`, `Key Questions`, `Planned Sections`, `Nexus Case Study Connection`, `To be expanded`) or chapter-meta Quick Reference rows.
- Reference `src/running-example.md`; adapt only the part needed, do not copy the full scenario.

When done, self-check against `skills/write-handbook-chapter/SKILL.md`'s Verification Checklist line by line and report the result — do not report only "done."
