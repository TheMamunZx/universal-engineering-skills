---
name: android-ai-app-engineer
description: "Integrate AI capabilities into Android applications."
---

# android-ai-app-engineer

## Purpose
Build safe, responsive Android experiences around configured AI models and services.

## Use this skill when
Use this skill when the task materially requires: model adapters, streaming UI, file/image/audio input, local/cloud inference choices, caching, consent, and offline states.

## Scope
Model adapters, streaming UI, file/image/audio input, local/cloud inference choices, caching, consent, and offline states.

## Out of scope
Do not hard-code provider assumptions, expose API keys in the APK, or imply unlimited model access.

## Required inputs
Android app, provider/model matrix, modalities, latency/cost constraints, data policy.

## Workflow
1. Identify the AI task and verify provider capabilities and current limits.
2. Keep provider secrets on a trusted backend where possible; never ship private API keys in app code.
3. Design request lifecycle, streaming/cancellation, retries, and offline/error states.
4. Minimize and disclose user data sent to providers.
5. Implement file/media handling with size and type validation.
6. Test quota exhaustion, provider outage, malformed output, privacy, and accessibility.

## Expected outputs
AI feature architecture, client/server boundary, UX states, adapter integration, tests.

## Quality gates
No embedded secret keys; provider limits are surfaced; user data handling is explicit.

## Handoffs and collaboration
Coordinate with: android-app-engineer, ai-application-engineer, ai-model-integration, application-security-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
