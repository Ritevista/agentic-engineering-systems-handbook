# Decisions

Architecture Decision Records (ADRs) for decisions about this repository itself — its structure, tooling, and authoring process — not decisions that belong inside the book's content.

This mirrors Chapter 12's ADR pattern: use one when a decision would be expensive to re-derive later and future contributors need the reasoning, not just the outcome. Most day-to-day authoring work does not need an ADR — a spec in `specs/` is enough. Reach for an ADR when the decision is structural: a change to repo layout, the authoring workflow, the primary running example, or a rule in `AGENTS.md` or `docs/book-voice.md`.

Use `TEMPLATE.md` and number sequentially: `0001-title.md`, `0002-title.md`, and so on. An ADR is a permanent record — do not delete or renumber one once merged; supersede it with a new ADR that says so explicitly.
