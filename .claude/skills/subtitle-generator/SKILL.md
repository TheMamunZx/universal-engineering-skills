---
name: subtitle-generator
description: "Create accurately timed Hindi subtitles"
---

# subtitle-generator

## Purpose
Produce readable Hindi captions synchronized to final narration audio.

## Scope
Transcription from final audio, Devanagari spelling, segmentation, SRT timing, and subtitle QC.

## Boundaries
Do not time captions only from a draft script when final audio is available.

## Required inputs
Final voiceover audio, approved script, pronunciation glossary, frame rate if needed.

## Original workflow guidance (preserved from the supplied UNVELL DECODE pack)

## Objective
Produce readable Hindi captions synchronized to the final narration.

## Workflow
1. Transcribe from the final audio, not only from the original script.
2. Preserve Devanagari spelling and punctuation.
3. Break captions at natural phrase boundaries.
4. Avoid overly long lines; aim for readable line length and sufficient display time.
5. Check names, dates, technical terms and numbers manually.
6. Ensure SRT timestamps are sequential and do not overlap unless intended.

## Deliverables
`hindi_subtitles.srt`, `subtitle_qc.md`.

## Outputs
hindi_subtitles.srt, subtitle_qc.md.

## Handoff
Coordinate with: voiceover-director, ai-voice-generation-engineer, automated-video-renderer. Do not duplicate their responsibilities; provide the named artifacts and a concise handoff note.

## Completion checks
- Deliverables exist at the stated paths; do not claim a file was created unless it is present.
- Separate verified facts, supported interpretations, hypotheses, and unknowns.
- Record blockers and missing inputs explicitly.
- Never expose credentials or start paid/bulk actions without explicit approval.
