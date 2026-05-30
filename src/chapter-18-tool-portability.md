# Chapter 18: Tool Portability

## Reader problem

Workflows become brittle when they are designed around one vendor's surface area.

Specific tools matter. Their commands, permission models, and extension points shape what is possible. But the engineering structure should outlive any one interface.

## Design principle

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

Before this chapter, Nexus workflows are too easy to tie to one assistant product.

Nexus introduces a portability matrix. For the API contract running example, the team maps steering, skills, commands, permissions, verification, and artifacts across the tools used by different repositories.

After this chapter, Nexus can move workflow structure across tools without redesigning the operating model.

## Quick Reference

| Preserve | Adapt |
|---|---|
| Primitive boundary | Vendor syntax |
| Verification expectation | Local command names |
| Artifact requirement | Storage path |
| Permission policy | Tool approval mechanism |
| Workflow intent | Trigger implementation |
