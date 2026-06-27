# Amazon FinTech — Senior Applied Scientist (FinTelligence)

Active interview track. Annotated index — read entries before opening every file.

---

## Timeline

| Milestone | Date | Notes |
|-----------|------|-------|
| **PS1 — phone screen** | Tue 30 Jun 2026, 21:00 Asia/Jerusalem | Karan Aggarwal; Zoom + [Live Code](https://livecode.amazon.jobs/joinsession/e4618c8d-2a90-4c8f-8fb1-b6e875c77bd7) |
| Imry Kissos referral call | 23 Jun 2026 | Principal AS; referred to role — Karan-focused prep pivot |
| Prep window | 24–29 Jun 2026 (6 days) | See [`prep-plan.md`](prep-plan.md) — VLM depth + coding |

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
| [`job-description.md`](job-description.md) | **Full JD** — responsibilities, qualifications, JD→prep map | Before tailoring scripts/stories to JD wording |
| [`prep-plan.md`](prep-plan.md) | Karan-focused prep (24–29 Jun): VLM depth + coding | Daily — find today's block |
| [`ps1-questions-for-karan.md`](ps1-questions-for-karan.md) | **PS1 night** — 2 questions to ask Karan + backups + quick reference card | Mon 29 / interview day |
| [`CV_Azencot_10399493.pdf`](CV_Azencot_10399493.pdf) | Resume for this application | Before intro / resume walkthrough |
| [`stories/`](stories/) | STAR stories by Leadership Principle | Before LP drills and interview |
| [`debrief/`](debrief/) | Session debriefs & cross-chat handoffs | Start session B; after `/debrief` |
| [`mocks/`](mocks/) | Simulated interview drill logs | After timed-code / full-mock / mock-lp |
| [`debrief/`](debrief/) | FinTech-track session debriefs & reading notes | Start session B; after exploration reads |

---

## Role summary (from JD)

- LLM + multi-agent systems for **finance operations** at scale (payments, contracts, cash application, investigation)
- **Trust without manual review** — precision = compliance
- **Learning from user corrections**; eval frameworks that **gate** model changes
- **Tiered inference**: routing, SLMs, cost vs frontier quality

Full posting: [`job-description.md`](job-description.md).

### Writing rules (scripts + stories)

Agents and drafts for this track:

- **Use JD wording** from the role summary above — quote it; do not rewrite into pitch language.
- **No cheese:** avoid “I'm excited about,” “three things together,” “that's the discipline I want in production,” “not in a vacuum,” “deep problem-solving under uncertainty,” LP self-labels, or closing summaries that tell the interviewer what to think.
- **Motivation scripts** (~1:30 spoken): full sentences that read aloud; not telegraphic bullets. One concrete example in the middle — not a metric list.
- Tone model: [`elevator-pitch.md`](elevator-pitch.md) and Omri's plain spoken drafts — not corporate interview copy.

---

## Interviewer — Karan Aggarwal

- **Role:** Senior Applied Scientist — **de facto most senior technical person on the team** (Imry, 23 Jun); at Amazon since join; built many in-house tools/frameworks
- **Style (Imry):** Wants **maximum technical detail** — model, training, eval, ablations — not managerial “story.” Young; **rigid** on preferred solution patterns; use standard structure (problem → approach → complexity → code/metrics)
- **Lead with:** VLM time-series project (Imry: interesting + relevant). Prior loop risk: PI framing → keep every answer IC/hands-on
- **Likely interests:** document IE, limited-label learning, continual pre-training, production eval, time-series + LLMs
- **Read before PS1 (skim only):**
  - [Efficient continual pre-training LLMs for financial domains](https://aws.amazon.com/blogs/machine-learning/efficient-continual-pre-training-llms-for-financial-domains/) (co-authored) · [arxiv:2311.08545](https://arxiv.org/abs/2311.08545)
  - [ECG-QALM abstract](https://www.amazon.science/publications/ecg-qalm-entity-controlled-synthetic-text-generation-using-contextual-q-a-for-ner) — optional; bridge is your eval/audit work, not NER synth
- **Coding expectation:** Standard **LeetCode medium** (Python OK). Team uses pandas/numpy day-to-day; Imry says interviewers *rarely* ask that — don't trade coding reps for pandas drill
- **Questions to ask him (pick 2):** [`ps1-questions-for-karan.md`](ps1-questions-for-karan.md) — where trust is hardest; what strong impact looks like; corrections loop; hardest problem class (soft PS1 tone, not audit-style)

### Chronos (team stack — Imry)

Team uses **[Chronos](https://github.com/amazon-science/chronos-forecasting)** for time-series forecasting. **Imry’s patch note = Chronos-Bolt** (production path), not original v1:

| Gen | Representation | Output |
|-----|----------------|--------|
| **v1 (T5)** | 1 quantized bin token per timestep | AR sample paths (probabilistic) |
| **Bolt** | Patch-16 → encoder embedding | Direct multi-step **quantile** forecast |
| **Chronos-2** | Bolt + multivariate / covariates | Universal forecaster |

**Your bridge (VLM project):** Dual visual encodings (chart → Qwen ViT; delay embedding → DINO) — same motivation (efficient TS → general model), different bet (**reasoning + NL**, not forecast quantiles). **Routing answer:** Chronos-class for trajectories; VLM for explain/QA/compliance slices.

**Done (23 Jun):** Chronos bridge in [`prep-plan.md`](prep-plan.md) completed section.

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

Track which LPs have ready stories in [`stories/README.md`](stories/README.md). **Karan pivot:** target **2–3 technical LP reframes** on the VLM project (Ownership/TR kill, Dive Deep/audit, Deliver Results backup) — not an 8-story bank.

---

## Debrief index

| Date | Topic | File | Handoff for session B |
|------|-------|------|------------------------|
| 2026-06-21 | experience profile | [`omri_azencot_experience.md`](../.cursor/skills/debrief/omri_azencot_experience.md) | `@Files .cursor/skills/debrief/omri_azencot_experience.md` |
| 2026-06-21 | VLM project summary + Day 1 anchors | [`vlm_multimodal_project.md`](../.cursor/skills/debrief/vlm_multimodal_project.md) | `@Files vlm_multimodal_project.md` + `anchor-cheat-sheet.md` |
| 2026-06-21 | Day 2 — continual pre-training blog (Karan) | [`2026-06-21_continual-pretraining-blog.md`](debrief/2026-06-21_continual-pretraining-blog.md) | `@Files debrief/2026-06-21_continual-pretraining-blog.md` + `/ml-deep-dive` |
| 2026-06-21 | Day 2 — ML depth interactive (3 topics) | [`2026-06-21_day2-ml-depth.md`](debrief/2026-06-21_day2-ml-depth.md) | `@Files 2026-06-21_day2-ml-depth.md` + spoken drill retake |
| 2026-06-22 | Day 3 — LP stories DOC L6 (Invent + Deliver Results) | [`2026-06-22_day3-lp-stories.md`](debrief/2026-06-22_day3-lp-stories.md) | `@Files 2026-06-22_day3-lp-stories.md` + draft Ownership (TR kill) |
| 2026-06-24 | Chronos bridge (v1 / Bolt / VLM contrast) | [`2026-06-24_chronos-bridge.md`](debrief/2026-06-24_chronos-bridge.md) | `@Files 2026-06-24_chronos-bridge.md` |
| 2026-06-24 | Anchor A spoken drill (Jun 24) | [`2026-06-24_anchor-a-spoken-drill.md`](debrief/2026-06-24_anchor-a-spoken-drill.md) | `@Files 2026-06-24_anchor-a-spoken-drill.md` + Anchor B drill (Wed 25) |
| 2026-06-24 | timed-code 567 permutation | [`2026-06-24_timed-code-567.md`](debrief/2026-06-24_timed-code-567.md) | `@Files 2026-06-24_timed-code-567.md` + TMAY IC paragraph |
| 2026-06-25 | Anchor B/C spoken + Ownership LP | [`2026-06-25_anchor-bc-lp-debrief.md`](debrief/2026-06-25_anchor-bc-lp-debrief.md) | `@Files 2026-06-25_anchor-bc-lp-debrief.md` + `/timed-code` |
| 2026-06-25 | timed-code Islands + Learn & Curious LP | [`2026-06-25_timed-code-and-learn-curious-lp.md`](debrief/2026-06-25_timed-code-and-learn-curious-lp.md) | `@Files 2026-06-25_timed-code-and-learn-curious-lp.md` + Thu 26 coding sprint |
| 2026-06-25 | Qwen (HF) + PEFT/LoRA technical | [`2026-06-25_qwen-peft-technical.md`](debrief/2026-06-25_qwen-peft-technical.md) | `@Files 2026-06-25_qwen-peft-technical.md` + Karan ablation follow-ups |
| 2026-06-26 | Coding sprint #1 + JD technical mini-mock | [`2026-06-26_coding-and-jd-technical.md`](debrief/2026-06-26_coding-and-jd-technical.md) | `@Files 2026-06-26_coding-and-jd-technical.md` — resume JD mock at Q3 |
| 2026-06-26 | Mock LP — Learn & Be Curious (diffusion) | [`2026-06-26_mock-lp-learn-curious.md`](debrief/2026-06-26_mock-lp-learn-curious.md) | `@Files 2026-06-26_mock-lp-learn-curious.md` + story — drill full version, lock distillation numbers |
| 2026-06-26 | JD drill — LLM system choices (RAG/FT/CPT/routing) | [`2026-06-26_llm-system-choices-drill.md`](debrief/2026-06-26_llm-system-choices-drill.md) | `@Files 2026-06-26_llm-system-choices-drill.md` — resume JD track at agent-failure Q3 |
| 2026-06-27 | Karan full mock + PS1 questions | [`2026-06-27_karan-full-mock.md`](debrief/2026-06-27_karan-full-mock.md) | `@Files debrief/2026-06-27_karan-full-mock.md` + `ps1-questions-for-karan.md` — Sun 28 coding + JD refresh |
| 2026-06-27 | Finance eval & monitoring (teach-and-quiz) | [`2026-06-27_eval-monitoring-lesson.md`](debrief/2026-06-27_eval-monitoring-lesson.md) | `@Files debrief/2026-06-27_eval-monitoring-lesson.md` — fixes JD probe gap; rehearse shadow-vs-kill + corrections loop |

Add a row after each `/debrief`. Amazon FinTech session notes → [`debrief/`](debrief/); general profile/project refs → [`.cursor/skills/debrief/`](../.cursor/skills/debrief/).

## Mock log index

| Date | Type | File | Top weakness fixed? |
|------|------|------|---------------------|
| 2026-06-21 | ml-deep-dive | [`2026-06-21_ml-deep-dive.md`](mocks/2026-06-21_ml-deep-dive.md) | IC voice + metrics on Topics 1–2 (retake pending) |
| 2026-06-24 | vlm-spoken-drill | [`2026-06-24_vlm-spoken-drill.md`](mocks/2026-06-24_vlm-spoken-drill.md) | Precise metrics 0.618/0.402→0.905/0.452; TR gate numbers for Q7 |
| 2026-06-24 | timed-code | [`2026-06-24_timed-code.md`](mocks/2026-06-24_timed-code.md) | `while`+`le` for overlap; state O(n²) worst case if probed |
| 2026-06-25 | vlm-spoken-drill | [`2026-06-25_vlm-spoken-drill.md`](mocks/2026-06-25_vlm-spoken-drill.md) | Eval latencies; 0.382→0.405 verified |
| 2026-06-25 | mock-lp | [`2026-06-25_mock-lp-ownership.md`](mocks/2026-06-25_mock-lp-ownership.md) | Ownership ~78%; exact TR pp numbers |
| 2026-06-25 | mock-lp | [`2026-06-25_mock-lp-learn-curious.md`](mocks/2026-06-25_mock-lp-learn-curious.md) | Learn & Curious drafted (diffusion); unrehearsed, verify 7 papers |
| 2026-06-26 | ml-deep-dive | [`2026-06-26_jd-technical-mock.md`](mocks/2026-06-26_jd-technical-mock.md) | JD technical; agents ~80%, A/B ~60→85%; Q3 unanswered |
| 2026-06-26 | mock-lp | [`2026-06-26_mock-lp-learn-curious.md`](mocks/2026-06-26_mock-lp-learn-curious.md) | Learn & Curious (diffusion) ~85–90%; added single-step distillation; lock numbers |
| 2026-06-26 | ml-deep-dive | [`2026-06-26_jd-llm-system-choices.md`](mocks/2026-06-26_jd-llm-system-choices.md) | RAG/FT/CPT/routing ~70→85%; fixed RAG-vs-CPT inversion; eval-first framing |
| 2026-06-27 | full-mock | [`2026-06-27_full-mock.md`](mocks/2026-06-27_full-mock.md) | VLM ~85%; JD probe ~70% (precision guardrail, deterministic schema); TR-kill LP; LC19 pass ~18 min |

Add a row after each mock drill. Store files in [`mocks/`](mocks/).
