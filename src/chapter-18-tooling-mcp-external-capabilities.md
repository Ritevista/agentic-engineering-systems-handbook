# Chapter 18: Tooling, MCP, and External Capabilities

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

## Nexus case study

### Before this chapter

Agents cannot safely access external systems.

### After this chapter

Nexus creates a permissioned tool gateway for CI, issue tracker, docs, and deployment metadata.

## Quick Reference

| Do this | Avoid this |
|---|---|
| Define tool schemas and ownership. | Let tools become invisible prompt magic. |
| Route tool use through permissions. | Give broad access by default. |
| Preserve tool results when they matter. | Treat observations as unverifiable chat. |
| Separate agents from tools. | Call every integration an agent. |

## References and Further Reading

- See [Appendix: Agentic Patterns, Prompting Techniques, and Protocols](./appendix-agentic-patterns-and-protocols.md) for related protocol positioning.
