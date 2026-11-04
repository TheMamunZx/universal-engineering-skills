---
name: reliability-engineer
description: "Improve service reliability and operational resilience."
---

# reliability-engineer

## Purpose
Define measurable reliability expectations and prepare for failure and recovery.

## Use this skill when
Use this skill when the task materially requires: sLIs/SLOs, error budgets, monitoring, incident response, capacity, failover, and disaster recovery.

## Scope
SLIs/SLOs, error budgets, monitoring, incident response, capacity, failover, and disaster recovery.

## Out of scope
Do not claim uptime targets or recovery guarantees without measured operations and tested procedures.

## Required inputs
Service architecture, user impact, critical journeys, incident history, operational access.

## Workflow
1. Identify critical user journeys and reliability risks.
2. Define measurable SLIs and propose SLOs with stakeholder agreement.
3. Map dependencies and single points of failure.
4. Design actionable alerts, runbooks, backups, and recovery procedures.
5. Test failure and restore scenarios in a safe environment.
6. Review incidents and feed corrective actions back into architecture.

## Expected outputs
SLO proposal, monitoring plan, runbooks, failure-mode table, recovery test plan.

## Quality gates
Alerts are actionable and recovery procedures have been exercised.

## Handoffs and collaboration
Coordinate with: system-design-engineer, devops-engineer, distributed-systems-engineer, performance-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
