---
name: audio-engineer
description: "Process, analyze, and produce digital audio reliably."
---

# audio-engineer

## Purpose
Build audio workflows with controlled signal quality and format compatibility.

## Use this skill when
Use this skill when the task materially requires: sampling, codecs, filters, mixing, loudness, noise handling, segmentation, and audio validation.

## Scope
Sampling, codecs, filters, mixing, loudness, noise handling, segmentation, and audio validation.

## Out of scope
Do not impersonate a real person’s voice or remove rights metadata without authorization.

## Required inputs
Audio source, target format, sample rate, channel layout, loudness goal, usage rights.

## Workflow
1. Inspect source format, sample rate, channels, duration, and clipping.
2. Choose non-destructive processing steps appropriate to the problem.
3. Preserve sync and metadata where needed.
4. Measure loudness, peak, noise, and clipping before/after.
5. Test outputs on the intended playback environment.
6. Record source and rights information for external audio.

## Expected outputs
Audio processing pipeline, conversion settings, analysis report, test clips.

## Quality gates
Outputs meet format and signal-quality requirements; transformations are reproducible.

## Handoffs and collaboration
Coordinate with: video-processing-engineer, ai-voice-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
