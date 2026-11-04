#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".claude" / "skills"
errors = []
folders = sorted(p for p in SKILLS.iterdir() if p.is_dir()) if SKILLS.exists() else []
if len(folders) != 91:
    errors.append(f"Expected 91 skill folders, found {len(folders)}")
seen = set()
for folder in folders:
    sid = folder.name
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", sid):
        errors.append(f"Invalid folder ID: {sid}")
    if sid in seen:
        errors.append(f"Duplicate skill ID: {sid}")
    seen.add(sid)
    file = folder / "SKILL.md"
    if not file.is_file():
        errors.append(f"Missing SKILL.md: {sid}")
        continue
    text = file.read_text(encoding="utf-8")
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, flags=re.S)
    if not m:
        errors.append(f"Invalid/missing YAML frontmatter: {sid}")
        continue
    fm = m.group(1)
    name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", fm, flags=re.M)
    desc = re.search(r'^description:\s*"(.*)"\s*$', fm, flags=re.M)
    if not name or name.group(1) != sid:
        errors.append(f"Frontmatter name mismatch: {sid}")
    if not desc or not desc.group(1).strip() or len(desc.group(1)) > 200:
        errors.append(f"Missing/too-long description (max 200 chars): {sid}")
    if len(text.split()) < 100:
        errors.append(f"Skill appears too short (<100 words): {sid}")
if errors:
    print("VALIDATION FAILED")
    for e in errors: print("-", e)
    sys.exit(1)
print(f"VALIDATION PASSED: {len(folders)} unique skill folders; each has a matching SKILL.md and valid portable frontmatter.")
