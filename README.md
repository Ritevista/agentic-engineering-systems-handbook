# Agentic Engineering Systems

**Subtitle:** A Developer Handbook for Designing Reliable AI-Assisted Software Workflows

## What this handbook is
This repository hosts an mdBook-based technical handbook for designing reliable, reusable, and governable agentic engineering workflows.

## Who it is for
- Senior developers
- Software architects
- Platform engineers
- Engineering managers
- Technical leaders adopting coding agents and agentic CLIs

## Why this exists
Many teams use AI-assisted coding inconsistently across repositories, with uneven rules, review quality, and verification. This handbook provides a systems-architecture approach so teams can standardize how agentic work is scoped, executed, verified, and retained as durable engineering artifacts.

## Nexus Engineering Control Plane case study
The handbook uses a fictional running case study, **Nexus Engineering Control Plane**, to show how an organization evolves from ad-hoc assistant usage to a governed engineering control plane with shared skills, repo-specific steering, bounded agents, verification checklists, and durable outputs.

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

This handbook is published with GitHub Pages using a GitHub Actions workflow.

After GitHub Pages is enabled, the public URL will usually be:
- `https://<github-username>.github.io/agentic-engineering-systems-handbook/`

For an organization repository, it will usually be:
- `https://<github-org>.github.io/agentic-engineering-systems-handbook/`

The exact URL is shown in:
- GitHub repository → **Settings** → **Pages**
- The **Deploy mdBook to GitHub Pages** workflow output in the **Actions** tab
- Workflow definition: `.github/workflows/pages.yml`

## Enabling GitHub Pages

1. Go to the GitHub repository.
2. Open **Settings**.
3. Open **Pages**.
4. Under **Build and deployment**, set **Source** to **GitHub Actions**.
5. Push to `main` or run the workflow manually from the **Actions** tab.
6. After the workflow succeeds, open the Pages URL shown by GitHub.

## Publishing Safety Note

Do not publish confidential company information, private URLs, real credentials, internal hostnames, or proprietary architecture details. This repository is intended to use fictional/anonymized examples such as the Nexus Engineering Control Plane.
