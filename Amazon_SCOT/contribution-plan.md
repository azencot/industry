# Contribution plan — Omri → SCOT Forecasting / Labs

**Purpose:** Monday pitch to Boris. Convince him you are the right IC to join / deepen into SCOT — with a concrete 90-day contribution shape, not a generic interest statement.

**Tone:** peer who already ships research with the team. Say “I”, metrics, and kill criteria. Avoid PI / mentoring / grant framing.

**Spine:** [`mengfei-notes.md`](mengfei-notes.md) (19 Feb dinner) — generative as infrastructure; coherence already strong; cold-start / rare regimes / cost-latency next.

---

## Positioning (15s)

> I’m an applied scientist for messy sequential data — forecasting, generative models under scarcity, and systematic eval. We’ve already collaborated on a NeurIPS paper and an accepted workshop, and I’ve been working with you and Mayank on generative forecasting. I want to put that stack on SCOT’s problems at catalog scale: synthetic/sim pretrain, foundation forecasters, and generative infrastructure that survives production cost and measurement.

---

## Mengfei bridge (60–90s — say before theses)

> In February I sat down with Mengfei. What stuck was that generative modeling at SCOT looks less like a drop-in replacement for quantile forecasting and more like **scalable infrastructure** — pretrain on synthetic to cut inference cost and latency, handle cold-start and rare regimes, without giving up the coherence / decision-alignment work (CLOVER and friends) that’s already strong. Mayank had also flagged generative TS and synthetic data as rising priorities. That’s the lane I’ve been building toward with ImagenTime / ImagenFew and Freq-Synth — joint temporal distributions as a data engine, not only as a point forecaster — and it’s why the collab with you already feels like the right problem class.

---

## Why SCOT (not another lab)

| SCOT need (Mengfei + public) | Your proof |
|------------------------------|------------|
| Synthetic / sim as pretrain infrastructure (ZSF-by-simulation); cost + latency + leakage | ImagenTime / ImagenFew / Freq-Synth; ongoing generative forecasting with Boris + Mayank |
| Cold-start SKUs + rare-regime robustness | Data-scarce + irregular-TS lines; rare-regime amplification framing from Feb dinner |
| Coherent hierarchical structure (by construction, not only post-hoc) | Can speak CLOVER/PHF vocabulary; pitch generative hierarchical pretrain |
| Quantiles when single-period; trajectories when path/coupled costs | Explicit decision framing prepared for Mengfei — reuse with Boris |
| Publish *and* ship | NeurIPS joint paper + accepted workshop |

Canonical arc: [`.cursor/skills/debrief/omri_azencot_experience.md`](../.cursor/skills/debrief/omri_azencot_experience.md).

---

## Four contribution theses (pick 2 to speak; keep 4 as backup)

### 1. Synthetic / sim as foundation-forecasting infrastructure (primary)

**Bet:** ZSF-by-simulation / synthetic pretrain is the SCOT-scale play — cost, latency, leakage, cold-start. Needs people who have *built* generative TS systems and know when synthetic helps vs lies.

**What I would do in 90 days:**

- Own a narrow transfer study: which synthetic regimes help held-out demand families vs inflate offline metrics
- Cold-start + rare-regime slices explicit in the eval (Mengfei friction list)
- Guardrail note: distribution mismatch / bias amplification / calibration drift — how we’d detect them
- Internal note + optional workshop / follow-on paper track

**Ask Boris:** bottleneck today — generators, scaling, transfer to real demand, or production eval mismatch?

### 2. Hierarchically coherent synthetic data (by construction)

**Bet:** CLOVER showed joint bottom-level → aggregate can buy coherence; generative pretrain on *structurally coherent* hierarchies could internalize that before fine-tune — less reliance on post-hoc reconciliation.

**What I would do in 90 days:**

- Prototype or design: generate bottom-level jointly, aggregate up, pretrain, fine-tune on real category/region
- Compare vs independent-per-series synthetic + reconciliation baseline on a scoped hierarchy
- Stay honest about additive vs nonlinear cross-series limits (question you raised with Mengfei)

**Ask:** will reconciliation stay necessary long-term, or can structure live inside the generative model?

### 3. Trajectories where path costs beat marginal quantiles

**Bet:** Quantiles are right for single-period newsvendor; generative paths matter for lead times, carryover, multi-echelon coupling. Don’t oversell generation where P90 suffices.

**What I would do in 90 days:**

- Pick one decision setting where joint temporal dependence clearly changes the optimal policy vs independent quantiles
- Show a small simulation study: path samples → inventory evolution vs quantile-only rule
- Document when *not* to pay for generative inference (head SKUs, single-period, latency-bound serving)

**Ask:** do you simulate demand paths for policy eval today, or mostly quantile decision rules?

### 4. Synthetic stress-test as ship gate + collab surface

**Bet:** Synthetic generators as sandbox for forecast/policy changes before rollout — same kill-discipline muscle as research eval gates. Workshop + NeurIPS paper prove collaboration already works.

**What I would do in 90 days:**

- Define 2–3 shock scenarios (promo spike, cold-start burst, post-peak) used as a pre-deploy stress suite
- Finish paper/rebuttal cleanly; make workshop useful to Forecasting Labs
- One-pager charter with named Amazon owner + success metric for continued internal work

---

## 90-day sketch (speakable)

| Weeks | Focus | Exit artifact |
|-------|--------|---------------|
| 1–2 | Align with Boris/Mengfei on *one* problem (likely synthetic transfer or cold-start) + data access | 1-pager charter |
| 3–6 | Core experiments / audit harness + mismatch guards | Reproducible results + kill/ship recommendation |
| 7–10 | Harden cold-start / rare-regime / PPE-style slices; socialize | Internal note or design review |
| 11–13 | Write-up + next-quarter proposal; workshop logistics parallel | Decision: continue / expand / hand off |

---

## Spoken pitch outline (~8–10 min)

1. **Positioning** (15s) — sequential / generative forecasting IC; already with Boris + Mayank
2. **Mengfei bridge** (60–90s) — generative as infrastructure; coherence already strong
3. **Thesis 1** (2–3 min) — synthetic/sim foundation infrastructure; 90-day moves + risks
4. **Thesis 2** (2–3 min) — coherent hierarchical synthetic **or** trajectories-vs-quantiles (match his energy)
5. **Ask** (60s) — where to point me first next quarter + openings / intros

---

## Anti-patterns (do not do)

- Lead with PI lab size, grants, or student mentoring
- Over-sell VLMs / generative as default replacement for production quantile systems
- Vague “I’d love to help with whatever”
- Ignore cost/latency pushback — meet it head-on (Mar follow-up line)
- Treat Monday as a stealth interview loop — no LP labels unless he goes there

---

## TODO before Monday

- [x] Structure Mengfei notes; rewrite Mengfei bridge
- [ ] Fill paper/workshop titles in [`collaboration.md`](collaboration.md)
- [ ] Rehearse pitch once aloud; cut to ≤10 min
- [ ] Primary thesis = #1 synthetic/sim infrastructure (Boris ZSF line)
