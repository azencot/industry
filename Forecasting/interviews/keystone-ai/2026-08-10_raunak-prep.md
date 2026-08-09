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

### Thesis (Zero100 / Greg Richards — instrumental)

Source: [Keystone presents future of forecasting at Zero 100 Live](https://keystone.ai/resources/keystone-presents-future-of-forecasting-to-supply-chain-leaders-at-zero-100-live/) (also under [news-publications](https://www.keystone.ai/news-publications/keystone-presents-future-of-forecasting-to-supply-chain-leaders-at-zero-100-live)).

| They reject | They ship toward |
|-------------|------------------|
| **Point forecasts** + manual buffers / heuristics | **Probabilistic** forecasts (distributions, quantiles) |
| Forecast as a disconnected planning artifact | Forecast **conditioned on / wired into decision constraints** |
| “Better dashboards / faster planning runs” | **Decision intelligence** — inventory, production, service level, capital under uncertainty |

Spoken one-liner if it fits:

> Forecasting that isn’t decision-aware isn’t finished science — produce under uncertainty is a probabilistic + economic problem, not a point-MAPE problem.

**Problem they sell:** manufacturers don’t trust demand forecasts; ERP averages destroy the signals that matter; planning needs **probabilistic, multi-horizon, multi-level** forecasts optimized against real tradeoffs — not vanity point accuracy.

**Stack (their language):**

1. **RAIN** — turn ERP / orders / shipments / invoices into fine-grained **event streams** (timing + sequence preserved), enriched with market / weather / etc., into science-ready representations.
2. **Foundation Forecasting™** — proprietary models for **intermittent / irregular** demand across horizons and hierarchy (market → product line → SKU / customer / ship-to); **quantify uncertainty** so decisions can optimize against economics.
3. **DEEP** — decision layer that plugs into existing ERP / IBP (SAP, Oracle, Kinaxis, o9, …); forecasts → algorithms balancing **constraints + SKU economics** (not rip-and-replace).

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
| **Public themes** | Continuous belief updates from fine-grain signals; probabilistic demand planning; forecast as the **only forward-looking** enterprise signal — so it must be trustworthy and **decision-linked** |

**Tone:** peer IC scientist who ships systems, not PI managing grants. He lived Amazon-scale forecasting politics; he will smell roadmap theater. Prefer concrete failure modes and decision linkage.

**His signature frame ([interview](https://keystone.ai/resources/the-only-forward-looking-signal-in-your-enterprise-plan-is-broken/)):**

> It’s not a forecasting *literacy* problem — it’s a broken **API** problem. The forecast is the only forward-looking signal in the plan, and there are almost no mechanisms to **inject real enterprise context** into it.

RAIN is *their* answer (fine-grain event streams from how customers buy — explicitly *not* “dump everything into an LLM”). The broader research question he opens: **what are the APIs / representation interfaces that map existing enterprise context → better probabilistic demand beliefs → economic decisions?**

### Optional science angle (yours) — “CLIP for enterprises”

**Idea:** RAIN is one injection path (structured event encoding). Context injection can also look like **learned alignment** across heterogeneous enterprise modalities — analogous to CLIP joining image ↔ text spaces:

| Modality / context | Examples |
|--------------------|----------|
| Transactional events | orders, shipments, invoices (RAIN’s home turf) |
| Structured plan state | inventory, capacity, open POs, service targets |
| Catalog / hierarchy text | SKU descriptions, customer segments, product families |
| Semi-structured ops | planner notes, promotions, contract terms |
| Exogenous | weather, market, macro |

A “CLIP-like” enterprise stack would learn a **shared embedding space** so that plan/context tokens and demand trajectories become queryable / conditionable — then Foundation Forecasting consumes those embeddings (or cross-attends), and DEEP still owns constraint optimization.

**Why this is credible for you:** dual-encoding / multimodal TS work (chart + delay embedding → LLM), representation learning under scarcity, eval discipline — not “I reinvented RAIN.”

**Call hygiene:**

- Frame as a **question / research bet**, not a product pitch that competes with RAIN.
- Affirm his point: dump-to-LLM ≠ context injection; alignment must be grounded in fine-grain behavior + decision loss.
- Ask where they draw the line today between engineered event encoding vs learned multimodal context APIs.

**Spoken probe (optional, if he opens the “API / context” door):**

> One reading of your broken-API point is that RAIN is the structured event path — and I’m curious whether you also see room for learned alignment across plan state, catalog text, and demand trajectories, CLIP-style, so context becomes a first-class conditioner for probabilistic forecasts rather than a feature afterthought.

### Optional science angle (yours) — multimodal → **agentic decision** stack

He closes the interview on the long arc: agents that make **economically intelligent decisions** — not click automation. Chain he states:

```
enterprise context → better probabilistic demand beliefs → economic decision frameworks → agents
```

So “agentic” at Keystone is **not** a chat UI over SAP. It’s a loop that needs calibrated beliefs + constraint-aware actions. Map your multimodal work onto **layers of that loop**, not onto “I build agents”:

| Agent-loop layer | What it needs | Your transferable work |
|------------------|---------------|------------------------|
| **Perceive / inject context** | Turn messy multi-source enterprise signal into model-ready state | Dual encodings, multimodal fusion, irregular/scarce regimes; CLIP-like alignment bet above |
| **Believe (forecast)** | Probabilistic multi-horizon demand (quantiles / trajectories) | Generative / FM / TS modeling judgment; pinball–CRPS discipline; when *not* to use an LLM |
| **Reason over series + text** | Explain regimes, compare scenarios, answer planner-style questions | TS–VLM stack: curriculum, structured QA/regression over series, ablations, negative results |
| **Act (decide)** | Optimize under inventory / capacity / service / cost constraints | You don’t need to own OR solvers — speak the interface: beliefs → decision objective; DEEP’s job |
| **Verify / gate** | Don’t let agents ship uncalibrated actions | Your eval harness instinct: tiered eval, north-star metrics, rollback when mix/ablation fails |

**Concrete roles a multimodal scientist can own in their agent roadmap:**

1. **World-state encoder for the agent** — multimodal perception of demand + plan context (not free-form ERP chat).
2. **Belief interface** — agent tools that return *distributions / scenarios*, not point numbers.
3. **Planner-facing reasoner** — grounded answers over series (“why did P90 jump?”, “which customers drive intermittency?”) with parse/eval gates.
4. **Agent eval** — score the *decision* (service, inventory $, stockout) and belief calibration, not demo fluency.

**Call hygiene:**

- Agree with him: agents without trustworthy forward-looking beliefs are theater.
- Don’t pitch “agentic LLM app.” Pitch **perception + belief + eval** that make decision agents safe to automate.
- Ask what fraction of current science effort is Foundation Forecasting vs DEEP vs agent orchestration — and where IC scientists sit.

**Spoken probe (if he lands on agents):**

> If the end state is agents that act on economic decisions, I see multimodal work less as the agent itself and more as the perception and reasoning layer — grounding messy enterprise and time-series context into calibrated beliefs the decision layer can trust. How are you splitting science ownership between belief models, constraint optimization, and agent orchestration today?

**Reuse from your Nov meeting:** brief callback only (“good to reconnect — last time we talked about …”) if you remember a specific thread; otherwise don’t invent nostalgia.

---

## 4. Your 60–90s intro (practice out loud)

Frame for **enterprise forecasting product**, not FinTech or SCOT pitch:

> I’m an applied ML scientist focused on sequential and multimodal time series — generative models, representation learning, and rigorous eval. Most recently I’ve been building end-to-end systems that reason over time series with vision-language models, with heavy emphasis on curriculum, ablations, and honest negative results. I’m also deepening production forecasting judgment — baselines, intermittent demand, **probabilistic eval** (pinball/CRPS), and when boosting beats foundation models. I’m a US permanent resident; I reached out in the spring about relocating, and I’m now based in Seattle. I’d love to understand how Keystone is wiring Foundation Forecasting into **decision constraints** — and how far along the **agentic decision** path you are beyond the belief models.

**If he asks for depth:** pick *one* IC story (ImagenTime / irregular TS / dual-encoding VLM) with a metric and a tradeoff — then connect to **enterprise** problems: scarcity, irregular sampling, eval gates, not architecture tourism.

**Avoid:** grant/mentoring/lab-management framing; “we” without “I”; Chronos-everywhere evangelism; treating **point MAPE/WAPE** as the north star; pitching **chatbots / generic agent frameworks** without belief calibration + decision metrics.

---

## 5. Map your strengths → their problems

| Keystone pain (public) | Your credible angle |
|------------------------|---------------------|
| Point forecast + buffers as “planning” | Probabilistic outputs; decision needs quantiles / paths, not a single number |
| Forecast disconnected from decisions | Pinball/CRPS + service-level / newsvendor framing; forecast exists to change a plan |
| Intermittent / lumpy SKU×customer demand | Metrics by regime (WAPE/MASE); don’t use MAPE; bakeoff thinking |
| Short history / cold start | Pooling, priors, FMs for coverage; when *not* to fine-tune a giant model per client |
| Stock-outs → censored demand | Sales ≠ demand; censor-aware training / unconstrained demand framing |
| Multi-horizon, multi-level (SKU/customer/ship-to) | Hierarchy + coherence awareness; eval at the level that drives the decision |
| ERP events → model-ready signals (RAIN) | Irregular / event-timed series; representation learning under messiness |
| “Broken API” — inject enterprise context into the forecast | Multimodal / alignment lens (CLIP-like enterprise context ↔ demand); dual-encoding TS–VLM as **injection / perception** interfaces |
| Agentic economic decisions (their north star) | Multimodal = perceive + reason + eval gates; probabilistic forecast = agent **belief**; DEEP = act under constraints — you strengthen the stack agents need, not a chat wrapper |
| Foundation Forecasting → DEEP optimization | Research depth on TS FMs / generative — **plus** production judgment; cost/latency; client feature richness |

Cross-links in this repo: [`../../notes/method-decision-table.md`](../../notes/method-decision-table.md), [`../../notes/metrics-cheat-sheet.md`](../../notes/metrics-cheat-sheet.md), prep-plan “Keystone-style failure modes” table.

---

## 6. Questions to ask (pick 5–7; don’t firehose)

**Product / science strategy**

1. In the Zero100 framing you reject point forecasts for probabilistic ones wired to decisions — where does that boundary sit today between Foundation Forecasting (distributions) and DEEP (constraint / economic optimization)?
2. What does “Foundation Forecasting” mean in practice — pretrained backbone + client adaptation, or mostly global models on manufacturing panels?
3. Where do open FMs (Chronos-class) win vs lose against your proprietary stack on real client data?
4. How much of the hard problem is **RAIN / data encoding** vs the forecast model vs the decision layer?
5. Beyond event streams — what other context-injection APIs matter (plan state, hierarchy text, planner overrides), and where do you *refuse* LLM dump-in?
6. How do you evaluate success with clients — pinball at service-level quantiles, inventory/cash / service metrics, vs point WAPE?

**Failure modes (shows you know the job)**

7. How do you handle **censored demand** (stock-outs) in training and eval?
8. How do you segment series (smooth vs intermittent vs promo/event-driven) for model choice and monitoring?
9. What’s the hardest cold-start pattern in manufacturing vs retail e-comm?

**Agentic / roadmap**

10. How much of current science effort is belief models (Foundation Forecasting) vs decision optimization (DEEP) vs agent orchestration — and what’s still human-in-the-loop by design?
11. What would make you *not* trust an agent to act on a forecast (calibration, constraint violation, client override norms)?

**Org / Seattle / fit**

12. Where is science headcount growing — Bellevue vs NY vs client-embedded?
13. What would a strong principal / senior scientist own in the next 12 months on the forecasting ↔ decision ↔ agent stack?
14. After this briefing, what would a useful next step look like if there’s mutual interest?

**Soft Kari / FM probe (optional, only if natural)**

15. With Kari joining as Distinguished Scientist — how are you shaping the foundation-model side of Foundation Forecasting, and what gaps are you still hiring for?

---

## 7. Day-before checklist

- [ ] Skim [Zero100 future-of-forecasting](https://keystone.ai/resources/keystone-presents-future-of-forecasting-to-supply-chain-leaders-at-zero-100-live/) thesis (probabilistic + decision constraints) — 5 min
- [ ] Skim [Unified Forecasting](https://www.keystone.ai/solutions/unified-forecasting) + homepage DEEP/RAIN story (10 min)
- [ ] Skim Raunak’s public interview / LinkedIn themes (5 min)
- [ ] Rehearse 60–90s intro once out loud
- [ ] Rehearse one 2-min: “When LightGBM vs a foundation model for intermittent manufacturing demand?” (end on **probabilistic → decision**)
- [ ] Rehearse one 90s: “MAPE doubled on a client panel — how I debug” (and why point MAPE isn’t the client north star)
- [ ] Confirm call link / timezone; one-liner ready: **already in Seattle** (reached out in spring about the move)

### Spoken 2-min skeleton — LightGBM vs FM (manufacturing)

```
Problem: lumpy SKU×customer demand → inventory / production decisions under uncertainty.
North star is not a point forecast — need distributions/quantiles that can be optimized against service, inventory, and production constraints.
Data: often sparse, censored, short history; sometimes rich ERP event features via something like RAIN.
Baseline: seasonal naive / simple statistical per segment.
If trusted covariates: LightGBM/quantile boosting is still a strong workhorse — cheap, debuggable.
If many series, thin history, weak features: foundation / zero-shot or lightly adapted FM for coverage.
Always: probabilistic eval (pinball/CRPS) + business KPIs; don’t crown a model on portfolio MAPE.
Ship decision: hybrid by segment + monitoring; the forecast only “wins” if the downstream plan improves.
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
