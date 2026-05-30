# Chapter 11: Specs, Plans, and Tasks

## Reader problem

Agents move too quickly when work is not decomposed.

Directly asking for implementation can collapse requirement discovery, design, task sequencing, and coding into one opaque step. That may be acceptable for trivial changes. It is weak practice for work that affects contracts, data, security, or operations.

## Design principle

Specs, plans, and tasks are work structure.

| Artifact | Role |
|---|---|
| Spec | Defines what must be true and why |
| Plan | Defines the approach and trade-offs |
| Task list | Breaks execution into reviewable units |
| Acceptance criteria | States how completion will be judged |

Plan-and-Execute and lightweight spec-driven development patterns belong here when they produce reviewable work structure and execution evidence.

## Nexus case study

Before this chapter, Nexus agents often jump from request to patch.

Nexus requires a short spec and task plan for risky API changes. For the running example, the plan identifies compatibility, authorization, documentation, test, and rollout-note tasks before implementation begins.

After this chapter, Nexus has a work-structure template that slows the right things down.

## Quick Reference

| If the change is... | Required structure |
|---|---|
| Trivial and local | Short task note may be enough |
| Cross-module | Plan and task list |
| Contract-affecting | Spec, compatibility notes, and acceptance criteria |
| Security-sensitive | Spec, risk notes, and explicit review path |
| Operationally risky | Plan, rollback notes, and verification evidence |
