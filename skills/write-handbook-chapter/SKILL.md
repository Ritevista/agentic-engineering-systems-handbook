# Skill: write-handbook-chapter

## Name
write-handbook-chapter

## Description
Write one field manual chapter at a time using a consistent architecture-first structure and Nexus-aligned terminology.

## When to Use
- A single chapter needs full drafting from placeholder to substantive content.
- The team needs practical guidance with durable decision patterns.

## When Not to Use
- Building initial scaffold placeholders only.
- Reviewing an existing chapter without rewriting.

## Procedure
1. Confirm target chapter path and chapter objective.
2. Read and follow `docs/book-voice.md`.
3. Align terms with repository concept distinctions.
4. Identify the chapter's Nexus evolution asset: what Nexus lacked before, what decision it makes, and what concrete asset it has afterward.
5. Draft public chapters as finished field-manual guidance, not planning notes.
6. Use this shape where practical:
   1. Reader problem
   2. What breaks without this
   3. Design principle
   4. Implementation pattern
   5. Nexus case study
   6. Quick Reference
7. Add concise, mdBook-safe examples.
8. Add explicit verification and artifact expectations.
9. Update related references if needed.

## Nexus continuity

Each chapter should advance the Nexus Engineering Control Plane.

Expected early Nexus asset sequence:

1. Chapter 1 -> Nexus problem statement
2. Chapter 2 -> Nexus vocabulary map
3. Chapter 3 Steering -> sample repo `AGENTS.md`
4. Chapter 4 Skills -> sample `SKILL.md`
5. Chapter 5 Agents -> implementation-agent role contract
6. Chapter 6 Subagents -> subagent delegation model
7. Chapter 7 Slash Commands -> slash command catalog

The chapter should explicitly show:

1. what Nexus lacked before this concept
2. what design decision Nexus made
3. what concrete asset Nexus introduced
4. how that asset changes daily engineering behavior
5. what readers can reuse in their own teams

## Running example

Use the centralized running example from `src/running-example.md` when a concrete scenario helps the chapter. Reference only the relevant part of the example instead of copying the full scenario into every chapter.

Do not introduce a competing primary running example unless `src/running-example.md`, `src/nexus-evolution.md`, Chapter 1, `AGENTS.md`, and related templates are updated together.

Do not publish internal running-example maintenance guidance or avoid-term lists in chapter content. Keep that material in repo authoring guidance.

Do not copy the full running scenario into every chapter. Reference the canonical page and adapt only the part needed for the chapter.

## Public chapter rules

Public chapters must not expose scaffold headings such as:

- Purpose
- Key Questions
- Planned Sections
- Nexus Case Study Connection
- To be expanded

If planning content is useful, convert it into finished prose, a decision table, a Nexus case study, or Quick Reference content.

Keep Markdown mdBook-compatible with blank lines around headings, tables, lists, and fenced blocks.

Quick Reference sections must be reader-operational. Do not include chapter-meta rows such as "What does this chapter add?", "What is the concrete scenario?", or other authoring rationale.

During review, inspect `src/` as the source of truth and rebuild with `mdbook build` before evaluating generated `book/` output.

## Output Expectations
- One complete chapter with practical depth.
- Consistent terminology.
- At least one decision table.
- Clear verification guidance and durable artifact outcomes.
- Explicit Nexus before/after evolution with a concrete new asset.
- A Quick Reference section.

## Verification Checklist
- Structure follows the field-manual shape requested for the chapter.
- Terminology matches AGENTS.md distinctions.
- Nexus case study is present and coherent.
- Nexus leaves the chapter with a concrete policy, template, skill, command, convention, checklist, contract, artifact, decision table, failure pattern, or maturity assessment.
- Markdown renders cleanly in mdBook.
- Anti-patterns and verification are included where they fit the chapter scope.
