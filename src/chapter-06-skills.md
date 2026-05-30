# Chapter 6: Skills

## Reader problem

Repeated prompts become process debt.

If a task is performed often, the team should not rely on each developer remembering the right prompt, checklist, examples, and quality bar. That behavior belongs in a reusable playbook.

## Design principle

A skill is a reusable task playbook. It describes when to use the procedure, what inputs are required, what steps to follow, what outputs to produce, and how to verify the result.

| Skill section | Role |
|---|---|
| When to use | Prevents accidental overuse |
| Inputs | Defines required context |
| Process | Makes the workflow repeatable |
| Output format | Makes review easier |
| Verification | Prevents "done" without evidence |

DSPy, few-shot examples, and prompt-standardization patterns can support skills when behavior needs measurable repeatability. They do not replace the playbook.

## Nexus case study

Before this chapter, Nexus developers copy private prompt fragments for recurring work.

Nexus introduces an API-change test-plan skill. For the running example, the skill generates checks for contract compatibility, authorization, documentation, regression risk, and PR evidence.

After this chapter, Nexus has a reusable task playbook instead of repeated prompt improvisation.

## Quick Reference

| Create a skill when... | Do not create a skill when... |
|---|---|
| The task repeats across people or repos. | The task is a one-time exploration. |
| The quality bar can be written down. | The work has no stable procedure yet. |
| The output should follow a pattern. | Repository doctrine is the real need. |
| The procedure should be improved over time. | A simple command wrapper is enough. |
