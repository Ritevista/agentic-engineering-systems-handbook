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
2. Align terms with repository concept distinctions.
3. Identify the chapter's Nexus evolution asset: what Nexus lacked before, what decision it makes, and what concrete asset it has afterward.
4. Draft content in this exact structure:
   1. What the primitive means
   2. Why it exists
   3. What problem it solves
   4. How it differs from nearby primitives
   5. Where it should live
   6. Nexus case study
   7. Good patterns
   8. Anti-patterns
   9. Decision table
   10. Quick reference summary
5. Add concise, mdBook-safe examples.
6. Add explicit verification and artifact expectations.
7. Update related references if needed.

## Nexus continuity

Each chapter should advance the Nexus Engineering Control Plane.

The chapter should explicitly show:

1. what Nexus lacked before this concept
2. what design decision Nexus made
3. what concrete asset Nexus introduced
4. how that asset changes daily engineering behavior
5. what readers can reuse in their own teams

## Running example

Use the centralized running example from `src/running-example.md` when a concrete scenario helps the chapter. Reference only the relevant part of the example instead of copying the full scenario into every chapter.

Do not introduce a competing primary running example unless `src/running-example.md`, `src/nexus-evolution.md`, Chapter 1, `AGENTS.md`, and related templates are updated together.

## Output Expectations
- One complete chapter with practical depth.
- Consistent terminology.
- At least one decision table.
- Clear verification guidance and durable artifact outcomes.
- Explicit Nexus before/after evolution with a concrete new asset.

## Verification Checklist
- Structure follows required 10-part sequence.
- Terminology matches AGENTS.md distinctions.
- Nexus case study is present and coherent.
- Nexus leaves the chapter with a concrete policy, template, skill, command, convention, checklist, contract, artifact, decision table, failure pattern, or maturity assessment.
- Markdown renders cleanly in mdBook.
- Anti-patterns and verification are included.
