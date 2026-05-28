# Agentic Engineering Field Manual

**Subtitle:** Designing Governed AI-Assisted Software Workflows

## What this field manual is

This repository hosts an mdBook-based field manual for engineering teams that want to move from ad-hoc AI coding experiments to structured, reviewable, reusable, and governable AI-assisted software engineering workflows.

This field manual helps engineering teams structure repositories, agents, skills, tool access, verification evidence, and durable artifacts so AI-assisted software engineering can survive real team usage.

## Book promise

This field manual helps engineering teams move from individual AI coding experiments to structured, reviewable, and governable AI-assisted software engineering.

It focuses on the engineering system around agents:

- repository steering
- reusable skills
- bounded agents and subagents
- slash commands and workflow triggers
- hooks and lifecycle guardrails
- permissions, approvals, and sandboxing
- context and memory boundaries
- specs, plans, and tasks
- durable artifacts
- verification evidence
- MCP and external tool access
- team maturity and operating models

## Who it is for

Primary audience:

- senior developers
- staff engineers
- software architects
- platform engineers
- technical leads responsible for standardizing AI-assisted engineering workflows

Secondary audience:

- engineering managers
- DevOps/platform leaders
- toolsmiths building internal AI engineering enablement

This is not positioned as a beginner AI book.

## What this book is not

This is not:

- a prompt cookbook
- a beginner introduction to ChatGPT or coding assistants
- a generic agent framework tutorial
- a vendor-specific Codex, Claude Code, Cursor, Kiro, or MCP manual
- a replacement for software architecture, security review, testing, or engineering judgment

## Why this exists

Many teams use AI-assisted coding inconsistently across repositories, with uneven rules, review quality, and verification. This field manual provides a systems-architecture approach so teams can standardize how AI-assisted work is scoped, executed, verified, and retained as durable engineering artifacts.

## Nexus Engineering Control Plane case study

The field manual uses a fictional running case study, **Nexus Engineering Control Plane**, to show how an organization evolves from ad-hoc assistant usage to a governed engineering control plane with shared skills, repo-specific steering, bounded agents, verification checklists, and durable outputs.

## Local build and preview

Prerequisites:

- [mdBook](https://rust-lang.github.io/mdBook/)

Commands:

```bash
mdbook build
mdbook serve --open
```

## Project status

This repository is an initial scaffold. Chapters are intentionally placeholders and will be expanded iteratively.

## Additional scaffold coverage

This scaffold now also includes a secondary migration-oriented example track (**Mercury GitOps Platform Migration**) and starter agent/skill placeholders for cross-tool portability discussions.

## Reading the Book Online

This field manual is published with GitHub Pages using a GitHub Actions workflow.

After GitHub Pages is enabled, the public URL for this repository will usually be:

- `https://ritevista.github.io/agentic-engineering-systems-handbook/`

The exact URL is shown in:

- GitHub repository -> **Settings** -> **Pages**
- The **Deploy mdBook site to Pages** workflow output in the **Actions** tab
- Workflow definition: `.github/workflows/pages.yml`

You can also browse the raw Markdown chapters directly on GitHub from:

- [`src/SUMMARY.md`](src/SUMMARY.md)

## Publishing with GitHub Pages

1. Go to the GitHub repository.
2. Open **Settings**.
3. Open **Pages**.
4. Under **Build and deployment**, select **GitHub Actions** if available.
5. If the UI initially shows only **Branch**, keep this workflow and run it from the **Actions** tab; GitHub may expose/show the Actions deployment option after the workflow is present.
6. Run the workflow manually from **Actions** or push to `main`.
7. Open the deployment URL shown by the workflow output.

## Publishing Safety Note

The published GitHub Pages site may be publicly accessible depending on repository and account settings. Do not include confidential company data, private URLs, credentials, internal hostnames, or proprietary architecture details. Use fictional/anonymized examples such as Nexus Engineering Control Plane.
