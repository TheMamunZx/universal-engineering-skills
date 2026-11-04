---
name: ai-image-engineer
description: "Build image-generation and image-editing application workflows."
---

# ai-image-engineer

## Purpose
Integrate approved image models into controllable, repeatable product features.

## Use this skill when
Use this skill when the task materially requires: prompt composition, image input validation, generation parameters, edit workflows, provenance, moderation, and asset management.

## Scope
Prompt composition, image input validation, generation parameters, edit workflows, provenance, moderation, and asset management.

## Out of scope
Do not promise exact text rendering, unlimited generations, or provider features that are not verified.

## Required inputs
Use case, model/provider, image dimensions/formats, reference assets, usage rights, budget/latency limits.

## Workflow
1. Map task to generate, transform, inpaint, or analyze and verify provider support.
2. Validate input type, dimensions, rights, and any reference-image consent.
3. Create prompts tied to user intent and expose only supported parameters.
4. Handle async jobs, retries, cancellation, and quota errors.
5. Record provider/model/version, prompt, parameters, and output provenance.
6. Review output for visual defects, unintended text, and policy/rights issues.

## Expected outputs
Image generation adapter, prompt templates, asset manifest, quality checks, UI states.

## Quality gates
Generated assets are traceable and limitations are disclosed; no fabricated provider capability.

## Handoffs and collaboration
Coordinate with: multimodal-ai-engineer, ai-model-integration, computer-vision-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
