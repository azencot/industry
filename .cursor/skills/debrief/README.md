# Debrief files

**All session debriefs live here** — alongside [`.cursor/skills/debrief/SKILL.md`](SKILL.md).

Conclusions and handoffs from prep sessions. Use in a new Cursor chat via `@Files .cursor/skills/debrief/…`.

**vs [`Amazon_FinTech/mocks/`](../../Amazon_FinTech/mocks/):** `mocks/` = simulated interview drills (timed-code, full-mock, mock-lp). This folder = wrap-ups, synthesis, exploration notes, cross-session conclusions.

## Naming

| Pattern | Use for |
|---------|---------|
| `YYYY-MM-DD_{topic}.md` | Per-session debrief (e.g. `2026-06-24_prep-strategy.md`) |
| `{name}_{topic}.md` | Long-lived reference docs (e.g. `omri_azencot_experience.md`) |

Update the debrief index in [`Amazon_FinTech/INDEX.md`](../../Amazon_FinTech/INDEX.md) after each entry.

## Template (per-session)

```markdown
# Debrief — [YYYY-MM-DD] — [topic]

## Session

- Type: [exploration | strategy | post-mock | post-interview | other]
- Duration:
- Prior context: [@Past Chats link or "session A on …"]

## Conclusions

-

## Decisions / artifacts updated

- [ ] prep-plan.md
- [ ] stories/
- [ ] omri_azencot_experience.md (if experience framing changed)
- [ ] AGENTS.md or skills

## Open questions

-

## Next session (one prompt for session B)

> Read this file and …
```

## Handoff (session B)

```text
@Files .cursor/skills/debrief/YYYY-MM-DD_topic.md
Synthesize and update [target file].
```

Run **`/debrief`** to fill this template and promote recurring fixes to [`AGENTS.md`](../../AGENTS.md) or other skills.
