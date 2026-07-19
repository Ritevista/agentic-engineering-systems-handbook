# Chapter 15: Repo Layout

## Reader problem

Agent-ready repositories fail when guidance is scattered.

If steering, skills, specs, artifacts, examples, and verification evidence all live in different ad-hoc places, teams cannot reuse or govern the workflow. An agent working in a new repository has to rediscover where everything lives every time, and a human reviewer has no consistent place to check for the artifacts the rest of this book requires. Layout is part of the control plane, not a cosmetic concern.

## What breaks without this

Every primitive this book has introduced — steering, skills, agent role contracts, permission matrices, specs, artifacts — needs a place to live that both humans and agents can find without being told. When location is ad hoc, discoverability depends on tribal knowledge: someone has to already know that this repo keeps its ADRs in `docs/decisions` while another keeps them in `adr/`. That knowledge does not transfer to a new hire, a new agent session, or a new repository.

The cost compounds across a multi-repo organization. If every repository organizes its steering and skills differently, a shared skill (Chapter 4) cannot be dropped into a new repo and simply work — someone has to first figure out where "here" expects it to go.

## Design principle: layout makes structure discoverable

Repository layout should make AI-assisted engineering structure discoverable.

| Concern | Typical location |
|---|---|
| Repository steering | `AGENTS.md` or equivalent |
| Reusable skills | `skills/` |
| Specs and plans | `specs/` or `docs/` |
| Durable decisions | `docs/adrs/` or `docs/decisions/` |
| Examples | `examples/` |
| Verification evidence | PR description, CI, or evidence directory |

The exact names can vary by team or language ecosystem convention. The responsibilities should not: every agent-ready repository needs an answer to "where does steering live," "where do skills live," and "where does a decision get recorded," and that answer should be the same answer every time someone asks it in that repository.

## Standard directory structure

A minimal agent-ready repository layout looks like this:

```text
repo-root/
├── AGENTS.md                 # repository steering (Chapter 3)
├── skills/                   # reusable task playbooks (Chapter 4)
│   └── <skill-name>/
│       └── SKILL.md
├── specs/                    # specs and plans (Chapter 11)
│   └── <change-name>.md
├── docs/
│   └── decisions/            # ADRs (Chapter 12)
│       └── ADR-NNN-<title>.md
├── examples/                 # sanitized worked examples
└── src/ (or equivalent)      # application code
```

Verification evidence (Chapter 13) does not always need its own directory — a PR template that requires linked evidence, or a CI system that preserves run history, can satisfy discoverability without a dedicated folder. What matters is that the location is consistent and known, not that it is elaborate.

## Monorepo and multi-repo layout patterns

The right layout pattern depends on how many repositories the organization's agentic engineering surface spans.

**Monorepo**: one `AGENTS.md` at the root can state organization-wide doctrine, with module-specific steering nested where it applies — the pattern Chapter 3 and Chapter 5 already assume when they mention "module steering, if present." Skills and specs can live at the root and apply everywhere, or nest under a module when they are module-specific.

**Multi-repo**: steering, skills, and governance need a deliberate distribution strategy, or they drift independently in every repository. Three patterns cover most organizations:

| Pattern | How it works | Trade-off |
|---|---|---|
| Central governance repo | Shared skills, ADR conventions, and cross-repo policy live in one repo; product repos reference or vendor them in | Single source of truth; requires a sync or reference mechanism |
| Per-repo duplication | Each repo carries its own full steering and skill set | No sync mechanism needed; drifts silently without active maintenance |
| Layered | Org-wide doctrine lives centrally; repo-local steering only states what is specific to that repo | Balances consistency and local autonomy; requires clarity on which layer wins on conflict |

The layered pattern is usually the strongest default for organizations with more than a handful of repositories: it keeps org-wide rules in one place while letting a product repo state only what genuinely differs.

## Layout conventions, naming, and discoverability

Three habits keep a layout usable as the repository grows:

**Put steering at the repo root.** `AGENTS.md` at the root is the first place both agents and humans look. Burying it in a subdirectory defeats the purpose of a predictable location.

**Keep skills separate from steering.** Steering is doctrine; skills are procedure, and they evolve on a different schedule (Chapter 4). Mixing them into one file or directory makes both harder to maintain independently.

**Store artifacts in durable, named paths.** `docs/decisions/ADR-014-...` is discoverable by pattern even to someone who has never seen this repository. A decision buried in a wiki page or a Slack thread is not part of the repository's layout at all — it is outside the control plane this chapter defines.

## Nexus case study

### Before this chapter

Every repo organizes AI guidance differently. `nexus-service` keeps its steering in a wiki, `nexus-delivery` keeps deployment rules in a README, and there is no shared place for organization-level ADRs or skills.

### Design decision

Nexus defines a common layout applied across three repository roles: a product/service repository, a delivery/platform repository, and a playbook/governance repository — the layered multi-repo pattern, with organization-wide doctrine centralized and repo-local steering stating only what differs.

### Implementation

```text
nexus-service/                # product/service repo
├── AGENTS.md                 # local steering: API conventions, test commands, ownership
├── skills/
│   └── api-change-test-plan/
├── specs/
└── docs/decisions/

nexus-delivery/                # delivery/platform repo
├── AGENTS.md                 # local steering: deploy rules, approval boundaries
├── ci-templates/
└── docs/decisions/

nexus-playbook/                # playbook/governance repo
├── AGENTS.md                 # org-wide doctrine, referenced by product/delivery repos
├── skills/                   # shared skills, vendored or referenced by product repos
├── docs/decisions/           # org-level ADRs
└── runbooks/
```

`nexus-service/AGENTS.md` states only what is specific to that service — API conventions, local test commands, ownership boundaries — and references `nexus-playbook` for organization-wide rules on permissions, verification, and incident response. This is the layered pattern: one place owns the doctrine that should not drift per repository, and each product repo stays short.

### After this chapter

Nexus defines common layout for steering, specs, docs, artifacts, and skills — consistent across the product, delivery, and playbook repositories, with a clear rule for which layer wins when local and organization-wide steering could conflict.

### Lesson

A layout only pays off when it is the same answer every time. Pick locations, keep the responsibilities separate, and apply the pattern to every repository the same way.

## Quick Reference

### Layout rules and reasons

| Layout rule | Reason |
|---|---|
| Put steering at the repo root. | Agents and humans find local rules quickly. |
| Keep skills separate from steering. | Procedures evolve differently from doctrine. |
| Store artifacts in durable paths. | Decisions survive chat and tool sessions. |
| Keep examples realistic but sanitized. | Readers can copy patterns safely. |

### Nexus asset

Repository layout applied across `nexus-service`, `nexus-delivery`, and `nexus-playbook`, using the layered multi-repo pattern.

### Reader action

Pick one repository your team maintains. Check whether steering, skills, specs, and decisions each have one consistent, predictable location. Where the answer is "it depends who you ask," that is the gap this chapter closes.
