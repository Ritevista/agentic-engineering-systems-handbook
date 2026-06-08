# Chapter 17: Tooling, MCP, and External Capabilities

> **Status: in progress.** This chapter has a complete structure and plan below.
> Prose, templates, and worked examples are being written.

## What this chapter will deliver

- Tool contract design: capability, schema, permission, ownership, auditability, verification
- MCP and the external capability layer
- Permission integration for tool use (connects to Chapter 9)
- Tool adapter patterns and auditability
- Nexus tool adapter / connector contract for the API contract running example

## Reader problem

Tools are not agents, and agents are not tools.

External systems give AI-assisted workflows real power: Git, CI, issue trackers, documentation systems, deployment platforms, observability, and internal APIs. That power needs contracts, ownership, permissions, and auditability.

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

MCP remains the primary tool/context capability layer for this field manual. Adjacent protocols such as A2A, AG-UI, AP2, and UCP belong in the appendix unless a chapter needs a specific interoperability comparison.

## Tool contracts and schemas

_Planned: what a tool contract must specify; how schemas define valid inputs and outputs; why informal tool access is a governance gap._

## MCP and the capability layer

_Planned: how MCP works as the tool/context capability layer; what belongs in an MCP server contract versus in context._

## Permission integration for tool use

_Planned: how tool calls become authorization events (see Chapter 9); how permission tiers apply to tool access; allowlists and audit._

## Tool adapter patterns and auditability

_Planned: how to wrap external systems in governed adapters; what the audit record must contain for tool calls._

## Applying tool governance to the running example

_Planned: thread the canonical running example (see running-example.md) through this chapter's concept._

## Nexus case study

### Before this chapter

Agents cannot safely access external systems.

### Design decision

_Planned._

### Implementation

_Planned._

### After this chapter

Nexus creates a permissioned tool gateway for CI, issue tracker, docs, and deployment metadata.

### Lesson

_Planned._

## Templates

_Planned: tool adapter / connector contract — the named Nexus asset for this chapter._

## Quick Reference

| Do this | Avoid this |
|---|---|
| Define tool schemas and ownership. | Let tools become invisible prompt magic. |
| Route tool use through permissions. | Give broad access by default. |
| Preserve tool results when they matter. | Treat observations as unverifiable chat. |
| Separate agents from tools. | Call every integration an agent. |

## References and Further Reading

- See [Appendix: Agentic Patterns, Prompting Techniques, and Protocols](./appendix-agentic-patterns-and-protocols.md) for related protocol positioning.

## Source Notes

_Planned. Analysis, decision frameworks, and Nexus Engineering Control Plane examples are original to this field manual; source-backed references are added only where tool- or protocol-specific behavior is discussed._
