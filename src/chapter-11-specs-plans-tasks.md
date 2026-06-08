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

## Nexus case study

### Before this chapter

Agents jump directly into code.

### After this chapter

Nexus requires specs and task plans for risky changes.

## Quick Reference

| If the change is... | Required structure |
|---|---|
| Trivial and local | Short task note may be enough |
| Cross-module | Plan and task list |
| Contract-affecting | Spec, compatibility notes, and acceptance criteria |
| Security-sensitive | Spec, risk notes, and explicit review path |
| Operationally risky | Plan, rollback notes, and verification evidence |
