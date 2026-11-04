---
name: secure-code-reviewer
description: "Review code specifically for security weaknesses."
---

# secure-code-reviewer

## Purpose
Find security-relevant defects in changed or targeted code and suggest mitigations.

## Use this skill when
Use this skill when the task materially requires: input handling, authentication, authorization, secrets, injection classes, deserialization, path handling, dependencies, and crypto usage.

## Scope
Input handling, authentication, authorization, secrets, injection classes, deserialization, path handling, dependencies, and crypto usage.

## Out of scope
Do not replace ordinary maintainability review or provide exploit weaponization instructions.

## Required inputs
Code diff, threat model, data flow, dependency manifest, test scope and authorization.

## Workflow
1. Trace untrusted input to sensitive sinks and trust boundaries.
2. Verify identity and authorization checks on each sensitive operation.
3. Review secret handling, cryptographic library use, file/path handling, and dependencies.
4. Check error/logging behavior for sensitive data leakage.
5. Validate findings with safe proof and avoid speculative severity inflation.
6. Recommend minimal fixes and regression tests; note residual risk.

## Expected outputs
Security findings with severity rationale, affected paths, impact, remediation, regression test.

## Quality gates
Findings are reproducible, scoped, impact-based, and paired with mitigations.

## Handoffs and collaboration
Coordinate with: code-review-engineer, application-security-engineer, api-security-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
