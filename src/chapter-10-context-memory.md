# Chapter 10: Context and Memory

## Reader problem

More context is not automatically better.

Teams often paste architecture notes, logs, tickets, code snippets, and prior decisions into a session until the assistant appears informed. That can help locally while making boundaries, provenance, and retention unclear.

## Design principle

Context and memory define what the agent knows or carries. Treat them as engineering inputs, not dumping grounds.

| Context type | Use |
|---|---|
| Repository steering | Stable rules and local facts |
| Task brief | Current objective, scope, and constraints |
| Retrieved context | Relevant files, tickets, docs, or metadata |
| Durable memory | Decisions or facts meant to survive sessions |
| Transient chat | Temporary reasoning and exploration |

Zero-shot and few-shot prompting belong inside context-discipline decisions when teams decide what stays one-off and what becomes a skill or template.

## Nexus case study

Before this chapter, Nexus relies on pasted context and personal memory.

Nexus introduces a context boundary policy. For the API contract running example, the task brief can include API conventions and sanitized examples, while sensitive payloads and client usage data require approval and must not become casual memory.

After this chapter, Nexus has a policy for what agents may know, retrieve, and retain.

## Quick Reference

| Context question | Field-manual answer |
|---|---|
| Is it stable repo doctrine? | Put it in steering. |
| Is it task-specific? | Put it in the task brief. |
| Is it sensitive? | Gate it with permissions. |
| Must it survive? | Store it as an artifact or durable memory. |
| Is it only exploratory? | Keep it transient. |
