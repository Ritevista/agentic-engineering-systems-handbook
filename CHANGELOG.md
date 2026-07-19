# Changelog

All notable changes to this field manual are recorded here. Versioning follows [Semantic Versioning](https://semver.org/): the major/minor number reflects the book's structural completeness and stability, not a page count.

## [0.1.0] - 2026-07-19

Initial complete release.

### Added

- All 21 chapters, the introduction, and the appendix as finished field-manual guidance. Fourteen chapters (Subagents, Slash Commands, Hooks, Specs/Plans/Tasks, Artifacts, Verification, Incident Response and Rollback, Repo Layout, Decision Frameworks, Anti-Patterns, Tooling/MCP, Tool Portability, Metrics/Cost/Spend Governance, Team Maturity Model) moved from in-progress skeletons to complete chapters, each following the book's standard shape: reader problem, design principle, implementation pattern, decision tables, Nexus case study, anti-patterns, and a quick reference.
- Closed two remaining internal planning notes in Chapter 3 (Steering) and Chapter 9 (Permissions, Approvals, and Sandboxing) that referenced not-yet-written content.

### Changed

- `src/SUMMARY.md` no longer marks any chapter `(in progress)`.
- README project status section rewritten to reflect a complete v0.1.0 release instead of an in-progress source tree.

## Prior history

Chapters 1-5, 9, and 10, the introduction, the appendix, and the Nexus running-example infrastructure were written and iteratively revised before this changelog began. See the git history for that detail.
