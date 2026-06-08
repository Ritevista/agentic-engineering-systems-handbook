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

## Nexus case study

### Before this chapter

The main agent role is bounded, but some review and analysis tasks need isolation.

### After this chapter

Nexus uses subagents for compatibility review, test planning, security checks, and documentation review.

## Quick Reference

| Use a subagent for... | Keep in the main agent when... |
|---|---|
| Independent review | The task is small and low risk |
| Specialized analysis | The main agent already owns the concern |
| Parallel evidence gathering | Shared context would be simpler and safer |
| Boundary-sensitive work | Delegation would hide accountability |
