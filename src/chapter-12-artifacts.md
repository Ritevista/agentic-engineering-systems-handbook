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

## Nexus case study

### Before this chapter

Important decisions disappear in chat.

### After this chapter

Nexus stores ADRs, specs, runbooks, PR evidence, and review notes in repos.

## Quick Reference

| Preserve this... | As this artifact |
|---|---|
| Architectural rationale | ADR |
| Change intent and impact | Change note |
| Verification result | PR evidence |
| Repeated workflow structure | Template or skill |
| Operational procedure | Runbook |
