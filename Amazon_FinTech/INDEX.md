# Amazon FinTech — Senior Applied Scientist (FinTelligence)

Active interview track. Annotated index — read entries before opening every file.

---

## Timeline

| Milestone | Date | Notes |
|-----------|------|-------|
| **PS1 — phone screen** | Tue 30 Jun 2026, 21:00 Asia/Jerusalem | Karan Aggarwal; Zoom + [Live Code](https://livecode.amazon.jobs/joinsession/e4618c8d-2a90-4c8f-8fb1-b6e875c77bd7) |
| Prep window | ~21–30 Jun 2026 | See [`prep-plan.md`](prep-plan.md) |

---

## Key files

| File | What | When to read |
|------|------|--------------|
| [`.cursor/skills/debrief/omri_azencot_experience.md`](../.cursor/skills/debrief/omri_azencot_experience.md) | **Canonical experience profile** — research arc, VLM flagship, JD alignment, interview framing | Start of every session; before pitch / ML deep-dive |
| [`elevator-pitch.md`](elevator-pitch.md) | **PS1 intro script** (~90s spoken) — who → work → why FinTelligence; optional 30s + 45s cuts | Day 1; read aloud before PS1 |
| [`prep-plan.md`](prep-plan.md) | 7-day prep schedule (coding, ML, LP, mocks) | Daily — find today's block |
| [`CV_Azencot_10399493.pdf`](CV_Azencot_10399493.pdf) | Resume for this application | Before intro / resume walkthrough |
| [`stories/`](stories/) | STAR stories by Leadership Principle | Before LP drills and interview |
| [`.cursor/skills/debrief/`](../.cursor/skills/debrief/) | Session debriefs & cross-chat handoffs | Start session B; after `/debrief` |
| [`mocks/`](mocks/) | Simulated interview drill logs | After timed-code / full-mock / mock-lp |

---

## Role summary (from JD)

- LLM + multi-agent systems for **finance operations** at scale (payments, contracts, cash application, investigation)
- **Trust without manual review** — precision = compliance
- **Learning from user corrections**; eval frameworks that **gate** model changes
- **Tiered inference**: routing, SLMs, cost vs frontier quality

Full posting context lives in prep chat / recruiter email — not duplicated here.

---

## Interviewer — Karan Aggarwal

- **Role:** Senior Applied Scientist (FinTech background; NLP, limited-label learning)
- **Likely interests:** document IE for payments/cash optimization, synthetic data for NER, continual pre-training for financial LLMs, production eval
- **Read before PS1:**
  - [Efficient continual pre-training LLMs for financial domains](https://aws.amazon.com/blogs/machine-learning/efficient-continual-pre-training-llms-for-financial-domains/) (co-authored)
  - [ECG-QALM — synthetic text for NER](https://www.amazon.science/publications/ecg-qalm-entity-controlled-synthetic-text-generation-using-contextual-q-a-for-ner) (abstract)
- **Questions to ask him (pick 2):** eval gating before ship; how user corrections feed back; SLM vs frontier routing; hardest LLM failure mode on financial docs

---

## PS1 format (~60 min)

1. Intro / resume — 10–15 min
2. ML / LLM technical — 15–20 min
3. Leadership Principles — 10–15 min (1–2 STAR)
4. Live coding — 20–25 min (1 medium, Python OK)
5. Your questions — 5 min

**Logistics:** Join Zoom at start time (waiting room ~10 min). Test AV at https://amazon.zoom.us/test

---

## Story bank status

Track which LPs have ready stories in [`stories/README.md`](stories/README.md). Target: **8 strong stories** covering the priority LPs before PS1.

---

## Debrief index

| Date | Topic | File | Handoff for session B |
|------|-------|------|------------------------|
| 2026-06-21 | experience profile | [`omri_azencot_experience.md`](../.cursor/skills/debrief/omri_azencot_experience.md) | `@Files .cursor/skills/debrief/omri_azencot_experience.md` |

Add a row after each `/debrief`. Store files in [`.cursor/skills/debrief/`](../.cursor/skills/debrief/).

## Mock log index

| Date | Type | File | Top weakness fixed? |
|------|------|------|---------------------|
| | | | |

Add a row after each mock drill. Store files in [`mocks/`](mocks/).
