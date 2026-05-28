# Write Chapter Prompt Template

Write exactly one field manual chapter for this repository.

Inputs:
- Chapter file path: `<chapter-path>`
- Chapter title: `<chapter-title>`
- Primary primitive: `<primitive>`
- Audience: senior developers, staff engineers, architects, platform engineers, and technical leads

Requirements:
- Keep a practical, architectural, reference-oriented tone.
- Use the Nexus Engineering Control Plane case study throughout.
- Show what Nexus lacked before the chapter and what concrete asset Nexus gains after the chapter.
- Use mdBook-compatible Markdown.
- Include concise examples and at least one decision table.
- Include verification and artifact guidance.

Required chapter structure:
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

Nexus continuity:
- what Nexus lacked before this concept
- what design decision Nexus made
- what concrete asset Nexus introduced
- how that asset changes daily engineering behavior
- what readers can reuse in their own teams
