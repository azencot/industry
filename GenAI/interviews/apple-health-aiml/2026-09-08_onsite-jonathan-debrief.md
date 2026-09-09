# Debrief — 2026-09-08 — Apple Health AIML on-site (Jonathan)

**Type:** Virtual on-site slot 1 of 5 — Tyler #3 **research depth & scientific rigor**. Ran that way.  
**When:** Tue 2026-09-08, 11:05–11:50 AM PDT (Webex)  
**Interviewer:** **Jonathan** (working ID: Bourim, ARE / SWE, Health AI, Seattle). Do not confirm the last name on loop.  
**Role:** ML Research Scientist — Health AIML (Shirley Ren HM; Tyler recruiter)  
**Prior:** [`2026-08-27_onsite-jonathan.md`](2026-08-27_onsite-jonathan.md) · rigor mock [`2026-09-01_onsite-jonathan-research-rigor.md`](2026-09-01_onsite-jonathan-research-rigor.md) · Sat 3Q [`2026-09-04_onsite-second-cycle-mocks.md`](2026-09-04_onsite-second-cycle-mocks.md)  
**Same day:** **this slot** → Yujie 1:05 ([debrief](2026-09-08_onsite-yujie-debrief.md)) → Chung-Cheng 2:05 → Haraldur 3:05 → Vincent 4:05. Hub: [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md)

Captured same afternoon. His answers to your two questions **not recovered**. Dual-tower / DoF / TR-mix **not asked**. No pad.

---

## Flow (as reported)

1. Brief mutual introductions.
2. **ImagenFew** as the object for the rest of the hour. Asked to **describe the paper**.
3. Motivation you gave: **data scarcity**; want a generative model when little data is available.
4. He wanted the **approach**, specifically **1D → 2D**.
5. **What is DE**, and whether it needs **smoothness** or **stationarity**.
6. **Objective / loss.** You sketched **DDPM** and **EDM**, and said you used the **EDM formulation because it was not a claim of the paper**.
7. **Results.** He wanted the **eval setting**, whether it is **fair**, what the results **mean**, and a description of the **tests**. You walked that; **he sounded happy**.
8. **Adding constraints** to the system. You described **AdaGAN**, **forgot the name live**, recalled later and named it.
9. Your questions (two): (1) what is most important to work on for **healthcare**; (2) how work **splits between eng and research**.

No dual-tower. No complementarity / shuffle. No researcher-DoF / hill-climbing. No coding.

---

## What he was testing

Tyler’s map was scientific rigor. He ran it as a **paper defense on one object**, not a CV tour and not a dual-tower bakeoff.

Same spine as the Jonathan sheet: claim → mechanism → loss (what is actually optimized) → whether the comparison is fair → what you would add (constraints). He interrupted at the 1D→2D and DE assumptions, then at eval fairness — those are the two places a skeptical reader stops.

| Probe | What it tests |
|-------|----------------|
| Describe the paper | Can you state problem vs method vs result without collapsing them |
| 1D → 2D | Mechanism, not “vision models are strong” |
| DE: smoothness / stationarity | Do you know the **assumptions of the representation**, not only the recipe |
| Loss: DDPM vs EDM | Can you separate **training objective** from **scientific claim** |
| Eval setting / fair? | Module 3: baselines, scarcity unit, what the metric allows |
| Constraints / AdaGAN | Can the generator take a **condition**, or is it only unconditional scarcity |
| Your two questions | You used the ARE seat: product-priority + RS/RE split (Qs 3-ish and 5) |

---

## What landed

- **Object choice was right.** He wanted ImagenFew. Dual-tower was prepared and unused — that is fine; do not force it later.
- **EDM not a paper claim** is the strongest rigor sentence of the hour. You distinguished implementation choice from contribution.
- **Eval fairness** is what he cared about after the method. You had the tests; he sounded convinced. That is the pass condition from the sheet (“identify weaknesses / defend the comparison”).
- You **asked two questions** (Yujie left none). Height was right for an ARE: healthcare priority + eng/research split.
- Name-blank on AdaGAN, then **self-corrected in the same meeting** — cheaper than leaving it unnamed.

---

## What was thin / leftover

| Said / happened | Why it is thin | If this theme returns |
|-----------------|----------------|------------------------|
| Opened on scarcity / gen-when-little-data | Correct problem. The **hypothesis** is representation + reusable visual prior, not “we trained a diffusion model” | If Vincent asks why images: geometry + pretrained prior; rendering can destroy information |
| 1D→2D as the approach ask | He did not stop at “we render an image.” Need invertibility / DE vs STFT vs chart vs GAF if someone else pulls it | Do **not** replay the paper to Chung-Cheng / Haraldur |
| DE smoothness / stationarity | Probe not fully logged. Pocket below | Haraldur / anyone who treats DE as a dynamical-systems object |
| AdaGAN name late | Mechanism first is fine; **name on first mention** next time | Constraints → concat + **AdaGN** (scale/shift) vs AdaGAN (mode-covering GAN). Confirm which you meant tonight |
| His answers to your Qs | Not recovered | Log tonight if they come back; do not email him |
| Dual-tower unused | Complementary-view / +0.08 / shuffle **untested** by Jonathan | Vincent leadership ≠ ImagenFew. Cards **3+4**. Yujie already spent ImagenTime |

ImagenFew **is spent** for the rest of Tuesday. Do not reopen it unless they ask.

---

## Corrections (do not recant this call)

### 1. Remaining day — do not import this hour

**Chung-Cheng:** profile → batch vs comm vs mem. Not 1D→2D.  
**Haraldur:** labels / operating points / when simple models win. Not generative scarcity.  
**Vincent:** discriminating experiment + kill. ImagenFew and ImagenTime are both **spent** (this slot + Yujie). Cards **4 then 3**. Mentorship **A**.

### 2. DE pocket (if smoothness / stationarity comes back)

> Delay embedding is a lagged-coordinate map. It does not assume ARIMA-style stationarity. The classical Takens story wants a smooth enough deterministic flow so the reconstruction is a diffeomorphism onto the attractor. I can still *draw* a DE of a nonstationary or switching series — I should not then claim I recovered a single attractor. Smoothness helps the 2D image be a useful object; it is not a formal ticket to apply the map.

Do not invent “DE requires stationarity.” Do not invent “DE requires C∞.”

### 3. Constraints — name lock

You described the idea, blanked the name, then said AdaGAN.

If you meant **conditional diffusion** (likely, given EDM): the usual construction is concat the condition, then **AdaGN** (adaptive group norm) to scale and translate. That is what you have been using with students. **AdaGAN** is a different paper (sequential GAN generators for missing modes). Tonight, write which one you actually described. Next mention: **name first, then the mechanism.**

If constraints come back (Vincent / Haraldur): condition vs guidance vs hard constraint at sample time — pick one, say what you ran.

### 4. EDM sentence (keep)

> I trained with the EDM formulation. That was an implementation choice, not a claim of the paper.

That is the model for any “why this loss / this sampler / this encoder.”

---

## Facts to keep (his / this slot)

- Confirmed **scientific rigor**; ImagenFew was the vehicle.
- Drill order: paper → 1D→2D → DE assumptions → loss (DDPM/EDM, EDM not claimed) → **eval fairness / tests** (happy) → constraints (AdaGAN, name late).
- You asked: **healthcare priority** + **eng vs research split**. His answers **not in this file**.
- Dual-tower, DoF, TR mix, pad: **not this hour**.
- Do not email Jonathan, Shirley, or the remaining interviewers. Tyler owns process.

---

## Next (same day)

Chung-Cheng is **infra**. Open the diagnosis order in your head, not this file. After the day: fold this into [`2026-09-08_onsite-debrief.md`](2026-09-08_onsite-debrief.md) (hub: Tue night wrap) and recover his two answers if you remember them.

## Next session (post-onsite)

> Read this debrief. Jonathan = ImagenFew rigor: 1D→2D, DE smoothness/stationarity, EDM not a claim, eval fairness (he was happy), constraints (AdaGAN named late). Dual-tower unused. You asked healthcare-priority + RS/RE split; answers not logged. Remaining slots: do not replay ImagenFew. Vincent: Cards 3+4, not this paper. Confirm AdaGAN vs AdaGN tonight. Do not email interviewers.
