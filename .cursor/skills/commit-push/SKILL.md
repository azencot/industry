---
name: commit-push
description: >-
  Commit and push git changes in the industry repo without Cursor co-author
  attribution or --trailer failures. Use when the user asks to commit, push,
  save to GitHub, or invokes /commit-push.
---

# Commit and push (no Cursor attribution)

## Rules

- **Never** add Cursor co-author trailers, `Co-authored-by`, or Cursor attribution in commit messages
- **Never** use `git commit -m` or HEREDOC `-m` — environment may inject unsupported `--trailer`
- **Never** update git config
- Use **`/usr/local/bin/git`** if plain `git commit` fails
- Push only when the user explicitly asked to commit/push

## Workflow

1. Run in parallel from repo root:
   ```bash
   /usr/local/bin/git status
   /usr/local/bin/git diff
   /usr/local/bin/git diff --staged
   /usr/local/bin/git log -1 --oneline
   ```
2. Stage only relevant paths — do not commit secrets (`.env`, credentials)
3. Write commit message to temp file and commit with `-F`:

   ```bash
   MSG="$(mktemp)"
   cat > "$MSG" <<'EOF'
   Short summary line.

   Optional body with why, not what only.
   EOF
   /usr/local/bin/git add <paths>
   /usr/local/bin/git commit -F "$MSG"
   rm -f "$MSG"
   ```

4. Verify:
   ```bash
   /usr/local/bin/git status
   /usr/local/bin/git log -1 --format=full
   ```
   Confirm author is **Omri Azencot** with no Cursor trailer lines.

5. Push (if requested):
   ```bash
   /usr/local/bin/git push -u origin HEAD
   ```
   Remote: `git@github.com:azencot/industry.git`

## If commit fails with `unknown option trailer`

1. Retry with full path: `/usr/local/bin/git commit -F "$MSG"`
2. Do not pass `--trailer`, `--cleanup`, or amend unless user rules allow amend
3. Do not use `git commit -m`

## Commit message style

- 1–2 sentences; focus on **why**
- Match repo tone (prep infra, stories, code solutions, debrief logs)
- Examples:
  - `Add AGENTS.md and prep skills for Amazon FinTech interview loop.`
  - `Log 2026-06-24 timed-code mock; update sliding window notes.`

## Optional helper script

```bash
.cursor/skills/commit-push/scripts/commit.sh "subject line" "optional body"
```

Push separately: `/usr/local/bin/git push origin main`
