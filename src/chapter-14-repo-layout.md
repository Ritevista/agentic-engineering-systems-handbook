# Chapter 14: Repo Layout

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

## Standard directory structure

_Planned: a reference layout showing where each concern lives in a typical single-service repository, with rationale for each placement._

## Placing steering, skills, specs, and artifacts

_Planned: rules for co-locating guidance with what it governs; when to use root-level versus module-level placement; avoiding scattered guidance._

## Monorepo and multi-repo patterns

_Planned: how the layout scales to a monorepo; how multiple repositories share conventions without duplicating doctrine._

## Naming conventions and discoverability

_Planned: naming rules that make structure findable by agents and humans; how to avoid layout drift across teams._

## Applying layout to the running example

_Planned: thread the canonical running example (see running-example.md) through this chapter's concept._

## Nexus case study

### Before this chapter

Every repo organizes AI guidance differently.

### Design decision

_Planned._

### Implementation

_Planned._

### After this chapter

Nexus defines common layout for steering, specs, docs, artifacts, and skills.

### Lesson

_Planned._

## Templates

_Planned: repository layout — the named Nexus asset for this chapter._

## Quick Reference

| Layout rule | Reason |
|---|---|
| Put steering at the repo root. | Agents and humans find local rules quickly. |
| Keep skills separate from steering. | Procedures evolve differently from doctrine. |
| Store artifacts in durable paths. | Decisions survive chat and tool sessions. |
| Keep examples realistic but sanitized. | Readers can copy patterns safely. |

## Source Notes

_Planned. Analysis, decision frameworks, and Nexus Engineering Control Plane examples are original to this field manual; source-backed references are added only where tool- or protocol-specific behavior is discussed._
