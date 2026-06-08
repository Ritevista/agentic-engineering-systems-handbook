# Chapter 8: Hooks

> **Status: in progress.** This chapter has a complete structure and plan below.
> Prose, templates, and worked examples are being written.

## What this chapter will deliver

- Hook types and their lifecycle points
- How to author a hook contract — when, what, output, failure mode
- Hook failures and escalation paths
- Hooks as guardrails versus hooks as automation — and when each applies
- Nexus hook policy for the API contract running example

## Reader problem

Manual guardrails fail when the team is busy.

Reviewers forget checklist items. Developers skip local checks under time pressure. Agents claim completion without attaching evidence. If a rule matters, the workflow should not depend entirely on memory.

## Design principle: hooks are lifecycle guardrails

A hook is lifecycle automation or a guardrail. It runs at a defined point in the workflow and checks, blocks, records, or routes work.

| Hook point | Typical use |
|---|---|
| Pre-change | Confirm scope and permissions |
| Pre-commit | Run local formatting or static checks |
| Pre-PR | Require evidence and artifact links |
| Pre-release | Confirm operational readiness |

Hooks should make important behavior harder to skip. They should not become opaque policy engines that no one can inspect.

## Hook types and lifecycle points

_Planned: expand the lifecycle points table with examples of check, block, record, and route behaviors at each point._

## Authoring a hook contract

_Planned: what a hook definition must specify — trigger point, check logic, pass/fail criteria, output, and escalation behavior._

## Hook failures and escalation

_Planned: what happens when a hook fails; how the team responds; how to avoid hooks that block silently or without actionable output._

## Guardrail versus automation

_Planned: when a hook should enforce by blocking versus when it should record and alert; the difference between compliance gates and efficiency automation._

## Applying hooks to the running example

_Planned: thread the canonical running example (see running-example.md) through this chapter's concept._

## Nexus case study

### Before this chapter

Humans remember guardrails manually.

### Design decision

_Planned._

### Implementation

_Planned._

### After this chapter

Nexus adds pre-change, pre-commit, pre-release, and evidence-check hooks.

### Lesson

_Planned._

## Templates

_Planned: hook policy — the named Nexus asset for this chapter._

## Quick Reference

| Hook design question | Good answer |
|---|---|
| When does it run? | At a specific lifecycle point. |
| What does it enforce? | A narrow, reviewable rule. |
| What does it produce? | A clear pass/fail result or evidence record. |
| How does it fail? | Loudly enough for the team to act. |

## Source Notes

_Planned. Analysis, decision frameworks, and Nexus Engineering Control Plane examples are original to this field manual; source-backed references are added only where tool- or protocol-specific behavior is discussed._
