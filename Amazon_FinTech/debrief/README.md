# Debrief files

**Amazon FinTech-specific session debriefs live here** — alongside [`mocks/`](../mocks/) for simulated interview drills.

Conclusions and handoffs from prep sessions. Use in a new Cursor chat via `@Files Amazon_FinTech/debrief/…`.

**vs [`mocks/`](../mocks/):** `mocks/` = simulated interview drills (timed-code, full-mock, mock-lp). This folder = Amazon FinTech wrap-ups, synthesis, exploration notes, cross-session conclusions.

**General reusable references** about Omri or project background live in [`.cursor/skills/debrief/`](../../.cursor/skills/debrief/) — e.g. `omri_azencot_experience.md` and `vlm_multimodal_project.md`.

Run **`/debrief`** (skill: [`.cursor/skills/debrief/SKILL.md`](../../.cursor/skills/debrief/SKILL.md)) to fill the template and promote recurring fixes to [`AGENTS.md`](../../AGENTS.md) or other skills.

## Naming

| Pattern | Use for |
|---------|---------|
| `YYYY-MM-DD_{topic}.md` | Per-session debrief (e.g. `2026-06-24_prep-strategy.md`) |

Update the debrief index in [`../INDEX.md`](../INDEX.md) after each entry.

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
@Files Amazon_FinTech/debrief/YYYY-MM-DD_topic.md
Synthesize and update [target file].
```
