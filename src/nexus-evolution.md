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

Use this example throughout the field manual where a concrete scenario is needed:

**Service rollout configuration change**

A developer asks AI to update how a service is configured for rollout in `nexus-service`.

In the ad-hoc state, the assistant may produce a plausible patch: change a timeout, update a Helm value, modify a deployment setting, or adjust a pipeline step. But without structure, the change may miss environment-specific constraints, rollback behavior, deployment verification, ownership rules, or operational documentation.

As Nexus matures, this same change moves through repository steering, planning, reusable skills, subagent review, permission controls, durable artifacts, and verification evidence.

| Chapter area | Service rollout configuration example |
|---|---|
| Structure | The change is treated as a governed workflow, not a casual prompt. |
| Vocabulary | The team separates agent, skill, artifact, verification, permission, and tool. |
| Agent | An implementation agent owns the bounded configuration change. |
| Subagent | A review subagent checks rollout risk, rollback behavior, and environment assumptions. |
| Steering | `AGENTS.md` defines service ownership, deployment rules, safe files, and test commands. |
| Skill | A rollout test-plan skill generates validation, rollback, and environment checks. |
| Slash command | `/plan-rollout-change` starts the standard workflow. |
| Hook | A PR evidence hook blocks incomplete rollout submissions. |
| Permissions | Access to deployment metadata or environment-specific configuration requires approval. |
| Context | Sensitive environment details are bounded and not stored casually. |
| Specs/plans/tasks | The rollout change becomes a short spec, implementation plan, and task list. |
| Artifacts | An ADR or change note captures why the rollout behavior changed. |
| Verification | The PR includes CI results, dry-run output, rollout risk notes, rollback notes, and review evidence. |
| Tools/MCP | The tool gateway exposes CI status, issue metadata, and safe deployment metadata. |
| Repo layout | Specs, ADRs, runbooks, and PR evidence are stored consistently. |
| Decisions | A decision table explains why this became a governed workflow, not just a prompt. |
| Anti-patterns | Failure case: the agent changes rollout configuration without checking environment-specific behavior or rollback impact. |
| Portability | The same workflow maps across different coding-agent tools. |
| Maturity | The team moves from ad-hoc AI usage toward governed engineering practice. |
