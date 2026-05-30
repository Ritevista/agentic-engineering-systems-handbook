# Chapter 17: Tooling, MCP, and External Capabilities

## Reader problem

Tools are not agents, and agents are not tools.

External systems give AI-assisted workflows real power: Git, CI, issue trackers, documentation systems, deployment platforms, observability, and internal APIs. That power needs contracts, ownership, permissions, and auditability.

## Design principle

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

Before this chapter, Nexus agents use external systems inconsistently.

Nexus introduces a tool gateway contract. For the API contract running example, agents may read CI status, issue metadata, API docs, schema metadata, and safe usage metadata through governed tool interfaces.

After this chapter, Nexus has a controlled external capability layer.

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

This chapter uses source-backed references only where tool-specific behavior or protocol terminology is discussed. The analysis, decision frameworks, and Nexus Engineering Control Plane examples are original to this field manual.
