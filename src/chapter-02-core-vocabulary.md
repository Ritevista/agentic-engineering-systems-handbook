# Chapter 2: Core Vocabulary

## Purpose

Establish a shared language so teams can design and govern agentic engineering workflows without ambiguity.

## Key Questions

- Which core terms must remain stable across chapters and repositories?
- How do these terms prevent architecture and governance drift?

## Nexus Case Study Connection

Nexus uses this vocabulary as a cross-repo contract so `nexus-service`, `nexus-delivery`, and `nexus-playbook` can align implementation, governance, and verification.

## Planned Sections

1. Core one-line definitions
2. Relationship map between primitives
3. Terms commonly confused in practice

> Related pattern catalog: ReAct, BDI, DSPy, LLM Guard, MCP, and A2A are supporting terms discussed in [Appendix: Agentic Patterns, Prompting Techniques, and Protocols](./appendix-agentic-patterns-and-protocols.md). They should not be flattened into the core vocabulary without classifying their layer first.

## Quick Reference

- **Agent**: A bounded role that executes defined responsibilities within explicit workflow constraints.
- **Subagent**: An isolated delegated worker used for scoped parallel or specialized tasks.
- **Steering**: Doctrine, rules, and context that constrain and guide agent behavior.
- **Skill**: A reusable task playbook describing repeatable procedure and quality expectations.
- **Slash command**: A workflow trigger that invokes predefined agentic actions.
- **Hook**: Lifecycle automation or guardrail executed at specific workflow events.
- **Permissions / approvals / sandboxing**: Blast-radius controls that limit capability, require authorization, and constrain execution context.
- **Context / memory**: The information an agent knows, carries, and retrieves while working.
- **Specs / plans / tasks**: Work-structure artifacts that translate goals into executable units.
- **Artifacts**: Durable outputs stored in systems of record, not only in chat.
- **Verification / tests / evals / checklists**: Evidence mechanisms used to validate correctness, safety, and policy compliance.
- **Tooling / MCP / external capabilities**: The separate but connected external capability layer that agents call through governed interfaces.

Tooling / MCP / external capabilities will be discussed later and treated as a separate but connected layer.
