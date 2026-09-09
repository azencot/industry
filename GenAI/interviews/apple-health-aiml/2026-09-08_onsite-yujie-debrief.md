# Debrief — 2026-09-08 — Apple Health AIML on-site (Yujie Li)

**Type:** Virtual on-site slot 2 of 5 — scheduled as **multimodal architecture + time-series encoding**; ran as **system thinking** (method adoption, collaboration without reports, problem decomposition, ambiguity)  
**When:** Tue 2026-09-08, 1:05–1:50 PM PDT (Webex)  
**Interviewer:** **Yujie Li** — Senior MLE, Health AI, Seattle  
**Role:** ML Research Scientist — Health AIML (Shirley Ren HM; Tyler recruiter)  
**Prior:** [`2026-08-27_onsite-yujie.md`](2026-08-27_onsite-yujie.md) · [`2026-09-05_yujie-advanced.md`](2026-09-05_yujie-advanced.md) · stories: [`2026-08-30_behavioral-stories.md`](2026-08-30_behavioral-stories.md)  
**Same day:** Jonathan 11:05 ([debrief](2026-09-08_onsite-jonathan-debrief.md)) → **this slot** → Chung-Cheng 2:05 → Haraldur 3:05 → Vincent 4:05. Hub: [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md)

Captured same afternoon. Dependent-steps answer beyond “deliverables and gates” **not remembered**. No candidate questions — she used the full 45 min.

---

## Flow (as reported)

1. **System thinking** as the frame (not tokens / fusion / clocks).
2. **An evaluation or method you developed that others used?** → **ImagenTime** and the **1D-as-images** bet. **Most of the hour.**
3. **How do you deal with collaborations?** → Bosch (BCAI Haifa), **not the full Card 5** (no full irregular/noisy diagnosis-change plot).
4. **People who do not report to you?** → Map uncertainties; discuss with **their team manager** how to mitigate; **concrete examples**.
5. **How do you decompose a problem for students?** → Multimodal project: **motivation (gap) → bet (1D as images) → short PoC → data / modeling / training / evaluation**; elaborated on each part.
6. **What if steps depend on one another?** → Predefine **deliverables and gates** per step. More was said; not recovered.
7. **Example of an ambiguous project?** → **Koopman distillation**: goal was **sample in less [steps]** and little else. Learned how sampling actually works; during that, saw that **diffusion can be represented differently**, and the **alternative representation is efficient for sampling**.
8. **No time left for questions.**

No wearable architecture case. No patch / STFT / resampler / shuffle-B. No WBM name-drop reported.

---

## What she was testing

Tyler’s map was encoding + fusion. She ran **research-process and people**: does a method travel, can you work sideways, can you slice a large problem, can you operate when the charter is thin.

This is closer to Shirley’s HM bar (**break a large problem into concrete slices**) and to Vincent’s leadership hour than to the four Yujie modules.

| Probe | What it tests |
|-------|----------------|
| Method / eval others used | Adoption, not a paper recap. Did the representation bet become something other people could pick up? |
| Long ImagenTime thread | Can you stay in one scientific object and reason about it as a *system* (bet → evidence → reuse), not a CV bullet |
| Collaborations | Cross-org, not student-as-report. Bosch is the right object |
| People who don’t report to you | Influence without authority — **their manager as the path**, uncertainty as the artifact |
| Decompose for students | Mentorship as **problem architecture**: gap → bet → PoC → four workstreams |
| Dependent steps | Sequencing / gates, not a Gantt slogan |
| Ambiguous project | Dive Deep: learn the bottleneck (sampling) until a representation insight appears — not “I waited for spec” |

---

## What landed

- She **stayed on ImagenTime for most of the hour** — engagement on the representation bet, not a 90-second card dump.
- Decomposition spine is senior: **gap → bet → cheap PoC → data / modeling / training / eval**. That *is* how ImagenTime and the VLM were actually run.
- Dependent work → **predefined deliverables and gates** matches the two-stage + kill discipline Shirley already heard.
- Influence-without-reports: **map uncertainties, talk to their manager, mitigate** — concrete, not “I aligned stakeholders.”
- Ambiguous project: **learn sampling first**, then the modeling insight (alternative diffusion representation → cheaper sampling). That is the honest SKD / single-step distillation plot, not a fake requirements doc.

---

## What was thin / leftover

| Said / happened | Why it is thin | If this theme returns (Vincent) |
|-----------------|----------------|----------------------------------|
| ImagenTime ≈ whole hour | Correct object for “method others used.” Architecture modules (clocks, fusion, neglect tests) **untested**. Dual-tower bakeoff (Card 2) unused | Do **not** replay ImagenTime as the leadership story. Vincent: Cards **3 + 4** (post-kill plan + TR kill). If collab: **full Card 5** |
| Bosch, not full story | Missing the Card 5 turn: their sensor reality **changed the diagnosis** (irregular / noisy / partial / misaligned), then LDDBM robustness | If asked again: diagnosis change, then the ML translation — not only “I work with Bosch” |
| “For my students” | She asked it. Still a **PI cue**. Hub hard rule was IC-first / don’t lead with students | If Vincent asks mentorship: Card **A** (unblock, they keep ownership). One sentence of title if needed, then the technical split |
| Dependent steps beyond gates | Forgotten. The missing half is usually: **what is allowed to start before the previous gate**, and **what is frozen** so later work does not thrash | Pocket: Stage A frozen LM; representation screen before full 2D stack (Card B); don’t train the expensive fusion until the encoder bakeoff survives |
| Koopman distillation | Right ambiguity story. “Koopman” as brand is noisy for industry. Mechanism: operator / alt representation of the reverse process → **sample in fewer steps** | If retold: goal = fewer sampling steps; I had to understand the sampler; alt representation made one-step / few-step distillation possible. Skip the brand if they didn’t ask Koopman |
| No questions for her | Lost encoding / complementarity / clocks questions. No new facts about her work | Do not email her. Remaining slots: still pick 1–2 from [`2026-09-05_questions-for-interviewers.md`](2026-09-05_questions-for-interviewers.md) |

Encoder / fusion hour **did not happen**. That is not a fail by itself — she chose process. Do not self-reject for not reciting Module 1. Do not assume the architecture signal was collected elsewhere.

---

## Corrections (do not recant this call)

### 1. Remaining day — do not import this hour

**Chung-Cheng:** diagnosis order (profile → batch vs comm vs mem), not system-thinking recap.  
**Haraldur:** labels / operating points / when simple models win. Not ImagenTime.  
**Vincent:** leadership = discriminating experiment + kill. ImagenTime and Bosch-lite are **spent**. Use **#4 then #3**. Mentorship = **A**, not another student-decomposition lecture.

### 2. Bosch full plot (if collab comes back)

Card 5: benchmarks worked → real Bosch sensors failed → I thought “stronger model” → **they** showed irregular / noisy / partial / misaligned → I translated that into the robustness problem. Collaborators, not reports. No Watch / BU ship claim.

### 3. Ambiguous project — speakable lock (if asked again)

> The charter was only “sample in fewer steps.” I had to learn how the sampler actually worked. While doing that I saw that the reverse process can be represented differently, and that representation is what made efficient sampling possible. I would not have got there from a library recipe.

Do not open with “Koopman.” Do not invent FID / speedup numbers that are still unlocked.

---

## Facts to keep (hers / this slot)

- She ran **system thinking**, not Tyler’s encoding track.
- Adoption question: **method others used** → ImagenTime / 1D-as-images.
- People probe: **non-reports** → their manager + mapped uncertainties.
- Decomposition probe: **students** + interdependent **gates**.
- Ambiguity probe: **distillation / sampling**, thin charter.
- **No time for your questions.**

Do not email Yujie, Shirley, or the remaining interviewers. Tyler owns process.

---

## Next (same day)

Chung-Cheng 2:05 is **infra**. Open [`2026-08-27_onsite-chung-cheng.md`](2026-08-27_onsite-chung-cheng.md) / advanced sheet in your head, not this file. After the day: fold this into [`2026-09-08_onsite-debrief.md`](2026-09-08_onsite-debrief.md) (hub: Tue night wrap).

## Next session (post-onsite)

> Read this debrief. Yujie ≠ encoding hour. She tested adoption (ImagenTime), sideways collab (Bosch, partial), non-reports (their manager), decompose (gap → bet → PoC → four streams + gates), ambiguity (sampling / distillation). Architecture modules untested. Vincent: do not replay ImagenTime; Cards 3+4 / full Card 5 / mentorship A. Do not email interviewers.
