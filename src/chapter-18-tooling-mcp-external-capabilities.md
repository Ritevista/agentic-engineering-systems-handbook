# Chapter 18: Tooling, MCP, and External Capabilities

## Reader problem

Tools are not agents, and agents are not tools.

External systems give AI-assisted workflows real power: Git, CI, issue trackers, documentation systems, deployment platforms, observability, and internal APIs. That power needs contracts, ownership, permissions, and auditability — the same discipline this book applies to every other capability boundary, applied to the moment an agent reaches outside its own reasoning and touches something else.

## What breaks without this

Chapter 9 already established that a tool call is an authorization event, not a convenience. Without a contract behind it, a tool integration tends to arrive informally: someone wires up API access because a task needed it, the access works, and it quietly becomes permanent infrastructure with no schema, no named owner, and no record of what it was actually supposed to do. The tool functions correctly for months and then gets used for something nobody intended, and there is no contract to check the use against.

Treating tools as informal context — background capability the agent can reach for — also blurs the line Chapter 5 draws around agent responsibility. An agent that can silently call anything is not meaningfully bounded, regardless of how carefully its role contract is worded.

## Design principle: tools are governed external capabilities

MCP/tools are the external capability layer. Treat every tool as an interface with a contract, not as informal context.

| Tool concern | Required design question |
|---|---|
| Capability | What can the tool do? |
| Schema | What inputs and outputs are valid? |
| Permission | Who may call it, and when? |
| Ownership | Who maintains the integration? |
| Auditability | What is logged or preserved? |
| Verification | How do callers know the result is trustworthy? |

MCP remains the primary tool/context capability layer for this field manual. Adjacent protocols such as A2A, AG-UI, AP2, and UCP belong in the appendix unless a chapter needs a specific interoperability comparison — this chapter stays focused on the shape a tool contract needs, not a survey of every protocol that can carry one.

## Tool contract design

Each of the six concerns above is a separate design question, and skipping one tends to produce a specific, recognizable failure.

**Capability** states precisely what the tool does — not "accesses the issue tracker" but "reads issue status and metadata; does not create, close, or comment." A capability statement that is broader than what the tool actually needs to do is the first place blast radius creeps in.

**Schema** defines valid inputs and outputs. An agent calling a tool with an unconstrained free-text parameter can send anything; a schema is what turns "the agent asked the tool to do something" into "the agent asked the tool to do one of a bounded set of things." This is the same discipline Chapter 2's Frame-shaped thinking about structured data applies to tool boundaries specifically.

**Permission** answers who may call the tool and when — and routes directly into Chapter 9's permission tiers. A tool is not exempt from the permission model because it is "just a tool call"; it is one of the primary things the permission model exists to govern.

**Ownership** names who maintains the integration: who updates it when the external system's API changes, who is accountable when it breaks, who reviews a request to widen its capability. An unowned integration is infrastructure nobody is responsible for keeping correct.

**Auditability** states what gets logged: the caller, the inputs, the result, and the outcome — mirroring Chapter 9's audit trail requirement, applied specifically to external calls, which are often the actions with the largest blast radius because they leave the boundary of what the team directly controls.

**Verification** states how a caller knows the tool's result is trustworthy — not every external system is reliable, and an agent that treats every tool response as ground truth inherits every failure mode of the system on the other end.

## MCP and the external capability layer

MCP (Model Context Protocol) standardizes how an agent discovers and calls external tools: a common shape for exposing capability, schema, and results instead of every integration inventing its own calling convention. That standardization is valuable for portability (Chapter 19) — a tool contract expressed through MCP does not need to be rewritten for every agent runtime that supports the protocol.

MCP standardizes the calling convention. It does not by itself supply permission, ownership, or auditability — those remain engineering decisions the team makes for each tool, informed by Chapter 9, regardless of which protocol carries the call. An MCP server with no permission tier behind it is exactly as unsafe as any other unmanaged integration; the protocol changes how the call is shaped, not whether it was authorized.

## Tool adapter patterns and auditability

A tool adapter is the boundary component between an agent and an external system: it enforces the schema, checks the permission, and produces the audit record, so that individual tool calls do not each have to reimplement this discipline.

| Adapter responsibility | What it prevents |
|---|---|
| Validate inputs against schema | Malformed or out-of-contract calls reaching the external system |
| Check permission before calling | An agent invoking a capability it was not granted |
| Log caller, inputs, and outcome | An unauditable action with no record of what happened |
| Normalize the external system's response | Callers coupling directly to a third party's API shape |

Centralizing these responsibilities in an adapter, rather than leaving each tool call to enforce its own discipline, is what makes a permissioned tool gateway (this chapter's Nexus asset) coherent instead of being a permission check copy-pasted into a dozen call sites, most of which will eventually drift.

## Anti-patterns

| Anti-pattern | Why it fails | Better pattern |
|---|---|---|
| Invisible prompt magic | A tool is called with no visible contract; behavior is implicit in a prompt | Define capability, schema, permission, ownership, auditability, and verification explicitly |
| Unowned integration | No one is accountable when the external system changes or the integration breaks | Name an owner at the time the tool is added |
| Schema-free calls | Free-text parameters let an agent request anything the external system will accept | Define a bounded schema for inputs and outputs |
| Tool call as untracked action | No log of caller, inputs, or outcome | Route every call through an adapter that produces an audit record |
| Treating tool output as ground truth | The agent inherits every failure mode of an unreliable external system | State how a caller verifies a tool's result before trusting it |
| Calling an integration an agent | A tool adapter is given autonomy it does not have or need | Keep the distinction: tools perform capability; agents own responsibility |

## Nexus case study

### Before this chapter

Agents cannot safely access external systems. A developer wires up direct API access to the issue tracker for one task, and it quietly becomes a standing integration with no schema, no owner, and no log of what it has been used for since.

### Design decision

Nexus creates a permissioned tool gateway for CI, issue tracker, docs, and deployment metadata — one adapter layer, with every tool behind it defined by the six-concern contract.

### Implementation

```md
# Tool contract: ci-status

## Capability
Read CI run status and logs for a given commit or PR. Does not
trigger, cancel, or retry runs.

## Schema
Input: { repo, ref }
Output: { status, started_at, finished_at, log_url }

## Permission
Caller: implementation-agent, compatibility-review subagent (Chapter 6).
Tier: read-only-local (Chapter 9).

## Ownership
Owned by: platform team. Update on CI provider API changes.

## Auditability
Logged: caller, repo, ref, timestamp, result status.

## Verification
Callers treat `status` as authoritative only when `finished_at` is set;
a missing `finished_at` means the run is still in progress.
```

Nexus defines parallel contracts for the issue tracker (read-only metadata), the docs system (read and propose-edit), and deployment metadata (read-only), each routed through the same adapter layer so permission checks and audit logging are enforced once, not per call site.

### After this chapter

Nexus creates a permissioned tool gateway for CI, issue tracker, docs, and deployment metadata. Every external call an agent makes now has a named capability, a schema, a permission tier, an owner, and an audit record behind it.

### Lesson

A tool call is an authorization event whether or not the team treats it like one. Give it a contract before it becomes standing infrastructure nobody remembers approving.

## Quick Reference

### Do this / avoid this

| Do this | Avoid this |
|---|---|
| Define tool schemas and ownership. | Let tools become invisible prompt magic. |
| Route tool use through permissions. | Give broad access by default. |
| Preserve tool results when they matter. | Treat observations as unverifiable chat. |
| Separate agents from tools. | Call every integration an agent. |

### Nexus asset

Permissioned tool gateway with contracts for CI, issue tracker, docs, and deployment metadata, routed through one adapter layer.

### Reader action

Find one external integration your team's agents already use informally. Write its six-concern contract: capability, schema, permission, ownership, auditability, verification. If you cannot name an owner, that is the gap this chapter closes.

## References and Further Reading

- [Model Context Protocol official documentation](https://modelcontextprotocol.io/docs/getting-started/intro)
- See [Appendix: Agentic Patterns, Prompting Techniques, and Protocols](./appendix-agentic-patterns-and-protocols.md) for related protocol positioning.

## Source Notes

This chapter uses the sources below for tool-specific behavior and terminology. The tool contract model, the adapter pattern, the Nexus tool gateway example, and the decision and anti-pattern tables are original to this field manual.

The supporting source catalog is maintained in the repository at `references/bibliography.md`.
