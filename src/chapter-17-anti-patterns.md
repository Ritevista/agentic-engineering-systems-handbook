# Chapter 17: Anti-Patterns

## Reader problem

Bad AI-assisted workflows often look productive at first.

The failure is not always obvious. A team may ship patches quickly while accumulating hidden context, weak evidence, unclear responsibility, and unsafe access patterns. Each individual session looks like progress; the debt only becomes visible later, usually during an incident (Chapter 14) or when a new hire asks a question nobody in the room can answer.

## Design principle: anti-patterns are named failure modes

Anti-patterns are named failure patterns. They help teams recognize when useful assistant output is masking structural weakness.

| Anti-pattern | Failure |
|---|---|
| God agent | One role owns too many responsibilities |
| Mega-skill | A reusable playbook becomes an unreadable process blob |
| Fake verification | The agent claims checks ran without evidence |
| Context flooding | More input hides the important constraints |
| Tool overreach | External capability is added without blast-radius control |
| Chat as system of record | Decisions disappear after the session |

Naming the failure makes it easier to design the correction. A team that can say "this is a god agent" has a specific, well-understood fix to reach for — split the role — instead of a vague sense that something about the setup feels wrong.

## God agents and unbounded role failures

A god agent is what happens when Chapter 5's discipline of bounded responsibility never gets applied. It implements, reviews its own work, decides what is compatible, and judges when it is done — with no boundary a reviewer can check any one of those claims against.

The tell is usually retrospective: an incident review (Chapter 14) asks "whose job was it to catch this," and the honest answer is "the same agent that made the change." A role that owns implementation, review, and sign-off has no independent check on any of them, which is precisely the self-grading problem Chapter 6 introduces subagents to solve.

The correction is not "give the agent more instructions to be more careful." It is structural: split the role. Give implementation a bounded contract (Chapter 5), delegate review to an isolated subagent (Chapter 6), and require verification evidence (Chapter 13) neither one can wave away.

## Mega-skills, fake verification, and completion theater

A mega-skill starts as a genuinely reusable procedure (Chapter 4) and grows, one edge case at a time, into a process blob nobody can read start to finish. Each addition seemed reasonable; the sum is a skill that takes longer to understand than to just do the task manually, which defeats the entire premise of writing it down. The correction is decomposition: split the skill along the same boundaries this book uses everywhere else — one skill per repeatable procedure, not one skill per domain.

Fake verification and completion theater are close cousins, both covered in depth in Chapter 13: an agent states that tests passed, review happened, or compatibility was checked, and the statement is not backed by anything a reviewer can independently open and inspect. This is the single most consequential anti-pattern in the book, because every other primitive's safety claims — a role contract's escalation conditions, a hook's pass result, a subagent's clean findings — ultimately reduce to "were they actually checked." The correction is always the same: require linked, inspectable evidence, not a sentence describing evidence.

## Context flooding and tool overreach

Context flooding is the failure mode Chapter 10 exists to prevent: dumping logs, docs, prior conversation, and tangential files into an agent's context on the theory that more information can only help. In practice, the constraints that actually matter — the one steering rule, the one compatibility requirement — get buried in volume, and the agent is statistically less likely to weight them correctly. The correction is a stated context boundary: what belongs in steering, what belongs in task-specific context, and what does not belong in the session at all.

Tool overreach is Chapter 9's and Chapter 18's shared failure mode: an external capability gets wired up because it was convenient, with no permission tier, no ownership, and no audit trail behind it. The tool works fine until the day it is used for something the team never intended to allow, and there is no record of who granted that access or why. The correction is treating every tool as a governed capability with a contract, not as informal context that happens to be callable.

## Chat as system of record and other persistence failures

Chat as system of record is Chapter 12's core failure mode: a decision, a trade-off, or a piece of evidence exists only inside a conversation and nowhere else. It is the quietest anti-pattern on this list because nothing visibly breaks when it happens — the session ends, everyone moves on, and the cost only appears later, when someone needs the reasoning and cannot find it. The correction is durable artifacts, written for a reader who was not in the room.

A close relative is the stale artifact: something was written down once, correctly, and never updated as the system changed underneath it — a runbook (Chapter 14) that no longer matches the actual rollback procedure, or a steering file that still describes a workflow the team replaced. A trusted stale artifact is often more dangerous than no artifact, because it is consulted with confidence during exactly the moment — an incident — when confidence in wrong information does the most damage.

## The anti-pattern library

Every chapter in this book names anti-patterns specific to its primitive. Collected together, they are Nexus's failure library — the reference a reviewer checks against, rather than relying on recognizing a bad pattern from memory.

| Anti-pattern | Primitive | See |
|---|---|---|
| Unbounded agent / god agent | Agent | Chapter 5 |
| Self-review in the same context | Subagent | Chapter 6 |
| Command as disguised prompt | Slash command | Chapter 7 |
| Opaque or silently-failing hook | Hook | Chapter 8 |
| Capability by default; approval theater | Permissions | Chapter 9 |
| Context flooding; unbounded memory growth | Context and memory | Chapter 10 |
| Straight to code; spec theater | Specs, plans, tasks | Chapter 11 |
| Chat as system of record; write-only artifacts | Artifacts | Chapter 12 |
| Completion theater; self-graded verification | Verification | Chapter 13 |
| Improvised rollback; review with no corrective action | Incident response | Chapter 14 |
| Scattered, inconsistent repo layout | Repo layout | Chapter 15 |
| Vague or stale decision criteria | Decision frameworks | Chapter 16 |
| Tool overreach; invisible prompt magic | Tools and MCP | Chapter 18 |
| Vendor lock-in by accident | Tool portability | Chapter 19 |
| Unattributed spend; unmeasured governance | Metrics and governance | Chapter 20 |

A team that recognizes one of these patterns does not need to invent a fix. The chapter it links to already names the structural correction.

## Nexus case study

### Before this chapter

Teams repeat the same AI mistakes. Each repeats them independently, discovers the fix independently, and never writes either the failure or the fix down for the next team.

### Design decision

Nexus documents god agents, mega-skills, fake verification, context flooding, and tool overreach as a maintained anti-pattern library, cross-referenced to the chapter that names the structural correction for each.

### Implementation

Nexus commits the library table above to `nexus-playbook` (Chapter 15), and adds one habit to its incident review template (Chapter 14): beat four, "steering gap," must name an anti-pattern from the library when one applies, so recurring failures accumulate evidence instead of being treated as one-off surprises each time.

### After this chapter

Nexus documents god agents, mega-skills, fake verification, context flooding, and tool overreach. A new engineer encountering a familiar-looking mess can name the anti-pattern and go straight to the chapter with the fix, instead of re-deriving the diagnosis from scratch.

### Lesson

An unnamed failure gets rediscovered by every team that hits it. A named one gets fixed once and recognized everywhere else.

## Quick Reference

### If you see this, check for that

| If you see... | Check for... |
|---|---|
| One agent doing everything | Missing role boundaries |
| Large opaque prompt templates | Missing skills or commands |
| Confident completion summaries | Missing verification evidence |
| Pasted logs and docs everywhere | Missing context policy |
| Broad tool permissions | Missing approval and sandbox rules |

### Nexus asset

Anti-pattern library, cross-referenced to the correcting chapter for each named failure.

### Reader action

Pick one workflow on your team that "mostly works but feels fragile." Match it against the library table above. Name the anti-pattern, then apply the structural correction from the linked chapter instead of patching around it again.
