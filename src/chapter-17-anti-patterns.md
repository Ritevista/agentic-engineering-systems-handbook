# Chapter 17: Anti-Patterns

> **Status: in progress.** This chapter has a complete structure and plan below.
> Prose, templates, and worked examples are being written.

## What this chapter will deliver

- Named failure patterns across all major primitives
- God agents and unbounded role failures
- Mega-skills, fake verification, and completion theater
- Context flooding and tool overreach
- Chat as system of record and other persistence failures
- Nexus anti-pattern library

## Reader problem

Bad AI-assisted workflows often look productive at first.

The failure is not always obvious. A team may ship patches quickly while accumulating hidden context, weak evidence, unclear responsibility, and unsafe access patterns.

## Design principle: anti-patterns are named failure modes

Anti-patterns are named failure patterns. They help teams recognize when useful assistant output is masking structural weakness.

| Anti-pattern | Failure |
|---|---|
| God agent | One role owns too many responsibilities |
| Mega-skill | A reusable playbook becomes an unreadable process blob |
| Fake verification | The agent claims checks ran without evidence |
| Context flooding | More input hides the important constraints |
| Tool overreach | External capability is added without blast-radius control |
| Chat as system of record | Decisions disappear after the session |

Naming the failure makes it easier to design the correction.

## Nexus case study

### Before this chapter

Teams repeat the same AI mistakes.

### After this chapter

Nexus documents god agents, mega-skills, fake verification, context flooding, and tool overreach.

## Quick Reference

| If you see... | Check for... |
|---|---|
| One agent doing everything | Missing role boundaries |
| Large opaque prompt templates | Missing skills or commands |
| Confident completion summaries | Missing verification evidence |
| Pasted logs and docs everywhere | Missing context policy |
| Broad tool permissions | Missing approval and sandbox rules |
