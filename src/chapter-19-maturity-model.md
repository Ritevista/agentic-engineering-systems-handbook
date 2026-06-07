# Chapter 19: Team Maturity Model

> Status: To be done.

## Reader problem

AI adoption is hard to improve when the team cannot describe its current state.

One group may have strong prompts. Another may have repository steering. A third may have tool integrations without governance. Without a maturity model, leaders confuse activity with capability.

## Design principle

A maturity model is a measurement tool. It should show what capability exists, what evidence proves it, and what the next practical move is.

| Level | Pattern | Evidence |
|---|---|---|
| L0 | Ad-hoc prompting | Useful outputs remain in chat |
| L1 | Individual discipline | Personal prompts, manual checks, local habits |
| L2 | Repository steering | Shared repo rules and verification expectations |
| L3 | Reusable workflows | Skills, commands, hooks, and artifacts |
| L4 | Governed tool access | Permissions, tool contracts, and auditability |
| L5 | Continuous improvement | Metrics, review loops, and maturity assessment |

Methodologies such as BMAD or lightweight spec-driven development can be discussed as adoption patterns. They are not substitutes for measuring the control plane itself.

## Nexus case study

Before this chapter, Nexus has practices but no shared maturity assessment.

Nexus introduces a maturity rubric across `nexus-service`, `nexus-delivery`, and `nexus-playbook`. Each repository is assessed by evidence: steering quality, workflow reuse, permission boundaries, verification records, and durable artifacts.

After this chapter, Nexus has a way to improve deliberately instead of celebrating scattered AI usage.

## Quick Reference

| Weak maturity signal | Strong maturity signal |
|---|---|
| Many assistant sessions | Repeatable workflows |
| Impressive demos | Durable artifacts |
| Private prompt libraries | Repository steering and skills |
| Broad tool access | Governed permissions |
| Claimed productivity | Evidence-backed engineering outcomes |
