# Chapter 16: Anti-Patterns

## Reader problem

Bad AI-assisted workflows often look productive at first.

The failure is not always obvious. A team may ship patches quickly while accumulating hidden context, weak evidence, unclear responsibility, and unsafe access patterns.

## Design principle

Anti-patterns are named failure patterns. They help teams recognize when useful assistant output is masking structural weakness.

| Anti-pattern | Failure |
|---|---|
| God agent | One role owns too many responsibilities |
| Mega-skill | A reusable playbook becomes an unreadable process blob |
| Fake verification | The agent claims checks ran without evidence |
| Context flooding | More input hides the important constraints |
| Tool overreach | External capability is added without blast-radius control |
| Chat as system of record | Decisions disappear after the session |

Naming the failure makes it easier to design the correction.

## Nexus case study

Before this chapter, Nexus treats recurring AI workflow failures as isolated incidents.

Nexus creates an anti-pattern library. For the API contract running example, the library records failures such as changing a response contract without compatibility review or claiming documentation was updated without a linked artifact.

After this chapter, Nexus has a failure catalog that improves review and training.

## Quick Reference

| If you see... | Check for... |
|---|---|
| One agent doing everything | Missing role boundaries |
| Large opaque prompt templates | Missing skills or commands |
| Confident completion summaries | Missing verification evidence |
| Pasted logs and docs everywhere | Missing context policy |
| Broad tool permissions | Missing approval and sandbox rules |
