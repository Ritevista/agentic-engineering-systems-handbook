# Chapter 19: Tool Portability

## Reader problem

Workflows become brittle when they are designed around one vendor's surface area.

Specific tools matter. Their commands, permission models, and extension points shape what is possible. But the engineering structure should outlive any one interface — a team that rebuilds its steering, skills, and permission model from scratch every time it changes coding assistants has not been building an engineering system. It has been building a collection of vendor-specific habits.

## What breaks without this

Every primitive in this book has a portable shape and a vendor-specific implementation. A role contract (Chapter 5) is portable: responsibility, allowed actions, output contract, escalation conditions. How a specific tool represents "this agent may edit these files" is not portable — one vendor might use a config file, another a UI setting, another a convention inside a markdown file.

Teams that do not separate the two tend to encode workflow intent directly in vendor-specific syntax. The workflow then only exists inside that vendor's surface, and changing tools means rediscovering what the workflow was actually trying to accomplish, because the intent was never written down independently of the implementation.

## Design principle: separate workflow intent from tool implementation

Separate workflow intent from tool implementation.

| Portable layer | Tool-specific layer |
|---|---|
| Role contract | Agent configuration syntax |
| Skill procedure | Tool-specific skill file format |
| Workflow trigger | Slash command implementation |
| Verification requirement | CI provider or command syntax |
| Tool contract | MCP server, connector, or API binding |

Portability does not mean pretending tools are identical. It means preserving the architecture when the tool changes — the same distinction Chapter 9 draws between a declared boundary and its enforcement, applied here to vendor surfaces instead of runtime controls.

## The portable layer versus the tool-specific layer

The portable layer is everything this book defines: steering doctrine, skill procedures, agent role contracts, subagent delegation, command intent, hook conditions, permission tiers, verification requirements, artifact taxonomy. None of this depends on which coding assistant a team uses. A role contract's responsibility and non-goals read the same whether the agent runs in Codex, Claude Code, or an internal runner.

The tool-specific layer is how each vendor represents that portable content: which file format holds steering, whether skills are discovered automatically or invoked explicitly, how permissions are configured, what a hook's trigger syntax looks like. This layer changes constantly and varies significantly across vendors — and that is fine, as long as nothing load-bearing lives only here.

The test for whether something belongs in the portable layer: if the tool disappeared tomorrow, would the answer to "what was this workflow trying to do" survive in a document, or only in a vendor's config format? If only the latter, it was never actually portable — it just happened to be readable.

## The portability matrix

A portability matrix maps each portable primitive to its representation across the tools a team actually uses. The point is not exhaustive vendor coverage — it is confirming that every tool the team relies on has *some* representation for each primitive, so switching or adding a tool is a mapping exercise, not a redesign.

| Primitive | Codex | Claude Code | Kiro | GitHub (Copilot) |
|---|---|---|---|---|
| Steering | `AGENTS.md` | `CLAUDE.md` / memory | Steering files | Repository custom instructions |
| Skills | Agent Skills | Agent Skills | — | — |
| Hooks | — | Hooks | — | — |
| Permissions | — | Permissions | — | Cloud agent firewall/secrets config |
| Sandboxing | — | Sandboxing | — | Cloud agent environment config |

Cells left blank are not failures of the matrix — they mean that vendor does not (yet, or by design) expose a first-class surface for that primitive. A blank cell is a real finding: it tells the team that primitive's enforcement, for that tool, has to live somewhere else (often a hook or CI step outside the tool itself), which is exactly the kind of gap Chapter 9's declaration-versus-enforcement discipline exists to catch before it becomes a false sense of coverage.

IDE-native and platform-native surfaces — an AI-native editor's own agent configuration, or a DevOps platform's merge-request and pipeline configuration — belong in the same matrix using the same method: find where each portable primitive lands in that tool's actual surface, and mark the gaps honestly rather than assuming coverage that was never confirmed.

## Vendor abstraction patterns

Three patterns keep the portable layer from leaking into vendor-specific syntax:

**Write the portable artifact first.** A role contract, a skill procedure, a hook condition — write it in the vendor-neutral shape this book defines, then translate it into whatever format the current tool needs. The vendor-specific file becomes a generated or hand-translated view of the portable artifact, not the source of truth.

**Keep a translation note per tool.** When a portable primitive has no first-class representation in a given tool (a blank cell in the matrix), document where its enforcement actually lives instead — a hook, a CI step, a manual review step. This is the artifact (Chapter 12) that keeps the gap visible instead of assumed away.

**Re-verify enforcement after every tool change.** Chapter 9 already warns that enforcement is runtime-specific and does not automatically travel with a ported role contract. Treat re-establishing enforcement as a required step of any tool migration, checked against the matrix, not an assumption that porting the config was enough.

## How to test and validate portability

Portability is a claim, and like any claim in this book, it needs evidence rather than trust:

- Take one role contract, skill, or hook and translate it to a second tool your team does not currently use. If the translation requires re-deriving intent instead of mapping an existing definition, the primitive was not actually portable.
- Confirm enforcement, not just configuration, survives the translation — a permission tier that translates to config in the new tool but nothing actually checks it is a declaration with no enforcement behind it (Chapter 9).
- Re-run the verification evidence requirements (Chapter 13) against the ported workflow before trusting it in the new tool.

## Anti-patterns

| Anti-pattern | Why it fails | Better pattern |
|---|---|---|
| Vendor lock-in by accident | Workflow intent only exists in one tool's config syntax | Write the portable artifact first; treat vendor config as a translation |
| Assuming tools are identical | A blank matrix cell gets silently assumed to be covered | Mark gaps honestly; find where enforcement actually lives instead |
| Porting config without enforcement | The new tool has the settings but nothing checks them | Re-verify enforcement (Chapter 9) after every tool migration |
| Duplicated logic per vendor | The same workflow reimplemented from scratch per tool, drifting independently | One portable definition; per-tool translation, not per-tool redesign |
| No portability check until forced | The gap is discovered mid-migration under time pressure | Test one translation before the team is forced to migrate everything |

## Nexus case study

### Before this chapter

Workflows become tied to one vendor. Nexus's implementation-agent role contract, skills, and hooks exist only as one tool's configuration, and no one is confident what would survive a tool change.

### Design decision

Nexus separates core patterns from Codex, Claude Code, Cursor, Kiro, GitHub, and GitLab specifics, building a portability matrix and confirming enforcement survives translation for its highest-value primitives first: the implementation-agent role contract and the permission matrix.

### Implementation

```md
# Portability matrix: implementation-agent role contract

## Portable definition
Responsibility, non-goals, allowed actions, output contract,
escalation conditions (Chapter 5) — stored as `nexus-playbook/agents/
implementation-agent.md`.

## Codex
Translated to AGENTS.md conventions for nexus-service.

## Claude Code
Translated to CLAUDE.md / memory plus Claude Code skills for the
api-change-test-plan procedure.

## Kiro
Translated to steering files; no native skills surface — the
api-change-test-plan procedure is enforced via a CI step instead.

## GitHub (Copilot cloud agent)
Translated to repository custom instructions; permission tier
enforcement handled via cloud agent firewall and secrets configuration,
not a native permission primitive.

## Gaps found
Kiro has no first-class skills surface: procedure enforcement moved to
CI. GitHub Copilot's permission model differs structurally from
Chapter 9's tiers: mapped to firewall/secrets config, re-verified
against the permission matrix rather than assumed equivalent.
```

### After this chapter

Nexus separates core patterns from Codex, Claude Code, Cursor, Kiro, GitHub, and GitLab specifics. A tool migration is now a mapping exercise against the portability matrix, with gaps documented instead of discovered mid-migration.

### Lesson

Portability is not "the config looks similar." It is "the enforcement still holds after the translation." Test that claim before trusting it.

## Quick Reference

### Preserve / adapt

| Preserve | Adapt |
|---|---|
| Primitive boundary | Vendor syntax |
| Verification expectation | Local command names |
| Artifact requirement | Storage path |
| Permission policy | Tool approval mechanism |
| Workflow intent | Trigger implementation |

### Nexus asset

Portability matrix mapping steering, skills, hooks, and permissions across Codex, Claude Code, Kiro, GitHub, Cursor, and GitLab, with enforcement gaps documented per tool.

### Reader action

Pick one role contract, skill, or hook your team relies on. Translate it to a tool you do not currently use. If enforcement does not survive the translation, document where it would have to live instead — that gap is the real state of your portability, not the matrix cell that looks filled in.

## References and Further Reading

- [OpenAI Codex: Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md)
- [OpenAI Codex: Agent Skills](https://developers.openai.com/codex/skills)
- [Anthropic Claude Code: Memory / CLAUDE.md](https://code.claude.com/docs/en/memory)
- [Anthropic Claude Code: Agent Skills](https://code.claude.com/docs/en/skills)
- [Anthropic Claude Code: Hooks](https://code.claude.com/docs/en/hooks)
- [Anthropic Claude Code: Permissions](https://code.claude.com/docs/en/permissions)
- [Kiro Steering documentation](https://kiro.dev/docs/steering/)
- [GitHub Copilot: Adding repository custom instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)
- [GitHub Copilot cloud agent: Customize firewall](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-firewall)

## Source Notes

This chapter uses the sources above for tool-specific behavior and terminology. Cursor and GitLab are referenced by their general public role (AI-native IDE; DevOps platform with CI/CD and merge-request review) rather than pinned documentation, since this field manual does not maintain vendor-specific citations for every tool in the matrix. The portability matrix model, the abstraction patterns, and the Nexus example are original to this field manual.

The supporting source catalog is maintained in the repository at `references/bibliography.md`.
