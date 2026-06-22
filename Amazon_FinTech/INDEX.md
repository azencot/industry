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
| [`anchor-cheat-sheet.md`](anchor-cheat-sheet.md) | **Day 1 deliverable** — 3 VLM anchors (A/B/C): metric, IC role, JD map, LP hooks | Before ML deep-dive and LP drills |
| [`.cursor/skills/debrief/vlm_multimodal_project.md`](../.cursor/skills/debrief/vlm_multimodal_project.md) | **Extended VLM project summary** — architecture, results, problems solved; extend over time | `@Files` for ML deep-dive, new results, follow-ups |
| [`elevator-pitch.md`](elevator-pitch.md) | **PS1 intro script** (~90s spoken) — who → work → why FinTelligence; optional 30s + 45s cuts | Day 1; read aloud before PS1 |
| [`stories/tell-me-about-yourself.md`](stories/tell-me-about-yourself.md) | **TMAY** (~2–3 min) — career arc; IC para 2 | Intro / resume block |
| [`stories/why-amazon.md`](stories/why-amazon.md) | **Why Amazon** (~1:30) — speakable prose; JD phrases verbatim | Day 3; if asked in intro |
| [`prep-plan.md`](prep-plan.md) | 7-day prep schedule (coding, ML, LP, mocks) | Daily — find today's block |
| [`CV_Azencot_10399493.pdf`](CV_Azencot_10399493.pdf) | Resume for this application | Before intro / resume walkthrough |
| [`stories/`](stories/) | STAR stories by Leadership Principle | Before LP drills and interview |
| [`.cursor/skills/debrief/`](../.cursor/skills/debrief/) | Session debriefs & cross-chat handoffs | Start session B; after `/debrief` |
| [`mocks/`](mocks/) | Simulated interview drill logs | After timed-code / full-mock / mock-lp |
| [`debrief/`](debrief/) | FinTech-track session debriefs & reading notes | Start session B; after exploration reads |

---

## Role summary (from JD)

- LLM + multi-agent systems for **finance operations** at scale (payments, contracts, cash application, investigation)
- **Trust without manual review** — precision = compliance
- **Learning from user corrections**; eval frameworks that **gate** model changes
- **Tiered inference**: routing, SLMs, cost vs frontier quality

Full posting context lives in prep chat / recruiter email — not duplicated here.

### Writing rules (scripts + stories)

Agents and drafts for this track:

- **Use JD wording** from the role summary above — quote it; do not rewrite into pitch language.
- **No cheese:** avoid “I'm excited about,” “three things together,” “that's the discipline I want in production,” “not in a vacuum,” “deep problem-solving under uncertainty,” LP self-labels, or closing summaries that tell the interviewer what to think.
- **Motivation scripts** (~1:30 spoken): full sentences that read aloud; not telegraphic bullets. One concrete example in the middle — not a metric list.
- Tone model: [`elevator-pitch.md`](elevator-pitch.md) and Omri's plain spoken drafts — not corporate interview copy.

---

## Interviewer — Karan Aggarwal

- **Role:** Senior Applied Scientist (FinTech background; NLP, limited-label learning)
- **Likely interests:** document IE for payments/cash optimization, synthetic data for NER, continual pre-training for financial LLMs, production eval
- **Read before PS1:**
  - [Efficient continual pre-training LLMs for financial domains](https://aws.amazon.com/blogs/machine-learning/efficient-continual-pre-training-llms-for-financial-domains/) (co-authored) · paper [arxiv:2311.08545](https://arxiv.org/abs/2311.08545)
  - [ECG-QALM — synthetic text for NER](https://www.amazon.science/publications/ecg-qalm-entity-controlled-synthetic-text-generation-using-contextual-q-a-for-ner) (abstract only; [ACL PDF](https://aclanthology.org/2023.findings-acl.349.pdf) if needed)
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
| 2026-06-21 | VLM project summary + Day 1 anchors | [`vlm_multimodal_project.md`](../.cursor/skills/debrief/vlm_multimodal_project.md) | `@Files vlm_multimodal_project.md` + `anchor-cheat-sheet.md` |
| 2026-06-21 | Day 2 — continual pre-training blog (Karan) | [`2026-06-21_continual-pretraining-blog.md`](debrief/2026-06-21_continual-pretraining-blog.md) | `@Files debrief/2026-06-21_continual-pretraining-blog.md` + `/ml-deep-dive` |
| 2026-06-21 | Day 2 — ML depth interactive (3 topics) | [`2026-06-21_day2-ml-depth.md`](../.cursor/skills/debrief/2026-06-21_day2-ml-depth.md) | `@Files 2026-06-21_day2-ml-depth.md` + spoken drill retake |
| 2026-06-22 | Day 3 — LP stories DOC L6 (Invent + Deliver Results) | [`2026-06-22_day3-lp-stories.md`](../.cursor/skills/debrief/2026-06-22_day3-lp-stories.md) | `@Files 2026-06-22_day3-lp-stories.md` + draft Ownership (TR kill) |

Add a row after each `/debrief`. FinTech-track notes → [`debrief/`](debrief/); cross-session profile → [`.cursor/skills/debrief/`](../.cursor/skills/debrief/).

## Mock log index

| Date | Type | File | Top weakness fixed? |
|------|------|------|---------------------|
| 2026-06-21 | ml-deep-dive | [`2026-06-21_ml-deep-dive.md`](mocks/2026-06-21_ml-deep-dive.md) | IC voice + metrics on Topics 1–2 (retake pending) |

Add a row after each mock drill. Store files in [`mocks/`](mocks/).
