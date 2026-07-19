# Chapter 20: Metrics, Cost, and Spend Governance

## Reader problem

Teams adopting AI-assisted engineering cannot improve what they do not measure.

Without explicit metrics, the control plane has no feedback loop. Token spend grows without attribution. Verification pass rates hide quality regressions. Maturity claims remain impressionistic. Measurement is the foundation of continuous improvement at L4 and above — everything this book has built up to this point produces the events worth measuring; this chapter is where those events become a feedback loop instead of just history.

## What breaks without this

Every control this book introduces — permission tiers (Chapter 9), verification evidence (Chapter 13), rollback runbooks (Chapter 14) — produces a record. Without measurement, those records sit unread. A permission escalation happens, gets approved, and nobody notices that the same escalation has happened eleven times this month, which is a much stronger signal than any single instance: it means the permission tier is wrong, not that the eleventh request was suspicious.

Spend has the same problem in reverse. Without attribution, cost is a lump sum with no story behind it — no way to tell whether spend is concentrated in one workflow that needs redesign or spread evenly across healthy usage.

## Design principle: measure the control plane, not just the output

Measuring only code output (lines, PRs, velocity) misses what governs agent behavior. The control plane itself — permission policy, verification rate, rollback frequency, spend attribution — needs its own instrumentation.

| Metric category | Example metrics |
|---|---|
| Spend and cost | Token usage per workflow, per agent role, per team |
| Verification quality | Verification evidence rate, test pass rate, eval scores |
| Governance health | Permission escalations, sandbox violations, skipped hooks |
| Artifact durability | ADR coverage, spec currency, runbook freshness |
| Incident and rollback | Rollback frequency, mean time to escalate, incident closure rate |

Good metrics produce actionable reviews, not dashboards no one reads. A metric that never changes a decision is decoration.

## Spend governance

Spend governance needs three things: a budget structure, an attribution model, and alert thresholds — in that order, because thresholds are meaningless without knowing which budget they apply to, and attribution is meaningless without knowing which workflow class a spend event belongs to.

| Budget tier | Applies to | Typical control |
|---|---|---|
| Exploratory | Ad-hoc individual sessions, no production impact | Soft cap; monitor, no block |
| Workflow-scoped | A defined workflow (e.g. the API-change workflow) | Budget per run; alert on overrun |
| Team-scoped | Aggregate spend across a team's workflows | Monthly budget; review at the monthly loop below |
| Production-critical | Workflows touching release or incident response | Hard cap with named approver for overrun |

Attribution ties every spend event back to team, project, and workflow class — the same three dimensions that make the budget tiers above actually enforceable. A token spend event with no attribution is unbudgetable by construction: there is no tier it can be checked against.

Alert thresholds should escalate the same way Chapter 9's approval tiers do: a soft warning at a workflow-scoped overrun, a named-approver gate at a production-critical one. Reuse the escalation machinery this book already built rather than inventing a parallel one for spend specifically.

## Verification and quality metrics

Chapter 13 established that a claim of completion needs linked evidence. This chapter measures how often that evidence actually shows up.

**Verification evidence rate** is the percentage of completed work that has linked test output, review checklist completion, and risk notes attached — not merely claimed. A low or dropping rate means Chapter 13's discipline is being skipped somewhere, and it is a leading indicator: it tends to move before an incident does, not after.

**Eval scores** measure repeated agent behavior quality across sessions (Chapter 5, Chapter 13) — scope adherence, escalation behavior, output contract compliance. A quality regression shows up as a drop in one of these specific eval suites, not as a vague sense that "the agent seems worse lately." Tie any perceived regression to the specific eval suite that moved; if none moved, the regression claim needs more evidence before it becomes a governance action.

## Governance health signals

Permission escalations and skipped hooks are not incidents by themselves — they are signals about whether the permission matrix (Chapter 9) and hook policy (Chapter 8) are correctly calibrated.

| Signal | What it indicates |
|---|---|
| Repeated escalation at the same tier | The tier boundary is probably wrong; work that legitimately needs this access keeps hitting a gate designed for something riskier |
| Skipped or overridden hooks | Either the hook is too strict for a real, legitimate case, or the override path itself needs tightening |
| Sandbox violations | An agent's declared scope and its actual behavior are drifting apart |

The correction is always to feed the signal back into the actual policy — widen a permission tier that is legitimately too narrow, or tighten an override path that is being used too casually — rather than treating each individual escalation as a one-off exception to wave through.

## Review loops

Metrics only close the loop if a recurring review actually reads them and changes something. Nexus runs this monthly, not because monthly is universally correct, but because it matches the pace at which permission and steering changes are worth batching rather than actioning individually.

A monthly governance review reads:

- spend by budget tier, with any overruns and their resolution
- verification evidence rate, trended against the prior period
- governance health signals: repeated escalations, skipped hooks, sandbox violations
- rollback frequency and incident closure rate (Chapter 14)

And produces, as its output:

- specific steering amendments, if a rule is being routinely worked around
- specific skill revisions, if a skill's output is repeatedly incomplete
- specific permission tier adjustments, if escalation patterns point to a miscalibrated boundary

A review that reads the metrics but changes nothing is not a governance review — it is a status update. The output has to be a concrete change to steering, a skill, or the permission matrix, or the loop is not actually closed.

## Nexus case study

### Before this chapter

Nexus has an operating model but no feedback loop. Spend is unattributed and verification quality is assumed rather than measured — the team believes the API-change workflow is healthy because no one has complained, not because anyone has checked.

### Design decision

Nexus instruments spend, verification rate, and governance health for the API contract change workflow, and establishes a monthly review loop that feeds findings back into steering and permission policy.

### Implementation

```md
# Metrics dashboard: API contract change workflow

## Spend
- Tier: workflow-scoped
- Attribution: nexus-service team, api-change workflow class
- This period: [token spend], [vs. budget]

## Verification
- Evidence rate: [% of merged changes with complete PR evidence checklist]
- Contract test pass rate: [%]

## Governance health
- Permission escalations this period: [count, by tier]
- Hooks skipped or overridden: [count, with reason]

## Incidents
- Rollback frequency: [count]
- Mean time to escalate: [duration]
```

```md
# Monthly governance review agenda

1. Review spend by tier; resolve any overruns.
2. Review verification evidence rate trend.
3. Review governance health signals; identify repeated escalations.
4. Review incident and rollback metrics.
5. Decide: any steering amendment, skill revision, or permission
   tier adjustment this period requires. Assign an owner and date.
```

Nexus's first monthly review finds that the sensitive-data permission tier (Chapter 9) is being escalated to almost every week for the same category of request — read access to anonymized client usage samples for compatibility testing. The review's corrective action is a new, narrower permission tier for that specific, recurring, lower-risk case, rather than continuing to route it through the tier meant for genuinely sensitive access.

### After this chapter

Nexus instruments spend, verification rate, and governance health. Monthly review loops feed corrections back into steering and permission policy — the miscalibrated sensitive-data tier gets fixed because the metrics made the pattern visible, not because someone happened to notice.

### Lesson

A metric that never triggers a change in steering, a skill, or a permission tier was not worth collecting. Close the loop, or the dashboard is theater.

## Anti-patterns

| Anti-pattern | Why it fails | Better pattern |
|---|---|---|
| Unattributed spend | Cost is a lump sum with no workflow, team, or project story | Attribute every spend event to team, project, and workflow class |
| Dashboards no one reads | Metrics exist but never trigger a decision | Tie every review to required, concrete outputs |
| Escalations treated as one-offs | The same permission gap gets waved through repeatedly instead of fixed | Feed repeated escalations back into the permission matrix |
| Vague quality regression claims | "It seems worse" with no eval suite to point to | Tie regression claims to the specific eval or metric that moved |
| Review with no output | The meeting happens; nothing in steering, skills, or permissions changes | Require a named steering, skill, or permission change per review |

## Quick Reference

### Measure → why it matters

| Measure | Why it matters |
|---|---|
| Token spend by workflow | Attributes cost; finds waste |
| Verification evidence rate | Shows whether controls are being used |
| Rollback frequency | Signals steering or verification gaps |
| Permission escalations | Indicates policy friction or missing tiers |
| Artifact currency | Shows whether decisions stay documented |

### Nexus asset

Metrics dashboard and monthly governance review agenda for the API contract change workflow, with spend attribution and permission-tier feedback.

### Reader action

Pick one metric from the table above that your team does not currently track. Start collecting it for one workflow. At the first review, ask specifically what steering, skill, or permission change the data points to — if the answer is none, keep tracking until it produces one.
