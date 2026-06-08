# Chapter 15: Decision Frameworks

> **Status: in progress.** This chapter has a complete structure and plan below.
> Prose, templates, and worked examples are being written.

## What this chapter will deliver

- How to read and use decision tables
- Criteria for choosing between adjacent primitives
- Common decision points teams face when designing workflows
- How to build and maintain a team decision framework
- Nexus decision framework for workflow design

## Reader problem

Teams need a way to choose the right primitive.

Without decision frameworks, every workflow design becomes taste: one team adds an agent, another writes a prompt, another creates a tool, and another adds a checklist. The result is inconsistency disguised as flexibility.

## Design principle: decision frameworks make choices reviewable

Decision frameworks are reusable tables for choosing structure. They convert judgment into reviewable criteria.

| Decision | Criteria |
|---|---|
| Steering or skill? | Stable doctrine belongs in steering; repeatable procedure belongs in a skill. |
| Skill or slash command? | A playbook explains how; a command starts the workflow. |
| Agent or subagent? | A primary role owns work; a subagent handles isolated delegated work. |
| Hook or checklist? | A hook enforces at a lifecycle point; a checklist guides human review. |
| Tool or context? | A tool performs external capability; context informs the agent. |

Good decision tables make trade-offs explicit. They do not remove engineering judgment.

## How to use decision tables

_Planned: how to apply the criteria in the design principle table; what makes a decision table useful versus one that is too vague to act on._

## Choosing between adjacent primitives

_Planned: worked examples of close calls — when steering and skill genuinely overlap, when a hook and a checklist could both work, when tool and context blur._

## Common decision points in workflow design

_Planned: the decisions most teams hit repeatedly; how to capture them as reusable framework entries rather than ad-hoc choices._

## Building and maintaining a team decision framework

_Planned: how to create your own decision table; how to keep it current as the team's primitives and patterns evolve._

## Applying decision frameworks to the running example

_Planned: thread the canonical running example (see running-example.md) through this chapter's concept._

## Nexus case study

### Before this chapter

Teams do not know when to use agent vs skill vs tool.

### Design decision

_Planned._

### Implementation

_Planned._

### After this chapter

Nexus creates decision frameworks for workflow design.

### Lesson

_Planned._

## Templates

_Planned: decision framework — the named Nexus asset for this chapter._

## Quick Reference

| Good framework trait | Weak framework trait |
|---|---|
| Uses concrete criteria | Uses vague preference |
| Separates nearby primitives | Treats all agentic terms as equivalent |
| Produces an artifact | Stays in chat |
| Can be reviewed later | Depends on one person's taste |

## Source Notes

_Planned. Analysis, decision frameworks, and Nexus Engineering Control Plane examples are original to this field manual; source-backed references are added only where tool- or protocol-specific behavior is discussed._
