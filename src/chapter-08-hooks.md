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

## Nexus case study

### Before this chapter

Humans remember guardrails manually.

### After this chapter

Nexus adds pre-change, pre-commit, pre-release, and evidence-check hooks.

## Quick Reference

| Hook design question | Good answer |
|---|---|
| When does it run? | At a specific lifecycle point. |
| What does it enforce? | A narrow, reviewable rule. |
| What does it produce? | A clear pass/fail result or evidence record. |
| How does it fail? | Loudly enough for the team to act. |
