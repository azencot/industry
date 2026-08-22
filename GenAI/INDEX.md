# GenAI — generative AI roles track

Prep for **generative AI / LLM** applied scientist roles and **multimodal / time-series foundation-model** research scientist interviews (RAG, agents, eval, TSFMs beyond forecasting). **Not** forecasting-AS loops (LightGBM vs Chronos, demand) — that lives in [`Forecasting/`](../Forecasting/). **Not** Amazon FinTelligence PS1 loop scaffolding — that stays in [`Amazon_FinTech/`](../Amazon_FinTech/) (reuse `/ml-deep-dive` and shared experience profile when useful).

---

## Goal

Company / exploratory call prep and ongoing GenAI interview depth: systems, eval gates, tradeoffs (RAG vs fine-tune vs routing), and production constraints — not paper recaps.

---

## Key files

| File | What |
|------|------|
| [`notes/`](notes/) | Session debriefs, one-pagers, mock answers |
| [`interviews/`](interviews/) | Company / exploratory call prep |
| [`../talks/ts-vlm/`](../talks/ts-vlm/) | Bosch 25-min VLM talk (HTML); later Sep 7 community extension |

Shared profile: [`.cursor/skills/debrief/omri_azencot_experience.md`](../.cursor/skills/debrief/omri_azencot_experience.md).

Related skill (shared with FinTech depth practice): **`/ml-deep-dive`**.

---

## Session log

| Date | Session | Notes |
|------|---------|-------|
| 2026-08-12 | Apple Health AIML recruiter prep | [`interviews/apple-health-aiml/2026-08-12_recruiter-prep.md`](interviews/apple-health-aiml/2026-08-12_recruiter-prep.md) — multimodal + TS fit; soft screen scripts |
| 2026-08-12 | Apple Health AIML recruiter screen (~10 min) | [`interviews/apple-health-aiml/2026-08-12_recruiter-debrief.md`](interviews/apple-health-aiml/2026-08-12_recruiter-debrief.md) — loop mapped; HM **Shirley Ren**; next = HM screen |
| 2026-08-12 | Apple Health AIML HM screen prep | [`interviews/apple-health-aiml/2026-08-12_hm-screen-prep.md`](interviews/apple-health-aiml/2026-08-12_hm-screen-prep.md) — **Fri 2026-08-21 11:05–11:50 AM PDT**; health AI · Apple · LLM training run; day-by-day schedule |
| 2026-08-12 | Apple Health AIML HM 3C training-run detail | [`interviews/apple-health-aiml/2026-08-12_hm-3c-training-run.md`](interviews/apple-health-aiml/2026-08-12_hm-3c-training-run.md) — 9B/27B + 8B champion; **resume at §4** |
| 2026-08-20 | Apple Health AIML — Shirley group briefing | [`interviews/apple-health-aiml/2026-08-20_shirley-group-briefing.md`](interviews/apple-health-aiml/2026-08-20_shirley-group-briefing.md) — RelCon / speech-FM / TS-LLM; sensor glossary; Workout Buddy = LinkedIn shipped claim, not authorship |
| 2026-08-20 | Apple Health AIML — why-Apple-Health drill (5 Q) | [`interviews/apple-health-aiml/2026-08-20_why-apple-health-drill.md`](interviews/apple-health-aiml/2026-08-20_why-apple-health-drill.md) — question same / setting different; kill scale slogans; locked 50s |
| 2026-08-20 | Apple Health AIML — LLM training-run drill (5 Q) | [`interviews/apple-health-aiml/2026-08-20_training-run-drill.md`](interviews/apple-health-aiml/2026-08-20_training-run-drill.md) — run not a project; TR 26.9 → 21.9; never “images keep all information” |
| 2026-08-20 | LLM training judgments (general) | [`notes/2026-08-20_llm-training-judgments.md`](notes/2026-08-20_llm-training-judgments.md) — NLL vs task, packing/token budget, ckpt selection, accum clip, completion-only; **tech screen**, not HM skim |
| 2026-08-21 | SFT starting pitfalls (general) | [`notes/2026-08-21_sft-starting-pitfalls.md`](notes/2026-08-21_sft-starting-pitfalls.md) — data/template/loss, Qwen chatML vs thinking, LoRA modules, eval vs NLL, don’t jump to RL; **tech screen**, not HM skim |
| 2026-08-21 | Apple Health AIML — pre-call notes | [`interviews/apple-health-aiml/2026-08-21_pre-call-notes.md`](interviews/apple-health-aiml/2026-08-21_pre-call-notes.md) — RelCon ~3.9M vs 1B segments; why LLM hire; IMU/PPG/longitudinal |
| 2026-08-21 | Apple Health AIML HM screen (Shirley Ren) | [`interviews/apple-health-aiml/2026-08-21_hm-screen-debrief.md`](interviews/apple-health-aiml/2026-08-21_hm-screen-debrief.md) — scheduled fit, ran technical; encodings + eval + gates + ImagenFew |
| 2026-08-21 | Apple Health AIML — advancing to tech screen | [`interviews/apple-health-aiml/2026-08-21_tech-screen-invite.md`](interviews/apple-health-aiml/2026-08-21_tech-screen-invite.md) — **Tue 8/25 1:35–2:20 PM PDT**, Webex, **Feng Zhu**; spoken LLM training + multimodality; CoderPad = ignore; [prep](interviews/apple-health-aiml/2026-08-21_tech-screen-prep.md) |
| 2026-08-21 | Apple Health AIML — Sapiro / Giryes org graph | [`interviews/apple-health-aiml/2026-08-21_sapiro-giryes-org.md`](interviews/apple-health-aiml/2026-08-21_sapiro-giryes-org.md) — Shirley↔Sapiro collab; Raja = AI Research/speech not this req; Kimmel intro = scientific not lobby |
| 2026-08-22 | Apple Health AIML — Sapiro replied | [`interviews/apple-health-aiml/2026-08-22_kimmel-sapiro-outreach.md`](interviews/apple-health-aiml/2026-08-22_kimmel-sapiro-outreach.md) — former report line; applied ML / ~1-year product; Omri sent one research-vs-product ask; **no third email**; no name-drop Tue |
| 2026-08-21 | Apple Health AIML — group PDFs | [`interviews/apple-health-aiml/papers/README.md`](interviews/apple-health-aiml/papers/README.md) — RelCon, speech-FM, TS-LLM, Feng periodicity; do not name-drop |
| 2026-08-21 | Apple Health AIML tech-screen bootcamp | [`interviews/apple-health-aiml/2026-08-21_tech-screen-prep.md`](interviews/apple-health-aiml/2026-08-21_tech-screen-prep.md) — 3-day: LLM pipeline + attention, multimodal fusion, SFT/debug + 12 Q; study code [`interviews/apple-health-aiml/code/`](interviews/apple-health-aiml/code/) |
| 2026-08-21 | LLM pipeline + attn lock-in (Day 1A) | [`notes/2026-08-21_llm-pipeline-attn-lockin.md`](notes/2026-08-21_llm-pipeline-attn-lockin.md) — tokenizer vs `E`; RoPE \(R_{j-i}\); \(Y=AV\); AdamW ≠ sample weights; attn impl not started |
| 2026-08-22 | LLM training mechanics lock-in (Day 1B) | [`notes/2026-08-22_llm-training-mechanics-lockin.md`](notes/2026-08-22_llm-training-mechanics-lockin.md) — \(\eta\) vs \(\lambda\); Adam \(m,v\); fp16 loss scale; pack `-100`; 7B try-order; \(\beta\) = weight on the **past** |
| 2026-08-22 | Multimodal fusion lock-in (Day 2, partial) | [`notes/2026-08-22_multimodal-fusion-lockin.md`](notes/2026-08-22_multimodal-fusion-lockin.md) — projector = spaces; concat vs xattn vs unified; `-100` ≠ last-vis→text; concat does not block text shortcut; CLIP / Q12 not started |
| 2026-08-12 | Bosch RTC-NA TSFM interview prep | [`interviews/bosch-rtc-tsfm/2026-08-12_interview-prep.md`](interviews/bosch-rtc-tsfm/2026-08-12_interview-prep.md) — multimodal TSFM (beyond forecasting); Sunnyvale hybrid |
| 2026-08-12 | Bosch HM invite (Shabnam) | [`interviews/bosch-rtc-tsfm/2026-08-12_hm-invite.md`](interviews/bosch-rtc-tsfm/2026-08-12_hm-invite.md) — **Multimodal FM** req; **Thu 2026-08-13 3:15–3:45 PM PDT** Teams fit |
| 2026-08-13 | Bosch HM screen (Shabnam + Joy) | [`interviews/bosch-rtc-tsfm/2026-08-13_hm-screen-debrief.md`](interviews/bosch-rtc-tsfm/2026-08-13_hm-screen-debrief.md) — fit; reloc required; they confer; if yes → **coding + deep dive** |
| 2026-08-19 | Bosch next-round invite (Joy) | [`interviews/bosch-rtc-tsfm/2026-08-19_next-round-invite.md`](interviews/bosch-rtc-tsfm/2026-08-19_next-round-invite.md) — **one 1h technical**; availability sent |
| 2026-08-20 | Bosch technical agenda (Joy) | [`interviews/bosch-rtc-tsfm/2026-08-20_technical-agenda.md`](interviews/bosch-rtc-tsfm/2026-08-20_technical-agenda.md) — **25 min talk + 20 min previous-work Q&A + 15 min coding discuss**; Teams |
| 2026-08-21 | Bosch technical **rescheduled** | [`interviews/bosch-rtc-tsfm/2026-08-20_technical-agenda.md`](interviews/bosch-rtc-tsfm/2026-08-20_technical-agenda.md) — **Thu 2026-08-27, 10:00–11:00 AM PT**; no overlap with Apple Tue 8/25 |

---

## Boundaries

| Track | Use for |
|-------|---------|
| **This folder (`GenAI/`)** | GenAI / LLM / multimodal TSFM research-scientist interviews and prep |
| [`Forecasting/`](../Forecasting/) | Forecasting AS roles (LightGBM, Chronos, demand, etc.) |
| [`Amazon_FinTech/`](../Amazon_FinTech/) | FinTelligence formal loop (LP, timed code, FinTech-framed LLM) |
| [`Amazon_SCOT/`](../Amazon_SCOT/) | SCOT relationship / contribution |
