# Chapter 6: Subagents

## Reader problem

Main agents become unreliable when every concern stays in one conversation.

Implementation, review, security analysis, test planning, and documentation each want a different kind of attention. Implementation wants momentum: keep the change moving, hold the plan in working memory, stay inside the approved scope. Review wants distance: forget the excuses the implementation already accepted, and look at the diff as if someone else wrote it. A single agent carrying both jobs in the same context tends to grade its own work leniently, not because it is dishonest, but because the reasoning that produced the change is still sitting in its context, quietly making the change look reasonable.

The implementation-agent contract in Chapter 5 already names this gap. Its escalation conditions say: if compatibility is unclear, stop and request a review subagent. This chapter defines what that subagent is, how it is isolated from the agent that called it, and what it owes back.

## What breaks without this

Without a separate delegation primitive, teams reach for one of two bad defaults.

The first is asking the same agent to review its own work in the same conversation. This produces the self-grading problem above: the reviewing pass inherits every assumption the implementing pass already made, so it tends to confirm rather than catch.

The second is spinning up a second full agent with its own role contract for every specialized pass — a review agent, a security agent, a docs agent — each with the overhead of Chapter 5's role-contract machinery: named responsibility, standing permissions, an identity in the permission matrix. Most specialized passes are short-lived, single-purpose, and disposable. Giving each one the full weight of a persistent role is over-engineering that makes the system harder to reason about, not safer.

A subagent is the missing middle: bounded like a role, but scoped to one delegated task and discarded when it returns.

## Design principle: subagents are isolated delegated workers

A subagent is an isolated delegated worker. It receives a scoped task and the specific inputs it needs, works in a context the parent does not share, and returns a structured result. It does not persist, and it does not carry standing permissions of its own — it operates within whatever the parent agent was already allowed to request.

| Property | Main agent (Chapter 5) | Subagent |
|---|---|---|
| Lifetime | Persists across a session or role | Exists for one delegated task |
| Context | Accumulates over the work | Isolated: receives only what the task needs |
| Accountability | Owns the outcome | Produces evidence; does not own the decision |
| Identity | Named role with standing permissions | Borrows the parent's authorization for the task |
| Output | Patch, artifact, or completed work | Findings, risks, and a recommendation |

Use a subagent when a task benefits from separation of context, independent judgment, or specialized focus that the main agent's accumulated context would compromise. Keep work in the main agent when the task is small, low-risk, or when the main agent already owns the concern and delegation would only add a handoff with nothing gained.

| Subagent type | Typical output |
|---|---|
| Review subagent | Findings, risks, and suggested fixes |
| Test-planning subagent | Test matrix and edge cases |
| Security subagent | Threat notes and sensitive-surface review |
| Documentation subagent | Doc impact and update checklist |

Subagents are not extra autonomy for its own sake. They are a boundary mechanism: a way to guarantee that a specific pass happens without the context that would bias it.

## The isolation model

Isolation is the entire value of a subagent. If the parent hands over its full conversation history "to save time," the subagent inherits the same assumptions the parent already made, and the isolation that justified delegating in the first place is gone.

A subagent's context should be built deliberately, not inherited wholesale:

| Input | Include? | Why |
|---|---|---|
| The specific task description | Yes | This is the delegation itself |
| The artifact under review (diff, spec, plan) | Yes | The subagent needs the actual thing to inspect |
| Relevant steering (Chapter 3) | Yes | Repo doctrine applies regardless of who is looking |
| The parent's full conversation history | No | Reintroduces the bias isolation exists to remove |
| The parent's stated conclusions | No | The point is an independent pass, not a second opinion primed to agree |
| Prior review findings on the same change, if re-reviewing | Sometimes | Useful for delta review; state explicitly when included |

A subagent that receives the parent's reasoning alongside the artifact is not isolated — it is a second voice reading the same script. Pass the artifact, the task, and the doctrine. Do not pass the argument for why the artifact is already fine.

## Output contract

A subagent's output is evidence, not a decision. It should be structured well enough that the parent agent — or a human reviewer — can act on it without re-deriving the analysis:

- what was reviewed, and against what scope
- findings, each tied to a specific location in the artifact
- severity or risk level per finding
- a suggested fix or next step, where applicable
- an explicit statement of what was *not* covered, if the task was scoped narrowly

An unstructured paragraph of impressions is not a subagent output. If the findings cannot be enumerated, they cannot be tracked, assigned, or verified as addressed.

## Delegation accountability

Delegating a task does not delegate the accountability for the outcome. The parent agent — or the human who reads the parent's summary — decides what to do with a subagent's findings. A subagent that flags a compatibility risk has not blocked the change; it has produced evidence. Someone with the standing to decide still has to weigh it.

This mirrors the boundary Chapter 5 draws between an agent's role and its output contract: the role decides what counts as done, not the tool that helped produce the evidence. A subagent is one of the tools that produces evidence. It is never the thing that decides the work is finished.

Treating a subagent's clean report as automatic sign-off is the most common way this accountability gets lost. "The review subagent found nothing" is a data point, not an approval.

## Anti-patterns

| Anti-pattern | Why it fails | Better pattern |
|---|---|---|
| Self-review in the same context | The reviewing pass inherits the implementing pass's assumptions | Delegate review to an isolated subagent |
| Context dump | Passing the parent's full history defeats isolation | Pass only the task, the artifact, and relevant steering |
| Subagent as approver | Treating a clean subagent report as sign-off | The parent or a human still owns the decision |
| Subagent sprawl | A persistent role contract for every disposable pass | Reserve full agent roles (Chapter 5) for standing responsibilities |
| Unstructured findings | A prose summary that cannot be tracked or verified | Require a findings format: location, severity, suggested fix |
| Redundant delegation | Two subagents assigned the same review with no coordination | One subagent per concern; state scope explicitly in the task |

## Nexus case study

### Before this chapter

The implementation-agent role from Chapter 5 is bounded, but its own escalation conditions expose a gap: when compatibility is unclear, the contract says to "stop and request a review subagent" — a primitive Nexus has not yet defined.

### Design decision

Nexus defines a subagent delegation model: a small set of named subagent types, each with a scoped task, an isolated context, and a required output contract. The implementation-agent's escalation condition now resolves to something concrete.

### Implementation

```md
# Subagent: compatibility-review

## Trigger
Implementation-agent escalates when API compatibility is unclear.

## Scope
Review the proposed diff against nexus-service's public response contract.
Does not decide whether to ship; does not fix the code.

## Inputs
- The diff under review
- nexus-service/AGENTS.md (API conventions, versioning rules)
- Known downstream client list, if available

## Explicitly excluded
- The implementation-agent's conversation history or stated rationale

## Output contract
- Compatibility findings, each tied to a file and line range
- Risk level per finding: breaking / risky / safe
- Suggested fix per breaking or risky finding
- Explicit note of any part of the contract not covered
```

Nexus adds parallel definitions for test-planning, security, and documentation subagents, each following the same shape: trigger, scope, inputs, explicit exclusions, and an output contract.

### After this chapter

Nexus uses subagents for compatibility review, test planning, security checks, and documentation review. Each is isolated from the agent that triggered it, and each returns findings the implementation-agent or a human reviewer must still act on.

### Lesson

Isolation is not a side effect of delegation. It is the reason to delegate. A subagent that shares the parent's context is a second draft of the same opinion, not a second opinion.

## Quick Reference

### Use a subagent when...

| Use a subagent for... | Keep in the main agent when... |
|---|---|
| Independent review | The task is small and low risk |
| Specialized analysis | The main agent already owns the concern |
| Parallel evidence gathering | Shared context would be simpler and safer |
| Boundary-sensitive work | Delegation would hide accountability |

### Subagent definition checklist

- Named trigger: what condition starts the delegation
- Scoped task: one concern, not a general "review this"
- Explicit inputs: task, artifact, relevant steering
- Explicit exclusions: parent's history and conclusions stay out
- Structured output contract: findings, severity, suggested fix
- A named owner for what happens to the findings

### Nexus asset

Subagent delegation model, starting with `compatibility-review`, extended to test-planning, security, and documentation subagents.

### Reader action

Take one escalation condition from an existing agent role contract. Write the subagent it should resolve to: trigger, scope, inputs, exclusions, and output contract. Confirm the subagent's context does not include the parent's reasoning — only the artifact and the task.
