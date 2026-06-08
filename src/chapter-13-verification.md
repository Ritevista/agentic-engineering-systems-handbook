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

## Nexus case study

### Before this chapter

Agents claim work is done without proof.

### After this chapter

Nexus requires test output, review checklist, risk notes, and verification evidence.

## Quick Reference

| Claim | Required evidence |
|---|---|
| Tests pass | Command output or CI link |
| Contract remains compatible | Contract test result and compatibility note |
| Documentation is updated | Linked doc change |
| Risk was reviewed | Checklist or reviewer note |
| Agent completed the task | Patch, artifacts, and verification evidence |
