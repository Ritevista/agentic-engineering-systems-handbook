# Chapter 13: Verification, Tests, Evals, and Checklists

> **Status: in progress.** This chapter has a complete structure and plan below.
> Prose, templates, and worked examples are being written.

## What this chapter will deliver

- Tests as behavioral verification
- Evals for repeated agent behavior quality
- Checklists and review evidence as verification types
- Verification gates and PR evidence collection
- Nexus PR evidence checklist for the API contract running example

## Reader problem

"Done" is not evidence.

AI-assisted work can sound complete before it is correct. A polished explanation, passing-looking patch, or confident summary does not prove behavior, safety, compatibility, or maintainability.

## Design principle: verification is evidence and checks

Verification is evidence and checks. It turns claims into reviewable proof.

| Verification type | What it proves |
|---|---|
| Tests | Behavior still works |
| Evals | Repeated agent behavior meets a quality bar |
| Checklists | Required review concerns were considered |
| Command output | A specific check actually ran |
| Review evidence | A qualified reviewer inspected the right risk |

Self-consistency, eval-backed prompt programs, and model metrics can support verification. They do not replace tests, review, or acceptance evidence.

## Tests and behavioral verification

_Planned: what tests verify; the difference between a passing test and a passing claim; contract tests versus regression tests._

## Evals for repeated agent behavior

_Planned: what evals are; when to use them; how eval results become verification evidence rather than just metrics._

## Checklists and review evidence

_Planned: how checklists work as verification; what a reviewer signature proves; when checklist evidence is sufficient and when it is not._

## Verification gates and PR evidence

_Planned: how verification is gated in the workflow; what the PR evidence record must contain; how hooks and CI enforce verification requirements._

## Observability and audit

_Planned: how verification results are logged and traced; the audit record as verification artifact (see also Chapter 12 and Chapter 9)._

## Applying verification to the running example

_Planned: thread the canonical running example (see running-example.md) through this chapter's concept._

## Nexus case study

### Before this chapter

Agents claim work is done without proof.

### Design decision

_Planned._

### Implementation

_Planned._

### After this chapter

Nexus requires test output, review checklist, risk notes, and verification evidence.

### Lesson

_Planned._

## Templates

_Planned: PR evidence checklist — the named Nexus asset for this chapter._

## Quick Reference

| Claim | Required evidence |
|---|---|
| Tests pass | Command output or CI link |
| Contract remains compatible | Contract test result and compatibility note |
| Documentation is updated | Linked doc change |
| Risk was reviewed | Checklist or reviewer note |
| Agent completed the task | Patch, artifacts, and verification evidence |

## Source Notes

_Planned. Analysis, decision frameworks, and Nexus Engineering Control Plane examples are original to this field manual; source-backed references are added only where tool- or protocol-specific behavior is discussed._
