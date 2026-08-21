# Debrief — 2026-08-21 — Apple Health AIML: pre-call notes (glossary + stack)

**Type:** Prep (overnight Qs + morning glossary)  
**Track:** GenAI / Apple Health AIML HM screen  
**When:** Thu night → Fri morning before the call  
**Call:** Fri 2026-08-21, 11:05–11:50 AM PDT · Shirley Ren · fit, no coding  
**Prior:** [`2026-08-20_why-apple-health-drill.md`](2026-08-20_why-apple-health-drill.md) · [`2026-08-20_training-run-drill.md`](2026-08-20_training-run-drill.md)  
**General LLM judgments (tech screen later):** [`../../notes/2026-08-20_llm-training-judgments.md`](../../notes/2026-08-20_llm-training-judgments.md)

---

## Session

Covered: extra hard LLM-training Qs (not the VLM project); IMU vs PPG vs longitudinal; RelCon/REBAR **parameter** size vs the 1B-segment figure; why the JD wants LLM training if RelCon is ~4M.

---

## Conclusions

**Do not mix data scale and model scale.** RelCon’s **1 billion** is segments (87,376 participants). The encoder is a 1D ResNet-34, **~3.9M parameters**, 256-d embedding. REBAR is an ICLR 2024 **contrastive recipe** (retrieval positives), not a billion-param Apple FM.

**Why they still hire LLM training:** RelCon is small **on purpose** (always-on IMU). The LLM seat is the **language layer** (TS encoder → Mistral-7B; speech-FM probes; Apple Intelligence fitness language), not a bigger Watch ResNet. 9B/27B = iterate/ceiling, then freeze / probe / distill. Do **not** say RelCon is “too small.”

**Glossary (if a term comes up, then stop):**

- **IMU** — motion chip: accel + gyro (sometimes mag). RelCon uses the **accel** (3-axis, ~100 Hz in the paper, 2.56 s windows).
- **PPG** — raw optical pulse waveform; **HR** is usually derived from it.
- **Longitudinal** — same users over time (personal baselines, missing days), not a one-off UCR clip.

**Overnight LLM drills:** useful for the **later tech screen**. Do not cram them this morning. IC on the HM call = own the run, gate, kill, stop.

---

## Decisions / artifacts updated

- [x] [`2026-08-20_shirley-group-briefing.md`](2026-08-20_shirley-group-briefing.md) — RelCon ~3.9M; IMU; longitudinal; “too small” anti-pattern
- [x] [`../../notes/2026-08-20_llm-training-judgments.md`](../../notes/2026-08-20_llm-training-judgments.md)
- [ ] `omri_azencot_experience.md` — no
- [ ] `AGENTS.md` — no

---

## Open questions

- None for this HM. Do not prep the 5-interview on-site before the call.

---

## Next session (this morning — 15 min, then stop)

Say locked why-Apple **50s** + training-run **2–3 min** + TR **26.9 → 21.9**. Join Webex **after 10:55 AM PDT**. After the call: write `2026-08-21_hm-screen-debrief.md`.

**Handoff prompt**

```
@GenAI/interviews/apple-health-aiml/2026-08-20_why-apple-health-drill.md
@GenAI/interviews/apple-health-aiml/2026-08-20_training-run-drill.md
@GenAI/interviews/apple-health-aiml/2026-08-20_shirley-group-briefing.md
@GenAI/interviews/apple-health-aiml/2026-08-12_hm-screen-prep.md
HM screen was Fri 2026-08-21 with Shirley Ren. Write 2026-08-21_hm-screen-debrief.md from the call notes; do not invent.
```
