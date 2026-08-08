# Prep — Raunak Singh (VP Science), Keystone.AI

**When:** Monday **2026-08-10** (two days after this note)  
**Format:** He invited you to hear what Keystone is building — **listening-first**, not a PS1. Still prepare like a soft screen: clear IC story, sharp questions, local Seattle / Bellevue fit.

---

## 1. What this meeting is

| Is | Isn’t |
|----|--------|
| Relationship restart + product briefing | Formal coding / LP loop |
| Soft mutual fit (science depth × **already in Seattle**) | Guaranteed next round |
| Chance to show production judgment on *their* problem (mfg intermittent demand → decisions) | Academic seminar or Chronos paper recap |

**Your goal:** leave him thinking *“this person already thinks about the hard parts of enterprise forecasting, and is already local.”*  
**His likely goal:** sell the science story, gauge interest/fit, maybe open a hiring path.

---

## 2. Company brief (5-minute read)

**Problem they sell:** manufacturers don’t trust demand forecasts; ERP averages destroy the signals that matter; planning systems need **probabilistic, decision-aligned** forecasts (service level, inventory, capacity), not vanity MAPE.

**Stack (their language):**

1. **RAIN** — turn ERP / orders / shipments / invoices into fine-grained **event streams** (timing + sequence preserved), enriched with market / weather / etc., into science-ready representations.
2. **Foundation Forecasting™** — proprietary models for **intermittent / irregular** SKU×customer demand across short and long horizons; **quantiles / uncertainty** tied to planning.
3. **DEEP** — decision layer that plugs into existing ERP / IBP (SAP, Oracle, Kinaxis, o9, …) rather than rip-and-replace.

**Who buys:** CPG, manufacturing, pharma — lumpy B2B demand, stock-outs, short history, hierarchical plans.

**People signal:** Raunak = Amazon forecasting leadership (SKU-level DL deployment era + topline / CapEx forecasting). Science org is building a **productized foundation forecasting** story for enterprise, not a pure research lab.

**Kari Torkkola:** Confirmed on **LinkedIn** as **Distinguished Scientist at Keystone.AI** (Chronos / Amazon TS FM lineage). Signal: they’re investing hard in foundation / pretrained forecasting for the product, not just classical boosters. Still: don’t lead with name-dropping; if the topic comes up naturally, you can acknowledge the hire as interest in how they’re shaping the FM side. Default soft question: *“How are you thinking about foundation / pretrained models vs client-specific structure?”*

---

## 3. Raunak — how to talk to him

| | |
|---|---|
| **Role** | VP Science, Keystone (NYC); Bellevue office exists |
| **Background** | 12+ years Amazon — Director of Science (SC + CX); led SKU-level unconstrained demand forecasting (DL system replacing legacy); later topline forecasting for CapEx / staffing / Street guidance; Sabre OR before Amazon |
| **Education** | MS Eng Columbia; BS Eng Mumbai |
| **Public themes** | Continuous belief updates from fine-grain signals; probabilistic demand planning; forecast as the **only forward-looking** enterprise signal — so it must be trustworthy |

**Tone:** peer IC scientist who ships systems, not PI managing grants. He lived Amazon-scale forecasting politics; he will smell roadmap theater. Prefer concrete failure modes and decision linkage.

**Reuse from your Nov meeting:** brief callback only (“good to reconnect — last time we talked about …”) if you remember a specific thread; otherwise don’t invent nostalgia.

---

## 4. Your 60–90s intro (practice out loud)

Frame for **enterprise forecasting product**, not FinTech or SCOT pitch:

> I’m an applied ML scientist focused on sequential and multimodal time series — generative models, representation learning, and rigorous eval. Most recently I’ve been building end-to-end systems that reason over time series with vision-language models, with heavy emphasis on curriculum, ablations, and honest negative results. I’m also deepening production forecasting judgment — baselines, intermittent demand metrics, when boosting beats foundation models and when it doesn’t. I’m a US permanent resident; I reached out in the spring about relocating, and I’m now based in Seattle. I’d love to understand what Keystone is prioritizing in Foundation Forecasting and where science ownership sits.

**If he asks for depth:** pick *one* IC story (ImagenTime / irregular TS / dual-encoding VLM) with a metric and a tradeoff — then connect to **enterprise** problems: scarcity, irregular sampling, eval gates, not architecture tourism.

**Avoid:** grant/mentoring/lab-management framing; “we” without “I”; Chronos-everywhere evangelism; MAPE as default for sparse demand.

---

## 5. Map your strengths → their problems

| Keystone pain (public) | Your credible angle |
|------------------------|---------------------|
| Intermittent / lumpy SKU×customer demand | Metrics discipline (WAPE/MASE/pinball/CRPS); don’t use MAPE; bakeoff thinking by regime |
| Short history / cold start | Pooling, priors, FMs for coverage; when *not* to fine-tune a giant model per client |
| Stock-outs → censored demand | Sales ≠ demand; censor-aware training / unconstrained demand framing |
| Probabilistic → inventory / service level | Quantiles aligned to asymmetric costs; CRPS vs point WAPE |
| ERP events → model-ready signals (RAIN) | Irregular / event-timed series; representation learning under messiness |
| Foundation Forecasting product | Research depth on TS FMs / generative / multimodal — **plus** production judgment from your Forecasting track (baselines first, cost/latency, client feature richness) |
| Decision layer, not forecast-in-a-vacuum | Forecast exists to change a plan (inventory, production, launch timing) |

Cross-links in this repo: [`../../notes/method-decision-table.md`](../../notes/method-decision-table.md), [`../../notes/metrics-cheat-sheet.md`](../../notes/metrics-cheat-sheet.md), prep-plan “Keystone-style failure modes” table.

---

## 6. Questions to ask (pick 5–7; don’t firehose)

**Product / science strategy**

1. What does “Foundation Forecasting” mean in practice today — pretrained backbone + client adaptation, or mostly global models trained on manufacturing panels?
2. Where do open FMs (Chronos-class) win vs lose against your proprietary stack on real client data?
3. How much of the hard problem is **RAIN / data encoding** vs the forecast model itself?
4. How do you evaluate success with clients — WAPE, pinball at service-level quantiles, inventory/cash metrics?

**Failure modes (shows you know the job)**

5. How do you handle **censored demand** (stock-outs) in training and eval?
6. How do you segment series (smooth vs intermittent vs promo/event-driven) for model choice and monitoring?
7. What’s the hardest cold-start pattern in manufacturing vs retail e-comm?

**Org / Seattle / fit**

8. Where is science headcount growing — Bellevue vs NY vs client-embedded?
9. What would a strong principal / senior scientist own in the next 12 months on the forecasting stack?
10. After this briefing, what would a useful next step look like if there’s mutual interest?

**Soft Kari / FM probe (optional, only if natural)**

11. With Kari joining as Distinguished Scientist — how are you shaping the foundation-model side of Foundation Forecasting, and what gaps are you still hiring for?

---

## 7. Day-before checklist

- [ ] Skim [Unified Forecasting](https://www.keystone.ai/solutions/unified-forecasting) + homepage DEEP/RAIN story (10 min)
- [ ] Skim Raunak’s public interview / LinkedIn themes (5 min)
- [ ] Rehearse 60–90s intro once out loud
- [ ] Rehearse one 2-min: “When LightGBM vs a foundation model for intermittent manufacturing demand?”
- [ ] Rehearse one 90s: “MAPE doubled on a client panel — how I debug”
- [ ] Confirm call link / timezone; one-liner ready: **already in Seattle** (reached out in spring about the move)

### Spoken 2-min skeleton — LightGBM vs FM (manufacturing)

```
Problem: lumpy SKU×customer demand → inventory / production decisions.
Data: often sparse, censored, short history; sometimes rich ERP event features via something like RAIN.
Baseline: seasonal naive / simple statistical per segment.
If trusted covariates (price, promo, calendar, inventory state): LightGBM/quantile boosting is still the workhorse — cheap, debuggable, wins bakeoffs.
If many series, thin history, weak features, need fast coverage: foundation / zero-shot or lightly adapted FM.
Always: probabilistic outputs for service levels; eval by regime; don’t crown a model on portfolio MAPE.
Ship decision: hybrid by segment + monitoring; escalate to FM where cold-start / transfer pays for cost.
```

---

## 8. During the call — operating rules

1. **Let him present** first; take notes on their wording (RAIN, Foundation Forecasting, client verticals).
2. Mirror their language; ask clarifying questions before pitching yourself.
3. When you speak, **one concrete bet + constraint** beats a paper list.
4. If asked “would you use Chronos everywhere?” — **no**; segment + cost + covariates (see method table).
5. Close with interest + you’re local (Seattle) + ask for next step (meet a scientist, role overview, follow-up).

---

## 9. Post-call (same day)

Capture in a new file `2026-08-10_raunak-debrief.md`:

- What they’re actually building (their words)
- Hiring / Seattle signal
- Any names (Kari? others?)
- Your strongest moment / weakest
- Promised follow-ups
- Update [`README.md`](README.md) table + [`../INDEX.md`](../INDEX.md) + [`../../INDEX.md`](../../INDEX.md) session log
