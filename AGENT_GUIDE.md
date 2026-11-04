# Universal Engineering Agent Guide

## Mission
Use this library as a modular set of specialist workflows for software, AI, infrastructure, and documentary projects. Select only the skills relevant to the task.

## How to select skills
1. Understand the requested outcome, constraints, and project instructions.
2. Read `SKILL_CATALOG.md` and choose the smallest set of skills with non-overlapping responsibilities.
3. Load specialist `SKILL.md` instructions when needed; do not paste all 91 skills into context.
4. Sequence dependent work and parallelize only independent tasks.
5. Keep artifacts, approvals, blockers, and handoffs explicit.

## Cross-platform conventions
- Shared skills live in `.claude/skills/<id>/SKILL.md`.
- Each skill directory name and frontmatter `name` must match.
- Use lowercase kebab-case IDs.
- `SKILL.md` contains core workflow instructions; supporting files are optional and should be loaded only when needed.

## Global rules
- Inspect existing source, project instructions, tests, configuration, and tool availability before making changes.
- Verify current APIs, model IDs, pricing, limits, licensing, and platform behavior against current official documentation.
- Do not invent features, test results, file paths, sources, or completed actions.
- Never hard-code or print credentials.
- Request approval before paid or bulk operations, production changes, destructive operations, or external publishing.
- Preserve working behavior and report exact files changed and tests run.
- For reverse engineering, work only on software/artifacts owned by the operator or explicitly authorized for analysis.

## Documentary-specific rules
For UNVELL DECODE, all audience-facing documentary deliverables (script, narration, on-screen text, subtitles, title, description, chapters, thumbnail copy) must be natural Hindi in Devanagari. Explain workflow to the operator in Bengali when appropriate.

Use `production-orchestrator` to coordinate the documentary pipeline. Research and fact-check must precede script approval; storyboard approval precedes generation; rights and provenance checks precede final publishing preparation. Mark AI reconstructions as reconstructions; never call them archival footage. Do not trigger paid or large-batch media generation without approval. Do not upload or publish without approval.

## Capability honesty
Skills provide instructions. They do not provide models, API access, MCP servers, GPU compute, TTS, image/video generation, or FFmpeg by themselves. Verify the required integration and local executable before claiming a task can be performed.
