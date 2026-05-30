# Chapter 12: Artifacts

## Reader problem

Engineering decisions disappear when chat is the system of record.

AI-assisted work produces plans, assumptions, trade-offs, review notes, and evidence. If those outputs stay in a private session, the repository loses the reasoning that future maintainers need.

## Design principle

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

Before this chapter, Nexus often loses the reason a change was made.

Nexus introduces an artifact taxonomy. For the API contract running example, a short change note or ADR records why the response contract changed, what compatibility checks were performed, and what documentation was updated.

After this chapter, Nexus has a durable record strategy for AI-assisted work.

## Quick Reference

| Preserve this... | As this artifact |
|---|---|
| Architectural rationale | ADR |
| Change intent and impact | Change note |
| Verification result | PR evidence |
| Repeated workflow structure | Template or skill |
| Operational procedure | Runbook |
