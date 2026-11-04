---
name: desktop-app-engineer
description: "Build cross-platform or native desktop applications."
---

# desktop-app-engineer

## Purpose
Deliver desktop workflows with safe local data access and reliable packaging.

## Use this skill when
Use this skill when the task materially requires: window lifecycle, IPC, filesystem boundaries, updates, menus, accessibility, sandboxing, and distribution.

## Scope
Window lifecycle, IPC, filesystem boundaries, updates, menus, accessibility, sandboxing, and distribution.

## Out of scope
Do not expose unrestricted shell or filesystem tools to renderer/UI processes.

## Required inputs
Target OSes, runtime/framework, UX flows, file access needs, packaging/update constraints.

## Workflow
1. Identify process model and platform-specific requirements.
2. Separate privileged main/backend process from untrusted UI/rendering context.
3. Define narrow IPC contracts and validate all messages.
4. Handle filesystem paths, updates, deep links, and external URLs safely.
5. Test installers, upgrades, crashes, multi-window behavior, and OS differences.
6. Document packaging, signing, and release steps.

## Expected outputs
Desktop app features, IPC contracts, permission model, packaging config, tests.

## Quality gates
IPC is constrained and validated; app lifecycle and packaging are reproducible.

## Handoffs and collaboration
Coordinate with: frontend-engineer, backend-engineer, application-security-engineer, cicd-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
