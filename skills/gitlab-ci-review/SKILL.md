# Skill: gitlab-ci-review

## Name
gitlab-ci-review

## Description
Review GitLab CI configurations for reliability, safety boundaries, and maintainability.

## When to Use
- Updating `.gitlab-ci.yml` or related pipeline templates.

## When Not to Use
- Non-CI code changes with no pipeline impact.

## Procedure
1. Parse pipeline stages/jobs and dependency flow.
2. Check unsafe defaults, secret handling, and destructive operations.
3. Validate cache/artifact usage and retry/timeouts.
4. Identify verification gaps and release-gate weaknesses.
5. Produce actionable fixes with risk labels.

## Output Expectations
- Findings grouped by severity
- Suggested remediations
- Verification checklist

## Verification Checklist
- Stage order and gates reviewed
- Secret/credential handling reviewed
- Failure and rollback behavior reviewed
