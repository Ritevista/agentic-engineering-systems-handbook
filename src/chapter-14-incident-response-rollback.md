# Chapter 14: Incident Response and Rollback

## Reader problem

Teams shipping agent-assisted changes need a response plan when something goes wrong.

An agent can produce a plausible-looking change that breaks a contract, introduces a regression, or writes to an unintended scope. If no rollback criteria exist, the team defaults to improvisation. Incident response is not optional at governance maturity above L2 — once agents are producing changes that reach production, "what do we do when one is wrong" needs an answer that exists before the moment it is needed.

## Design principle: rollback criteria must be defined before the change ships

Rollback criteria belong in the plan, not in the post-mortem. An agent-assisted change that lacks explicit rollback conditions and a designated escalation path is not ready to merge — this is the same discipline Chapter 11 requires for acceptance criteria, applied to the failure case instead of the success case.

| Incident type | Typical signal |
|---|---|
| Contract regression | Consumer test fails after deploy |
| Scope overreach | Agent modified files outside the declared scope |
| Data corruption | Writes to unintended records or state |
| Permission violation | Tool called outside its declared permission tier |
| Verification gap | Change shipped without required evidence |

Naming the incident type makes the rollback path and detection method explicit. "Something is wrong" does not tell a responder what to check first; "contract regression" tells them to look at consumer tests, and "permission violation" tells them to look at the audit trail from Chapter 9.

## When to pause and escalate

Not every anomaly needs a full incident response. The team needs a clear line between "the agent noticed something odd and adjusted" and "the workflow needs a human before it goes further."

Halt an in-progress agentic workflow and escalate when:

- the action would exceed the agent's declared scope or permission tier (Chapter 9) — this should already block automatically, but a near-miss is worth a pause to confirm why it was attempted
- verification (Chapter 13) fails in a way the agent cannot resolve within its role
- the agent's own escalation conditions, stated in its role contract (Chapter 5), are met
- a subagent (Chapter 6) returns a finding above the risk threshold the workflow defined

The escalation path itself belongs in steering (Chapter 3), not in tribal knowledge: who is on call, how to reach them, and what information the escalation must include. An escalation path that exists only as "ask in the team channel and hope someone responds" is not a path — it is a delay with a Slack icon.

## Rollback runbook structure

A rollback runbook is a runbook (Chapter 12): an operational procedure written before it is needed, and tested rather than assumed to work. A useful rollback runbook has five fields:

| Field | Answers |
|---|---|
| Trigger | What condition means this runbook should run |
| Scope | What the rollback affects, and what it explicitly does not touch |
| Steps | The exact sequence to execute, in order |
| Verification | How to confirm the rollback actually worked |
| Record | Where the incident and rollback action get logged |

The verification field matters as much as the steps: a rollback that is assumed to have worked because the steps completed is not verified. Chapter 13's verification discipline applies here too — command output or a check result, not a description of what should have happened.

Rollback evidence — what was rolled back, when, and confirmed how — feeds directly into the post-incident review below. Without that record, the review starts from memory instead of evidence.

## Post-incident review for agent-involved failures

A post-incident review for an agent-involved failure asks the same questions a human-caused incident review asks, plus one specific to this book's structure: which control was supposed to catch this, and why didn't it.

A useful review covers five beats:

1. **Timeline**: what happened, in sequence, with timestamps.
2. **Cause**: the proximate cause of the failure.
3. **Contributing agent behavior**: what the agent did, and whether it acted within its declared role, permissions, and scope.
4. **Steering gap**: what rule, permission, hook, or verification requirement was missing or insufficient to prevent this.
5. **Corrective action**: the specific change to steering, a skill, a hook, or the permission matrix that closes the gap.

Beat three is the one generic incident reviews often miss for agent-involved failures: it is not enough to know what broke. The review needs to know whether the agent stayed inside its declared boundary and the boundary was wrong, or the agent exceeded a boundary that was correctly declared but not enforced (Chapter 9's declaration-versus-enforcement gap). Those are different corrective actions.

The review is only useful if beat five actually happens. A review that documents the failure but does not change steering, a skill, a hook, or a permission rule guarantees the same incident recurs, because nothing in the system learned from it.

## Anti-patterns

| Anti-pattern | Why it fails | Better pattern |
|---|---|---|
| Improvised rollback after the incident | No tested procedure exists when it's needed most | Write and test the rollback runbook before the change ships |
| No named escalation owner | "Someone will notice" is not a path | Name the on-call owner and escalation method in steering |
| Assumed rollback success | The steps ran, but no one confirmed the system actually recovered | Require a verification step, not just a completed steps list |
| Review with no corrective action | The same failure recurs because nothing in steering changed | Every review closes with a specific change to steering, a hook, or permissions |
| Treating agent incidents as generic incidents | Missing whether the agent stayed inside its declared boundary | Review agent behavior against its role contract explicitly |

## Nexus case study

### Before this chapter

Agentic changes that regress production are handled by improvisation. When a backward-incompatible response change reaches consumers, the team's first response is to figure out what a rollback would even look like.

### Design decision

Nexus defines rollback criteria, an escalation path, and a post-incident review process before the next agent-assisted API change ships — not after the next incident.

### Implementation

Nexus discovers that a contract change reached consumers before the pre-PR evidence hook (Chapter 8) was in place to catch it: an older change, shipped before that hook existed, silently dropped a field a known client depended on.

```md
# Incident record: INC-2026-014

## Trigger
Consumer test failure reported by [client team] after deploy.

## Type
Contract regression

## Timeline
- 14:02 — Change deployed
- 14:47 — Client team reports failing integration
- 14:55 — Rollback runbook executed
- 15:10 — Rollback verified; consumer tests pass against rolled-back version

## Contributing agent behavior
Implementation-agent completed the change within its declared scope.
No permission or scope violation. The pre-PR evidence hook that would
now require compatibility-review sign-off did not yet exist at merge time.

## Steering gap
No hook enforced compatibility-review before this change shipped.

## Corrective action
Pre-PR evidence hook (Chapter 8) now required for all nexus-service
changes touching public response shape; backfilled to this incident.
```

```md
# Rollback runbook: nexus-service deploy rollback

## Trigger
Consumer contract test failure within 1 hour of a nexus-service deploy.

## Scope
Reverts the nexus-service deploy only. Does not affect nexus-delivery
pipeline configuration or other services.

## Steps
1. Identify last known-good deploy tag.
2. Redeploy that tag via [deploy command].
3. Confirm consumer contract tests pass against the redeployed version.

## Verification
Consumer contract test suite run against production; must pass.

## Record
File an incident record using the template above; link the deploy
and rollback CI runs.
```

### After this chapter

Nexus has a rollback runbook, escalation path, and post-incident review process for agent-involved failures. The gap that caused INC-2026-014 — no compatibility gate before merge — is now closed by the Chapter 8 hook, and the incident record proves it.

### Lesson

A rollback plan invented during the incident is not a plan. Write the runbook, name the escalation owner, and confirm the review always ends in a concrete change to steering.

## Templates

### Incident record template

```md
# Incident record: [ID]

## Trigger
## Type
## Timeline
## Contributing agent behavior
## Steering gap
## Corrective action
```

### Rollback runbook template

```md
# Rollback runbook: [system]

## Trigger
## Scope
## Steps
## Verification
## Record
```

### Post-incident review template

```md
# Post-incident review: [incident ID]

## Timeline
## Cause
## Contributing agent behavior
## Steering gap
## Corrective action
```

## Quick Reference

### Do this / avoid this

| Do this | Avoid this |
|---|---|
| Define rollback criteria before merge. | Improvise rollback after the incident. |
| Name the escalation path in steering. | Assume humans will notice automatically. |
| Record what the agent did in the incident. | Treat agent actions as unauditable. |
| Feed the review back into steering. | Close the incident without a corrective action. |

### Nexus asset

Incident response playbook: incident record, rollback runbook, and post-incident review templates for the API contract running example.

### Reader action

Pick one agent-assisted workflow currently in production. Write its rollback runbook's trigger and verification fields. If you cannot state how you would confirm a rollback worked, that is the gap this chapter closes.
