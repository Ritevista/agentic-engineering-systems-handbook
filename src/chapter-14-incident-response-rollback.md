# Chapter 14: Incident Response and Rollback

> **Status: in progress.** This chapter has a complete structure and plan below.
> Prose, templates, and worked examples are being written.

## What this chapter will deliver

- What qualifies as an agentic incident and how to detect one early
- Rollback criteria, triggers, and runbook structure for AI-assisted changes
- The handoff pattern: when to pause automation and escalate to a human
- Incident record format and post-incident review for agent-involved failures
- Nexus incident response playbook for the API contract change running example

## Reader problem

Teams shipping agent-assisted changes need a response plan when something goes wrong.

An agent can produce a plausible-looking change that breaks a contract, introduces a regression, or writes to an unintended scope. If no rollback criteria exist, the team defaults to improvisation. Incident response is not optional at governance maturity above L2.

## Design principle: rollback criteria must be defined before the change ships

Rollback criteria belong in the plan, not in the post-mortem. An agent-assisted change that lacks explicit rollback conditions and a designated escalation path is not ready to merge.

| Incident type | Typical signal |
|---|---|
| Contract regression | Consumer test fails after deploy |
| Scope overreach | Agent modified files outside the declared scope |
| Data corruption | Writes to unintended records or state |
| Permission violation | Tool called outside its declared permission tier |
| Verification gap | Change shipped without required evidence |

Naming the incident type makes the rollback path and detection method explicit.

## When to pause and escalate

_Planned: criteria for halting an in-progress agentic workflow and handing off to a human_

_Planned: the escalation path in steering — who is on call and how to reach them_

## Rollback runbook structure

_Planned: five-field runbook format: trigger, scope, steps, verification, and record_

_Planned: how rollback evidence feeds the post-incident review_

## Post-incident review for agent-involved failures

_Planned: five-beat review: timeline, cause, contributing agent behavior, steering gap, and corrective action_

_Planned: how the review feeds back into steering, skills, hooks, and permission rules_

## Applying to running example

_Planned: Nexus discovers a backward-incompatible contract change reached consumers before the consumer test hook ran. Incident record, rollback steps, and post-incident steering update._

## Nexus case study

### Before this chapter

Agentic changes that regress production are handled by improvisation.

### After this chapter

Nexus has a rollback runbook, escalation path, and post-incident review process for agent-involved failures.

## Templates

_Planned: incident record template, rollback runbook template, post-incident review template_

## Quick Reference

| Do this | Avoid this |
|---|---|
| Define rollback criteria before merge. | Improvise rollback after the incident. |
| Name the escalation path in steering. | Assume humans will notice automatically. |
| Record what the agent did in the incident. | Treat agent actions as unauditable. |
| Feed the review back into steering. | Close the incident without a corrective action. |
