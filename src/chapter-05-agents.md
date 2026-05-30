# Chapter 5: Agents

## Reader problem

An unbounded agent is a polite name for unclear responsibility.

Teams often ask one assistant to plan, implement, review, document, test, and decide. That may work for small tasks. It fails when reviewability, accountability, and permission boundaries matter.

## Design principle

An agent is a bounded role. Define its responsibility, inputs, allowed actions, expected outputs, and escalation points before treating it as part of the engineering workflow.

| Boundary | Question |
|---|---|
| Responsibility | What work does this agent own? |
| Inputs | What context may it use? |
| Actions | What files, tools, or commands may it touch? |
| Outputs | What artifact or evidence must it produce? |
| Escalation | When must it stop or hand off? |

Related reasoning patterns such as ReAct, Plan-and-Execute, and BDI can shape agent behavior. They do not remove the need for a role contract.

## Nexus case study

Before this chapter, Nexus relies on generic assistants with inconsistent behavior across repositories.

Nexus introduces an implementation-agent role contract. The implementation agent can edit code within an approved scope, must preserve repository steering, and must produce verification evidence before claiming completion.

After this chapter, Nexus has a role contract instead of a generic helper.

## Quick Reference

| Use an agent when... | Avoid an agent when... |
|---|---|
| The responsibility is bounded and repeatable. | The task is exploratory with no clear output. |
| Inputs and permissions can be stated. | The agent would need broad unreviewed authority. |
| The result can be verified. | The result depends on private reasoning only. |
| The output becomes a durable artifact or patch. | The work is only a one-off explanation. |
