# AGENTS.md

## Quick-start checklist

Do these in order for any content task. This checklist is intentionally self-sufficient — if you only read this section, you can still do the task correctly.

1. **Find or write the spec.** Nontrivial work (a chapter revision, a new chapter, a structural change) should have a spec at `specs/<task-slug>.md`. If none exists, write one from `specs/TEMPLATE.md` before touching `src/`. A one-line link or typo fix does not need a spec.
2. **Use the skill, not your own judgment about structure.** For chapter work, follow `skills/write-handbook-chapter/SKILL.md` exactly — it names the required shape. Do not improvise a different chapter structure.
3. **Copy Nexus continuity, do not invent it.** Every chapter's before/after state and its new Nexus asset come from `src/nexus-evolution.md`. If your change isn't in that table, stop and ask before proceeding.
4. **Never publish scaffolding.** No `Purpose` / `Key Questions` / `Planned Sections` / `Nexus Case Study Connection` / `To be expanded` headings, and no `_Planned:` markers, in anything under `src/`.
5. **Check terminology against the Concept Distinctions table** (below) before using any primitive name.
6. **Run the real checks before claiming done**: `make check` and `make build` if the tooling is available in your environment; if it is not, say so explicitly rather than asserting the build passed. CI (`Content quality` workflow) runs markdownlint, an mdBook build, and a lychee link check on every push — it is the source of truth if you cannot run these locally.
7. **Leave the working tree clean**: no stray spec files for finished work (delete a spec once its task is merged, per `specs/README.md`), no debug output committed.

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
- When adding diagrams, follow `src/diagrams/README.md`; it is the source of truth for diagram authoring and publishing.
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

## Book Voice Rule

Use the repository's Book Voice Contract in `docs/book-voice.md` when writing or editing chapters.

The book should use the author's published thinking style, not casual chat style.

That means:

- direct
- practical
- architectural
- systems-oriented
- evidence-oriented
- slightly adversarial toward weak engineering practices
- free of hype and filler

Do not imitate typos, casual phrasing, or exploratory chat language.

When in doubt, write like a senior architect producing a field manual for other senior engineers.

## Chapter Order Rule

The early chapters should follow the maturity flow:

1. Why structure is needed
2. Core vocabulary
3. Steering
4. Skills
5. Agents
6. Subagents
7. Slash commands

Reasoning:

- Chapter 1 moves the reader from L0/L1 toward L2 repository steering.
- Chapter 2 stabilizes the vocabulary.
- Steering comes before skills because reusable workflows need repo rules, local commands, and architecture constraints.
- Skills come before agents because repeated workflows should become reusable task playbooks before assigning execution roles.
- Agents come before subagents because delegation only makes sense after the main role is bounded.

Do not reorder these casually. If the order changes, update `src/SUMMARY.md`, `src/nexus-evolution.md`, diagram sources, and chapter-writing guidance together.

## Public Chapter Rule

Public chapters should not expose internal planning scaffold sections such as:

- Purpose
- Key Questions
- Planned Sections
- To be expanded
- Nexus Case Study Connection

If these sections contain useful content, convert them into finished prose, quick-reference sections, or move them into authoring guidance.

Public quick-reference sections should be operational for the reader. Do not publish chapter-meta rows such as "What does this chapter add?", "What is the concrete scenario?", or other authoring rationale.

When checking published content, treat `src/` as the source of truth. The generated `book/` directory can be stale until `mdbook build` is run.

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

Follow `src/diagrams/README.md` for diagram source, generated SVGs, naming, and regeneration commands. Keep that file as the single source of truth for diagram conventions.

## Repository Layout for Authoring Work

This repository applies its own Chapter 15 (Repo Layout), Chapter 11 (Specs, Plans, and Tasks), and Chapter 12 (Artifacts) guidance to itself:

| Concern | Location | Purpose |
|---|---|---|
| Book content | `src/` | The published field manual. Source of truth for readers. |
| Repository steering | `AGENTS.md` (this file) | Doctrine for anyone — human or model — authoring in this repo. |
| Voice and tone | `docs/book-voice.md` | How chapters should sound. |
| Reusable authoring procedures | `skills/` | `write-handbook-chapter`, `review-handbook-chapter`, `create-decision-table`. |
| Bounded authoring roles | `agents/` | Role contracts for planner, implementer, and reviewer work on this repo, following Chapter 5's own shape. |
| In-flight task specs | `specs/` | One spec per nontrivial task; see `specs/README.md`. Deleted once the task is merged. |
| Durable decisions about the repo itself | `docs/decisions/` | ADRs for structural changes — repo layout, workflow, running example. Not for chapter content decisions; those live in the chapter's own Nexus case study. |
| Ready-to-run task prompts | `prompts/codex/` | Thin wrappers that point to the skill; they do not restate it. |

Do not duplicate a rule across two of these locations. If `prompts/codex/write-chapter.md` and `skills/write-handbook-chapter/SKILL.md` ever say different things about chapter structure, the skill wins — fix the prompt, not the other way around.

## Working with Smaller or Cheaper Models

Do not assume every contributor — human or model — will hold this entire file, `docs/book-voice.md`, `src/nexus-evolution.md`, and `src/running-example.md` in working memory at once. A smaller or cheaper model in particular will do better with less synthesis and more explicit, bounded input.

- Prefer handing off one self-contained spec (`specs/TEMPLATE.md`, filled in) over a bare instruction. The spec should inline the Nexus continuity fields and the required shape so the implementer does not have to cross-reference four files to start.
- Prefer the checklist-style Verification Checklists in `skills/write-handbook-chapter/SKILL.md` and `skills/review-handbook-chapter/SKILL.md` over open-ended "review for quality" instructions — a checklist a weak model can execute mechanically is more reliable than judgment it may not consistently apply.
- Keep each task scoped to one chapter or one clearly bounded change. Do not ask for multi-chapter consistency passes in one unscoped instruction; split them into one spec per chapter instead.
- When in doubt about whether an instruction is explicit enough for a weaker model to follow without guessing, tighten it — this repository would rather have a slightly longer checklist than a rule that depends on inference.

## Quality Gates

Before raising a PR that changes book content, Markdown guidance, diagrams, or CI, run the relevant local checks:

- `make check`
- `make serve`

Use the local serve check to confirm the generated book can be viewed in a browser before publishing a PR. Stop the server after verification unless the user asks to keep it running.

GitHub Actions must keep the same quality surface:

- Markdown linting with `markdownlint-cli2`
- mdBook build validation
- source and generated HTML link checking

The generated `book/` directory is build output. Do not commit it unless the repository publishing model changes explicitly.

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

## Related Patterns and Protocols Rule

Related agent patterns, prompting techniques, guardrail tools, and interoperability protocols should support the book's core primitives, not replace them.

Do not flatten BMAD, GSD, DSPy, LLM Guard, ReAct, Plan-and-Execute, BDI, zero-shot, few-shot, CoT, self-consistency, meta-prompting, MCP, A2A, AP2, UCP, and AG-UI into one undifferentiated glossary.

Classify them by layer:

- methodology/workflow framework
- prompt/program standardization
- guardrail/boundary component
- reasoning/orchestration pattern
- prompting technique
- interoperability protocol

Core chapters should stay focused on durable engineering primitives. Appendices may catalog related methods, tools, and protocols.

## Adjacent Concepts Rule

Do not dump external AI patterns, prompting techniques, protocols, or tools into core vocabulary chapters.

Place them where they affect engineering behavior:

- reasoning patterns go in agent/orchestration chapters
- prompt/programming frameworks go near skills and verification
- guardrail libraries go near permissions, context boundaries, and safety
- interoperability protocols go near tools, MCP, and portability
- methodology frameworks go in appendices or adoption/maturity chapters

Chapter 2 should define the book's core vocabulary only.

## Field Notes and Update Cadence

The field this book covers moves fast — vendor surfaces, protocol versions, and adoption patterns change on a shorter cycle than a chapter revision does. This section defines how the book stays current without forcing every observation into a full chapter rewrite immediately.

**Capture first, promote later.** When something new or changed is worth recording — a protocol version bump, a new vendor surface, a pattern seen repeatedly in practice — add a dated entry to the `Field Notes` section at the bottom of `src/appendix-agentic-patterns-and-protocols.md`. A field note is terse and does not need the chapter quality bar; it is explicitly exempt from the no-planning-notes rule elsewhere in this document, because it is published, dated, working material by design, not a scaffold.

**Promotion criterion.** A field note graduates into real chapter or appendix-table content when it becomes load-bearing: it would change a decision table, it contradicts something a chapter currently asserts, or it has recurred enough times to be more than a one-off observation. Until then, it stays a field note. Promotion follows the normal path: write a spec (`specs/TEMPLATE.md`), then use `skills/write-handbook-chapter/SKILL.md` or `skills/create-decision-table/SKILL.md` as appropriate.

**Cadence.** Review the Field Notes list on a recurring basis — monthly is a reasonable default, mirroring the governance review cadence Chapter 20 recommends for Nexus itself. A review either promotes a note, deletes it as no longer relevant, or leaves it for next time. A note that has sat unreviewed for multiple cycles is a sign the cadence isn't being followed, not a sign nothing changed.

**Versioning.** Record every meaningful change in `CHANGELOG.md`, per [Semantic Versioning](https://semver.org/): a patch bump (0.1.x) for link fixes, corrections, and authoring-infrastructure changes that do not alter chapter content; a minor bump (0.x.0) when a field note is promoted or a chapter changes meaningfully; a major bump only for a structural change to the book itself (a new primary running example, a reordered chapter sequence).

## Running Example Rule

The current primary running example is **Backward-compatible API contract change**.

Treat the running example as a centralized book-level asset, not scattered prose.

The canonical source is `src/running-example.md`.

When writing chapters:

- reference the running example only where it clarifies the chapter concept
- adapt only the relevant part of the example
- avoid copying the full scenario into every chapter
- do not introduce a competing primary running example without updating `src/running-example.md`
- payment retry, service rollout configuration, dependency upgrade, and authorization changes may be used as secondary examples when they fit a specific chapter
- Avoid using these as primary running-example terms in published chapters: "payment retry policy change", "payment retry and idempotency policy change", "duplicate charges", "sensitive payment logs", "service rollout configuration change", "rollout timeout", "Helm value", and "deployment setting".
- Keep running-example maintenance checklists in repo guidance such as `AGENTS.md` or authoring skills, not in published `src/` content.

## Running Example Change Checklist

If the primary running example changes later, update:

1. `src/running-example.md`
2. `src/nexus-evolution.md`
3. Chapter 1 Nexus case-study micro-story
4. `AGENTS.md`
5. chapter-writing skills/templates
6. any `examples/nexus/` artifacts that depend on the old example

## Style Rules

- Prefer concrete engineering language over hype.
- Prefer "workflow," "artifact," "evidence," "boundary," "contract," and "control" over vague agentic language.
- Avoid exaggerated claims about AI autonomy.
- Avoid generic productivity claims unless tied to concrete engineering evidence.
- Avoid vendor lock-in framing.
- Keep examples tool-neutral unless the chapter is explicitly tool-specific.
