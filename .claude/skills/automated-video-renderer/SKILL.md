---
name: automated-video-renderer
description: "Assemble approved media, narration, music, and subtitles into a verified final video."
---

# automated-video-renderer

## Purpose
Render a documentary timeline to a deliverable video file using installed, configured editing/rendering tools.

## Use this skill when
Use this skill when the task materially requires: timeline manifest, FFmpeg/Remotion or existing editor automation, sync, transitions, captions, encoding, and output verification.

## Scope
Timeline manifest, FFmpeg/Remotion or existing editor automation, sync, transitions, captions, encoding, and output verification.

## Out of scope
Do not invent missing assets, silently change creative decisions, overwrite source files, or claim export success without checking the file.

## Required inputs
Approved edit decision/timeline, verified media assets, voice/audio files, subtitle file, render settings, output path.

## Workflow
1. Inspect available render tools and versions; do not assume FFmpeg/Remotion is installed.
2. Validate all referenced media paths, codecs, durations, frame rates, and subtitle timing.
3. Build an explicit timeline from approved shot order and actual narration durations.
4. Keep original assets intact; render to a new versioned temporary output.
5. Run render with progress/error capture and stop on missing media or invalid inputs.
6. Probe the output and verify file exists, duration, resolution, frame rate, streams, audio sync, and playback before marking complete.

## Expected outputs
Editable render project or script, render command/config, final video, render log, verification report.

## Quality gates
Final file is verified by filesystem and media probing; missing components are reported rather than fabricated.

## Handoffs and collaboration
Coordinate with: documentary-editor, video-processing-engineer, subtitle-generator, video-quality-checker. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
