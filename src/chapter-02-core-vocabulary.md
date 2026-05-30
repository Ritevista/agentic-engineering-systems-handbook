# Chapter 2: Core Vocabulary

## Reader problem

Teams cannot govern what they cannot name precisely.

A team cannot govern AI-assisted engineering if it uses one word — "agent" — for every role, workflow, instruction, tool, guardrail, and artifact.

That is not an academic problem. It is an operating problem. Teams fail when every capability is called an agent, every reusable procedure is hidden in a prompt, and every external integration is treated like ordinary context. The result is architecture drift: unclear ownership, misplaced rules, weak review, unsafe tool access, and no shared way to decide where a concern belongs.

Vocabulary defines control surfaces. If the term is vague, the ownership will be vague. If the ownership is vague, governance will be weak.

## Why overloaded language creates weak systems

Overloaded language makes weak systems look simpler than they are.

Calling everything an agent hides the difference between a role, a procedure, a workflow trigger, a permission boundary, a tool, and a durable output. Those differences matter because each one is reviewed, versioned, tested, and governed differently.

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
| Slash command | Workflow trigger | A team needs a consistent way to start a known workflow. | The full workflow, the skill it invokes, or the agent that executes it. |
| Hook | Lifecycle automation/guardrail | A rule should run at a defined workflow point such as pre-change, pre-commit, pre-PR, or pre-release. | Human review, general verification, or a broad policy document. |
| Permissions, approvals, and sandboxing | Blast-radius control | Access, execution, write scope, sensitive data, or risky tool use must be limited or approved. | Context, verification, or trust in the assistant. |
| Context and memory | What the agent knows/carries | The agent needs task facts, repository facts, retrieved documents, examples, or durable remembered information. | Tool access, durable artifacts, or unrestricted data ingestion. |
| Specs, plans, and tasks | Work structure | Work needs to be decomposed before execution so scope, sequence, risk, and acceptance criteria are reviewable. | Verification evidence or the implementation itself. |
| Artifacts | Durable outputs | A decision, note, runbook, template, PR evidence record, or other result must survive beyond chat. | Temporary conversation, reasoning, or generated prose with no system of record. |
| Verification | Evidence and checks | The team needs proof that behavior, quality, policy, or acceptance criteria were satisfied. | Confidence, reviewer memory, or an assistant's completion summary. |
| MCP/tools | External capability layer | An agent needs governed access to external systems, APIs, repositories, CI, documentation, metadata, or other capabilities. | The agent role itself, ordinary context, or permission approval. |

This map is deliberately small. It gives the team a way to stop mixing primitives while leaving the detailed contracts to the chapters that own each one.

## Common vocabulary mistakes

Misclassification is not harmless. It puts the right concern in the wrong control surface.

| Mistake | Why it fails | Better classification |
|---|---|---|
| Calling every assistant an agent | It hides role boundaries, ownership, and allowed actions. | Define the agent role, then name any tools, skills, or commands it uses. |
| Calling a repeated prompt a skill before it is reviewable | A private prompt has no stable inputs, procedure, output contract, or verification bar. | Convert it into a skill only when the playbook can be reviewed and reused. |
| Putting repo rules into personal prompts instead of steering | Repository doctrine becomes private habit. | Put stable rules in steering. |
| Treating tool access as context | The assistant may gain capability without permission design. | Classify external capability as MCP/tool and govern it with permissions. |
| Treating verification as a reviewer's memory | Evidence disappears and claims become hard to audit. | Store tests, checks, checklist results, or review notes as verification evidence. |
| Treating chat as an artifact | Future maintainers cannot rely on private conversation history. | Preserve decisions as ADRs, change notes, PR evidence, templates, or runbooks. |
| Treating a slash command as the workflow itself | The trigger is confused with the procedure and roles behind it. | Use the slash command as the entry point; keep the workflow in skills, agents, checks, and artifacts. |
| Using MCP/tool as a synonym for agent | Capability is confused with responsibility. | Treat MCP/tools as external capability; keep agent responsibility in the role contract. |

The correction is usually simple: ask what kind of control surface the concern needs.

## Applying the vocabulary to the running example

The primary running example is the [Running Example](./running-example.md): a backward-compatible API contract change.

The table below classifies the parts of that workflow so later chapters can deepen them without changing the language.

| Part of the API contract change | Vocabulary term |
|---|---|
| API conventions, schema/versioning rules, ownership boundaries | Steering |
| Repeatable API-change review workflow | Skill |
| `/plan-api-change` entry point | Slash command |
| Implementation responsibility | Agent |
| Compatibility and downstream-impact review | Subagent |
| Contract tests and regression checks | Verification |
| ADR or change note | Artifact |
| API docs, CI status, schema metadata, safe usage metadata | MCP/tool |
| Sensitive payload or client usage access | Permissions / approvals / sandboxing |
| Task brief, examples, known clients, compatibility assumptions | Context and memory |
| Spec, implementation plan, task list | Specs, plans, and tasks |

This is the chapter's practical test. If the team cannot classify the API change without calling every part "the agent," the workflow is not designed yet.

## Related patterns are not core primitives

Related patterns and protocols can support the field manual's primitives. They do not replace them.

ReAct is a reasoning/action pattern, not the same thing as an agent role. Plan-and-Execute is an orchestration pattern, not a substitute for specs, plans, tasks, or verification. BDI is a design lens, not a repository control surface.

DSPy is an implementation and optimization framework, not the same thing as a skill. A skill is the team's reusable task playbook, whether or not it uses an optimization framework.

LLM Guard is a guardrail component, not the whole permission model. A scanner may help detect risk, but blast-radius control still needs permissions, approvals, sandboxing, ownership, and auditability.

A2A and AG-UI are interoperability and user-interface protocols, not replacements for repository structure. AP2 and UCP are commerce-oriented protocols and should not become core vocabulary unless a chapter needs that domain.

MCP/tools are the external capability layer. They are not the agent itself.

For the catalog of adjacent methods, prompting techniques, guardrail tools, and protocols, see [Appendix: Agentic Patterns, Prompting Techniques, and Protocols](./appendix-agentic-patterns-and-protocols.md).

## Nexus case study

### Before this chapter

Nexus Software Systems has accepted that AI-assisted engineering needs more structure, but teams still use overloaded language. Developers call prompts agents, checklists skills, tool access context, and completion summaries verification.

That language makes review harder. A reviewer cannot tell whether a proposed change modifies a role, a procedure, a tool, a permission boundary, or an artifact expectation.

### Design decision

Nexus Engineering Control Plane defines a small vocabulary with hard boundaries.

The decision is intentionally narrow: Nexus does not try to standardize every agentic pattern in the industry. It standardizes the control surfaces its teams need to design governed AI-assisted workflows.

### Implementation

Nexus introduces the `Nexus vocabulary map`.

`nexus-service`, `nexus-delivery`, and `nexus-playbook` use the same vocabulary when designing AI-assisted workflows. A concern must be classified as steering, skill, slash command, agent, subagent, hook, permission control, context/memory, specs/plans/tasks, artifact, verification, or MCP/tool before the team decides where it lives.

### After this chapter

Nexus can now classify whether a concern belongs in steering, a skill, an agent contract, a tool contract, a permission rule, verification evidence, or a durable artifact.

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
| How should a known workflow start? | Slash command | It provides a consistent trigger, not the whole workflow. |
| What should run at a lifecycle point? | Hook | It automates or guards a specific workflow boundary. |
| What limits risky access or execution? | Permissions, approvals, and sandboxing | It controls blast radius before capability expands. |
| What information does the agent know or carry? | Context and memory | It distinguishes task input from tools and artifacts. |
| How should work be decomposed before execution? | Specs, plans, and tasks | It makes scope, sequence, and acceptance criteria reviewable. |
| What must survive beyond chat? | Artifacts | It preserves decisions, evidence, templates, and operational knowledge. |
| What proves the work is acceptable? | Verification | It turns claims into evidence and checks. |
| What external capability is being called? | MCP/tools | It separates system access from the agent role. |

### Chapter asset

`Nexus vocabulary map`

### Reader action

Take one AI-assisted workflow your team already performs and classify each part using the vocabulary in this chapter. If everything is called "the agent," the workflow is not yet designed.
