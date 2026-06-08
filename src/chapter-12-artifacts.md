# Chapter 12: Artifacts

> **Status: in progress.** This chapter has a complete structure and plan below.
> Prose, templates, and worked examples are being written.

## What this chapter will deliver

- What makes output an artifact versus transient chat
- Artifact taxonomy: ADRs, change notes, runbooks, PR evidence, templates
- Storage, lifecycle, and ownership of durable outputs
- Artifact quality and discoverability
- Nexus artifact taxonomy for the API contract running example

## Reader problem

Engineering decisions disappear when chat is the system of record.

AI-assisted work produces plans, assumptions, trade-offs, review notes, and evidence. If those outputs stay in a private session, the repository loses the reasoning that future maintainers need.

## Design principle: artifacts are durable outputs

Artifacts are durable outputs. They preserve decisions, evidence, and reusable knowledge outside the assistant session.

| Artifact | What it preserves |
|---|---|
| ADR | Architectural decision and rationale |
| Change note | Intent, risk, and compatibility impact |
| Runbook | Operational procedure |
| PR evidence | Tests, checks, review notes, and links |
| Template | Repeatable structure for future work |

Artifacts should be written for future readers, not only for the current agent.

## What makes output an artifact

_Planned: criteria for when to promote agent output to a durable artifact; the difference between a session note and a repository record._

## Artifact types and their purposes

_Planned: deep-dive on each type in the taxonomy — who writes it, when, what it must contain, and who maintains it._

## Storage, lifecycle, and ownership

_Planned: where artifacts live in the repository; who owns them; when they are updated, archived, or superseded._

## Artifact quality and discoverability

_Planned: what makes an artifact useful to future readers; naming, linking, and cross-referencing conventions._

## Applying artifacts to the running example

_Planned: thread the canonical running example (see running-example.md) through this chapter's concept._

## Nexus case study

### Before this chapter

Important decisions disappear in chat.

### Design decision

_Planned._

### Implementation

_Planned._

### After this chapter

Nexus stores ADRs, specs, runbooks, PR evidence, and review notes in repos.

### Lesson

_Planned._

## Templates

_Planned: artifact taxonomy — the named Nexus asset for this chapter._

## Quick Reference

| Preserve this... | As this artifact |
|---|---|
| Architectural rationale | ADR |
| Change intent and impact | Change note |
| Verification result | PR evidence |
| Repeated workflow structure | Template or skill |
| Operational procedure | Runbook |

## Source Notes

_Planned. Analysis, decision frameworks, and Nexus Engineering Control Plane examples are original to this field manual; source-backed references are added only where tool- or protocol-specific behavior is discussed._
