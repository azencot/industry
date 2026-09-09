# Debrief — 2026-09-08 — Apple Health AIML virtual on-site (day)

**When:** Tue 2026-09-08, five Webex slots.  
**Role:** ML Research Scientist — Health AIML.  
**Hub:** [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md)

Tyler’s person↔theme map did **not** hold 1:1. Capture that, then wait.

| Slot | Person | Ran as | Log |
|------|--------|--------|-----|
| 11:05 | Jonathan | Scientific rigor on **ImagenFew** (not dual-tower) | [`2026-09-08_onsite-jonathan-debrief.md`](2026-09-08_onsite-jonathan-debrief.md) |
| 1:05 | Yujie Li | **System thinking**, not encoding | [`2026-09-08_onsite-yujie-debrief.md`](2026-09-08_onsite-yujie-debrief.md) |
| 2:05 | Chung-Cheng | Not yet written up | — |
| 3:05 | Haraldur | **Time-series representations** (details not recovered same evening) | This file, thin |
| 4:05 | Vincent Chan | Background, then **fitness-team infra**, then **menstrual onset**; ran **~15 min over** | This file, thin |

Do not email interviewers. Outcome unknown.

---

## Haraldur (thin)

Hour felt **good**. Object was **time-series representations**, not the PPV / ship sheet. Details not remembered the same evening — append if they come back (JEPA/MAE, native Hz, patch vs task, what he pushed).

Mapping note: this group’s sensor-FM work lives in representation. A “health” name on the invite does not force a metrics hour.

---

## Vincent (thin)

Long background chat, then two technical threads. Energy at the end of five; he **extended ~15 min**.

1. **Infra for the Apple fitness team.** Discussion covered data, encoding, modeling, training, eval. Self-read: **not great** — walked the research program rather than systems that make the next experiment cheap (permitted data, labeling, participant-disjoint **harness**, train/serve, on-device vs cloud, ownership).
2. **Predict menstrual onset.** Data, labels, first PoC, metrics, train/test split. Right skeleton for his product shape (sparse self-report + physiology + population). Do **not** mention a patent.

Signals: overtime with an EM is interest, not courtesy. Infra question is the owned miss. Menstrual thread staying in labels / PoC / split / metrics is the exam even if it felt messy.

---

## Chung-Cheng

Not captured in this dump. Add a per-person file if the hour comes back (bottleneck vs tool names; global batch).

---

## Wait

Tyler / Shirley decide. No follow-up email to the five. Next write-up: recover Haraldur representation probes and Chung-Cheng if possible.
