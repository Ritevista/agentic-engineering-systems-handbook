# Chapter 2: Core Vocabulary

## Reader problem

Teams cannot govern what they cannot name precisely.

A team cannot govern AI-assisted engineering if it uses one word — "agent" — for every role, workflow, instruction, tool, guardrail, and artifact.

That is not an academic problem. It is an operating problem. Teams fail when every capability is called an agent, every reusable procedure is hidden in a prompt, and every external integration is treated like ordinary context. The result is architecture drift: unclear ownership, misplaced rules, weak review, unsafe tool access, and no shared way to decide where a concern belongs.

Vocabulary defines control surfaces. If the term is vague, the ownership will be vague. If the ownership is vague, governance will be weak.

## Why overloaded language creates weak systems

Overloaded language makes weak systems look simpler than they are.

Calling everything an agent hides the difference between a role, a procedure, a human-facing interaction surface, a workflow trigger, a tool, a connector, a permission boundary, and a durable output. Those differences matter because each one is reviewed, versioned, tested, and governed differently.

| Vocabulary failure | What it causes |
|---|---|
| Unclear ownership | No one knows which role owns the outcome. |
| Misplaced rules | Stable repository doctrine ends up in private prompts. |
| Hidden workflows | Repeated procedures are copied instead of reviewed. |
| Weak review | Reviewers cannot tell which control surface changed. |
| Unsafe tool access | External capabilities are treated as ordinary context. |
| Missing artifacts | Decisions stay in chat instead of the repository. |
| Poor portability | Workflows cannot move across tools because intent and implementation are mixed. |

Bad systems use loose words and compensate with heroics. Good systems separate concerns.

## Design principle: one concept, one control surface

Each primitive in this field manual has a different job in the engineering system.

The point is not to create a glossary. The point is to make work classifiable. Once a team can classify a concern, it can decide where that concern lives, who owns it, how it is reviewed, what evidence proves it worked, and what artifact should survive the session.

One concept should map to one primary control surface.

## Core vocabulary map

| Term | Meaning in this book | Use when | Do not confuse with |
|---|---|---|---|
| Agent | Bounded role | A defined responsibility needs an owner, inputs, allowed actions, and expected outputs. | A tool, prompt, workflow, or unrestricted assistant. |
| Subagent | Isolated delegated worker | A focused review, test, security, documentation, or analysis task should be separated from the main agent. | A second chat window with no boundary or accountability. |
| Steering | Doctrine/rules/context | Stable repository rules, architecture constraints, local commands, ownership, or unsafe areas should guide many tasks. | A reusable task procedure; that belongs in a skill. |
| Skill | Reusable task playbook | A repeated task needs a reviewable procedure, inputs, steps, outputs, and verification expectations. | A private prompt fragment or repository doctrine. |
| Interaction surface | Human-facing entry point | People need a place to invoke, steer, observe, or review agentic work. Examples include chat UI, TUI, CLI, IDE panel, web dashboard, slash command surface, issue comment, and pull request comment. | The agent, workflow, skill, or tool behind the surface. |
| Slash command | Workflow trigger | A team needs a consistent way to start a known workflow. | The full workflow, the skill it invokes, or the agent that executes it. |
| Hook | Lifecycle automation/guardrail | A rule should run at a defined workflow point such as pre-change, pre-commit, pre-PR, or pre-release. | Human review, general verification, or a broad policy document. |
| Tool | Callable capability | An agent, workflow, hook, or human needs to call a shell command, git operation, test runner, browser, CI API, documentation search, ticketing API, schema registry, internal service API, or MCP tool. | The agent role or the connector that exposes the capability. |
| Tool adapter / connector | Safe exposure contract | A callable capability needs a stable interface, input/output contract, permission model, and audit boundary. MCP is one connector/protocol option, not the whole category. | The tool capability itself, the workflow goal, or generic context. |
| Permissions, approvals, and sandboxing | Blast-radius control | Access, execution, write scope, sensitive data, or risky tool use must be limited or approved. | Context, verification, or trust in the assistant. |
| Context and memory | What the agent knows/carries | The agent needs task facts, repository facts, retrieved documents, examples, or durable remembered information. | Tool access, durable artifacts, or unrestricted data ingestion. |
| Specs, plans, and tasks | Work structure | Work needs to be decomposed before execution so scope, sequence, risk, and acceptance criteria are reviewable. | Verification evidence or the implementation itself. |
| Artifacts | Durable outputs | A decision, note, runbook, template, PR evidence record, or other result must survive beyond chat. | Temporary conversation, reasoning, or generated prose with no system of record. |
| Verification | Evidence and checks | The team needs proof that behavior, quality, policy, or acceptance criteria were satisfied. | Confidence, reviewer memory, or an assistant's completion summary. |
| Agent-independent interface | Portable contract | A prompt, skill, command, tool contract, or workflow surface should survive movement across Codex, Claude, Gemini, Kiro, Copilot, or future agent runtimes. | Vendor-specific hidden behavior, private memory, or chat-only output. |
| Tools and connectors | External capability layer | A workflow needs governed access to external systems, APIs, repositories, CI, documentation, metadata, or other capabilities. | The agent role itself, ordinary context, or permission approval. |

This map is deliberately small. It gives the team a way to stop mixing primitives while leaving the detailed contracts to the chapters that own each one.

## Common vocabulary mistakes

Misclassification is not harmless. It puts the right concern in the wrong control surface.

| Mistake | Why it fails | Better classification |
|---|---|---|
| Calling every assistant an agent | It hides role boundaries, ownership, and allowed actions. | Define the agent role, then name any tools, skills, or commands it uses. |
| Calling a repeated prompt a skill before it is reviewable | A private prompt has no stable inputs, procedure, output contract, or verification bar. | Convert it into a skill only when the playbook can be reviewed and reused. |
| Calling the TUI or IDE panel the agent | The human-facing surface is confused with the workflow and role behind it. | Classify the TUI, CLI, IDE panel, chat UI, or dashboard as an interaction surface. |
| Treating a UX prompt as the whole skill | The visible prompt may start or guide work, but it does not define the full procedure, outputs, and checks. | Keep prompt text inside a reviewable skill, command, or workflow contract. |
| Putting repo rules into personal prompts instead of steering | Repository doctrine becomes private habit. | Put stable rules in steering. |
| Treating tool access as context | The assistant may gain capability without permission design. | Classify external capability as tools and connectors, then govern it with permissions. |
| Treating MCP as the entire tool category | One connector/protocol becomes a substitute for naming tools, adapters, schemas, ownership, and permissions. | Treat MCP as one connector option within the broader tools-and-connectors layer. |
| Treating verification as a reviewer's memory | Evidence disappears and claims become hard to audit. | Store tests, checks, checklist results, or review notes as verification evidence. |
| Treating chat as an artifact | Future maintainers cannot rely on private conversation history. | Preserve decisions as ADRs, change notes, PR evidence, templates, or runbooks. |
| Treating a slash command as the workflow itself | The trigger is confused with the procedure and roles behind it. | Use the slash command as the entry point; keep the workflow in skills, agents, checks, and artifacts. |
| Hardcoding workflows to one agent runtime | The workflow cannot move when the team changes assistant, IDE, CLI, or platform. | Define agent-independent interfaces for prompts, skills, commands, tools, and verification artifacts. |
| Using a tool as a synonym for agent | Capability is confused with responsibility. | Treat tools as callable capability; keep agent responsibility in the role contract. |

The correction is usually simple: ask what kind of control surface the concern needs.

## Interaction surfaces are not agents

An interaction surface is the human-facing entry point through which people invoke, steer, observe, or review agentic work. It is not the agent. It is the place where the human meets the workflow.

The same workflow can be exposed through several surfaces: an IDE slash command, a local TUI, a CLI command, a GitHub issue comment, a pull request review command, or a web dashboard approval button. The surface may change by team, repository, or operating model. The workflow contract should remain stable.

That separation matters for governance. A team can improve the UX prompt, move a command from an IDE panel to a CLI, or add a PR-comment trigger without redefining the agent role, skill procedure, tool contract, or verification evidence.

## Tools are capability boundaries

Tools do not own goals. Agents own bounded responsibility. Workflows define sequence and acceptance criteria. Tools expose callable capability.

A tool might be a shell command, git, a test runner, a browser, a CI API, documentation search, a ticketing API, a schema registry, an internal service API, or an MCP tool. A tool adapter or connector exposes that capability safely through a stable contract. MCP is one way to expose tools, but the architecture should not treat MCP as the whole tool category.

Before a tool becomes part of an agentic workflow, answer the governance questions:

| Governance question | Why it matters |
|---|---|
| Who is allowed to call the tool? | Capability should not expand just because a workflow found an integration. |
| Under what approval mode? | Risky calls need human approval, sandboxing, or stricter policy. |
| With what input contract? | Stable schemas make calls reviewable and portable. |
| With what audit trail? | Important observations and actions need a system of record. |
| With what rollback path? | Mutating tools need recovery before they are trusted in workflows. |
| With what verification evidence? | Tool output should support checks, not replace them. |

## Applying the vocabulary to the running example

The primary running example is the [Running Example](./running-example.md): a backward-compatible API contract change.

The table below classifies the parts of that workflow so later chapters can deepen them without changing the language.

| Part of the API contract change | Vocabulary term |
|---|---|
| API conventions, schema/versioning rules, ownership boundaries | Steering |
| Repeatable API-change review workflow | Skill |
| `/plan-api-change` in an IDE, TUI, PR comment, or web dashboard | Interaction surface |
| `/plan-api-change` command contract | Slash command |
| Implementation responsibility | Agent |
| Compatibility and downstream-impact review | Subagent |
| Contract tests and regression checks | Verification |
| ADR or change note | Artifact |
| Schema diff, test runner, CI status API, documentation search | Tool |
| MCP server, REST wrapper, internal gateway, repo script | Tool adapter / connector |
| Stable command, skill, and tool contract usable across Codex, Claude, Gemini, Kiro, or Copilot | Agent-independent interface |
| Sensitive payload or client usage access | Permissions / approvals / sandboxing |
| Task brief, examples, known clients, compatibility assumptions | Context and memory |
| Spec, implementation plan, task list | Specs, plans, and tasks |

This is the chapter's practical test. If the team cannot classify the API change without calling every part "the agent," the workflow is not designed yet.

## Adjacent concepts belong in the right layer

The vocabulary in this chapter is the field manual's core vocabulary. It names the control surfaces we use throughout the book: roles, rules, workflows, guardrails, tools, evidence, and durable outputs.

Other agentic patterns, prompting techniques, guardrail libraries, and interoperability protocols are useful. But they should enter the book at the layer where they help.

A reasoning pattern belongs in the agent chapter.

A prompt-programming framework belongs near skills and verification.

A scanner or guardrail library belongs near permissions, context boundaries, and safety.

An interoperability protocol belongs near tools, connectors, MCP, and portability.

Do not flatten all of these into one glossary. A team gets better structure when each concept is placed where it affects engineering behavior.

This chapter defines the book's core terms. Later chapters and the [appendix](./appendix-agentic-patterns-and-protocols.md) connect those terms to adjacent methods, tools, and protocols.

## Nexus case study

### Before this chapter

Nexus Software Systems has accepted that AI-assisted engineering needs more structure, but teams still use overloaded language. Developers call prompts agents, checklists skills, tool access context, and completion summaries verification.

That language makes review harder. A reviewer cannot tell whether a proposed change modifies a role, a procedure, a tool, a permission boundary, or an artifact expectation.

### Design decision

Nexus Engineering Control Plane defines a small vocabulary with hard boundaries.

The decision is intentionally narrow: Nexus does not try to standardize every agentic pattern in the industry. It standardizes the control surfaces its teams need to design governed AI-assisted workflows.

Nexus also decides that interaction surfaces can vary by team. One team may invoke the API-change workflow through an IDE command. Another may use a local TUI, a CLI, a pull request comment, or a dashboard approval button. Those surfaces can differ without changing the underlying workflow contract.

The workflow contract must remain portable across agent runtimes. Nexus prefers reviewable skill files, stable command contracts, explicit tool input/output schemas, durable verification artifacts, and portable workflow triggers over vendor-specific hidden behavior, private memory, or chat-only summaries.

### Implementation

Nexus introduces the `Nexus vocabulary map`.

`nexus-service`, `nexus-delivery`, and `nexus-playbook` use the same vocabulary when designing AI-assisted workflows. A concern must be classified as steering, skill, interaction surface, slash command, agent, subagent, hook, tool, connector, permission control, context/memory, specs/plans/tasks, artifact, verification, or agent-independent interface before the team decides where it lives.

For external capability, Nexus routes tool access through explicit adapters and connectors. MCP is one connector option. It is not the vocabulary category itself. A schema diff, test runner, CI status API, documentation search, ticketing API, or internal service API is named as a tool first, then exposed through a governed connector.

### After this chapter

Nexus can now classify whether a concern belongs in steering, a skill, an interaction surface, an agent contract, a tool contract, a connector, a permission rule, verification evidence, a portable interface, or a durable artifact.

The organization is not fully mature yet. It has gained a shared vocabulary map. That is enough to make the next chapters reviewable.

### Lesson

Naming is governance.

Unclear terms produce unclear systems. Clear vocabulary lets teams assign ownership, review the right surface, and preserve the right artifact.

## Quick Reference

| If the team asks... | Use this term | Why |
|---|---|---|
| Who owns this bounded responsibility? | Agent | It defines role, scope, inputs, actions, and outputs. |
| Who should perform isolated delegated work? | Subagent | It separates focused review or analysis from the main agent. |
| Where do stable repository rules belong? | Steering | It keeps doctrine, rules, and context visible to the repo. |
| Where does a repeated procedure belong? | Skill | It turns a repeated task into a reviewable playbook. |
| Where does the human invoke or review the workflow? | Interaction surface | It names the human-facing entry point without confusing it with the workflow or agent. |
| How should a known workflow start? | Slash command | It provides a consistent trigger, not the whole workflow. |
| What should run at a lifecycle point? | Hook | It automates or guards a specific workflow boundary. |
| What callable capability is being used? | Tool | It separates capability from agent responsibility. |
| How is the capability exposed safely? | Tool adapter / connector | It gives the capability a stable contract, permission model, and audit boundary. |
| What limits risky access or execution? | Permissions, approvals, and sandboxing | It controls blast radius before capability expands. |
| What information does the agent know or carry? | Context and memory | It distinguishes task input from tools and artifacts. |
| How should work be decomposed before execution? | Specs, plans, and tasks | It makes scope, sequence, and acceptance criteria reviewable. |
| What must survive beyond chat? | Artifacts | It preserves decisions, evidence, templates, and operational knowledge. |
| What proves the work is acceptable? | Verification | It turns claims into evidence and checks. |
| Can this workflow survive a change of agent runtime? | Agent-independent interface | It preserves prompts, skills, commands, tool contracts, and workflow surfaces across assistants. |
| What external capability layer is being governed? | Tools and connectors | It separates system access from the agent role while keeping MCP as one connector option. |

### Chapter asset

`Nexus vocabulary map`

### Reader action

Take one AI-assisted workflow your team already performs and classify each part using the vocabulary in this chapter. If everything is called "the agent," the workflow is not yet designed.
