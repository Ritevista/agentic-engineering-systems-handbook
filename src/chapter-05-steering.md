# Chapter 5: Steering

## Reader problem

Agents cannot respect repository rules they cannot see.

When architecture rules, local commands, unsafe areas, ownership boundaries, and review expectations live only in human memory, AI-assisted work becomes inconsistent. Prompting harder does not fix missing repository doctrine.

## Design principle

Steering is doctrine, rules, and context. Put stable repository guidance where people and agents can both use it.

| Steering content | Example |
|---|---|
| Architecture boundaries | Which modules own which responsibilities |
| Local commands | Build, test, lint, and documentation commands |
| Unsafe areas | Files or systems requiring explicit approval |
| Review expectations | Evidence needed before merge |
| Terminology | Repository-specific names and constraints |

Steering is not a task procedure. Repeatable procedures belong in skills.

## Nexus case study

Before this chapter, Nexus repositories depend on informal team memory.

Nexus adds repository steering to `nexus-service`. For the API contract running example, steering records API conventions, schema/versioning expectations, ownership, test commands, and evidence requirements.

After this chapter, Nexus has its first durable repository-level control surface.

## Quick Reference

| Put it in steering when... | Put it elsewhere when... |
|---|---|
| It is stable repository doctrine. | It is a reusable task sequence: use a skill. |
| It constrains many tasks. | It triggers a workflow: use a slash command. |
| It helps agents understand local rules. | It proves completion: use verification evidence. |
| It should be reviewed with the repository. | It is external access: use a tool contract. |
