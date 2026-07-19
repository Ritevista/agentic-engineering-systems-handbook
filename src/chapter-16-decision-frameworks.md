# Chapter 16: Decision Frameworks

## Reader problem

Teams need a way to choose the right primitive.

Without decision frameworks, every workflow design becomes taste: one team adds an agent, another writes a prompt, another creates a tool, and another adds a checklist. The result is inconsistency disguised as flexibility — each choice might be individually defensible, but nobody can predict what the next team will build for the same problem, and no one can review a choice against a stated standard because no standard was written down.

## Design principle: decision frameworks make choices reviewable

Decision frameworks are reusable tables for choosing structure. They convert judgment into reviewable criteria.

| Decision | Criteria |
|---|---|
| Steering or skill? | Stable doctrine belongs in steering; repeatable procedure belongs in a skill. |
| Skill or slash command? | A playbook explains how; a command starts the workflow. |
| Agent or subagent? | A primary role owns work; a subagent handles isolated delegated work. |
| Hook or checklist? | A hook enforces at a lifecycle point; a checklist guides human review. |
| Tool or context? | A tool performs external capability; context informs the agent. |

Good decision tables make trade-offs explicit. They do not remove engineering judgment — a table narrows the decision to the few criteria that actually matter and forces the chooser to state which side of the criterion applies, which is a very different act from picking whatever feels familiar.

## How to read and use a decision table

A decision table is not a lookup — it is a forcing function. Reading one well means checking each criterion against the actual situation, not scanning for the row that matches the answer you already wanted.

Every table in this book, including the one above, follows the same shape:

1. **The decision**: two or more options that are genuinely easy to confuse.
2. **The criterion**: the specific property that actually distinguishes them.
3. **The recommendation**: which option the criterion points to.

The value collapses if the criterion is vague. "Use an agent when it feels like the work needs autonomy" is not a criterion — it cannot be checked against a real situation, and two people can read it and reach opposite conclusions with equal confidence. "A primary role owns work; a subagent handles isolated delegated work" can be checked: does this piece of work need to own an outcome, or does it need one isolated pass with a return value? That is answerable.

## Criteria for choosing between adjacent primitives

The strongest decision-table criteria in this book recur across chapters because they are the properties that actually matter for agentic engineering structure:

| Criterion | What it distinguishes |
|---|---|
| Risk | Whether the action needs an approval gate (Chapter 9) or can proceed unattended |
| Ownership | Whether one role is accountable for the outcome, or the output is evidence for someone else to weigh (Chapter 6) |
| Auditability | Whether the action needs a durable, inspectable record (Chapter 9, Chapter 12) |
| Speed | Whether the workflow can tolerate a blocking gate or needs to proceed with monitoring (Chapter 9's oversight modes) |
| Blast radius | How much damage a mistake could cause before something stops it (Chapter 9) |

Building a new decision table for a team-specific question means picking from these — or a similarly checkable property — rather than inventing a criterion like "complexity" or "importance" that different people will weight differently.

## Common decision points

The individual chapters in this book each answer one adjacent-primitive question in depth. Collected together, they form the framework a team actually reaches for during workflow design:

| Question | Answer | See |
|---|---|---|
| Repository-wide rule, or reusable procedure? | Stable and applies broadly: steering. Repeatable task: skill. | Chapter 3, Chapter 4 |
| Reusable procedure, or one-off entry point? | The procedure is the skill; the trigger that starts it is the command. | Chapter 4, Chapter 7 |
| One bounded role, or isolated delegated pass? | Standing responsibility: agent. Scoped, disposable task: subagent. | Chapter 5, Chapter 6 |
| Enforce automatically, or ask a human to review? | Lifecycle-point automation or gate: hook. Judgment-based review: checklist. | Chapter 8, Chapter 13 |
| External capability, or informing context? | Performs an action or fetches live data: tool. Background information: context. | Chapter 10, Chapter 18 |
| Full spec, or a short task note? | Match structure to risk: contract-affecting and above needs a spec; trivial and local does not. | Chapter 11 |
| Durable record, or leave it in the session? | Anything future readers need survives as an artifact. | Chapter 12 |
| Claim of completion, or proof? | Every completion claim needs linked evidence. | Chapter 13 |
| Everything in one repo, or centralized governance? | Depends on repo count and drift tolerance; the layered pattern usually wins past a handful of repos. | Chapter 15 |

This table is the book's own decision framework, expressed as a table because that is the standard this chapter asks every team to hold itself to.

## Building and maintaining a team decision framework

A decision framework is only useful while it stays accurate and small. Three habits keep it that way:

- **Start from a real recurring confusion.** Build a table because two people on the team recently made different choices for the same kind of situation, not because a table seemed like good practice in the abstract.
- **Keep criteria checkable.** If a criterion cannot be answered by looking at the actual situation, replace it before publishing the table.
- **Review the framework when the primitives change.** A decision table for "skill or command" is only current as long as skills and commands mean what the table assumes. Chapter 3's steering and this book's own concept distinctions are the source of truth; update the table when they move, not the other way around.

A decision framework that never gets revisited becomes exactly the kind of undocumented tribal assumption it was built to replace.

## Anti-patterns

| Anti-pattern | Why it fails | Better pattern |
|---|---|---|
| Vague criteria | "Use judgment" or "if it feels right" cannot be checked | State a checkable property: risk, ownership, auditability, speed, blast radius |
| Decision by precedent alone | "We did it this way last time" with no stated reason | Cite the criterion, not just the prior example |
| Table that hides the real trade-off | The table picks a winner without showing what was given up | State what the non-chosen option would have offered |
| Stale framework | The table no longer matches how primitives are actually defined | Review when steering or concept distinctions change |
| One-person framework | The table reflects one engineer's taste, not a reviewed standard | Frameworks are artifacts (Chapter 12): reviewed and committed, not personal notes |

## Nexus case study

### Before this chapter

Teams do not know when to use agent vs skill vs tool. Two teams building similar workflows make different structural choices with no shared reasoning either could point to.

### Design decision

Nexus creates decision frameworks for workflow design, starting from the recurring confusions its own chapters already surfaced: steering vs. skill, agent vs. subagent, hook vs. checklist.

### Implementation

Nexus commits the common decision points table above as `nexus-playbook/docs/decision-framework.md` (Chapter 15's central governance repository), referenced from each product repo's `AGENTS.md` rather than duplicated per repo.

### After this chapter

Nexus creates decision frameworks for workflow design. A team choosing between a skill and a slash command for a new workflow now checks a criterion instead of asking around.

### Lesson

A decision framework's only job is to make a choice checkable by someone who was not in the room. If the criterion cannot be checked, the table is decoration.

## Quick Reference

### Framework quality signal

| Good framework trait | Weak framework trait |
|---|---|
| Uses concrete criteria | Uses vague preference |
| Separates nearby primitives | Treats all agentic terms as equivalent |
| Produces an artifact | Stays in chat |
| Can be reviewed later | Depends on one person's taste |

### Nexus asset

Decision framework document, centralized in `nexus-playbook`, covering the recurring adjacent-primitive choices from this book.

### Reader action

Find one recent workflow-design disagreement on your team. Write the decision table that would have settled it: the options, the checkable criterion, and the recommendation. Commit it where the next disagreement can find it.
