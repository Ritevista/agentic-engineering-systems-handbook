# Chapter 2: Core Vocabulary

## Reader problem

Teams cannot govern what they cannot name precisely.

Agentic engineering fails early when every capability is called an agent, every procedure is hidden in a prompt, and every external integration is treated like ordinary context. The result is architecture drift: unclear ownership, weak review, and no shared way to decide where a rule, workflow, or artifact belongs.

## Design principle

Use a small vocabulary with hard boundaries.

The core terms in this field manual are not synonyms. Each term names a different control surface in the engineering system.

| Term | Meaning in this book |
|---|---|
| Agent | Bounded role |
| Subagent | Isolated delegated worker |
| Steering | Doctrine, rules, and context |
| Skill | Reusable task playbook |
| Slash command | Workflow trigger |
| Hook | Lifecycle automation or guardrail |
| Permissions, approvals, and sandboxing | Blast-radius control |
| Context and memory | What the agent knows or carries |
| Specs, plans, and tasks | Work structure |
| Artifacts | Durable outputs |
| Verification | Evidence and checks |
| MCP/tools | External capability layer |

Related patterns such as ReAct, BDI, DSPy, LLM Guard, MCP, and A2A can support these primitives. They do not replace the vocabulary. See [Appendix: Agentic Patterns, Prompting Techniques, and Protocols](./appendix-agentic-patterns-and-protocols.md).

## Nexus case study

Nexus Software Systems starts with overloaded language. Teams call prompts "agents," call checklists "skills," and treat tool access as a convenience instead of an architecture boundary.

Nexus Engineering Control Plane introduces a vocabulary map. The map lets `nexus-service`, `nexus-delivery`, and `nexus-playbook` describe the same workflow without redefining the terms in every repository.

After this chapter, Nexus has a shared language for reviewing AI-assisted engineering designs.

## Quick Reference

| If the team asks... | Use this term |
|---|---|
| What role owns this responsibility? | Agent |
| What isolated worker should handle a delegated task? | Subagent |
| What repository rules guide the work? | Steering |
| What reusable procedure should be followed? | Skill |
| How is the workflow invoked? | Slash command |
| What guardrail runs at a lifecycle point? | Hook |
| What limits access or execution? | Permissions, approvals, and sandboxing |
| What information is supplied or retained? | Context and memory |
| How is work decomposed before execution? | Specs, plans, and tasks |
| What durable output survives the session? | Artifact |
| What proves the work is acceptable? | Verification |
| What external system capability is being called? | MCP/tool |
