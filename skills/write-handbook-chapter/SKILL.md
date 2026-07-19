# Skill: write-handbook-chapter

## Name
write-handbook-chapter

## Description
Write one field manual chapter at a time using a consistent architecture-first structure and Nexus-aligned terminology.

## When to Use
- A single chapter needs full drafting from placeholder to substantive content, or a targeted revision.
- The team needs practical guidance with durable decision patterns.

## When Not to Use
- Building initial scaffold placeholders only (use `prompts/codex/scaffold-book.md`).
- Reviewing an existing chapter without rewriting (use `review-handbook-chapter`).

## Procedure

1. Confirm a spec exists at `specs/<task-slug>.md` (`specs/TEMPLATE.md`). If not, stop and write one — do not draft from an unscoped instruction.
2. Read `docs/book-voice.md` and follow it.
3. Align terms with `AGENTS.md`'s Concept Distinctions table exactly.
4. Copy the chapter's Nexus continuity (before / adds / after / asset) verbatim from `src/nexus-evolution.md` — do not invent it.
5. Write the chapter using the **required shape** below. This is not a suggestion; every finished chapter in this book follows it. Omit a numbered item only if the spec states a reason.
6. Add concise, mdBook-safe examples: fenced code blocks, always language-tagged, blank lines around every heading/table/list/fence.
7. Add explicit verification and artifact expectations appropriate to the topic.
8. Update `src/SUMMARY.md` if this is a new chapter.

## Required chapter shape

1. **Reader problem** — one crisp opening naming the failure that happens without this concept. No throat-clearing.
2. **Design principle** (headed `## Design principle: <the one-sentence rule>`) — the boundary or definition this chapter establishes, usually introduced with a short definitional table.
3. **Implementation pattern(s)** specific to the topic — as many `##` sections as the topic needs, each answering one concrete "how" question. Include **at least one decision table** somewhere in this range.
4. **Anti-patterns** — a table: anti-pattern, why it fails, better pattern.
5. **Nexus case study** — exactly these five `###` subheadings, in order: `Before this chapter`, `Design decision`, `Implementation`, `After this chapter`, `Lesson`. `Implementation` should show a concrete artifact (a template, a YAML/Markdown example, a filled-in contract) whenever the chapter's topic produces one.
6. **Quick Reference** — at least one operational table (not a summary of the chapter, a table the reader can use), a `Nexus asset` line naming the concrete artifact this chapter leaves Nexus with, and a `Reader action` line telling the reader what to do with their own team's work right now.

Add `## References and Further Reading` (and `## Source Notes` if the chapter leans on named external sources) only when the chapter makes a tool- or vendor-specific claim. Do not add it otherwise.

## Nexus continuity

Each chapter should advance the Nexus Engineering Control Plane using the exact row from `src/nexus-evolution.md` for that chapter — do not paraphrase the before/after state, copy it.

## Running example

Use the centralized running example from `src/running-example.md` when a concrete scenario helps the chapter. Reference only the relevant part instead of copying the full scenario into every chapter.

Do not introduce a competing primary running example unless `src/running-example.md`, `src/nexus-evolution.md`, Chapter 1, `AGENTS.md`, and related templates are updated together — this is a structural change and needs an ADR in `docs/decisions/`, not a chapter-level spec.

## Public chapter rules

Public chapters must never contain these scaffold headings, anywhere, for any reason:

- Purpose
- Key Questions
- Planned Sections
- Nexus Case Study Connection
- To be expanded
- Any sentence starting with `_Planned:` or containing `Status: in progress`

If planning content is useful, convert it into finished prose, a decision table, a Nexus case study, or Quick Reference content — or leave it in the spec under `specs/`, which is not published.

Quick Reference sections must be reader-operational. Do not include chapter-meta rows such as "What does this chapter add?" or "What is the concrete scenario?"

## Output Expectations
- One complete chapter with practical depth, following the required shape above.
- Consistent terminology.
- At least one decision table and one anti-pattern table.
- Explicit Nexus before/after evolution matching `src/nexus-evolution.md`, with a concrete new asset.
- A Quick Reference section that is operational, not a summary.

## Verification Checklist
- Every numbered item in the required shape is present, or its absence is justified in the spec.
- Terminology matches `AGENTS.md` exactly.
- Nexus case study matches `src/nexus-evolution.md`'s row for this chapter.
- No scaffold headings or `_Planned:` markers anywhere in the file.
- Markdown renders cleanly in mdBook: fences balanced and language-tagged, blank lines around blocks, file ends with one trailing newline.
- If tool-specific claims are made, a References and Further Reading section with real, working links is present.
