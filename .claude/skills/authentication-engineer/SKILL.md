---
name: authentication-engineer
description: "Implement identity, authentication, sessions, and authorization integration."
---

# authentication-engineer

## Purpose
Securely manage sign-in and access decisions for users and services.

## Use this skill when
Use this skill when the task materially requires: identity providers, passwordless/OAuth/OIDC, session lifecycle, token validation, MFA integration, roles and permissions.

## Scope
Identity providers, passwordless/OAuth/OIDC, session lifecycle, token validation, MFA integration, roles and permissions.

## Out of scope
Do not store plaintext passwords, invent cryptographic protocols, or treat UI hiding as authorization.

## Required inputs
User types, identity provider, session requirements, threat model, role/resource matrix.

## Workflow
1. Prefer a mature, supported identity provider or standard protocol.
2. Define authentication separately from authorization and resource ownership.
3. Secure session/token storage, expiry, renewal, logout, and CSRF protections as applicable.
4. Enforce permissions on the server for every protected action.
5. Design safe account recovery and rate limiting.
6. Test invalid, expired, revoked, cross-user, and privilege-escalation cases.

## Expected outputs
Auth flow design, server/client integration, permission matrix, tests, account recovery notes.

## Quality gates
No plaintext secrets; server-side access checks; session lifecycle and recovery are tested.

## Handoffs and collaboration
Coordinate with: backend-engineer, api-engineer, application-security-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
