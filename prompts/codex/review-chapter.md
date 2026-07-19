# Review Chapter Prompt Template

Review chapter `<chapter-path>` and provide actionable feedback.

Follow `skills/review-handbook-chapter/SKILL.md` — this is the canonical procedure and output shape. This prompt does not restate it.

If a spec exists at `specs/<task-slug>.md` for the change under review, check the chapter against the spec's scope and acceptance criteria first, before general quality review.

Evaluate:

- Clarity
- Consistency with `docs/book-voice.md`
- Practical usefulness
- Nexus case study continuity against `src/nexus-evolution.md`
- Terminology consistency against `AGENTS.md`'s Concept Distinctions table
- mdBook compatibility (fence balance, language tags, trailing newline, blank lines around blocks)
- Decision-table and anti-pattern-table quality
- Missing verification guidance
- No scaffold headings or chapter-meta Quick Reference rows

Output format: use the exact shape in `skills/review-handbook-chapter/SKILL.md`'s Output Expectations — strengths, ranked gaps with rationale, terminology corrections, mdBook concerns, and an explicit merge-readiness recommendation (yes/no, with reasons). Cite specific sections, not general impressions.
