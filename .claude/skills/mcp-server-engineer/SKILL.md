---
name: mcp-server-engineer
description: "Build Model Context Protocol servers and tool integrations."
---

# mcp-server-engineer

## Purpose
Expose well-described resources, prompts, and tools through a maintainable MCP server.

## Use this skill when
Use this skill when the task materially requires: mCP transport choice, tool schemas, input validation, resource design, auth boundaries, errors, and client compatibility.

## Scope
MCP transport choice, tool schemas, input validation, resource design, auth boundaries, errors, and client compatibility.

## Out of scope
Do not expose arbitrary host access, secrets, or dangerous side effects as unrestricted tools.

## Required inputs
Target client, runtime, required capabilities, external services, auth method, deployment constraints.

## Workflow
1. Read the current MCP specification and target-client support.
2. Define the smallest useful set of tools/resources with clear descriptions.
3. Validate inputs and constrain paths, URLs, queries, and side effects.
4. Implement structured outputs, safe errors, cancellation, and timeouts.
5. Protect credentials and separate read-only from mutating capabilities.
6. Test discovery, tool calls, malformed inputs, client compatibility, and failure states.

## Expected outputs
MCP server implementation, tool/resource schemas, setup guide, contract tests, security notes.

## Quality gates
Tools are least-privilege, discoverable, schema-valid, and tested against intended clients.

## Handoffs and collaboration
Coordinate with: ai-agent-architect, function-calling-engineer, application-security-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
