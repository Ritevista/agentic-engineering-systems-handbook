# Chapter 16: Decision Frameworks

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

## Nexus case study

### Before this chapter

Teams do not know when to use agent vs skill vs tool.

### After this chapter

Nexus creates decision frameworks for workflow design.

## Quick Reference

| Good framework trait | Weak framework trait |
|---|---|
| Uses concrete criteria | Uses vague preference |
| Separates nearby primitives | Treats all agentic terms as equivalent |
| Produces an artifact | Stays in chat |
| Can be reviewed later | Depends on one person's taste |
