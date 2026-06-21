#!/usr/bin/env bash
# Commit with -F to avoid --trailer injection. No Cursor attribution.
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"

GIT="${GIT:-/usr/local/bin/git}"
SUBJECT="${1:?Usage: commit.sh \"subject\" [body line ...]}"
shift || true

MSG="$(mktemp)"
if [ $# -gt 0 ]; then
  printf '%s\n\n' "$SUBJECT" > "$MSG"
  printf '%s\n' "$@" >> "$MSG"
else
  printf '%s\n' "$SUBJECT" > "$MSG"
fi

"$GIT" add -A
"$GIT" commit -F "$MSG"
rm -f "$MSG"

"$GIT" log -1 --format='Committed %h by %an <%ae>%n%s'
