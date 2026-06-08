# Chapter 21: Team Maturity Model

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

## Adoption and change management

A maturity model without an adoption plan stays a diagram. Teams need a practical path from their current level to the next.

| Transition | Common blocker | Practical move |
|---|---|---|
| L0 → L1 | No shared starting point | Add a shared `AGENTS.md` with one concrete rule |
| L1 → L2 | Rules stay in personal prompts | Commit the first shared skill to the repository |
| L2 → L3 | Workflows are not triggered consistently | Add one slash command with a defined output contract |
| L3 → L4 | Tools are used without permission boundaries | Introduce a permission matrix and one enforcement hook |
| L4 → L5 | No feedback loop on the control plane itself | Instrument one metric; hold a monthly governance review |

Change management for an engineering control plane is not a one-time rollout. Each level adds new obligations, new reviewers, and new maintenance work. Adoption needs ownership: someone must track the current level, set the next target, and keep the evidence current.

_Planned: how to structure a team-level adoption review: who attends, what evidence is reviewed, what gets updated_

_Planned: how to extend the maturity model to a second team or product area without forking the control plane_

## Nexus case study

### Before this chapter

Adoption is inconsistent across teams.

### After this chapter

Nexus becomes a measurable engineering operating model.

## Quick Reference

| Weak maturity signal | Strong maturity signal |
|---|---|
| Many assistant sessions | Repeatable workflows |
| Impressive demos | Durable artifacts |
| Private prompt libraries | Repository steering and skills |
| Broad tool access | Governed permissions |
| Claimed productivity | Evidence-backed engineering outcomes |
