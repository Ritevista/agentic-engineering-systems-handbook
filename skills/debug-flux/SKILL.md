# Skill: debug-flux

## Name
debug-flux

## Description
Investigate Flux/GitOps reconciliation issues using a structured diagnosis workflow.

## When to Use
- Drift, failed sync, or unhealthy Flux/Kustomization state.

## When Not to Use
- Non-GitOps deployment systems.

## Procedure
1. Collect reconciliation status and recent events.
2. Trace source, kustomization, and dependency chain.
3. Isolate manifest/schema/permissions issues.
4. Propose minimal safe remediation and rollback path.
5. Capture findings as durable incident notes.

## Output Expectations
- Root-cause hypothesis
- Confirmed evidence list
- Remediation plan and verification steps

## Verification Checklist
- Status/events captured
- Dependency chain checked
- Proposed fix validated by checks
