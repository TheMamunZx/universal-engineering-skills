# Universal Engineering Skills Library

A reusable library of 91 modular agent skills for Claude Code and OpenCode. Each skill lives in `.claude/skills/<skill-id>/SKILL.md`, the shared Claude-compatible discovery path supported by both tools.

## Contents
- 63 universal software and engineering skills
- 10 Android and AI application specialization skills
- 15 original UNVELL DECODE documentary skills preserved and integrated from the supplied ZIP
- 3 additional documentary execution skills for media generation, voice generation, and automated rendering

See `SKILL_CATALOG.md` for the complete index and responsibility boundaries. See `AGENTS.md`, `CLAUDE.md`, and `AGENT_GUIDE.md` for portable operating guidance.

## Install
- Project-local: copy `.claude/skills/` into the root of the project you want to work on.
- Global Windows: run `./install-global-windows.ps1` in PowerShell.
- Global macOS/Linux: run `./install-global-unix.sh`.

Both installers preserve existing same-name skills and skip them rather than overwrite. Review and merge manually if you intentionally want to update an existing skill.

Validate with `python scripts/validate_skills.py`.

## Important
Skills are instruction packages, not model APIs or media-generation engines. Real capabilities depend on tools, provider configuration, permissions, network access, quota, licensing, and local software. Never place API keys in this repository.
