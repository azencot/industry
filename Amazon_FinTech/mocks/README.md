# Mock session logs

Create one file per session: `YYYY-MM-DD_{type}.md` (e.g. `2026-06-26_full-mock.md`, `2026-06-24_timed-code.md`).

Update the mock index table in [`../INDEX.md`](../INDEX.md) after each entry.

## Template

```markdown
# Mock — [YYYY-MM-DD] — [type: full-mock | timed-code | ml-deep-dive | mock-lp]

## Setup

- Duration:
- Focus:
- Problems / LPs / ML topics covered:

## What went well

-

## What broke

- [ ] Verbal / structure issue:
- [ ] Technical gap:
- [ ] LP story weak (which):

## Corrections to promote

| Observation | Update where |
|-------------|--------------|
| e.g. forgot to state complexity | AGENTS.md or timed-code skill |
| e.g. story used "we" too much | stories/[file].md |

## Next session (one thing)

-
```

## Closing the loop

Recurring phrases in your corrections ("still wrong", "did you check", "can you also") mean something should move from session chat into:

- [`AGENTS.md`](../../AGENTS.md) — behavior or convention
- [`.cursor/skills/`](../../.cursor/skills/) — workflow step
- [`stories/`](../stories/) — story content
- [`INDEX.md`](../../INDEX.md) — timed log or index annotation

Run `/debrief` to automate this write-up.
