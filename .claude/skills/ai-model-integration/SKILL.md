---
name: ai-model-integration
description: "Integrate external or local AI model providers through maintainable adapters."
---

# ai-model-integration

## Purpose
Connect configured models to an application without coupling business logic to one vendor.

## Use this skill when
Use this skill when the task materially requires: provider clients, authentication via secrets, capability registry, streaming, timeouts, retries, and normalized errors.

## Scope
Provider clients, authentication via secrets, capability registry, streaming, timeouts, retries, and normalized errors.

## Out of scope
Do not invent endpoints/model IDs, expose API keys, or assume router availability based on a provider name alone.

## Required inputs
Provider documentation, configured credentials reference, model IDs, required modalities, application interface.

## Workflow
1. Read official provider docs and current local configuration.
2. Record verified model capabilities, request schemas, limits, quotas, and data policy.
3. Design a normalized adapter while preserving provider-specific options where needed.
4. Load secrets from environment or a secret manager; redact logs.
5. Implement timeout, cancellation, retry, error normalization, and usage reporting.
6. Test happy path, malformed responses, rate limits, and unavailable-provider fallback.

## Expected outputs
Provider capability matrix, adapter implementation, configuration schema, integration tests, operational notes.

## Quality gates
No hard-coded secrets; capability matrix matches verified configuration; errors are transparent.

## Handoffs and collaboration
Coordinate with: llm-engineer, api-engineer, ai-inference-optimizer, application-security-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
