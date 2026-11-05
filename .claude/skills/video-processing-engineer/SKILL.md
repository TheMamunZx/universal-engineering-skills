---
name: video-processing-engineer
description: "Process, transform, and analyze video files and streams."
---

# video-processing-engineer

## Purpose
Build dependable media pipelines for decoding, transcoding, filtering, and inspection.

## Use this skill when
Use this skill when the task materially requires: containers/codecs, frame rates, timestamps, resolution, filters, metadata, stream handling, and validation.

## Scope
Containers/codecs, frame rates, timestamps, resolution, filters, metadata, stream handling, and validation.

## Out of scope
Do not conflate file processing with documentary editing/render orchestration; delegate final timeline assembly to the separate ai-documentary-studio skill.

## Required inputs
Input files, target format, resolution/frame rate, platform, quality/size constraints.

## Workflow
1. Probe source streams and record metadata before transformation.
2. Choose codec, container, bitrate/quality mode, and frame handling for target needs.
3. Preserve or intentionally transform timestamps, audio sync, and rotation metadata.
4. Handle variable frame rate, color space, and subtitles explicitly.
5. Use temporary outputs and verify decode, duration, and audio/video sync.
6. Document lossy steps and keep originals until outputs are validated.

## Expected outputs
Processing pipeline, command/config, metadata report, validation results.

## Quality gates
Output stream metadata and playback are verified; source files remain intact.

## Handoffs and collaboration
Coordinate with: audio-engineer, performance-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
