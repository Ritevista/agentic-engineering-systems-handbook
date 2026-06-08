# Chapter 19: Tool Portability

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

## Nexus case study

### Before this chapter

Workflows become tied to one vendor.

### After this chapter

Nexus separates core patterns from Codex, Claude Code, Cursor, Kiro, GitHub, and GitLab specifics.

## Quick Reference

| Preserve | Adapt |
|---|---|
| Primitive boundary | Vendor syntax |
| Verification expectation | Local command names |
| Artifact requirement | Storage path |
| Permission policy | Tool approval mechanism |
| Workflow intent | Trigger implementation |
