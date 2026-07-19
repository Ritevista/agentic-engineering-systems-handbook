# Chapter 13: Verification, Tests, Evals, and Checklists

## Reader problem

"Done" is not evidence.

AI-assisted work can sound complete before it is correct. A polished explanation, a passing-looking patch, or a confident summary does not prove behavior, safety, compatibility, or maintainability. An agent that says "I ran the tests and they pass" has made a claim. Nothing about the sentence proves it happened.

## What breaks without this

Every artifact this book has built up to this point — the spec's acceptance criteria (Chapter 11), the subagent's findings (Chapter 6), the permission matrix's audit trail (Chapter 9) — is only as trustworthy as the checks behind it. Without verification, "acceptance criteria met" is an assertion the reviewer has to take on faith, and faith is exactly what the rest of this book's structure exists to replace with evidence.

The risk compounds with agents specifically. An agent under instruction to finish a task has every incentive, explicit or not, to report success. A confident, well-written completion summary is not harder to produce than an honest one — sometimes it is easier, because it does not require actually confronting a failing check.

## Design principle: verification is evidence and checks

Verification is evidence and checks. It turns claims into reviewable proof.

| Verification type | What it proves |
|---|---|
| Tests | Behavior still works |
| Evals | Repeated agent behavior meets a quality bar |
| Checklists | Required review concerns were considered |
| Command output | A specific check actually ran |
| Review evidence | A qualified reviewer inspected the right risk |

Self-consistency, eval-backed prompt programs, and model metrics can support verification. They do not replace tests, review, or acceptance evidence — they are additional signal about the process that produced the change, not a substitute for checking the change itself.

## The five verification types

**Tests** prove behavior against a specification: given this input, the system produces that output, before and after the change. Chapter 11's acceptance criteria should be written so tests can check them directly — "contract tests pass for the new field" is a test-shaped criterion for exactly this reason.

**Evals** prove that repeated agent behavior meets a quality bar over many runs, not just this one. A single successful session proves the agent can succeed; an eval proves it does so reliably enough to trust unattended. Chapter 5 already introduced scope, boundary, and escalation evals for agent roles — this chapter is where those evals sit inside the broader verification picture, alongside tests and checklists rather than instead of them.

**Checklists** prove that the required review concerns were actually considered, not just that someone glanced at a diff. A checklist's value is in naming the specific things review must not skip — compatibility, authorization, documentation, rollback — so that "I reviewed it" means something specific instead of something vague.

**Command output** proves a specific check actually ran, as opposed to being described as having run. A pasted test summary a human typed from memory is not command output. A CI link, a terminal transcript, or a build log is.

**Review evidence** proves a qualified human — or a subagent standing in for a specific concern, per Chapter 6 — actually inspected the risk that mattered, not merely that a PR received an approval click. A rubber-stamp approval and a genuine compatibility review produce the same GitHub state and very different evidence.

None of these five types substitutes for another. A checklist that says "tests pass" without linked command output is a checklist item, not proof the tests ran. An eval score with no underlying tests proves the agent behaves consistently, not that the behavior is correct.

## Verification gates and PR evidence collection

Verification only has teeth when something checks for it before work counts as complete. This is where Chapter 8's hooks and this chapter meet directly: a pre-PR evidence hook is the mechanism that turns "verification is required" from a stated expectation into an enforced one.

The PR evidence checklist is where the five verification types come together into one reviewable package:

- test output or CI link
- eval results, if the change touches agent behavior directly
- the review checklist, completed
- compatibility or risk notes
- links to the spec and any subagent findings that informed the change

This checklist is itself an artifact (Chapter 12) — it does not live in a PR description that disappears into history, but in a durable, linkable form the pre-PR hook can check for completeness and a future reader can still find.

## Anti-patterns

| Anti-pattern | Why it fails | Better pattern |
|---|---|---|
| Completion theater | A confident summary substitutes for actual proof | Require linked command output, not a description of output |
| Self-graded verification | The same agent that made the change attests it is correct | Independent review or subagent check (Chapter 6) for risky changes |
| Checklist without teeth | Items are checked without evidence backing each one | Each checklist item links to the evidence that satisfies it |
| Eval as test substitute | Behavioral consistency is treated as functional correctness | Evals support tests; they do not replace them |
| Approval without inspection | A click that did not involve reading the actual risk | Review evidence names the specific risk that was inspected |

## Nexus case study

### Before this chapter

Agents claim work is done without proof. A PR for the API contract change is described as "tested and compatible" with no artifact a reviewer can independently check.

### Design decision

Nexus requires test output, review checklist, risk notes, and verification evidence — enforced by the pre-PR evidence hook from Chapter 8 — before any change counts as complete.

### Implementation

```md
# PR evidence checklist: backward-compatible API contract change

## Spec and plan
- [ ] Linked spec: acceptance criteria stated
- [ ] Linked plan: approach and rejected alternative stated

## Tests
- [ ] Contract tests pass (existing shape): [CI link]
- [ ] Contract tests pass (new field): [CI link]

## Review
- [ ] compatibility-review subagent findings attached: [link]
- [ ] No unresolved breaking findings

## Documentation
- [ ] API docs updated: [link]

## Risk
- [ ] Known-client schema risk noted, with mitigation
```

A PR missing any unchecked, unlinked item is blocked by the pre-PR evidence hook (Chapter 8) before it reaches human review.

### After this chapter

Nexus requires test output, review checklist, risk notes, and verification evidence. A "done" claim on the API contract change now means a reviewer can open three links and confirm it themselves.

### Lesson

A claim of completion is not evidence of completion. Require the artifact that proves it, not the sentence that describes it.

## Quick Reference

### Claim → required evidence

| Claim | Required evidence |
|---|---|
| Tests pass | Command output or CI link |
| Contract remains compatible | Contract test result and compatibility note |
| Documentation is updated | Linked doc change |
| Risk was reviewed | Checklist or reviewer note |
| Agent completed the task | Patch, artifacts, and verification evidence |

### Nexus asset

PR evidence checklist for the backward-compatible API contract running example, enforced by the pre-PR evidence hook.

### Reader action

Take one recent "done" claim from an agent session. Find the artifact that proves it — a CI link, a review note, a checklist. If none exists, that claim was completion theater, not verification.
