# Specs

This directory holds task specs for in-flight or upcoming authoring work — chapter revisions, field-note promotions, structural changes. It applies Chapter 11's own guidance (Specs, Plans, and Tasks) to this repository's own maintenance.

A spec exists so that a task can be handed to an implementer — human or model, and especially a smaller or cheaper model — as a single, self-contained brief, instead of requiring it to first synthesize `AGENTS.md`, `docs/book-voice.md`, `src/nexus-evolution.md`, and `src/running-example.md` from scratch. The spec inlines what those files say about the specific task at hand.

## When to write one

Follow Chapter 11's own structure-by-risk table:

| If the change is... | Required structure |
|---|---|
| A link fix, typo, or one-line correction | No spec needed; make the change directly |
| A chapter revision or new chapter | Write a spec using `TEMPLATE.md` first |
| A change to the primary running example, chapter order, `AGENTS.md`, or `docs/book-voice.md` | Spec plus explicit human approval before implementation starts |

## Lifecycle

A spec is a working document, not a permanent record. Once the task it describes is complete and merged, the finished chapter is the source of truth — the spec has served its purpose and can be deleted in the same change that completes the work. If the decision behind the task is worth preserving permanently (a structural or policy choice, not just "chapter 9 needed a paragraph on X"), write an ADR in `docs/decisions/` instead; specs describe work, ADRs describe decisions.

## How to use `TEMPLATE.md`

Copy it to `specs/<short-task-slug>.md` and fill in every field. Do not leave placeholder tokens (`<...>`) in a spec that gets handed off for implementation — an unfilled field is exactly the kind of ambiguity this directory exists to remove.
