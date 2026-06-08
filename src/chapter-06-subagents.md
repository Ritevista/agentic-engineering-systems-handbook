# Chapter 6: Subagents

> **Status: in progress.** This chapter has a complete structure and plan below.
> Prose, templates, and worked examples are being written.

## What this chapter will deliver

- When to delegate work to a subagent and when to keep it in the main agent
- Subagent types and their output contracts
- Isolation model and context boundary design
- Delegation accountability and the subagent delegation model
- Nexus subagent delegation model for API contract review

## Reader problem

Main agents become unreliable when every concern stays in one conversation.

Implementation, review, security analysis, test planning, and documentation require different attention. A single agent can blur those responsibilities and miss the reason a second pass exists.

## Design principle: subagents are isolated delegated workers

A subagent is an isolated delegated worker. Use subagents when a task benefits from separation of context, independent review, or specialized focus.

| Subagent type | Typical output |
|---|---|
| Review subagent | Findings, risks, and suggested fixes |
| Test-planning subagent | Test matrix and edge cases |
| Security subagent | Threat notes and sensitive-surface review |
| Documentation subagent | Doc impact and update checklist |

Subagents are not extra autonomy for its own sake. They are a boundary mechanism.

## When to delegate to a subagent

_Planned: criteria for deciding when isolation adds value versus when it adds unnecessary overhead._

## Subagent types and output contracts

_Planned: define what each subagent type is responsible for, what inputs it receives, and what structured output it must produce._

## Isolation model and context boundaries

_Planned: explain what isolation means for a subagent — what context it receives, what it cannot see, and why that separation matters for review quality._

## Delegation accountability

_Planned: how responsibility is assigned when work is delegated; how the main agent and subagent results are reconciled._

## Applying subagents to the running example

_Planned: thread the canonical running example (see running-example.md) through this chapter's concept._

## Nexus case study

### Before this chapter

The main agent role is bounded, but some review and analysis tasks need isolation.

### Design decision

_Planned._

### Implementation

_Planned._

### After this chapter

Nexus uses subagents for compatibility review, test planning, security checks, and documentation review.

### Lesson

_Planned._

## Templates

_Planned: subagent delegation model — the named Nexus asset for this chapter._

## Quick Reference

| Use a subagent for... | Keep in the main agent when... |
|---|---|
| Independent review | The task is small and low risk |
| Specialized analysis | The main agent already owns the concern |
| Parallel evidence gathering | Shared context would be simpler and safer |
| Boundary-sensitive work | Delegation would hide accountability |

## Source Notes

_Planned. Analysis, decision frameworks, and Nexus Engineering Control Plane examples are original to this field manual; source-backed references are added only where tool- or protocol-specific behavior is discussed._
