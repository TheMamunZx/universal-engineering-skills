---
name: coding-agent-engineer
description: "Build AI coding agents that inspect, edit, and test codebases."
---

# coding-agent-engineer

## Purpose
Create a developer agent with safe repository understanding and controlled tool execution.

## Use this skill when
Use this skill when the task materially requires: workspace discovery, context selection, patch planning, file edits, terminal tools, test loops, diffs, and approvals.

## Scope
Workspace discovery, context selection, patch planning, file edits, terminal tools, test loops, diffs, and approvals.

## Out of scope
Do not execute untrusted repository scripts or destructive commands without inspection and appropriate approval.

## Required inputs
Target languages, repo structure, permitted tools, sandbox model, user workflows, test commands.

## Workflow
1. Define supported tasks and workspace boundary.
2. Implement repository indexing and selective context retrieval.
3. Expose read/write/terminal tools with schema validation and least privilege.
4. Use plan → inspect → patch → test → review → summarize loops.
5. Show diffs before risky changes; protect secrets and ignored files.
6. Evaluate patch correctness, regression rate, tool misuse, and recovery behavior.

## Expected outputs
Coding-agent architecture, tool schemas, edit/approval policy, test harness, sample task evaluations.

## Quality gates
All changes are reviewable; tool calls respect permission boundaries; tests are honestly reported.

## Handoffs and collaboration
Coordinate with: ai-agent-architect, codebase-intelligence, mcp-server-engineer, test-automation-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
