# Chapter 13: Verification, Tests, Evals, and Checklists

## Reader problem

"Done" is not evidence.

AI-assisted work can sound complete before it is correct. A polished explanation, passing-looking patch, or confident summary does not prove behavior, safety, compatibility, or maintainability.

## Design principle

Verification is evidence and checks. It turns claims into reviewable proof.

| Verification type | What it proves |
|---|---|
| Tests | Behavior still works |
| Evals | Repeated agent behavior meets a quality bar |
| Checklists | Required review concerns were considered |
| Command output | A specific check actually ran |
| Review evidence | A qualified reviewer inspected the right risk |

Self-consistency, eval-backed prompt programs, and model metrics can support verification. They do not replace tests, review, or acceptance evidence.

## Nexus case study

Before this chapter, Nexus accepts too many agent claims without proof.

Nexus introduces a PR evidence checklist. For the API contract running example, the checklist requires contract tests, regression tests, compatibility notes, authorization review where needed, documentation updates, and recorded command output.

After this chapter, Nexus has a verification standard instead of a confidence standard.

## Quick Reference

| Claim | Required evidence |
|---|---|
| Tests pass | Command output or CI link |
| Contract remains compatible | Contract test result and compatibility note |
| Documentation is updated | Linked doc change |
| Risk was reviewed | Checklist or reviewer note |
| Agent completed the task | Patch, artifacts, and verification evidence |
