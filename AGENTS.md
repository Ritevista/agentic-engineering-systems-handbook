# AGENTS.md

## Repository Intent

This repository contains the mdBook source for **Agentic Engineering Field Manual: Designing Governed AI-Assisted Software Workflows**.

The field manual helps engineering teams move from ad-hoc AI coding experiments to structured, reviewable, reusable, and governable AI-assisted software engineering workflows.

The book is practical, architectural, and reference-oriented. It should help senior developers, staff engineers, architects, platform engineers, and technical leaders make better decisions about agents, skills, steering, tools, permissions, verification, and durable engineering artifacts.

## Audience

Primary audience:

- senior developers
- staff engineers
- software architects
- platform engineers
- technical leads responsible for standardizing AI-assisted engineering workflows

Secondary audience:

- engineering managers
- DevOps/platform leaders
- toolsmiths building internal AI engineering enablement

Do not write this as a beginner AI book, a prompt cookbook, or a vendor-specific tool manual.

## Authoring Rules for Agents

- Keep chapters practical, architectural, and reference-oriented.
- Optimize for field use: examples, decision tables, diagrams, checklists, and reusable templates.
- Do not make the book DevOps-only.
- Use the Nexus Engineering Control Plane case study consistently.
- Where appropriate, use "we" to describe engineering-team decisions, but avoid a casual or promotional tone.
- Keep Markdown compatible with mdBook.
- Do not claim commands were run unless they were actually run.
- Do not write the full book in one pass unless explicitly asked.
- Keep terminology consistent across chapters.
- Important decisions should become artifacts, not remain only in chat.
- When adding new chapters, update `src/SUMMARY.md`.
- When adding diagrams, follow `diagrams/README.md`; it is the source of truth for diagram authoring and publishing.
- Use references for tool-specific claims.
- Prefer official documentation and standards over blogs.
- Do not copy long passages from external sources.
- Paraphrase in original language and link to sources.
- Add `References and Further Reading` to chapters that mention tool-specific behavior.
- Track reused or adapted material in `references/licenses.md`.

## Book Promise

This field manual should help readers answer practical engineering questions such as:

- How do we make a repository agent-ready?
- What belongs in repo steering versus a reusable skill?
- When should a workflow become a slash command?
- When should an external capability become an MCP tool?
- How do we bound agent roles and subagent delegation?
- How do we control blast radius with permissions, approvals, and sandboxing?
- How do we verify agent output before it becomes part of the system of record?
- How do we preserve durable artifacts instead of losing decisions in chat?
- How do we scale from individual AI usage to team-level engineering governance?

## Nexus Evolution Rule

Nexus is the running case study for this field manual. It must evolve cumulatively across chapters.

Every major chapter should answer:

> What does Nexus have after this chapter that it did not have before?

A chapter is weak if the only answer is "better understanding." A strong chapter leaves Nexus with a concrete asset, such as:

- a policy
- a template
- a skill
- a command
- a repository convention
- a verification checklist
- a role contract
- an artifact
- a decision table
- a failure pattern
- a maturity assessment

When adding or editing a chapter, include a Nexus case-study section using this structure where practical:

    ## Nexus case study

    ### Before this chapter

    What was broken or missing in Nexus?

    ### Design decision

    What did Nexus decide to introduce?

    ### Implementation

    What changed in the repo, workflow, skill, command, policy, tool contract, or artifact?

    ### After this chapter

    What new capability does Nexus now have?

    ### Lesson

    What should readers copy into their own organization?

Do not make Nexus decorative. It should function as a running reference implementation for the book.

## Diagram Authoring

Follow `diagrams/README.md` for diagram source, generated SVGs, naming, and regeneration commands. Keep that file as the single source of truth for diagram conventions.

## Chapter Quality Bar

Each major chapter should include, where relevant:

1. The reader problem
2. A precise definition
3. The failure mode without the concept
4. Design principles
5. Boundary with nearby concepts
6. Implementation patterns
7. Minimal examples
8. Nexus Engineering Control Plane example
9. Decision table
10. Anti-patterns
11. Verification guidance
12. Durable artifacts
13. Quick reference

Do not add all sections mechanically if they do not fit, but preserve this field-manual structure whenever possible.

## Chapter Ending Template Rules

For chapters that discuss tools, end with:

```md
## References and Further Reading

- ...
```

For chapters relying heavily on external docs, also include:

```md
## Source Notes

This chapter uses the sources below for tool-specific behavior and terminology. The analysis, decision frameworks, and Nexus Engineering Control Plane examples are original to this field manual.
```

## Concept Distinctions

Preserve these distinctions exactly:

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

## Style Rules

- Prefer concrete engineering language over hype.
- Prefer "workflow," "artifact," "evidence," "boundary," "contract," and "control" over vague agentic language.
- Avoid exaggerated claims about AI autonomy.
- Avoid generic productivity claims unless tied to concrete engineering evidence.
- Avoid vendor lock-in framing.
- Keep examples tool-neutral unless the chapter is explicitly tool-specific.
