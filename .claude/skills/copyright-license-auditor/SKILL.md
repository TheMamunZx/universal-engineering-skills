---
name: copyright-license-auditor
description: "Track copyright, licenses and media provenance"
---

# copyright-license-auditor

## Purpose
Reduce rights risk and preserve provenance for all third-party and generated assets.

## Scope
Creators, source URLs, license terms, attribution, commercial use, modifications, dates, and provider terms.

## Boundaries
Do not assume “free” means reusable, remove watermarks, or provide legal guarantees.

## Required inputs
Asset manifest, source URLs, license texts, provider terms, planned distribution.

## Original workflow guidance (preserved from the supplied UNVELL DECODE pack)

## Objective
Reduce copyright risk and preserve provenance for every third-party asset.

## Workflow
1. For each image, video, music track, SFX, font or map, record creator, source URL, license, attribution, commercial-use terms, modification terms and download date.
2. Do not infer a license from “free download” or from the website name alone.
3. Flag assets with unclear license, non-commercial-only terms, attribution requirements, editorial-only terms or account restrictions.
4. For provider-generated assets, check the service's current terms for intended use and redistribution.
5. Never remove watermarks or bypass access controls.
6. Require human review for unclear rights.

## Deliverable
`asset_license_register.csv` and a blocking issue list.

## Outputs
asset_license_register.csv and blocking issue list.

## Handoff
Coordinate with: documentary-media-generator, audio-designer, youtube-packager. Do not duplicate their responsibilities; provide the named artifacts and a concise handoff note.

## Completion checks
- Deliverables exist at the stated paths; do not claim a file was created unless it is present.
- Separate verified facts, supported interpretations, hypotheses, and unknowns.
- Record blockers and missing inputs explicitly.
- Never expose credentials or start paid/bulk actions without explicit approval.
