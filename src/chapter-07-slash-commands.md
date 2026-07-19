# Chapter 7: Slash Commands

## Reader problem

Good workflows decay when every person starts them differently.

A team may agree that risky changes need planning, review, verification, and artifacts. If the entry point is still an improvised prompt, the workflow remains fragile: one developer's version of "plan this change" produces a spec; another's produces two paragraphs and a patch. The doctrine exists in steering, the procedure exists in a skill, but nothing forces either one to actually run.

## What breaks without this

Steering (Chapter 3) states the rules. Skills (Chapter 4) encode the procedure. Neither one triggers itself. Without a standard entry point, invoking the right workflow depends on someone remembering it exists and phrasing a prompt that happens to invoke it. That is not a workflow; it is a hope that today's prompt resembles yesterday's.

The failure compounds with agents. An agent that is supposed to escalate to a subagent, run a skill, and attach evidence needs a reliable way to start that sequence — not a fresh natural-language description assembled under time pressure.

## Design principle: slash commands are workflow triggers

A slash command is a workflow trigger. It gives people and agents a standard way to start a known procedure, with a defined shape rather than a fresh negotiation every time.

| Command concern | What it should define |
|---|---|
| Intent | What workflow starts |
| Inputs | What task context is required |
| Routing | Which agent, skill, or checklist is invoked |
| Outputs | What artifact or evidence is expected |
| Limits | What the command must not do |

A command is an interface, not a shortcut for typing less. `/plan-api-change` is not shorthand for "please help me plan an API change" — it is a contract that a specific sequence runs, with specific inputs, producing a specific artifact. The five fields above are what make that contract inspectable instead of implicit.

Meta-prompting can help shape command behavior internally, but the command itself is the operational interface a team relies on. Its value is that intent, inputs, routing, outputs, and limits stay stable and reviewable — not that it was assembled cleverly.

## Command anatomy

**Intent** names the workflow in one line: what problem this command exists to start. If the intent needs a paragraph to explain, the command is trying to do too much.

**Inputs** are the task-specific facts the command needs before it can route anywhere: a change description, a target module, a ticket reference. A command with no defined inputs will improvise them, which reintroduces the inconsistency the command was supposed to remove.

**Routing** is the command's real job: which agent role it invokes, which skill it runs, which checklist it attaches. Routing should be explicit and inspectable — a teammate reading the command definition should be able to say exactly what happens next without running it.

**Outputs** state what the command is expected to produce: a spec, a plan, a checklist, a PR comment, an ADR draft. A command with no defined output cannot be verified as having worked; it can only be trusted.

**Limits** state what the command must not do on its own — it must not merge, must not bypass approval gates, must not skip verification. Limits keep a convenient trigger from quietly becoming an unreviewed shortcut around the controls the rest of the book builds.

## When to use a slash command versus an adjacent primitive

| Use a slash command when... | Prefer another primitive when... |
|---|---|
| The workflow has a repeatable entry point. | You only need stable repository rules: steering. |
| The same task should start consistently. | You need a reusable procedure: skill. |
| Routing should be explicit. | You need external access: tool contract. |
| Outputs should be predictable. | You need proof of completion: verification. |

A command is not a replacement for the skill or agent it routes to — it is the door. Building the workflow logic directly into the command definition, instead of routing to a skill or agent that owns it, duplicates procedure in two places and guarantees they drift.

## Command catalog design and maintenance

A catalog is a small, named, discoverable set of commands — not an ever-growing list that only its author remembers. Three practices keep it usable:

**Name commands after intent, not implementation.** `/plan-api-change` survives a change in which agent or skill it routes to. A name tied to internal mechanics breaks every time the mechanics change.

**Keep routing changes invisible to callers, visible to reviewers.** The command's name and inputs are the stable contract; what it routes to internally can evolve. Treat a routing change like any other change to the underlying skill or agent — reviewed, not silent — but do not require callers to learn a new command name for it.

**Retire commands deliberately.** A catalog that only grows becomes as unreliable as no catalog: nobody can tell which of thirty overlapping commands is the current one. Mark a command deprecated, point it at its replacement, and remove it on a schedule — do not let it linger unmaintained next to its successor.

## Slash commands in the broader workflow

A command does not act alone. It is the trigger; the rest of the chapters in this book are what it triggers into:

- Steering (Chapter 3) constrains what the routed agent or skill is allowed to do.
- A skill (Chapter 4) supplies the reusable procedure the command starts.
- An agent (Chapter 5) or subagent (Chapter 6) is what the command's routing actually invokes.
- A hook (Chapter 8) can run before a command starts — to check preconditions — or after it finishes — to check its output before it counts as done.
- Verification (Chapter 13) defines what evidence the command's output must include before the workflow is considered complete.

A command that routes to nothing structured — that just expands into a large prompt inline — has not gained anything over an improvised message. The value of a command comes entirely from what it reliably connects to.

## Anti-patterns

| Anti-pattern | Why it fails | Better pattern |
|---|---|---|
| Command as disguised prompt | The command expands to a big inline prompt instead of routing to a skill or agent | Route to a named, reusable skill or agent |
| Catalog sprawl | Dozens of overlapping commands; no one knows which is current | Name by intent, deprecate deliberately, keep the catalog small |
| Silent routing change | The command's underlying behavior changes without review | Treat routing changes like any other reviewed change |
| Undefined output | No one can tell whether the command "worked" | State the expected artifact or evidence explicitly |
| Command bypasses limits | The command merges, deploys, or skips approval on its own | State limits explicitly; commands trigger workflows, not override controls |

## Nexus case study

### Before this chapter

Workflows are hard to trigger consistently. Developers describe the same intent — "help me plan this API change" — in a dozen different ways, and the resulting depth varies with how the prompt happened to be phrased.

### Design decision

Nexus defines a small slash command catalog anchored to the backward-compatible API contract running example. Each command states intent, required inputs, routing, expected output, and explicit limits.

### Implementation

```md
# Command: /plan-api-change

## Intent
Start the standard workflow for a backward-compatible API contract change.

## Inputs
- Target service and endpoint
- Description of the proposed change
- Known or suspected downstream clients, if any

## Routing
Invokes the implementation-agent role (Chapter 5) and the
api-change-test-plan skill (Chapter 4).

## Output
- A short spec: scope, compatibility notes, and acceptance criteria
- A task list

## Limits
- Does not implement the change.
- Does not merge or deploy.
- Does not skip the compatibility-review subagent if compatibility is unclear.
```

```md
# Command: /review-pr

## Intent
Trigger the review pass for an open change.

## Inputs
- PR or diff reference

## Routing
Invokes the compatibility-review subagent (Chapter 6) and attaches
the PR evidence checklist (Chapter 13).

## Output
- Structured findings with severity and suggested fixes
- Updated PR evidence checklist

## Limits
- Does not approve or merge the PR.
- Findings require a human or the implementation-agent to act on them.
```

```md
# Command: /create-adr

## Intent
Capture an architectural decision as a durable artifact.

## Inputs
- Decision summary and context
- Alternatives considered, if any

## Routing
Invokes the ADR template (Chapter 12).

## Output
- A committed ADR file in the repository's decisions directory.

## Limits
- Does not implement the decision.
```

### After this chapter

Developers use commands like `/plan-api-change`, `/review-pr`, and `/create-adr` instead of improvising prompts of varying depth. Each command's routing, inputs, and expected output are inspectable in the repository rather than living in one person's habits.

### Lesson

A command is only as strong as what it routes to. Define the destination — the skill, the agent, the checklist — before naming the trigger.

## Quick Reference

### Command design checklist

- Intent stated in one line
- Required inputs named explicitly
- Routing is explicit and inspectable
- Expected output or artifact stated
- Limits state what the command must not do
- Retired commands point to their replacement

### Nexus asset

Slash command catalog: `/plan-api-change`, `/review-pr`, `/create-adr`, anchored to the backward-compatible API contract running example.

### Reader action

Pick one workflow your team currently starts by improvised prompt. Write it as a command definition: intent, inputs, routing, output, limits. Confirm the routing points to a real skill or agent, not an inline prompt.
