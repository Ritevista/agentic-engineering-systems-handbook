# AGENTS.md

## Repository Intent
This repository contains an mdBook handbook scaffold for **Agentic Engineering Systems**. Contributions should preserve a practical, architectural, and reference-oriented tone.

## Authoring Rules for Agents
- Keep chapters practical, architectural, and reference-oriented.
- Use the Nexus Engineering Control Plane case study consistently.
- Do not make the book DevOps-only.
- Prefer clear examples, decision tables, diagrams, and reusable mental models.
- Keep Markdown compatible with mdBook.
- Do not claim commands were run unless they were actually run.
- Do not write the full book in one pass unless explicitly asked.
- Keep terminology consistent across chapters.
- Important decisions should become artifacts, not remain only in chat.
- When adding new chapters, update `src/SUMMARY.md`.
- When adding diagrams, prefer Mermaid-compatible `.mmd` files.
- Use references for tool-specific claims.
- Prefer official documentation and standards over blogs.
- Do not copy long passages from external sources.
- Paraphrase in original language and link to sources.
- Add "References and Further Reading" to chapters that mention tool-specific behavior.
- Track reused/adapted material in `references/licenses.md`.

## Chapter Ending Template Rules
For chapters that discuss tools, end with:

```md
## References and Further Reading

- ...
```

For chapters relying heavily on external docs, also include:

```md
## Source Notes

This chapter uses the sources below for tool-specific behavior and terminology. The analysis, decision frameworks, and Nexus Engineering Control Plane examples are original to this handbook.
```

## Concept Distinctions (Preserve Exactly)
- steering = doctrine/rules/context
- skill = reusable task playbook
- slash command = workflow trigger
- agent = bounded role
- subagent = isolated delegated worker
- hook = lifecycle automation/guardrail
- permissions/approvals/sandboxing = blast-radius control
- context/memory = what the agent knows/carries
- specs/plans/tasks = work structure
- artifacts = durable outputs
- verification = evidence and checks
- MCP/tools = external capability layer
