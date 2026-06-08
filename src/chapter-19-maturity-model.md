# Chapter 19: Team Maturity Model

> **Status: in progress.** This chapter has a complete structure and plan below.
> Prose, templates, and worked examples are being written.

## What this chapter will deliver

- How to use the maturity ladder as an assessment instrument
- Evidence required at each level
- How to move from one level to the next
- Team and repository-wide assessment process
- Nexus maturity assessment rubric

## Reader problem

AI adoption is hard to improve when the team cannot describe its current state.

One group may have strong prompts. Another may have repository steering. A third may have tool integrations without governance. Without a maturity model, leaders confuse activity with capability.

## Design principle: a maturity model is a measurement instrument

This chapter expands the maturity ladder introduced in the introduction. It adds assessment evidence and a next move for each level so teams can locate themselves and act.

A maturity model is a measurement tool. It should show what capability exists, what evidence proves it, and what the next practical move is.

| Level | Pattern | Evidence | Next move |
|---|---|---|---|
| L0 | Ad-hoc prompting | Useful outputs remain in chat; no repeatability | Add a shared repo steering file |
| L1 | Individual discipline | Personal prompts and manual checks in use | Commit one shared skill or checklist |
| L2 | Repository steering | AGENTS.md, repo conventions, local verification in place | Convert a repeated workflow into a reusable skill |
| L3 | Reusable workflows | Skills, slash commands, hooks, and repeatable artifacts in use | Add permission tiers and tool contracts |
| L4 | Governed tool use | Permissions, sandboxing, tool contracts, and auditability in place | Instrument the control plane; add metrics and review loops |
| L5 | Engineering control plane | Metrics, policies, lifecycle management, and portability in place; continuous improvement running | Extend the model to the next team or product area |

Methodologies such as BMAD or lightweight spec-driven development can be discussed as adoption patterns. They are not substitutes for measuring the control plane itself.

## Using the maturity ladder as an assessment instrument

_Planned: how to assess a repository or team against each level; what counts as evidence; how to avoid self-reporting bias._

## Evidence for each level

_Planned: expand the Evidence column with concrete, inspectable signals for each level — what an auditor would look for._

## Moving between maturity levels

_Planned: the practical steps to move from each level to the next; common blockers; how to prioritize the next move._

## Team and repository-wide assessment

_Planned: how to run a maturity assessment across multiple repositories or teams; how to track progress over time._

## Applying the maturity model to the running example

_Planned: thread the canonical running example (see running-example.md) through this chapter's concept._

## Nexus case study

### Before this chapter

Adoption is inconsistent across teams.

### Design decision

_Planned._

### Implementation

_Planned._

### After this chapter

Nexus becomes a measurable engineering operating model.

### Lesson

_Planned._

## Templates

_Planned: maturity assessment rubric — the named Nexus asset for this chapter._

## Quick Reference

| Weak maturity signal | Strong maturity signal |
|---|---|
| Many assistant sessions | Repeatable workflows |
| Impressive demos | Durable artifacts |
| Private prompt libraries | Repository steering and skills |
| Broad tool access | Governed permissions |
| Claimed productivity | Evidence-backed engineering outcomes |

## Source Notes

_Planned. Analysis, decision frameworks, and Nexus Engineering Control Plane examples are original to this field manual; source-backed references are added only where tool- or protocol-specific behavior is discussed._
