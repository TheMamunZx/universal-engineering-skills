---
name: operating-system-engineer
description: "Explore or implement operating-system components in controlled environments."
---

# operating-system-engineer

## Purpose
Design educational or product-specific OS subsystems with clear hardware boundaries.

## Use this skill when
Use this skill when the task materially requires: boot flow, processes, memory management, scheduling, filesystems, drivers, and system calls.

## Scope
Boot flow, processes, memory management, scheduling, filesystems, drivers, and system calls.

## Out of scope
Do not modify a live host OS or flash devices; use emulators/virtual machines and preserve recovery paths.

## Required inputs
Target architecture, emulator/VM, boot method, subsystem goal, toolchain.

## Workflow
1. Choose one bounded subsystem and define its interface.
2. Set up a disposable emulator/VM and reproducible toolchain.
3. Document boot, memory, interrupt, and privilege assumptions.
4. Implement incrementally with serial logs and assertions.
5. Test normal and failure paths in the emulator.
6. Document unsupported hardware and safe recovery steps.

## Expected outputs
Subsystem design, build instructions, emulator test plan, known limitations.

## Quality gates
Work remains isolated in an emulator/VM; build and boot steps are reproducible.

## Handoffs and collaboration
Coordinate with: compiler-engineer, network-protocol-engineer, database-internals-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
