---
name: application-security-engineer
description: "Threat-model and improve application security defensively."
---

# application-security-engineer

## Purpose
Identify attack surfaces and establish practical mitigations for an owned application.

## Use this skill when
Use this skill when the task materially requires: threat modeling, trust boundaries, secure design, secrets, dependency risk, input validation, and security controls.

## Scope
Threat modeling, trust boundaries, secure design, secrets, dependency risk, input validation, and security controls.

## Out of scope
Do not exploit third-party systems or develop harmful payloads; testing must remain authorized and scoped.

## Required inputs
Architecture, data classification, user roles, deployment context, applicable security requirements.

## Workflow
1. Inventory assets, actors, entry points, trust boundaries, and data flows.
2. Identify plausible threats and abuse cases using a structured method.
3. Prioritize by impact, likelihood, and exposure; state assumptions.
4. Recommend layered mitigations and secure defaults.
5. Verify fixes with safe tests and configuration review.
6. Track residual risk and incident/response considerations.

## Expected outputs
Threat model, prioritized risk register, mitigation plan, verification tests.

## Quality gates
Scope is authorized; findings map to assets and mitigations; secrets are protected.

## Handoffs and collaboration
Coordinate with: api-security-engineer, secure-code-reviewer, authentication-engineer, reliability-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
