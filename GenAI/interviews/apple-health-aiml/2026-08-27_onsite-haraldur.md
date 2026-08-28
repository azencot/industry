# On-site — Haraldur Hallgrímsson (Wed 3:05 PDT)

**Track:** health / applied ML / wearable TS. **Conf:** very high. Most Apple-Health-specific hour.  
**Who (private):** Senior Applied RS, Health AI, Seattle. RelCon, TS-LLM, periodicity. Public: sensor FMs → Watch hypertension / AirPods calories (modeling **and** infra).  
**Hub:** [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md)

**Cultural signal (do not recap papers):** this group will keep **periodic features + GBDT** when they beat a deep TS model under **missingness shift**. SSL motion FMs exist too (~3.9M encoder, 1B **segments** — not 1B params).

**Do not assume deep learning wins.**

Do **not** name RelCon / periodicity / Workout Buddy / his LinkedIn posts. Do **not** say you shipped a Watch feature.

---

## Open (30s)

> First I’d define the **deployment distribution**, the **target**, available history, **missingness**, and the operating point. I’d put a strong statistical / tree / classical TS baseline on the table before I decide whether representation learning buys anything.

Then bakeoff. Not: “Transformer + multimodal LLM.”

---

## Missingness (one layer down)

You already have: empty stays missing; \(P(M\mid X,Y)\neq P(M)\).

Add **shift**:

\[
P_{\text{train}}(M) \neq P_{\text{deploy}}(M)
\]

Ask: does performance **hold when the missingness process changes** (new firmware, battery, adherence, illness) — not only “can the model impute a channel.”

Informative missingness is a **shortcut risk** as well as a signal.

---

## Personalization

Population prior → **personal baseline** → deviation / longitudinal adapt. Cold start: no history → population; as days accrue, shrink toward the person. His older work: individual cardiovascular signatures **across years** — transfer is the question, not a slogan.

---

## 100× unlabeled vs labeled outcomes

1. SSL on the sensor corpus.  
2. **Probe** (linear / small head) before you unfreeze the world.  
3. Light downstream FT.  
4. Compare to a **task-specific supervised** baseline at the **same label budget**.  
5. Transfer: task / participant / device.  
6. Stress **missingness shift**.

Ask out loud: **does the FM beat simpler representations at realistic labels?** If no, you keep the simple model. That is the periodicity lesson without naming it.

**Augmentations (contrastive):** invariances from **sensing physics + downstream semantics**, not ImageNet crops. Accel: rotation of the watch can be invariance; scrambling time order is not. Bad positives → a FM of noise.

---

## Predicted questions

1. Predict X from six months of wearable data — **start**.  
2. Population vs personalized.  
3. 100× unlabeled — what do you do, and how do you know SSL helped?  
4. How do you choose contrastive augmentations for IMU?  
5. Missingness changes after a Watch OS update.  
6. When would you **not** train a foundation model?  
7. Participant vs time splits.  
8. Calibration / operating point for a screening nudge vs an intrusive alert.  
9. Your benches aren’t Watch data — transfer? (longitudinal, missing days, multi-stream; not UCR plots)  
10. Encoder bakeoff on IMU/PPG (he coauthored native TS-LLM — **2** can leak). Same gate, no matplotlib on PPG.

---

## Your evidence (IC)

- TR mix kill: average up, slice down → **killed**. Same instinct as “GBDT won under shift.”  
- ImagenFew / irregular: Bosch noisy data changed the **generative** model, not a Watch ship.  
- Dual views: one encoding **loses** information — relevant if he pulls representation, not as “I reprint charts.”

**Mock (35 min):** last Wed slot. Shipped-product scientist. You have not shipped. Land missingness **shift**, baselines first, SSL-vs-simple at low labels. Encoder only if he goes there.
