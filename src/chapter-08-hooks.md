# Chapter 8: Hooks

## Reader problem

Manual guardrails fail when the team is busy.

Reviewers forget checklist items under a backlog. Developers skip local checks under deadline pressure. Agents claim completion without attaching the evidence Chapter 13 requires. None of this is a discipline failure in any one person — it is what happens when a rule's only enforcement mechanism is someone remembering it at the right moment. If a rule matters, the workflow should not depend entirely on memory.

## What breaks without this

Steering (Chapter 3) states what should happen. Slash commands (Chapter 7) trigger a workflow. Neither one checks that the workflow's required steps actually ran. A rule that lives only in a document is enforced only by whoever happens to read the document that day — and under time pressure, that is close to nobody.

The gap is sharpest at handoff points: the moment before a commit lands, the moment before a PR opens, the moment before a release ships. These are exactly the moments a rushed human is most likely to skip a step, and exactly the moments an agent is most likely to claim a step happened without proof.

## Design principle: hooks are lifecycle guardrails

A hook is lifecycle automation or a guardrail. It runs at a defined point in the workflow and checks, blocks, records, or routes work — automatically, every time, regardless of who or what is doing the work.

| Hook point | Typical use |
|---|---|
| Pre-change | Confirm scope and permissions |
| Pre-commit | Run local formatting or static checks |
| Pre-PR | Require evidence and artifact links |
| Pre-release | Confirm operational readiness |

Hooks should make important behavior harder to skip. They should not become opaque policy engines that no one can inspect — a hook that silently rewrites, blocks, or approves work with no visible reason is a guardrail that has become a black box, and a black box is not something a reviewer can trust or debug.

## Authoring a hook contract

A hook needs the same discipline as an agent role contract or a permission rule: an inspectable definition, not an ad-hoc script that grew opinions over time.

| Field | Question it answers |
|---|---|
| When | What lifecycle point triggers this hook? |
| What | What specific, narrow condition does it check? |
| Output | What does it produce: pass/fail, a record, a routed action? |
| Failure mode | What happens when the check fails — block, warn, or escalate? |

The word "narrow" matters. A hook that checks one thing is inspectable and debuggable. A hook that bundles ten unrelated checks into one pass/fail becomes a black box the moment it fails — nobody can tell which of the ten conditions actually broke without reading the implementation. Prefer several narrow hooks over one broad one.

## Hooks as guardrails versus hooks as automation

Not every hook exists to stop something. The chapter title uses both words on purpose, because conflating them produces two different failure modes.

| Type | Job | Failure if conflated |
|---|---|---|
| Guardrail hook | Blocks or flags work that violates a rule | A guardrail that only logs is not a guardrail — it is a diary |
| Automation hook | Performs a routine step so a human does not have to | Automation that also silently blocks is a guardrail wearing a convenience label |

A pre-commit formatter is automation: it does something useful and does not need to stop the commit to do it. A pre-PR evidence check is a guardrail: if the evidence is missing, the PR should not proceed, because the entire point of Chapter 13's verification requirement is that it is not optional. Know which job a given hook is doing before you write it, and do not let a convenience hook quietly grow the power to block, or a guardrail quietly grow into something that "usually" blocks but sometimes just warns.

## Hook failures and escalation paths

A hook that fails needs to fail loudly enough for the team to act — and it needs a defined path for what happens next.

| Failure behavior | When appropriate |
|---|---|
| Block outright | The condition is non-negotiable: missing evidence, out-of-scope write, failing test |
| Warn and require acknowledgment | The condition is a judgment call the human should see but may override, with the override recorded |
| Escalate to a named owner | The hook cannot decide, but the workflow cannot silently continue either |

A hook that fails silently — logs an error nobody reads and lets the workflow continue — is worse than no hook, because it creates the appearance of a check that never actually ran. If a hook can fail, its failure path needs the same clarity as its success path: who is notified, what the record shows, and whether the workflow is blocked or merely flagged.

## Anti-patterns

| Anti-pattern | Why it fails | Better pattern |
|---|---|---|
| Opaque hook | No one can inspect what it checks or why it failed | Narrow, named condition with a documented reason |
| Guardrail that only warns | The rule becomes optional under pressure, exactly when it matters most | Block on non-negotiable conditions |
| Bundled mega-hook | Ten checks in one pass/fail; a failure gives no signal which broke | Split into narrow, independently reportable hooks |
| Silent failure | The hook errors out and the workflow proceeds anyway | Fail loudly; define the escalation path |
| Convenience hook that blocks | An automation step quietly grows the power to stop work, with no review | Keep guardrail and automation roles separate and explicit |

## Nexus case study

### Before this chapter

Humans remember guardrails manually. Evidence checklists get skipped under deadline pressure, and nothing catches it until a reviewer notices — sometimes after merge.

### Design decision

Nexus adds hooks at four lifecycle points, each with a narrow condition, a defined output, and an explicit failure mode: pre-change, pre-commit, pre-release, and an evidence-check hook tied to the PR evidence checklist from Chapter 13.

### Implementation

```md
# Hook: pre-change-scope-check

## When
Before an agent begins implementation work.

## What
Confirms the requested change stays within the scope declared in the
active spec or task (Chapter 11) and within the agent's role contract
(Chapter 5).

## Output
Pass, or a list of out-of-scope files/actions.

## Failure mode
Block. The agent must narrow scope or escalate for an expanded approval.
```

```md
# Hook: pre-commit-local-checks

## When
Before a commit is created.

## What
Runs formatting and static analysis.

## Output
Pass/fail per check.

## Failure mode
Block the commit; this is automation, not a judgment call.
```

```md
# Hook: pre-pr-evidence-check

## When
Before a PR is opened for review.

## What
Confirms the PR evidence checklist (Chapter 13) is attached: test
output, compatibility notes, and risk notes for any flagged item.

## Output
Pass, or a list of missing evidence fields.

## Failure mode
Block. This is the guardrail this chapter exists to enforce — an
incomplete evidence checklist is exactly the condition Chapter 13
requires to be non-optional.
```

```md
# Hook: pre-release-readiness-check

## When
Before a release that includes agent-assisted changes ships.

## What
Confirms rollback criteria (Chapter 14) are defined for every
included change above a low-risk threshold.

## Output
Pass, or a list of changes missing rollback criteria.

## Failure mode
Escalate to the release owner named in steering.
```

### After this chapter

Nexus adds pre-change, pre-commit, pre-release, and evidence-check hooks. Rules that used to depend on a reviewer's memory now run automatically at the moment they matter, with a defined failure mode instead of a silent skip.

### Lesson

A rule enforced only by memory is a rule that fails exactly when the team is busiest. Move it into a hook, and give the hook's failure a real consequence.

## Quick Reference

### Hook design question → good answer

| Hook design question | Good answer |
|---|---|
| When does it run? | At a specific lifecycle point. |
| What does it enforce? | A narrow, reviewable rule. |
| What does it produce? | A clear pass/fail result or evidence record. |
| How does it fail? | Loudly enough for the team to act. |

### Nexus asset

Hook policy: pre-change, pre-commit, pre-PR evidence check, and pre-release readiness check for the API contract running example.

### Reader action

Pick one rule your team currently enforces by memory or convention. Write it as a hook contract: when it runs, what it checks, what it produces, and what happens when it fails. If the answer to "what happens when it fails" is "nothing, really," that is the gap this chapter closes.
