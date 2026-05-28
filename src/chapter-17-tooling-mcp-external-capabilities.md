# Chapter 17: Tooling, MCP, and External Capabilities

## Purpose

Establish tooling and MCP-style integrations as a separate but connected capability layer in the overall agentic system.

## Key Questions

- What is the difference between an agent and a tool?
- Why should MCP be treated as an external capability layer, not as a skill or agent?
- How do permissions, approvals, sandboxing, hooks, and auditability apply to MCP tools?
- How should teams think about tool governance?
- Why should tools have contracts, schemas, ownership, and verification?
- How does the Nexus Engineering Control Plane use MCP-style tools for systems like Git, CI/CD, issue trackers, documentation, deployment platforms, and observability?

## Nexus Case Study Connection

Nexus treats MCP-style tools as governed integration points used by agents across `nexus-service`, `nexus-delivery`, and `nexus-playbook`, with explicit contracts, ownership, and verification evidence.

## Planned Sections

1. Agents vs tools: role and responsibility boundaries
2. External capability governance model (permissions, approvals, hooks, auditability)
3. Tool contracts, schemas, ownership, and verification patterns in Nexus

## Quick Reference

To be expanded. This chapter intentionally frames MCP/tooling as a separate but connected layer and does not yet attempt a full MCP implementation guide.

## References and Further Reading

- To be expanded from `../references/bibliography.md`.

## Source Notes

This chapter uses the sources below for tool-specific behavior and terminology. The analysis, decision frameworks, and Nexus Engineering Control Plane examples are original to this field manual.
