# Chapter 15: Repo Layout

> **Status: in progress.** This chapter has a complete structure and plan below.
> Prose, templates, and worked examples are being written.

## What this chapter will deliver

- Standard directory structure for agent-ready repositories
- Where to place steering, skills, specs, artifacts, and evidence
- Monorepo and multi-repo layout patterns
- Layout conventions, naming, and discoverability
- Nexus repository layout across nexus-service, nexus-delivery, and nexus-playbook

## Reader problem

Agent-ready repositories fail when guidance is scattered.

If steering, skills, specs, artifacts, examples, and verification evidence all live in different ad-hoc places, teams cannot reuse or govern the workflow. Layout is part of the control plane.

## Design principle: layout makes structure discoverable

Repository layout should make AI-assisted engineering structure discoverable.

| Concern | Typical location |
|---|---|
| Repository steering | `AGENTS.md` or equivalent |
| Reusable skills | `skills/` |
| Specs and plans | `specs/` or `docs/` |
| Durable decisions | `docs/adrs/` or `docs/decisions/` |
| Examples | `examples/` |
| Verification evidence | PR description, CI, or evidence directory |

The exact names can vary. The responsibilities should not.

## Nexus case study

### Before this chapter

Every repo organizes AI guidance differently.

### After this chapter

Nexus defines common layout for steering, specs, docs, artifacts, and skills.

## Quick Reference

| Layout rule | Reason |
|---|---|
| Put steering at the repo root. | Agents and humans find local rules quickly. |
| Keep skills separate from steering. | Procedures evolve differently from doctrine. |
| Store artifacts in durable paths. | Decisions survive chat and tool sessions. |
| Keep examples realistic but sanitized. | Readers can copy patterns safely. |
