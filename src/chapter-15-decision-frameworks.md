# Chapter 15: Decision Frameworks

## Reader problem

Teams need a way to choose the right primitive.

Without decision frameworks, every workflow design becomes taste: one team adds an agent, another writes a prompt, another creates a tool, and another adds a checklist. The result is inconsistency disguised as flexibility.

## Design principle

Decision frameworks are reusable tables for choosing structure. They convert judgment into reviewable criteria.

| Decision | Criteria |
|---|---|
| Steering or skill? | Stable doctrine belongs in steering; repeatable procedure belongs in a skill. |
| Skill or slash command? | A playbook explains how; a command starts the workflow. |
| Agent or subagent? | A primary role owns work; a subagent handles isolated delegated work. |
| Hook or checklist? | A hook enforces at a lifecycle point; a checklist guides human review. |
| Tool or context? | A tool performs external capability; context informs the agent. |

Good decision tables make trade-offs explicit. They do not remove engineering judgment.

## Nexus case study

Before this chapter, Nexus teams choose primitives inconsistently.

Nexus introduces decision tables for workflow design. For the API contract running example, the team can decide what belongs in steering, what belongs in an API-change skill, what should be triggered by a command, and what requires verification evidence.

After this chapter, Nexus has a shared way to make control-plane design decisions.

## Quick Reference

| Good framework trait | Weak framework trait |
|---|---|
| Uses concrete criteria | Uses vague preference |
| Separates nearby primitives | Treats all agentic terms as equivalent |
| Produces an artifact | Stays in chat |
| Can be reviewed later | Depends on one person's taste |
