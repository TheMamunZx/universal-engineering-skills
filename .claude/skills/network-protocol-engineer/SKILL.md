---
name: network-protocol-engineer
description: "Design and implement application-level network protocols."
---

# network-protocol-engineer

## Purpose
Define interoperable message formats and connection behavior.

## Use this skill when
Use this skill when the task materially requires: framing, encoding, versioning, errors, authentication boundaries, timeouts, and protocol tests.

## Scope
Framing, encoding, versioning, errors, authentication boundaries, timeouts, and protocol tests.

## Out of scope
Do not implement covert channels, interception, or unauthorized network manipulation.

## Required inputs
Use case, endpoints, threat model, transport, message sizes, compatibility requirements.

## Workflow
1. Define actors, states, messages, and expected transitions.
2. Specify framing, encoding, version negotiation, and error semantics.
3. Set bounds for message size, timeouts, and resource usage.
4. Design authentication and replay protection appropriate to the use case.
5. Implement parser validation and robust handling of malformed inputs.
6. Run interoperability and fuzz/property tests in a controlled environment.

## Expected outputs
Protocol specification, state machine, reference implementation, interoperability tests.

## Quality gates
Protocol is documented, bounded, versionable, and robust against malformed inputs.

## Handoffs and collaboration
Coordinate with: distributed-systems-engineer, operating-system-engineer, api-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
