# Chapter 8: Hooks

## Reader problem

Manual guardrails fail when the team is busy.

Reviewers forget checklist items. Developers skip local checks under time pressure. Agents claim completion without attaching evidence. If a rule matters, the workflow should not depend entirely on memory.

## Design principle

A hook is lifecycle automation or a guardrail. It runs at a defined point in the workflow and checks, blocks, records, or routes work.

| Hook point | Typical use |
|---|---|
| Pre-change | Confirm scope and permissions |
| Pre-commit | Run local formatting or static checks |
| Pre-PR | Require evidence and artifact links |
| Pre-release | Confirm operational readiness |

Hooks should make important behavior harder to skip. They should not become opaque policy engines that no one can inspect.

## Nexus case study

Before this chapter, Nexus relies on reviewers to notice missing evidence.

Nexus adds a PR evidence hook. For the API contract running example, the hook checks that contract tests, compatibility notes, documentation impact, and review evidence are present before the workflow can be treated as complete.

After this chapter, Nexus has a lifecycle guardrail that supports reviewers instead of replacing them.

## Quick Reference

| Hook design question | Good answer |
|---|---|
| When does it run? | At a specific lifecycle point. |
| What does it enforce? | A narrow, reviewable rule. |
| What does it produce? | A clear pass/fail result or evidence record. |
| How does it fail? | Loudly enough for the team to act. |
