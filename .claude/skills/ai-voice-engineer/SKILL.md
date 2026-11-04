---
name: ai-voice-engineer
description: "Design end-to-end speech and real-time voice AI systems."
---

# ai-voice-engineer

## Purpose
Coordinate speech recognition, turn-taking, dialogue, and speech output.

## Use this skill when
Use this skill when the task materially requires: sTT, TTS, audio streaming, VAD, interruption/barge-in, latency, language routing, and conversational state.

## Scope
STT, TTS, audio streaming, VAD, interruption/barge-in, latency, language routing, and conversational state.

## Out of scope
Do not focus on documentary voiceover batch generation; that belongs to ai-voice-generation-engineer.

## Required inputs
Voice interaction goal, languages, provider/model capabilities, latency target, client platform.

## Workflow
1. Define push-to-talk or consent-based activation and turn-taking rules.
2. Verify speech model languages, streaming support, and input/output limits.
3. Design audio capture, segmentation, VAD, recognition, dialogue, and response playback.
4. Handle interruption, cancellation, echo, partial transcripts, and reconnection.
5. Measure end-to-end latency and recognition quality by language/noise condition.
6. Protect recordings and transcripts with explicit retention and access controls.

## Expected outputs
Voice system architecture, state diagram, audio contracts, latency budget, test plan.

## Quality gates
Voice is user-controlled, interruption-safe, and measured end-to-end.

## Handoffs and collaboration
Coordinate with: android-voice-engineer, audio-engineer, multimodal-ai-engineer, ai-evaluation-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
