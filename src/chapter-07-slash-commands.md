# Chapter 7: Slash Commands

> **Status: in progress.** This chapter has a complete structure and plan below.
> Prose, templates, and worked examples are being written.

## What this chapter will deliver

- Command anatomy: intent, inputs, routing, outputs, and limits
- When to use a slash command versus steering, a skill, or a tool
- Command catalog design and maintenance
- Slash commands in the broader workflow — how they connect to agents, skills, and hooks
- Nexus slash command catalog anchored to the API contract running example

## Reader problem

Good workflows decay when every person starts them differently.

A team may agree that risky changes need planning, review, verification, and artifacts. If the entry point is still an improvised prompt, the workflow remains fragile.

## Design principle: slash commands are workflow triggers

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

### Before this chapter

Workflows are hard to trigger consistently.

### After this chapter

Developers use commands like `/plan-change`, `/review-pr`, and `/create-adr`.

## Quick Reference

| Use a slash command when... | Prefer another primitive when... |
|---|---|
| The workflow has a repeatable entry point. | You only need stable repository rules: steering. |
| The same task should start consistently. | You need a reusable procedure: skill. |
| Routing should be explicit. | You need external access: tool contract. |
| Outputs should be predictable. | You need proof of completion: verification. |
