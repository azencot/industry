# Log — 2026-08-20 — Bosch technical agenda (Joy)

**Status:** **Rescheduled.** **Thu 2026-08-27, 10:00–11:00 AM PT** (1h; confirm exact clock on Teams). **No overlap** with Apple Tue 8/25 1:35–2:20 PM PDT. Coding should arrive **now that the date is set**.  
**From:** Joy (Senior Recruitment Partner)  
**Role they used:** **AI Research Scientist — Multimodal Foundational Models** (matches the HM req; Aug 19 said “Sr.” — don’t fight either)  
**Prior:** [`2026-08-19_next-round-invite.md`](2026-08-19_next-round-invite.md) · [`2026-08-13_hm-screen-debrief.md`](2026-08-13_hm-screen-debrief.md)

---

## Slot (locked 2026-08-21)

| | |
|--|--|
| **When** | **Thu 2026-08-27, 10:00–11:00 AM PT** |
| **What** | 1h technical: 25 talk + 20 previous-work Q&A + 15 coding discuss |
| **Where** | Microsoft Teams — Accept the invite; join from that link |
| **vs Apple** | Apple tech screen is **Tue 8/25 1:35–2:20 PM PDT**. **No collision.** |

If the Teams item shows a different start minute, paste it here and use the invite, not this table.

---

## Agenda (locked — 60 min)

| Block | Time | What they wrote |
|-------|------|-----------------|
| **Talk** | **25 min** | Conference-style presentation: introduction of **research and background** |
| **Q&A** | **20 min** | Questions / discussions about **previous work** |
| **Coding** | **15 min** | Coding exercise **assessment and discussion** |

**Background introduction (~45 min)** = talk + research Q&A. Coding is a **separate 15 min** at the end, not mixed into the panel.

This supersedes the Aug 19 wording (30-min talk; take-home “two days prior”; Q&A untimed). Same hour, cleaner split.

---

## What changed vs Aug 19

| | Aug 19 invite | This agenda |
|--|---------------|-------------|
| Talk | 30 min | **25 min** — hard stop |
| Q&A | untimed “followed by panel Q&A” | **20 min**, explicitly **previous work** |
| Coding | sent **two days prior**; discuss in-hour | sent **once the date is confirmed**; **15 min** discuss |
| Title | Sr. Research Scientist | AI Research Scientist |
| Platform | (implied) | **Microsoft Teams** — install; join the invite link |
| Conflict | — | Tell them **≥1 hour prior** to reschedule |

Do **not** treat “background” as a CV walk. Conference-style + researcher-skills = the VLM talk. IC identity is **spoken** on the title slide, not a bio deck.

---

## Talk implication

The spoken map is **23 slides** at ~1 min. That already **is** a 25-min talk (2 min slack). Do **not** add slides. Do **not** cut five slides.

- **Hard stop on 23.** Slides 24–25 stay panel-only.
- If slow: **drop 21** (scale). Do not eat the 20-min Q&A.
- If fast: do **not** promote backups into the 25. Sit down; they paid for 20 min of previous-work questions.
- Transfer (22) still closes the method: if a sensor admits an image, it enters this VLM. Not a 6-month plan.

Deck: [`talks/ts-vlm/bosch-30min.html`](../../../talks/ts-vlm/bosch-30min.html) (filename stays; Bosch cut is 25). Map: [`talks/ts-vlm/README.md`](../../../talks/ts-vlm/README.md).

---

## Coding implication

15 min is a **walkthrough**, not a live problem from scratch. Take-home is in. PDF/zip stay in [`code_assignment/`](code_assignment/). **Working copy is outside this repo:** `~/bosch-rtc-coding/lightning-hydra-uv-template` (own `.git`; zip that folder). Discussion here; do not commit the working tree into `industry`. Q&A (20) is research; coding (15) is the exercise.

---

## Immediate next actions

1. Take-home **submitted** (2026-08-26). Numbers + 15-min spine: [`2026-08-26_take-home-submit.md`](2026-08-26_take-home-submit.md).
2. Talk = existing 23-slide map, **hard stop on 23**. Reloc / level-scope / don’t fight the title — unchanged. **20 min previous work:** [`2026-08-26_previous-work-qa.md`](2026-08-26_previous-work-qa.md) (LDDBM + ImagenTime; skip CV).
3. Thu 8/27 Teams: 25 + 20 + 15 coding walkthrough. Quote **best @ 116**, not last.ckpt. Don’t mix Apple scripts.

---

## Email (as received)

> Hello,
>
> Thank you for you continued interest in the AI Research Scientist- Multimodal Foundational Models role with Bosch Corporate Research in Sunnyvale, CA! This technical interview invitation will be to assess the skills you’ve refined as a researcher.
>
> Agenda:
>
> Background Introduction (~45 mins):
> Conference-style Presentation: Introduction of your research and background (25 mins)
> Questions / Discussions about your previous work (20 mins)
> Coding exercise assessment and discussion (15 mins)
>
> Once you confirm the interview date, we will send you the coding exercise. If you have any questions or need to reschedule, don't hesitate to contact me by replying to this invitation. Our team uses Microsoft teams, ensure your technology is installed and join the below link for the interview.
>
> Should a conflict arise at this time, please let us know at least an hour prior that we need to reschedule.
>
> All the best,
>
> Joy

---

## Hand-off prompt (next session)

```
@GenAI/interviews/bosch-rtc-tsfm/2026-08-20_technical-agenda.md
@GenAI/interviews/bosch-rtc-tsfm/2026-08-13_hm-screen-debrief.md
@talks/ts-vlm/README.md
Bosch 1h technical **Thu 2026-08-27, 10:00–11:00 AM PT**. Agenda: **25 min talk + 20 min previous-work Q&A + 15 min coding discuss**. Take-home debrief: [`2026-08-24_take-home-debrief.md`](2026-08-24_take-home-debrief.md). Code at `~/bosch-rtc-coding/lightning-hydra-uv-template`. Apple Feng is **Tue 8/25 first**. Talk = 23-slide map, hard stop on 23. Reloc in-play. Don’t fight title. Don’t mix Apple Health scripts.
```
