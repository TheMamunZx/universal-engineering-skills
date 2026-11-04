---
name: multimodal-ai-engineer
description: "Design AI systems that process multiple modalities."
---

# multimodal-ai-engineer

## Purpose
Coordinate text, image, audio, and video inputs/outputs using verified model capabilities.

## Use this skill when
Use this skill when the task materially requires: modality routing, preprocessing, synchronization, payload constraints, temporal context, and multimodal evaluation.

## Scope
Modality routing, preprocessing, synchronization, payload constraints, temporal context, and multimodal evaluation.

## Out of scope
Do not assume every model accepts every modality or that generated media is factually authentic.

## Required inputs
Modalities, sample assets, latency/quality targets, provider capabilities, privacy constraints.

## Workflow
1. Map each task to input/output modalities and required transformations.
2. Verify actual model support, limits, formats, and provider terms.
3. Design per-modality preprocessing and preserve timestamps/metadata.
4. Coordinate cross-modal context and define fallback paths when one modality fails.
5. Evaluate each modality and cross-modal consistency separately.
6. Record provenance for generated media and protect sensitive inputs.

## Expected outputs
Multimodal pipeline, capability matrix, preprocessing specification, evaluation cases.

## Quality gates
Every modality has a verified route, validated format, and quality check.

## Handoffs and collaboration
Coordinate with: ai-model-integration, computer-vision-engineer, audio-engineer, video-processing-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
