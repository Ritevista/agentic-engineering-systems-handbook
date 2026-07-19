# Skill: review-handbook-chapter

## Name
review-handbook-chapter

## Description
Review a drafted chapter for technical clarity, consistency, practical value, and governance completeness against this book's required shape.

## When to Use
- A chapter draft exists and needs quality review before merge.
- Terminology drift or case study drift is suspected.

## When Not to Use
- No chapter draft exists.
- Task is to create initial scaffold placeholders.

## Procedure

1. If a spec exists at `specs/<task-slug>.md` for this change, check the chapter against its scope and acceptance criteria first.
2. Check the chapter against the **required shape checklist** below — this is mechanical, do it before anything else.
3. Read the chapter and its immediate neighbors for terminology consistency against `AGENTS.md`'s Concept Distinctions table.
4. Validate Nexus case study continuity: does `Before this chapter` / `Design decision` / `Implementation` / `After this chapter` / `Lesson` match the row in `src/nexus-evolution.md`?
5. Evaluate examples, decision tables, anti-pattern tables, and verification guidance for whether they are operational (a reader can use them) versus decorative (they restate the prose).
6. Produce prioritized, actionable feedback in the Output Expectations shape below.

## Required shape checklist

Run through this in order; note every failure with a line number or section name:

- [ ] No scaffold headings (`Purpose`, `Key Questions`, `Planned Sections`, `Nexus Case Study Connection`, `To be expanded`)
- [ ] No `_Planned:` markers or `Status: in progress` banners
- [ ] Reader problem opens the chapter directly, no throat-clearing
- [ ] A `## Design principle: ...` section states the chapter's one-sentence rule
- [ ] At least one decision table outside the Quick Reference
- [ ] An Anti-patterns table: pattern / why it fails / better pattern
- [ ] Nexus case study has exactly the five subheadings, in order, matching `src/nexus-evolution.md`
- [ ] Quick Reference has at least one operational table, a `Nexus asset` line, and a `Reader action` line
- [ ] Quick Reference contains no chapter-meta rows ("What does this chapter add?")
- [ ] Every fenced code block is language-tagged; fences are balanced; file ends with one trailing newline
- [ ] `References and Further Reading` present if the chapter makes a tool-specific claim, absent if it does not

## Output Expectations
- Result of the required-shape checklist above, pass/fail per item.
- Clear strengths and gaps, each citing a specific section or line range — not a general impression.
- Ranked list of edits with rationale, high-priority first.
- Explicit terminology corrections against `AGENTS.md`.
- Merge readiness recommendation: yes/no, with reasons.

## Verification Checklist
- Feedback references specific sections, not general impressions.
- Terminology alignment checked against `AGENTS.md`.
- mdBook formatting concerns flagged (fence tags, blank lines, trailing newline).
- Nexus continuity checked against `src/nexus-evolution.md`, not just internal consistency.
- Missing verification or artifact guidance identified.
- Decision-table and anti-pattern-table quality evaluated for whether they are operational.
- State which checks were run against real command output (build, lint) versus read-only inspection.
