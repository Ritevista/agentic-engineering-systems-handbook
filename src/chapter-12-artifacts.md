# Chapter 12: Artifacts

## Reader problem

Engineering decisions disappear when chat is the system of record.

AI-assisted work produces plans, assumptions, trade-offs, review notes, and evidence. If those outputs stay in a private session, the repository loses the reasoning that future maintainers need. Six months later, someone finds an API field that looks arbitrary and has no way to learn it was a deliberate compatibility decision — the conversation that explained it is gone, and even if it were not, no one would think to search a chat log for the answer.

## What breaks without this

A spec (Chapter 11) that only exists inside a conversation is not a spec — it is a transcript. A subagent's findings (Chapter 6) that only exist in the parent agent's session cannot be checked by a human reviewer after the fact. Verification evidence (Chapter 13) that is described in a summary rather than attached as a real artifact cannot be audited later.

The pattern is the same across every chapter in this book: structure that exists only inside a session is structure the next person cannot see, trust, or build on. Artifacts are what make the rest of this book's discipline outlive the conversation that produced it.

## Design principle: artifacts are durable outputs

Artifacts are durable outputs. They preserve decisions, evidence, and reusable knowledge outside the assistant session.

| Artifact | What it preserves |
|---|---|
| ADR | Architectural decision and rationale |
| Change note | Intent, risk, and compatibility impact |
| Runbook | Operational procedure |
| PR evidence | Tests, checks, review notes, and links |
| Template | Repeatable structure for future work |

Artifacts should be written for future readers, not only for the current agent. A future reader has none of the current session's context: they were not there when the trade-off was discussed, and they are reading the artifact specifically because the original reasoning is not otherwise available to them.

## Artifact taxonomy

Not every output deserves the same artifact type. Matching the type to what actually needs preserving keeps the repository from accumulating either too little history or too much noise.

**ADR (Architecture Decision Record)** captures a decision and its rationale — what was decided, what alternatives were considered, and why. Write one when a decision would be expensive to re-derive later: a schema shape, a compatibility approach, a dependency choice. An ADR is not a status update; it exists because the reasoning behind a decision is worth more than the decision alone.

**Change note** captures intent, risk, and compatibility impact for a specific change — smaller in scope than an ADR, tied to one change rather than a standing architectural choice. A change note answers "what did this change do and what could it affect," which is exactly what Chapter 11's spec already states before implementation; the change note is that intent, confirmed against what actually shipped.

**Runbook** captures an operational procedure: how to do something a human or agent will need to repeat, especially under pressure. Chapter 14's rollback procedure is a runbook. A runbook that has never been tested is a hope, not a procedure.

**PR evidence** captures the proof that verification (Chapter 13) actually happened: test output, compatibility notes, review findings, links to the spec and plan it fulfills. PR evidence is the artifact type most directly at risk of becoming a summary instead of proof — "tests pass" is a claim; a link to the actual test run is evidence.

**Template** captures a repeatable structure so the next instance of a recurring artifact does not start from a blank page. Every worked example this book gives — the spec template in Chapter 11, the permission matrix template in Chapter 9 — is this artifact type.

## Storage, lifecycle, and ownership

An artifact that no one can find is functionally the same as an artifact that was never written. Three properties keep artifacts usable rather than merely present:

| Property | Requirement |
|---|---|
| Location | Consistent, predictable path per artifact type (Chapter 15 covers repository layout in depth) |
| Ownership | A named owner or team responsible for keeping it current |
| Lifecycle | A stated expectation for how long it stays authoritative, and what supersedes it |

Ownership matters because artifacts rot. An ADR does not need updates — it is a record of a decision at a point in time — but a runbook does, and a stale runbook that no longer matches the actual rollback procedure is worse than no runbook, because it will be trusted anyway during an incident. Decide at creation time whether an artifact is a permanent record or a living document, and treat it accordingly.

## Artifact quality and discoverability

An artifact written for the author, not the reader, tends to skip the context a future reader actually needs: why the decision mattered, what was rejected, what would change the answer. Three checks catch this:

- Does the artifact make sense to someone who was not in the original session?
- Does it state what was rejected or ruled out, not just what was chosen?
- Can someone find it without already knowing it exists — through a predictable location, a link from the related PR or spec, or an index?

An artifact that answers the first two questions but fails the third is still effectively lost. Discoverability is not a nice-to-have; it is the difference between a durable artifact and a file that happens to be durable.

## Anti-patterns

| Anti-pattern | Why it fails | Better pattern |
|---|---|---|
| Chat as system of record | Decisions and evidence live only in a session transcript | Commit the decision as an ADR, change note, or PR evidence |
| Write-only artifacts | Created once, never linked, never read again | Link from the PR, spec, or index; assign an owner |
| Artifact sprawl | No consistent location or naming; duplicates accumulate | Fixed location per type (Chapter 15); one canonical artifact per decision |
| Evidence as summary | "Tests pass" with no link to actual output | Attach the real test output or CI link, not a claim about it |
| Stale runbook | Procedure no longer matches reality; trusted anyway | Assign an owner; test the procedure periodically |

## Nexus case study

### Before this chapter

Important decisions disappear in chat. The reasoning behind why a field was made optional instead of versioned lives in one engineer's assistant session and nowhere else.

### Design decision

Nexus stores ADRs, specs, runbooks, PR evidence, and review notes in repos, using the taxonomy above to decide which type a given output should become.

### Implementation

```md
# ADR-014: Add optional field instead of versioning nexus-service response

## Status
Accepted

## Context
A new field needs to reach clients without breaking existing consumers.

## Decision
Add the field as optional/nullable rather than introducing a new API
version.

## Alternatives considered
- New API version: rejected, disproportionate for an additive change.

## Consequences
Clients with strict schema validation must tolerate unknown fields.
Compatibility-review subagent checks this before merge.
```

```md
# PR evidence: Add optional field to nexus-service response

## Spec
Link: specs/2026-nexus-service-optional-field.md

## Tests
Link: CI run #4821 — contract tests pass (existing + new field)

## Compatibility review
compatibility-review subagent findings: no breaking findings.
Link: pr-1042-review-findings.md

## Docs
Link: docs update in same PR, api/response-schema.md
```

### After this chapter

Nexus stores ADRs, specs, runbooks, PR evidence, and review notes in repos. A future engineer investigating why the field is optional finds ADR-014 instead of asking around.

### Lesson

An artifact that only the current session can see is not durable. Write for the reader who was not there.

## Quick Reference

### Preserve this... → as this artifact

| Preserve this... | As this artifact |
|---|---|
| Architectural rationale | ADR |
| Change intent and impact | Change note |
| Verification result | PR evidence |
| Repeated workflow structure | Template or skill |
| Operational procedure | Runbook |

### Nexus asset

Artifact taxonomy for the backward-compatible API contract running example: ADR, PR evidence, and change note templates.

### Reader action

Find one decision from the last month that currently exists only in a chat session. Write it as the artifact type it should have been — ADR, change note, or PR evidence — and link it from the PR or spec it belongs to.
