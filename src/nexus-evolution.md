# How Nexus Evolves Through This Field Manual

Nexus Engineering Control Plane is the running case study used throughout this field manual.

Nexus starts as an organization where developers use AI coding assistants individually and inconsistently. Across the book, Nexus gradually adds structure: shared vocabulary, bounded agents, repo steering, reusable skills, workflow triggers, hooks, permissions, context boundaries, specs, durable artifacts, verification evidence, tool access, repository layout, decision frameworks, anti-patterns, portability, and maturity assessment.

By the end of the book, Nexus should no longer look like "people using AI tools." It should look like an engineering control plane for governed AI-assisted software delivery.

Every chapter should answer:

> What does Nexus have after this chapter that it did not have before?

## Chapter-by-chapter evolution

| Chapter | Nexus state before | What this chapter adds | Nexus state after | New Nexus asset |
|---|---|---|---|---|
| Why Agentic Engineering Needs Structure | Developers use AI tools individually. Outputs are inconsistent. | The need for structure, governance, repeatability, and artifacts. | Nexus is introduced as a response to uncontrolled AI usage. | Nexus problem statement |
| Core Vocabulary | Teams use terms like agent, skill, tool, memory, and workflow loosely. | Shared language. | Nexus gets a common operating vocabulary. | Vocabulary map |
| Agents | One generic AI assistant is expected to do everything. | Bounded agent roles. | Nexus defines role-specific agents: implementation, review, documentation, and security. | Agent role contract |
| Subagents | Main agents become overloaded. | Delegated isolated workers. | Nexus uses subagents for review, test planning, security checks, and documentation. | Subagent delegation model |
| Steering | Agents do not understand repo rules. | Repository doctrine, rules, and context. | Product repos get `AGENTS.md` files with architecture rules, commands, and boundaries. | Sample repo `AGENTS.md` |
| Skills | Teams repeat the same prompts manually. | Reusable task playbooks. | Nexus creates skills such as `write-adr`, `generate-test-plan`, `review-pr`, and `write-runbook`. | Sample `SKILL.md` |
| Slash Commands | Workflows are hard to trigger consistently. | Standard workflow triggers. | Developers use commands like `/plan-change`, `/review-pr`, and `/create-adr`. | Slash command catalog |
| Hooks | Humans remember guardrails manually. | Lifecycle automation and guardrails. | Nexus adds pre-change, pre-commit, pre-release, and evidence-check hooks. | Hook policy |
| Permissions, Approvals, and Sandboxing | Tool access is too broad or unclear. | Blast-radius control. | Nexus introduces permission tiers and approval rules. | Permission matrix |
| Context and Memory | Teams paste context randomly into chat. | Context boundaries. | Nexus separates repo steering, task context, durable memory, and transient chat. | Context boundary policy |
| Specs, Plans, and Tasks | Agents jump directly into code. | Structured work decomposition. | Nexus requires specs and task plans for risky changes. | Spec/plan/task template |
| Artifacts | Important decisions disappear in chat. | Durable outputs. | Nexus stores ADRs, specs, runbooks, PR evidence, and review notes in repos. | Artifact taxonomy |
| Verification, Tests, Evals, and Checklists | Agents claim work is done without proof. | Evidence and checks. | Nexus requires test output, review checklist, risk notes, and verification evidence. | PR evidence checklist |
| Tooling, MCP, and External Capabilities | Agents cannot safely access external systems. | External capability layer. | Nexus creates a permissioned tool gateway for CI, issue tracker, docs, and deployment metadata. | MCP/tool gateway contract |
| Repo Layout | Every repo organizes AI guidance differently. | Standard repo structure. | Nexus defines common layout for steering, specs, docs, artifacts, and skills. | Repository layout |
| Decision Frameworks | Teams do not know when to use agent vs skill vs tool. | Reusable decision tables. | Nexus creates decision frameworks for workflow design. | Decision framework |
| Anti-Patterns | Teams repeat the same AI mistakes. | Failure library. | Nexus documents god agents, mega-skills, fake verification, context flooding, and tool overreach. | Anti-pattern library |
| Tool Portability | Workflows become tied to one vendor. | Concept/tool separation. | Nexus separates core patterns from Codex, Claude Code, Cursor, Kiro, GitHub, and GitLab specifics. | Portability matrix |
| Team Maturity Model | Adoption is inconsistent across teams. | Maturity ladder. | Nexus becomes a measurable engineering operating model. | Maturity assessment rubric |

## Chapter progression

![Nexus chapter progression](diagrams/generated/nexus-chapter-progression.svg)

## Nexus capability layers

![Nexus capability layers](diagrams/generated/nexus-capability-layers.svg)

## Running workflow example

For the primary running workflow, this field manual uses a backward-compatible API contract change. See [Running Example](./running-example.md).

Chapters should normally reference that canonical page and adapt only the part of the example needed for the chapter.
