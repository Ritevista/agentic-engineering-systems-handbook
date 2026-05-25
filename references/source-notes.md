# Source Notes Guidance

Each chapter should explicitly distinguish between these categories:

1. **Sourced facts**
   - Facts about tool behavior, standards, APIs, and platform limits.
   - Must be backed by links in chapter references.

2. **Original analysis**
   - The handbook's own reasoning, framing, and interpretation.
   - Should be written in original language.

3. **Nexus case-study examples**
   - Fictional, illustrative examples from the Nexus Engineering Control Plane.
   - Should not be presented as sourced real-world facts.

4. **Opinionated decision frameworks**
   - Recommended patterns, trade-offs, checklists, and decision tables.
   - Must be clearly framed as guidance, not external doctrine.

## Recommended chapter endings
For tool-heavy chapters:

```md
## References and Further Reading

- ...
```

For chapters with substantial dependence on external documentation:

```md
## Source Notes

This chapter uses the sources below for tool-specific behavior and terminology. The analysis, decision frameworks, and Nexus Engineering Control Plane examples are original to this handbook.
```
