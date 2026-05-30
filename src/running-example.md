# Running Example: Backward-Compatible API Contract Change

A developer asks AI to update a service API in `nexus-service` so clients can receive a new optional field in a response.

In the ad-hoc state, the assistant may produce a plausible patch: update the DTO, modify the handler, adjust one test, and move on. But without structure, the change may miss backward compatibility, schema or versioning rules, downstream client impact, authorization boundaries, documentation, rollout notes, or verification evidence.

As Nexus matures, this same change moves through repository steering, planning, reusable skills, subagent review, permission controls, durable artifacts, and verification evidence.

## Why this example

The backward-compatible API contract change is broad enough for senior developers, architects, platform engineers, reviewers, and technical leaders.

It touches code, tests, API design, compatibility, documentation, rollout, authorization, verification evidence, and durable artifacts without depending on a narrow domain such as payments or a platform-only scenario such as deployment configuration.

Secondary examples may include service rollout configuration changes, dependency upgrades, authorization changes, or payment retry/idempotency changes. These are useful in specific chapters, but the primary running example is the backward-compatible API contract change.

## Chapter-area mapping

| Chapter area | Backward-compatible API contract example |
|---|---|
| Structure | The change is treated as a governed workflow, not a casual prompt. |
| Vocabulary | The team separates agent, skill, artifact, verification, permission, and tool. |
| Agent | An implementation agent owns the bounded API change. |
| Subagent | A review subagent checks compatibility, downstream client impact, and edge cases. |
| Steering | `AGENTS.md` defines API conventions, versioning rules, test commands, ownership boundaries, and unsafe files. |
| Skill | An API-change test-plan skill generates contract, compatibility, authorization, documentation, and regression checks. |
| Slash command | `/plan-api-change` starts the standard workflow. |
| Hook | A PR evidence hook blocks incomplete API-change submissions. |
| Permissions | Access to client usage data, production examples, or sensitive payloads requires approval. |
| Context | API examples and client-impact context are bounded, sanitized, and not stored casually. |
| Specs/plans/tasks | The API change becomes a short spec, implementation plan, and task list. |
| Artifacts | An ADR or change note captures why the API contract changed. |
| Verification | The PR includes contract tests, regression tests, compatibility notes, docs updates, rollout notes, and review evidence. |
| Tools/MCP | The tool gateway exposes CI status, issue metadata, API docs, schema metadata, and safe usage metadata. |
| Repo layout | Specs, ADRs, API docs, changelogs, and PR evidence are stored consistently. |
| Decisions | A decision table explains why this became a governed workflow, not just a prompt. |
| Anti-patterns | Failure case: the agent changes a response contract without checking downstream clients. |
| Portability | The same workflow maps across different coding-agent tools. |
| Maturity | The team moves from ad-hoc AI usage toward governed engineering practice. |

## Terminology

Use these terms when applying the running example:

- backward-compatible API contract change
- new optional response field
- API conventions
- schema or versioning rules
- downstream client impact
- authorization boundaries
- API docs
- contract tests
- compatibility notes
- PR evidence

Avoid using these as the primary running-example terms:

- payment retry policy change
- payment retry and idempotency policy change
- duplicate charges
- sensitive payment logs
- service rollout configuration change
- rollout timeout
- Helm value
- deployment setting

## Changing the running example later

This running example is intentionally centralized because it may change as the book evolves.

If the primary running example changes later, update:

1. this canonical running example page
2. `src/nexus-evolution.md`, if it contains chapter-by-chapter references
3. Chapter 1 Nexus case-study micro-story
4. chapter-writing guidance in `AGENTS.md`
5. any chapter template or skill that instructs authors to use the running example
6. any examples under `examples/nexus/`, if they exist

Avoid scattering full scenario descriptions across chapters. Chapters should normally reference the running example briefly and adapt only the part relevant to that chapter.
