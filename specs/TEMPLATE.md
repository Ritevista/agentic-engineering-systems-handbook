# Spec: [short task title]

Delete this line and every instruction line in square brackets once filled in. Nothing in square brackets should survive into a spec handed off for implementation.

## Task type

[One of: new chapter | chapter revision | field-note promotion | bibliography or link fix | structural change (repo layout, AGENTS.md, book-voice.md)]

## Target file(s)

- `src/chapter-NN-....md` [or the actual file(s); list every file this task touches]

## Scope

[What must change, specifically. Name the section(s), the claim, the gap being closed. "Improve chapter 9" is not scope. "Add a subsection to chapter 9 explaining how license gates map to permission tiers" is scope.]

## Out of scope

[What must NOT change in this task even though it is related. If the scope is genuinely ambiguous on some point, say so here rather than silently picking an interpretation.]

## Nexus continuity

[Copy verbatim from the matching row in `src/nexus-evolution.md`. Do not paraphrase or invent. If this task does not touch a chapter with a Nexus row (e.g. a pure link fix), write "N/A -- no chapter content changes."]

- Before: ...
- What this chapter adds: ...
- After: ...
- New Nexus asset: ...

## Required chapter shape

[Delete this section entirely for non-chapter tasks (link fixes, structural changes). For any chapter-content task, this is the shape every finished chapter in this book follows -- see `skills/write-handbook-chapter/SKILL.md` for the full rules behind it. Do not omit a numbered item without stating why in this spec.]

1. Reader problem — one crisp paragraph naming the failure that happens without this concept.
2. What breaks without this / design principle — the boundary or rule this chapter establishes, usually with one definitional table.
3. Implementation pattern(s) specific to the topic, including at least one decision table.
4. Anti-patterns table: pattern, why it fails, better pattern.
5. Nexus case study, with exactly these five subheadings: Before this chapter / Design decision / Implementation / After this chapter / Lesson.
6. Quick Reference: at least one operational table, a "Nexus asset" line, and a "Reader action" line.

## Non-negotiable rules

[These do not change per task. Keep this section as-is; it is here so the implementer does not have to open `AGENTS.md` to find them.]

- No scaffold headings anywhere in `src/`: `Purpose`, `Key Questions`, `Planned Sections`, `Nexus Case Study Connection`, `To be expanded`.
- No chapter-meta Quick Reference rows such as "What does this chapter add?" — Quick Reference must be reader-operational.
- Reference `src/running-example.md`; do not copy the full running-example scenario into a chapter.
- mdBook-safe Markdown: blank lines around headings, tables, lists, and fenced code blocks; every opening fence has a language tag (` ```md `, ` ```yaml `, etc.); the file ends with exactly one trailing newline.
- Terminology matches `AGENTS.md`'s Concept Distinctions table exactly.
- Add a `References and Further Reading` section only if the chapter makes a tool-specific claim; cite real, working links.

## Acceptance criteria

- [ ] All required sections present, or an omission is justified in this spec
- [ ] No scaffold or chapter-meta headings
- [ ] At least one decision table and one anti-pattern table (chapter tasks only)
- [ ] Nexus case study matches the Nexus continuity fields above exactly
- [ ] Markdown fences balanced and language-tagged; file ends with one trailing newline
- [ ] Terminology checked against `AGENTS.md`

## Verification

[What proves this task is done: which command was run (`make check`, `make build`, `make lint`), or, if no local tooling is available, an explicit statement that verification relies on CI and a list of what was self-checked by inspection instead.]
