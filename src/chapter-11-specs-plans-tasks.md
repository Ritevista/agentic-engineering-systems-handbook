# Chapter 11: Specs, Plans, and Tasks

> **Status: in progress.** This chapter has a complete structure and plan below.
> Prose, templates, and worked examples are being written.

## What this chapter will deliver

- When to decompose work before an agent acts
- Spec format and required fields for contract-affecting changes
- Plan structure and trade-off documentation
- Task decomposition and acceptance criteria
- Nexus spec/plan/task template for the API contract running example

## Reader problem

Agents move too quickly when work is not decomposed.

Directly asking for implementation can collapse requirement discovery, design, task sequencing, and coding into one opaque step. That may be acceptable for trivial changes. It is weak practice for work that affects contracts, data, security, or operations.

## Design principle: specs, plans, and tasks are work structure

Specs, plans, and tasks are work structure.

| Artifact | Role |
|---|---|
| Spec | Defines what must be true and why |
| Plan | Defines the approach and trade-offs |
| Task list | Breaks execution into reviewable units |
| Acceptance criteria | States how completion will be judged |

Plan-and-Execute and lightweight spec-driven development patterns belong here when they produce reviewable work structure and execution evidence.

## When to decompose work before acting

_Planned: criteria for when a spec, plan, or task list is required versus when a short task note is enough — based on contract, data, security, and operational risk._

## Writing a spec

_Planned: what a spec must contain; the difference between a spec and a plan; minimum required fields for contract-affecting and security-sensitive work._

## Building a plan

_Planned: how to document approach and trade-offs; how a plan connects to the task list and acceptance criteria._

## Task decomposition and acceptance criteria

_Planned: how to break a plan into reviewable task units; how to write acceptance criteria the agent and reviewer can both use._

## Applying work structure to the running example

_Planned: thread the canonical running example (see running-example.md) through this chapter's concept._

## Nexus case study

### Before this chapter

Agents jump directly into code.

### Design decision

_Planned._

### Implementation

_Planned._

### After this chapter

Nexus requires specs and task plans for risky changes.

### Lesson

_Planned._

## Templates

_Planned: spec/plan/task template — the named Nexus asset for this chapter._

## Quick Reference

| If the change is... | Required structure |
|---|---|
| Trivial and local | Short task note may be enough |
| Cross-module | Plan and task list |
| Contract-affecting | Spec, compatibility notes, and acceptance criteria |
| Security-sensitive | Spec, risk notes, and explicit review path |
| Operationally risky | Plan, rollback notes, and verification evidence |

## Source Notes

_Planned. Analysis, decision frameworks, and Nexus Engineering Control Plane examples are original to this field manual; source-backed references are added only where tool- or protocol-specific behavior is discussed._
