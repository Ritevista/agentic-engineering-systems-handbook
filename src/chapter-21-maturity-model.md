# Chapter 21: Team Maturity Model

## Reader problem

AI adoption is hard to improve when the team cannot describe its current state.

One group may have strong prompts. Another may have repository steering. A third may have tool integrations without governance. Without a maturity model, leaders confuse activity with capability — a team running many assistant sessions per day is not the same as a team with repeatable, governed workflows, and without an instrument to tell them apart, the busier-looking team gets mistaken for the more mature one.

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

Methodologies such as BMAD or lightweight spec-driven development can be discussed as adoption patterns. They are not substitutes for measuring the control plane itself — a team can follow a rigorous methodology inside a single session and still be at L0 if nothing survives the session as a shared, reusable asset.

Each level's "Evidence" column is not a self-assessment question — it names an artifact this book already defined. L2's evidence is a real `AGENTS.md` (Chapter 3). L3's evidence is real skills, commands, and hooks (Chapters 4, 7, 8) that other people on the team actually use, not just one the assessor wrote once. L4's evidence is a real permission matrix and tool contracts (Chapters 9, 18) with an audit trail behind them, not a stated intention to add one. Assessing a level means checking whether the artifact exists and is in active use, not whether the team believes it has reached that level.

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

### Structuring a team-level adoption review

A team-level review is the assessment instrument in practice: a recurring, structured check of where a team actually sits on the ladder, not a one-time badge.

- **Who attends**: the team's technical lead or a designated owner, plus one reviewer from outside the team — an outside perspective is what stops a team from grading its own homework, the same self-assessment risk Chapter 6 addresses for code review.
- **What evidence is reviewed**: the concrete artifact for the team's claimed level and the level above it — the actual `AGENTS.md`, the actual permission matrix, the actual metrics dashboard (Chapter 20) if claiming L4 or L5. A claimed level with no artifact to point to is not yet that level.
- **What gets updated**: the team's current level, a named next move from the transition table above, and an owner and target date for that move. A review that confirms the current level without setting the next move has not used the instrument for anything.

This mirrors the monthly governance review from Chapter 20 in structure — evidence in, concrete action out — because a maturity review is a governance review scoped to the ladder itself rather than to spend and verification metrics specifically.

### Extending the model to a second team or product area

A maturity model that only ever applied to one team is a pilot, not an operating model. Extending it without forking the control plane means reusing the portable layer (Chapter 19) and letting only the team-specific detail vary:

- The ladder, its evidence requirements, and the transition table stay identical across every team — this is the portable layer, the same way a role contract's responsibility and escalation conditions are portable across tools.
- What differs per team is which artifacts satisfy the evidence bar locally: a second team's `AGENTS.md` will state different conventions than the first, but the requirement that one exists and is in use does not change.
- Central governance (Chapter 15's layered repository pattern) tracks every team's current level in one place, so an org-wide view does not require re-deriving the ladder per team.

A second team starting from L0 is not a failure of the first team's rollout. Each team climbs the same ladder at its own pace; the model's job is to make that pace visible, not to force synchronization.

## Nexus case study

### Before this chapter

Adoption is inconsistent across teams. `nexus-service` has repository steering and a growing skill library; a newer team on `nexus-delivery` is still at ad-hoc prompting, and there is no shared instrument to say so plainly or to plan the next move.

### Design decision

Nexus adopts the maturity ladder as a standing assessment instrument, with a team-level adoption review run against it and a plan to extend it to every team without forking the model.

### Implementation

```md
# Nexus maturity assessment: nexus-service

## Current level
L3 — reusable workflows

## Evidence
- AGENTS.md: present, in active use (L2 evidence)
- Skills: api-change-test-plan, in use by implementation-agent (L3 evidence)
- Slash commands: /plan-api-change, /review-pr, /create-adr (L3 evidence)
- Hooks: pre-change, pre-commit, pre-pr-evidence, pre-release (L3 evidence)
- Permission matrix: not yet present (L4 evidence gap)

## Next move
Introduce a permission matrix and one enforcement hook for
sensitive-data access. Owner: platform lead. Target: next quarter.
```

```md
# Nexus maturity assessment: nexus-delivery

## Current level
L0 — ad-hoc prompting

## Evidence
No shared AGENTS.md; deploy-related prompts are personal and
undocumented.

## Next move
Add a shared AGENTS.md with one concrete rule: deploy approval
boundaries. Owner: nexus-delivery lead. Target: this month.
```

### After this chapter

Nexus becomes a measurable engineering operating model. `nexus-service` and `nexus-delivery` are assessed against the same ladder, with different current levels and different next moves, tracked centrally rather than left to each team's self-perception.

### Lesson

A maturity level is a claim until it points to an artifact. Assess the evidence, not the impression, and always leave the review with a named next move.

## Quick Reference

### Weak signal / strong signal

| Weak maturity signal | Strong maturity signal |
|---|---|
| Many assistant sessions | Repeatable workflows |
| Impressive demos | Durable artifacts |
| Private prompt libraries | Repository steering and skills |
| Broad tool access | Governed permissions |
| Claimed productivity | Evidence-backed engineering outcomes |

### Nexus asset

Maturity assessment rubric applied per team, with a team-level adoption review process and a plan for extending the ladder across teams without forking it.

### Reader action

Assess one team against the ladder using its actual artifacts, not its self-perception. Name the current level, the evidence, and the next move — then assign an owner and a date for that move.
