# Chapter 4: Subagents

## Reader problem

Main agents become unreliable when every concern stays in one conversation.

Implementation, review, security analysis, test planning, and documentation require different attention. A single agent can blur those responsibilities and miss the reason a second pass exists.

## Design principle

A subagent is an isolated delegated worker. Use subagents when a task benefits from separation of context, independent review, or specialized focus.

| Subagent type | Typical output |
|---|---|
| Review subagent | Findings, risks, and suggested fixes |
| Test-planning subagent | Test matrix and edge cases |
| Security subagent | Threat notes and sensitive-surface review |
| Documentation subagent | Doc impact and update checklist |

Subagents are not extra autonomy for its own sake. They are a boundary mechanism.

## Nexus case study

Before this chapter, Nexus implementation work and review work often happen in the same thread.

Nexus introduces delegated review subagents for risky changes. For the API contract running example, a review subagent checks compatibility, downstream client impact, authorization boundaries, and documentation impact.

After this chapter, Nexus has a delegation model that separates execution from focused review.

## Quick Reference

| Use a subagent for... | Keep in the main agent when... |
|---|---|
| Independent review | The task is small and low risk |
| Specialized analysis | The main agent already owns the concern |
| Parallel evidence gathering | Shared context would be simpler and safer |
| Boundary-sensitive work | Delegation would hide accountability |
