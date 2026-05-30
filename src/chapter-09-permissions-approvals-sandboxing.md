# Chapter 9: Permissions, Approvals, and Sandboxing

## Reader problem

Tool access without blast-radius control is not engineering discipline.

AI-assisted workflows can read files, run commands, call tools, open network connections, and modify systems. Treating that access as a convenience creates avoidable risk.

## Design principle

Permissions, approvals, and sandboxing are blast-radius controls.

| Control | Role |
|---|---|
| Permission | Defines what action is allowed |
| Approval | Requires human authorization for higher-risk actions |
| Sandboxing | Limits where and how execution can happen |
| Audit trail | Records what was attempted or performed |

Scanners such as LLM Guard can help detect unsafe input or output, but they do not replace permissions, approvals, sandboxing, or review.

## Nexus case study

Before this chapter, Nexus has unclear boundaries around what assistants may inspect or modify.

Nexus introduces permission tiers. For the API contract running example, reading local source and running tests may be allowed, while accessing production payload samples or client usage data requires explicit approval and sanitized handling.

After this chapter, Nexus has a permission matrix that limits blast radius before tool use expands.

## Quick Reference

| Risk | Control |
|---|---|
| Accidental writes | Sandbox and write approval |
| Sensitive data exposure | Read approval and redaction rules |
| Unsafe command execution | Command allowlist and escalation path |
| Unclear accountability | Audit log and PR evidence |
