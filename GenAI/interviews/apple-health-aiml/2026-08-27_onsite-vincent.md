# On-site — Vincent Chan (Fri 11:05 PDT)

**Track:** technical leadership / system thinking + multimodal **strategy**. **Conf:** medium-high. Last slot.  
**Who (private):** Eng Manager, Health AIML. Recruits multimodal LLMs / fusion / VLMs / TS. Stats PhD (Wisconsin); menstrual-cycle patent. Thanked on TS-LLM.  
**Hub:** [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md)

He cares whether you can turn an **ambiguous multimodal-health objective into a research program**, not RoPE.

IC verbs. **Not** “I’d facilitate consensus.” **Not** associate professor / my lab. Why-Apple only if pulled: [`2026-08-20_why-apple-health-drill.md`](2026-08-20_why-apple-health-drill.md) — never “impact at scale.”

---

## Six months (structure before the net)

1. **Target** — what should the representation *enable* (not “train a big model”).  
2. **Eval first** — tasks, participant/time splits, missingness slices, robustness, **simple baselines**.  
3. **Data audit** — modalities, availability, timescales, labels, leakage.  
4. **Bakeoff** — native sensor encoder vs **behavioral-token** model vs fusion, **matched** harness.  
5. **Scale the winner** — not a third architecture.  
6. **Kill criteria** — pre-declared (your −3 / −5 pp; or no lift vs cheap baseline at month 3).  
7. **Stress** — missingness **shift**, participant shift, device gen, longitudinal.

Shirley’s bar: **~3-month slices**. Skeleton: 0–1 harness+baseline · 1–3 bakeoff · 3–4 scale · 4–5 robustness · 5–6 distill/product-ready **if** the gate holds.

---

## Two researchers disagree (giant E2E vs modality encoders)

Name the **factual** disagreement. Cheapest discriminating experiment:

same data + **same decoder** + matched compute + predefined slices.

Keep the winner. That **is** leadership.

---

## Four IC stories (<90s each)

| Story | Line |
|-------|------|
| Kill / sunk cost | Synth TR mix; average up; TR **26.9 → 21.9**; killed |
| Evidence redirect | Dual vs one view; delay-only numbers collapsed |
| Disagreement | 27B FT ~0.92 TSExam does **not** own TSRBench vs 8B — wrong north star |
| Hard system | Dual routing, collator, A→B merge, DDP — **I** designed/trained/gated |

---

## Predicted questions

1. Multimodal health FM — you lead research — first six months.  
2. Giant E2E vs frozen modality encoders — you decide.  
3. Six people, six months, limited GPUs — allocate.  
4. When do you **stop** an approach?  
5. Publish vs ship (Guillermo ~1 year product — **do not cite**; Feng 80/20 now).  
6. Eval before the large model — what slices?  
7. Fusion strategy: concat vs xattn vs behavioral tokens.  
8. Why this seat / why Apple Health (locked 50s).  
9. No consumer ship — how do you still have applied judgment? (Bosch irregular → model change)  
10. What would you **not** do in year one? (reprint charts on PPG; skip baselines)

---

## Traps

| Trap | Do instead |
|------|------------|
| Transformer diagram in sentence one | Target → metric → baseline |
| Facilitate / align stakeholders | Discriminating experiment |
| PI lab tour | IC + kill |

**Mock (35 min):** last Friday slot. Broad: 6-month FM. Drill: kill criteria + encoder disagreement. Scenario: month-3 baseline didn’t move.
