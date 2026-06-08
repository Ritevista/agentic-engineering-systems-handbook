# Chapter 18: Tool Portability

> **Status: in progress.** This chapter has a complete structure and plan below.
> Prose, templates, and worked examples are being written.

## What this chapter will deliver

- The portable layer versus the tool-specific layer
- The portability matrix: mapping primitives across tools
- Vendor abstraction patterns for steering, skills, and commands
- How to test and validate portability when changing tools
- Nexus portability matrix across Codex, Claude Code, Cursor, Kiro, GitHub, and GitLab

## Reader problem

Workflows become brittle when they are designed around one vendor's surface area.

Specific tools matter. Their commands, permission models, and extension points shape what is possible. But the engineering structure should outlive any one interface.

## Design principle: separate workflow intent from tool implementation

Separate workflow intent from tool implementation.

| Portable layer | Tool-specific layer |
|---|---|
| Role contract | Agent configuration syntax |
| Skill procedure | Tool-specific skill file format |
| Workflow trigger | Slash command implementation |
| Verification requirement | CI provider or command syntax |
| Tool contract | MCP server, connector, or API binding |

Portability does not mean pretending tools are identical. It means preserving the architecture when the tool changes.

## The portable layer and the tool-specific layer

_Planned: what belongs in the portable layer and why; what is legitimately tool-specific and should not be abstracted away._

## The portability matrix

_Planned: how to map each primitive (steering, skills, commands, agents, permissions, verification, artifacts) to its implementation in each tool; what the matrix reveals about coupling._

## Vendor abstraction patterns

_Planned: practical patterns for writing steering, skills, and commands that can be adapted to a new tool without redesigning the workflow._

## Testing and validating portability

_Planned: how to verify that a workflow survives a tool change; what evidence a portability review should produce._

## Applying portability to the running example

_Planned: thread the canonical running example (see running-example.md) through this chapter's concept._

## Nexus case study

### Before this chapter

Workflows become tied to one vendor.

### Design decision

_Planned._

### Implementation

_Planned._

### After this chapter

Nexus separates core patterns from Codex, Claude Code, Cursor, Kiro, GitHub, and GitLab specifics.

### Lesson

_Planned._

## Templates

_Planned: portability matrix — the named Nexus asset for this chapter._

## Quick Reference

| Preserve | Adapt |
|---|---|
| Primitive boundary | Vendor syntax |
| Verification expectation | Local command names |
| Artifact requirement | Storage path |
| Permission policy | Tool approval mechanism |
| Workflow intent | Trigger implementation |

## Source Notes

_Planned. Analysis, decision frameworks, and Nexus Engineering Control Plane examples are original to this field manual; source-backed references are added only where tool- or protocol-specific behavior is discussed._
