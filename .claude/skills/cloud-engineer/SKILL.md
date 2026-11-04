---
name: cloud-engineer
description: "Design and operate cloud resources with secure, cost-aware architecture."
---

# cloud-engineer

## Purpose
Map application needs to cloud services and infrastructure-as-code.

## Use this skill when
Use this skill when the task materially requires: compute, storage, network, identity, observability, resilience, backups, and cost controls.

## Scope
Compute, storage, network, identity, observability, resilience, backups, and cost controls.

## Out of scope
Do not create billable resources or change live infrastructure without explicit approval.

## Required inputs
Cloud provider, workload, region/data-residency needs, budget, identity model, availability target.

## Workflow
1. Verify current provider service capabilities and pricing from official sources.
2. Define environments, network boundaries, identity, and data residency.
3. Choose managed services where they reduce operational burden.
4. Represent repeatable infrastructure as code with reviewable plans.
5. Add budgets, alerts, backups, logging, and disaster recovery.
6. Test in a sandbox and require approval before billable or production changes.

## Expected outputs
Cloud architecture, infrastructure-as-code plan, cost assumptions, security and recovery checklist.

## Quality gates
Cost and security assumptions are visible; no resources are provisioned without permission.

## Handoffs and collaboration
Coordinate with: devops-engineer, docker-engineer, cicd-engineer, application-security-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
