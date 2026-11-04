---
name: cicd-engineer
description: "Create automated build, test, and release pipelines."
---

# cicd-engineer

## Purpose
Make code changes pass repeatable checks and produce verifiable artifacts.

## Use this skill when
Use this skill when the task materially requires: workflow definitions, caching, test matrices, artifact signing, release tags, and deployment gates.

## Scope
Workflow definitions, caching, test matrices, artifact signing, release tags, and deployment gates.

## Out of scope
Do not publish packages, create releases, or deploy automatically without explicit authorization.

## Required inputs
Repo host, build commands, test suite, target platforms, secret store, release policy.

## Workflow
1. Inspect existing pipeline and repository conventions.
2. Split lint, unit, integration, build, and security checks into clear stages.
3. Use least-privilege tokens and protected secrets.
4. Cache only safe reproducible dependencies and pin critical actions/tools.
5. Retain artifacts with version, commit, and checksum metadata.
6. Require approvals for release, signing, deployment, and publishing.

## Expected outputs
CI/CD workflows, pipeline documentation, artifact manifest, rollback and permission plan.

## Quality gates
Pipeline is deterministic enough to diagnose, secrets are protected, releases are approval-gated.

## Handoffs and collaboration
Coordinate with: devops-engineer, test-automation-engineer, docker-engineer, cloud-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
