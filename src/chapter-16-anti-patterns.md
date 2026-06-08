# Chapter 16: Anti-Patterns

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

## God agents and unbounded roles

_Planned: what a god agent looks like; why unbounded responsibility degrades output quality and accountability; the correction._

## Mega-skills and prompt soup

_Planned: how skills become unreadable; the signs of a mega-skill; how to decompose it._

## Fake verification and completion theater

_Planned: what fake verification looks like; why confident summaries are not evidence; how to require actual proof._

## Context flooding and tool overreach

_Planned: how adding more input hides constraints; how tool access expands without review; the corrections._

## Chat as system of record and other persistence failures

_Planned: why decisions in chat disappear; how this relates to artifacts and durable outputs (Chapter 12)._

## Applying anti-patterns to the running example

_Planned: thread the canonical running example (see running-example.md) through this chapter's concept._

## Nexus case study

### Before this chapter

Teams repeat the same AI mistakes.

### Design decision

_Planned._

### Implementation

_Planned._

### After this chapter

Nexus documents god agents, mega-skills, fake verification, context flooding, and tool overreach.

### Lesson

_Planned._

## Templates

_Planned: anti-pattern library — the named Nexus asset for this chapter._

## Quick Reference

| If you see... | Check for... |
|---|---|
| One agent doing everything | Missing role boundaries |
| Large opaque prompt templates | Missing skills or commands |
| Confident completion summaries | Missing verification evidence |
| Pasted logs and docs everywhere | Missing context policy |
| Broad tool permissions | Missing approval and sandbox rules |

## Source Notes

_Planned. Analysis, decision frameworks, and Nexus Engineering Control Plane examples are original to this field manual; source-backed references are added only where tool- or protocol-specific behavior is discussed._
