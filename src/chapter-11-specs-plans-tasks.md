# Chapter 11: Specs, Plans, and Tasks

## Reader problem

Agents move too quickly when work is not decomposed.

Directly asking for implementation can collapse requirement discovery, design, task sequencing, and coding into one opaque step. For a trivial change, that collapse is harmless — there is nothing to decompose. For work that affects contracts, data, security, or operations, it is weak practice: the agent picks an interpretation, a design, and an execution order all at once, and the reviewer only sees the result, not the decisions that produced it.

## What breaks without this

Skipping decomposition does not remove the decisions — it just removes their visibility. An agent implementing a backward-compatible API contract change still decides what "backward-compatible" means for this specific change, still decides which files to touch and in what order, and still decides when it is done. Without a spec, plan, and task list, those decisions live only inside the agent's reasoning for one session, and a reviewer evaluating the diff has no way to check them against what was actually intended.

This is also where compatibility gaps, missed authorization checks, and undocumented rollout risk tend to originate: not in the code itself, but in a requirement or trade-off nobody wrote down before implementation started.

## Design principle: specs, plans, and tasks are work structure

Specs, plans, and tasks are work structure. Each answers a different question, and none substitutes for another.

| Artifact | Role |
|---|---|
| Spec | Defines what must be true and why |
| Plan | Defines the approach and trade-offs |
| Task list | Breaks execution into reviewable units |
| Acceptance criteria | States how completion will be judged |

Plan-and-Execute and lightweight spec-driven development patterns belong here when they produce reviewable work structure and execution evidence — the pattern is only as good as the artifact it leaves behind. A pattern that reasons carefully but leaves nothing durable has the discipline without the proof.

## Spec format and required fields

A spec defines what must be true when the work is done, and why. For contract-affecting changes, a spec should state:

- **Scope**: what is changing, and explicitly what is not.
- **Compatibility requirement**: what existing behavior must be preserved, and for whom.
- **Constraints**: authorization boundaries, data handling limits, or steering rules that bound the solution space.
- **Acceptance criteria**: the specific, checkable conditions that mean the change is done.
- **Out of scope**: adjacent work explicitly deferred, so it is not silently picked up or silently dropped.

A spec is not a design document. It states what must be true, not how the code will achieve it — that is the plan's job. Confusing the two produces specs that are really implementation notes, which lock in a design before anyone has evaluated alternatives.

## Plan structure and trade-off documentation

A plan defines the approach and the trade-offs behind it. Where the spec says what must be true, the plan says how the team intends to get there and what it gave up to do so.

A useful plan states:

- the chosen approach, in enough detail that a reviewer can evaluate it before code exists
- at least one alternative that was considered and why it was not chosen
- the risk the chosen approach introduces, and how that risk is bounded
- dependencies or sequencing constraints on other work

A plan with no alternatives and no stated trade-off is usually not a plan — it is the first idea that came up, written down after the fact. The value of documenting a trade-off is that a reviewer can disagree with the reasoning, not just the outcome.

## Task decomposition and acceptance criteria

A task list breaks the plan into units small enough to review individually. Each task should be independently understandable: what it changes, and how anyone — human or agent — will know it is done.

| Task quality signal | What it means |
|---|---|
| Independently reviewable | A reviewer can evaluate this task without re-reading the whole plan |
| Has acceptance criteria | Completion is a checkable condition, not a feeling |
| Right-sized | Small enough to review, large enough to be a coherent unit of work |
| Ordered where order matters | Dependencies between tasks are explicit, not assumed |

Acceptance criteria at the task level should be concrete enough to verify: "contract tests pass for the new field" is checkable; "the API change works" is not. Chapter 13 covers how that verification is actually produced as evidence — this chapter is where the criteria that verification will check get written down in the first place.

## How much structure a change needs

Not every change needs a spec. The discipline is deciding the level of structure *before* work starts, not defaulting to the deepest option for everything or skipping structure because a change looked simple at first glance.

| If the change is... | Required structure |
|---|---|
| Trivial and local | Short task note may be enough |
| Cross-module | Plan and task list |
| Contract-affecting | Spec, compatibility notes, and acceptance criteria |
| Security-sensitive | Spec, risk notes, and explicit review path |
| Operationally risky | Plan, rollback notes, and verification evidence |

A backward-compatible API contract change sits squarely in the contract-affecting row: it needs a spec that states the compatibility requirement explicitly, not just a task list that assumes everyone already agrees what "compatible" means.

## Anti-patterns

| Anti-pattern | Why it fails | Better pattern |
|---|---|---|
| Straight to code | Requirement, design, and execution collapse into one opaque step | Match structure to risk using the table above |
| Spec theater | A spec is written but the implementation ignores it | Reference the spec in the task list; verify against its acceptance criteria |
| Plan with no trade-offs | Reads as the first idea, not a reviewed approach | Name at least one rejected alternative and why |
| Vague acceptance criteria | "Works correctly" cannot be checked | State a specific, verifiable condition per task |
| Over-decomposition | Trivial changes buried under unnecessary spec machinery | Use the lightest structure the risk actually requires |

## Nexus case study

### Before this chapter

Agents jump directly into code. A backward-compatible API contract change starts as a prompt and ends as a diff, with the compatibility reasoning — if it happened at all — visible only inside the agent's session.

### Design decision

Nexus requires specs and task plans for risky changes, using the structure-by-risk table to decide how much decomposition a given change needs.

### Implementation

```md
# Spec: Add optional field to nexus-service response

## Scope
Add a new optional field to the [endpoint] response. No existing
field changes shape or meaning.

## Compatibility requirement
Existing clients that do not read the new field must see no
behavioral change. Existing clients must not be required to change
to keep working.

## Constraints
- Must follow nexus-service/AGENTS.md versioning rules.
- Must not require a client-side migration.

## Acceptance criteria
- Contract tests pass for existing response shape.
- Contract tests pass for the new field.
- Compatibility notes attached to the PR.

## Out of scope
- Changes to request-side validation.
- Deprecating any existing field.
```

```md
# Plan: Add optional field to nexus-service response

## Approach
Add the field as nullable/optional in the response schema; default
omitted when not set.

## Alternative considered
Version the endpoint instead. Rejected: the change is additive and
does not require clients to opt in.

## Risk
Clients using strict schema validation could reject the response if
they disallow unknown fields. Bounded by: compatibility-review
subagent (Chapter 6) checks known client schemas before merge.

## Dependencies
None outside nexus-service.
```

```md
# Tasks

1. Add field to response DTO. Acceptance: field present in serialized
   response, defaults to omitted.
2. Update contract tests. Acceptance: existing + new contract tests pass.
3. Run compatibility-review subagent. Acceptance: findings attached
   to PR, no unresolved breaking findings.
4. Update API docs. Acceptance: doc change linked in PR.
```

### After this chapter

Nexus requires specs and task plans for risky changes. The backward-compatible API contract change now starts as a spec with an explicit compatibility requirement, not an assumption buried in an agent's reasoning.

### Lesson

The requirement, the trade-off, and the acceptance condition are decisions. Write them down before implementation, or a reviewer is left reverse-engineering them from a diff.

## Quick Reference

### If the change is... → required structure

| If the change is... | Required structure |
|---|---|
| Trivial and local | Short task note may be enough |
| Cross-module | Plan and task list |
| Contract-affecting | Spec, compatibility notes, and acceptance criteria |
| Security-sensitive | Spec, risk notes, and explicit review path |
| Operationally risky | Plan, rollback notes, and verification evidence |

### Nexus asset

Spec, plan, and task templates for the backward-compatible API contract running example.

### Reader action

Take one change currently in flight without a spec. Write its compatibility requirement or equivalent constraint as a single sentence, then check whether the current implementation actually satisfies it. If you cannot tell, that is the gap this chapter closes.
