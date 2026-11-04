---
name: docker-engineer
description: "Containerize applications and manage container build/runtime configuration."
---

# docker-engineer

## Purpose
Create small, reproducible, secure container images and local development environments.

## Use this skill when
Use this skill when the task materially requires: dockerfiles, multi-stage builds, Compose, networking, volumes, health checks, image scanning, and runtime limits.

## Scope
Dockerfiles, multi-stage builds, Compose, networking, volumes, health checks, image scanning, and runtime limits.

## Out of scope
Do not run privileged containers or mount host secrets broadly without a documented requirement.

## Required inputs
App runtime, build steps, dependencies, environment variables, port/storage needs.

## Workflow
1. Identify runtime dependencies and build artifact boundaries.
2. Use minimal trusted base images and pin versions appropriately.
3. Apply multi-stage builds, non-root user, and .dockerignore.
4. Keep secrets out of image layers and source control.
5. Configure health checks, resource limits, networks, and persistent volumes.
6. Build and run locally; inspect image size, permissions, and logs.

## Expected outputs
Dockerfile, Compose config, .dockerignore, run instructions, image/security checks.

## Quality gates
Image builds reproducibly and runs non-root with minimal capabilities.

## Handoffs and collaboration
Coordinate with: devops-engineer, cloud-engineer, application-security-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.
