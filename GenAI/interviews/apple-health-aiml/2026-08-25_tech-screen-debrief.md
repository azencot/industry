# Debrief — 2026-08-25 — Apple Health AIML tech screen (Feng Zhu)

**Type:** Tech screen — 45 min spoken LLM training + multimodality fundamentals (no coding)  
**When:** Tue 2026-08-25, 1:35–2:20 PM PDT (Webex)  
**Interviewer:** **Feng Zhu** — Applied RS, Health AI (he said he currently works on **multimodal for sensors**)  
**Role:** ML Research Scientist — Health AIML (Shirley Ren HM; Tyler recruiter)  
**Prior:** [`2026-08-21_tech-screen-prep.md`](2026-08-21_tech-screen-prep.md) · HM: [`2026-08-21_hm-screen-debrief.md`](2026-08-21_hm-screen-debrief.md)  
**Memory:** captured same afternoon; **first ML question forgotten** — add if it comes back.

**Do not email Shirley.** Tyler owns next. **No third email to Guillermo.** Do not name-drop RelCon / mood paper / Workout Buddy on later loops either.

---

## Flow (as reported)

1. Feng intro: multimodal **for sensors**.
2. Omri intro: also multimodal for **time-series reasoning** (not the locked IC + kill sentence).
3. First ML question — **not remembered**.
4. **Self-attention** — Q/K/V, complexity, equations, why it exists. Follow-up: greedy-decode cost → **KV cache**.
5. Open: **how to add a new modality to an LLM** — ~2–3 min **project talk** + concat vs xattn + tradeoffs + staged training. Follow-ups:
   - What is trained: Stage A **enc + proj**; Stage B **LLM + enc**.
   - How do you know **captioning** worked: CE, manual generation, **ROUGE**.
   - **Multivariate:** concatenate streams with **separator tokens**.
   - **Which encoder (substantial):** (1) UCR bakeoff, various encoders vs **DINO → DINO won**; (2) Qwen: **PatchTST vs chart vs chart+DE → chart+DE won**. Also: a **native / specialist encoder** is more appropriate if the LM **never saw** that kind of data.
6. Other questions possible — not remembered.
7. Omri’s Qs:
   - Challenges on their project: (1) **find a multimodal arch**, (2) **no data**, (3) **encoder**.
   - Research vs prod: **80/20 research** now; later could be **50/50**; they are in **early stages**.

Felt “very basic” to Omri.

---

## What he was testing

Tyler’s brief was fundamentals, not a second HM encodings tour. KV-cache after attention is “do you know inference vs train FLOPs.” Adding a modality is Q6/Q7 with freeze/eval follow-ups. Multivariate + caption eval are one layer down. His three challenges are the **team problem**, not trivia.

---

## What landed

- Attention + KV cache: right object. Greedy without cache is \(T^2\) per step; cache is prefill once, then cheap decode.
- Fusion families: concat vs xattn + staged A/B — the Q6/Q7 spine.
- **Encoder bakeoff (added same day):** UCR → DINO; Qwen → chart+DE over PatchTST / chart-only. Judgment: specialist encoder if the LM has no prior on that stream. That *is* his “encoder” challenge, with numbers, not a religion. Keep: dual won because **one view loses information** — not “images keep everything.”
- His research/prod answer is usable later: early, research-heavy, not “never product.” Do **not** cite Guillermo’s ~1-year line on loop; the two can both be true.
- Asking challenges + ratio was the right pair.

---

## What broke / stayed shallow

| Said / happened | Why it is thin | Do on on-site |
|-----------------|----------------|---------------|
| Intro = “I also do multimodal TS reasoning” | Mirrors him; no IC verb, no kill | One line: I train/gate; 0.62→0.90; I killed a mix |
| Add-modality → **2–3 min project** | Shirley already heard the stack. Design Q wants standard recipe **then** evidence | Encoder → projector (spaces) → concat or xattn → completion-only; *then* dual views / gates |
| A = enc+proj, B = llm+enc | **LM frozen in A** not stated. B “enc” is optional; LoRA on LM is the default | A: projector (maybe encoder), **LM frozen**. B: LoRA LM; encoder freeze is a choice |
| Captioning eval = CE + ROUGE + eyeball | CE falling ≠ captions work. ROUGE is n-gram overlap, weak for TS captions | Stage A: look at generations (slope/period, not fluency). Gate on **task** after B vs frozen baseline. Don’t promote on caption CE |
| Multivariate = cat + separators | Layout for **aligned** channels. Watch streams are async / **subset** | Encode what is present; mix IMU-only / HR+sleep / full; don’t drop incomplete rows; separators mark presence, not a loss wall |
| **No data** (his #2) not remembered as a land | Encoder *was* discussed; missingness / keep-subset-rows still the leftover | “No labels and naturalistic missing → keep incomplete rows, mix subsets, one gate on *your* IMU/PPG — not complete-case UCR” |

Encoder thread is **not** the miss. Q12 (missingness / no data) still is. Concat+separators is not that sentence.

---

## On “it felt basic”

The **format** was basic on purpose (fundamentals screen). That is not a fail by itself.

The **risk** is thinner than the first write-up: he did get an **encoder bakeoff** (DINO vs others; PatchTST vs chart vs dual) plus “native encoder if the LM never saw that data.” Remaining hole is **no data / missingness**, not “which encoder.” Caption CE/ROUGE and “LM frozen in A” are still soft.

KV cache + staged freeze is enough to **clear a fundamentals gate** if the answers were clean. Outcome is Tyler’s. Don’t self-reject; don’t assume on-site.

---

## Feng facts (keep; do not name-drop papers)

- His current work (his words): **multimodal for sensors**.
- Team pain (his words): **arch**, **no data**, **encoder**.
- Mix: **80/20 research** now → maybe **50/50**; **early**.

If on-site “research vs product”: early research to pick the representation; has to become something that lands — his 50/50 later, not an open-ended FM lab. Still do not cite Guillermo.

---

## Next

- Wait for **Tyler**. Do not email Feng or Shirley.
- If a first question comes back, append it here.
- If **on-site**: slot (2) multimodal + TS encoding = his three challenges. Drill Q12 + caption eval ≠ CE/ROUGE + LM frozen in A. Slot (1) training: run + kill, not the 2–3 min stack tour.
- Bosch Thu 8/27 is a **separate** track. Do not mix Watch scripts into Sunnyvale.

## Next session (if advancing)

> Read this debrief. On-site multimodal slot = Feng’s three: arch, no data, encoder. Speak Q12 (subset rows, mix, no charts on PPG). Caption eval = generations + **task** gate, not ROUGE. Do not reopen RelCon. Do not email Shirley.
