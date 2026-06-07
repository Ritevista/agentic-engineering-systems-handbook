# Chapter 14: Repo Layout

> Status: To be done.

## Reader problem

Agent-ready repositories fail when guidance is scattered.

If steering, skills, specs, artifacts, examples, and verification evidence all live in different ad-hoc places, teams cannot reuse or govern the workflow. Layout is part of the control plane.

## Design principle

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

Before this chapter, Nexus repositories organize agent guidance differently.

Nexus introduces a standard repository layout. `nexus-service`, `nexus-delivery`, and `nexus-playbook` can now place steering, skills, specs, artifacts, examples, and evidence in predictable locations.

After this chapter, Nexus has a repository convention that makes governance easier to inspect.

## Quick Reference

| Layout rule | Reason |
|---|---|
| Put steering at the repo root. | Agents and humans find local rules quickly. |
| Keep skills separate from steering. | Procedures evolve differently from doctrine. |
| Store artifacts in durable paths. | Decisions survive chat and tool sessions. |
| Keep examples realistic but sanitized. | Readers can copy patterns safely. |
