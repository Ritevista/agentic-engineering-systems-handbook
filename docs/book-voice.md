# Book Voice Contract

The field manual should sound like a practical systems architect explaining how to make AI-assisted engineering reliable at team scale.

## Voice

Use a direct, practical, architectural voice.

The tone should be:

- clear
- concise
- field-manual-like
- slightly adversarial when challenging weak assumptions
- focused on engineering trade-offs
- grounded in systems, workflows, artifacts, evidence, and governance

The tone should not be:

- chatty
- promotional
- motivational
- academic for its own sake
- vendor-hype driven
- casual blog style
- a transcript of exploratory conversation

## Style principles

Prefer:

- "Prompts can instruct. They cannot govern."
- "L1 improves the practitioner. L2 improves the engineering system."
- "Important engineering behavior should not depend on private prompts."
- "Bad systems hide responsibilities inside prompts. Good systems separate concerns."
- "The tool matters. The structure matters more."

Avoid:

- vague productivity claims
- excessive AI hype
- long abstract definitions before the reader feels the problem
- fictional drama around Nexus
- deep vendor-specific details in core chapters
- treating all AI terms as equivalent

## Sentence style

Use short paragraphs.

Use tables for decisions, boundaries, and quick references.

Use bullets only when they clarify structure.

Avoid very long paragraphs.

Avoid overusing parallel sentence fragments unless they create emphasis.

## Chapter behavior

Each chapter should answer:

1. What problem does this concept solve?
2. What breaks without it?
3. What engineering structure does it introduce?
4. How does Nexus evolve because of it?
5. What artifact, checklist, policy, template, or boundary does the reader get?
6. What should the reader do next?

Do not publish chapter-planning questions as reader content. A public quick reference should help the reader operate the concept; it should not ask meta questions such as "What does this chapter add?" or "What is the concrete scenario?"

Good quick references include:

- decision tables
- boundary tables
- implementation checklists
- maturity anchors
- what-to-use-when guidance

Weak quick references expose authoring scaffolds, chapter rationale, or editorial planning notes.

## Nexus style

Nexus should be boringly useful.

Nexus is not a corporate story. It is a running reference implementation.

Use canonical naming:

- Nexus Software Systems = fictional organization
- Nexus Engineering Control Plane = internal initiative
- Nexus = shorthand after introduction

Every major chapter should advance Nexus one capability at a time.
Do not make Nexus fully mature too early.

## Running example style

The primary running example is currently:

**Backward-compatible API contract change**

Treat it as volatile and centralized.

Do not scatter full scenario descriptions across every chapter.
Reference the canonical running example page instead.

## Publication hygiene

Public source lives under `src/`.

Generated output under `book/` can be stale until `mdbook build` is run. When checking whether content will be published, inspect `src/` first, then rebuild and inspect `book/` only as rendered output.

Do not publish internal notes, TODOs, avoid-term lists, chapter plans, or authoring checklists in `src/`.
