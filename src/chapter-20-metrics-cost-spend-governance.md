# Chapter 20: Metrics, Cost, and Spend Governance

> **Status: in progress.** This chapter has a complete structure and plan below.
> Prose, templates, and worked examples are being written.

## What this chapter will deliver

- What to measure in an agentic engineering system and why
- Cost and token spend governance: budgets, alerts, and attribution
- Quality metrics: verification pass rate, artifact durability, and rollback frequency
- Review loops: how metrics feed back into steering, skills, and permission policy
- Nexus metrics dashboard and spend governance model

## Reader problem

Teams adopting AI-assisted engineering cannot improve what they do not measure.

Without explicit metrics, the control plane has no feedback loop. Token spend grows without attribution. Verification pass rates hide quality regressions. Maturity claims remain impressionistic. Measurement is the foundation of continuous improvement at L4 and above.

## Design principle: measure the control plane, not just the output

Measuring only code output (lines, PRs, velocity) misses what governs agent behavior. The control plane itself — permission policy, verification rate, rollback frequency, spend attribution — needs its own instrumentation.

| Metric category | Example metrics |
|---|---|
| Spend and cost | Token usage per workflow, per agent role, per team |
| Verification quality | Verification evidence rate, test pass rate, eval scores |
| Governance health | Permission escalations, sandbox violations, skipped hooks |
| Artifact durability | ADR coverage, spec currency, runbook freshness |
| Incident and rollback | Rollback frequency, mean time to escalate, incident closure rate |

Good metrics produce actionable reviews, not dashboards no one reads.

## Spend governance

_Planned: budget tiers by workflow type, alert thresholds, and attribution model_

_Planned: how to tie spend back to team, project, and workflow class_

## Verification and quality metrics

_Planned: how to measure verification completeness across agent sessions_

_Planned: eval-backed quality scoring and what a quality regression looks like_

## Governance health signals

_Planned: what permission escalations and skipped hooks indicate about steering gaps_

_Planned: how to feed governance health metrics back into the permission matrix_

## Review loops

_Planned: monthly governance review cadence: what to read, who attends, what gets updated_

_Planned: how metrics trigger steering amendments and skill revisions_

## Applying to running example

_Planned: Nexus instruments the API contract change workflow — spend per session, verification pass rate, rollback frequency — and runs a first quarterly governance review._

## Nexus case study

### Before this chapter

Nexus has an operating model but no feedback loop. Spend is unattributed and verification quality is assumed.

### After this chapter

Nexus instruments spend, verification rate, and governance health. Monthly review loops feed corrections back into steering and permission policy.

## Templates

_Planned: metrics dashboard template, spend governance policy template, monthly review agenda_

## Quick Reference

| Measure | Why it matters |
|---|---|
| Token spend by workflow | Attributes cost; finds waste |
| Verification evidence rate | Shows whether controls are being used |
| Rollback frequency | Signals steering or verification gaps |
| Permission escalations | Indicates policy friction or missing tiers |
| Artifact currency | Shows whether decisions stay documented |
