#!/usr/bin/env bash
set -euo pipefail
SOURCE="$(cd "$(dirname "$0")" && pwd)/.claude/skills"
TARGET="$HOME/.claude/skills"
[[ -d "$SOURCE" ]] || { echo "Skills source not found: $SOURCE" >&2; exit 1; }
mkdir -p "$TARGET"
installed=0; skipped=0
for skill_dir in "$SOURCE"/*; do
  [[ -d "$skill_dir" ]] || continue
  name="$(basename "$skill_dir")"
  if [[ -e "$TARGET/$name" ]]; then
    echo "SKIP existing: $name"
    ((skipped+=1))
  else
    cp -R "$skill_dir" "$TARGET/$name"
    echo "INSTALLED: $name"
    ((installed+=1))
  fi
done
echo "Done. Installed=$installed Skipped=$skipped Target=$TARGET"
