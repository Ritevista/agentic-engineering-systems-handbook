# Chapter 7: Slash Commands

> Status: To be done.

## Reader problem

Good workflows decay when every person starts them differently.

A team may agree that risky changes need planning, review, verification, and artifacts. If the entry point is still an improvised prompt, the workflow remains fragile.

## Design principle

A slash command is a workflow trigger. It gives people and agents a standard way to start a known procedure.

| Command concern | What it should define |
|---|---|
| Intent | What workflow starts |
| Inputs | What task context is required |
| Routing | Which agent, skill, or checklist is invoked |
| Outputs | What artifact or evidence is expected |
| Limits | What the command must not do |

Meta-prompting can help shape command behavior, but the command is an operational interface, not a private prompt.

## Nexus case study

Before this chapter, Nexus developers start repeatable AI workflows through inconsistent chat phrasing.

Nexus introduces `/plan-api-change` as a standard workflow trigger. The command routes the API contract running example through steering, planning, compatibility checks, and evidence expectations.

After this chapter, Nexus has a repeatable entry point for governed work.

## Quick Reference

| Use a slash command when... | Prefer another primitive when... |
|---|---|
| The workflow has a repeatable entry point. | You only need stable repository rules: steering. |
| The same task should start consistently. | You need a reusable procedure: skill. |
| Routing should be explicit. | You need external access: tool contract. |
| Outputs should be predictable. | You need proof of completion: verification. |
