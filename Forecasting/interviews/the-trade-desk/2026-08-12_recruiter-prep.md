# Prep — TTD recruiter screen (Channel Growth)

**When:** 2026-08-12 (phone)  
**Role:** [Senior Applied Scientist, Channel Growth](https://careers.thetradedesk.com/jobs/5021488007/senior-applied-scientist-channel-growth) (REQ-8645; Bellevue / San Jose)  
**Format:** Recruiter screen — **fit + story + logistics**, not a forecasting seminar.

**Your goal:** clear the soft gate so you meet a hiring manager / scientist. Leave them able to say: *strong forecasting + sequential-ML scientist, ships models with eval discipline, PhD + IC hands-on, already in Seattle, available FT, genuinely interested in Channel Growth (forecast / pace / recommend on emerging channels).*

---

## 0. Next-hour checklist (do this, in order)

1. **Say the 60s intro out loud twice** (§3) — forecasting-first, not VLM/health.
2. **Lock logistics pocket** (§5): Seattle → **Bellevue** · Green Card · FT available · BGU leave Oct.
3. **Memorize 3 fit bridges** (§2): forecasting (stat/ML/DL) · custom models when off-the-shelf fails · eval + production judgment.
4. **Pick 3 questions** (§6) — don’t ask compensation first.
5. **Skim anti-patterns** (§7) once.

Skip: RTB auction theory, Kokai product trivia, Chronos-vs-LightGBM bakeoff unless they pull you there, compensation strategy beyond “happy to discuss later when we know level/team.”

---

## 1. What this call is

| Is | Isn’t |
|----|--------|
| Soft screen: who you are, why this role, location/auth/timing | Coding, whiteboard, or ads-auction quiz |
| Recruiter mapping you to **level + team fit** | Proof you already built a pacer |
| Chance to sound like an **IC scientist who owns models end-to-end** | Lab-PI / grant / mentoring pitch |
| Mutual interest + next-step logistics | Offer negotiation |

Recruiters often probe: walkthrough of recent work, why TTD / this team, forecasting vs research-only, Seattle/Bellevue, work auth, timeline, competing processes (optional honesty).

---

## 2. JD → you (fit map)

### They want (from [JD](https://careers.thetradedesk.com/jobs/5021488007/senior-applied-scientist-channel-growth))

| JD signal | Your evidence | How to say it |
|-----------|---------------|---------------|
| **Forecasting (stat, ML, DL)** | Koopman / sequential modeling lineage; ImagenTime; irregular TS; industry bakeoff (SN / ETS / LightGBM / Chronos) | “Forecasting is the center of my work — classical baselines through boosting and deep / foundation models, and I choose by constraint, not fashion.” |
| **Pacing (short-term vs long-term constraints)** | Weaker direct match. Bridge: allocation over a horizon under budget/inventory constraints; eval that matches the **decision**, not vanity MAPE | “I haven’t shipped an ads pacer. The science shape is familiar: forecast remaining opportunity, spend/allocate under constraints, measure the business loss.” |
| **Recommendations** | Weaker than forecasting. Public Kokai: channel recs from a forecast. Your recs/ranking depth is not the lead | Lead forecasting. If asked: “Recs here look like *which channel / inventory to add given a forecast and a goal* — a decision on top of the forecast.” |
| **Custom solutions; off-the-shelf doesn’t scale** | Dual encodings, irregular TS, data-scarce regimes; bakeoff: FMs lose when covariates dominate | “That’s been my default: when Chronos-style or generic DL doesn’t win, I keep the baseline and change the representation or the features.” |
| **Prototype → production with engineering** | End-to-end stacks (data → train → eval harness → kill bad ideas); Slurm / multi-GPU DDP | “I own the loop through eval gates. I’d expect to pair with TTD eng on Spark / serving — that’s a stack I learn, not a reason to hesitate.” |
| **Metrics, offline eval, A/B, business impact** | Tiered eval; WAPE/MASE vs MAPE; pinball/CRPS when the decision needs uncertainty | “I don’t ship on a single % error. Metric has to match the decision — under-delivery vs over-delivery is not symmetric.” |
| **Always-on production ML** | Research production (always-running training/eval), not ads RTB serving | Honest: “My production to date is research/training systems at cluster scale. The always-on serving + monitoring bar is why I want this role.” |
| **Python + PyTorch** | Primary stack | Easy checkbox. |
| **Spark / EMR / Databricks** | Gap. You run heavy distributed workloads (Slurm, DDP), not ads Spark pipelines | “I’ve run large distributed training jobs; Spark on EMR/Databricks is the platform translation, not a new science problem.” |
| **Programmatic / real-time auctions (preferred)** | Gap. Don’t fake it. | “Preferred, not required. I’m coming in as a forecasting scientist who wants to learn the auction/pacing constraints — not as an ads veteran.” |
| **PhD + 3y or MS + 5y, ideation → production** | PhD Technion + years of shipped research systems | One sentence; don’t list papers unless asked. |

### Gaps — don’t hide; don’t over-explain

| Gap | Pocket |
|-----|--------|
| Not a programmatic-ads insider | “Strongest overlap is forecasting + sequential models + eval. Ads auctions and pacing controllers are the domain constraints I’d learn on the job — that’s a reason I want the role.” |
| No shipped pacing system | Constraint-aware allocation over a flight; forecast remaining inventory/opportunity; asymmetric cost of over- vs under-spend. |
| Spark/Databricks vs Slurm | Distributed compute literacy; different API, same ownership muscle. |
| PI title can read managerial | Force IC verbs: designed, implemented, trained, evaluated, killed. |

**Headline fit (one sentence for yourself):**  
They asked for **one or more of** forecasting, pacing, or recs — forecasting is the deep match; pacing/recs are the product layer on top; emerging channels are why generic models fail.

---

## 3. Spoken scripts

### 60-second intro (practice this)

> I’m an applied ML research scientist focused on sequential data and forecasting. Most of my work is building models for messy time series — statistical and ML baselines through deep learning — and being honest about when a fancy model loses to a simpler one. I’ve owned that loop end-to-end: representations, training, and a strict eval harness so we only keep changes that actually move the metric that matches the decision. I have a PhD from the Technion and publish in NeurIPS, ICML, and ICLR. I’m a US permanent resident, I’m based in Seattle, and I’m looking for a full-time IC applied-scientist role where forecasting ships into a product. Channel Growth is a strong fit because it’s forecasting plus allocation under constraints — pacing and recommendations — on emerging channels where off-the-shelf models usually don’t work.

### Why TTD / why this role (20–30s)

> The Trade Desk is the independent platform for the open internet, and the hard science problem on emerging channels — CTV, podcasts, live events — is that history is shorter, inventory is lumpier, and a generic forecast will lie. This role is explicitly forecasting, pacing, and recommendations that change planning and allocation. That’s the kind of production forecasting I want to do: models that traders actually use, gated on eval and experiments, not a research demo.

### Flagship project (45–60s if they ask “tell me about a recent project”)

Pick **forecasting / sequential**, not the Apple Health VLM pitch:

> A through-line in my work is forecasting and representing time series that don’t look like clean retail demand — irregular sampling, short history, structure that a vanilla model misses. I’ve built image-based transforms and dual representations for series, and I’ve also run the industry-style bakeoff: seasonal naive and ETS against LightGBM and Chronos-class models, with metrics that don’t blow up on zeros. The working style I’d bring is: baseline first, escalate only when the constraint demands it, and kill ideas that don’t win on the decision metric.

If they specifically ask about deep learning / PyTorch at scale, *then* add one sentence on multimodal LLM training (Qwen 9B/27B, DDP, LoRA, eval gates) as evidence you can run heavy DL — not as the job pitch.

### Pacing in one breath (only if they ask)

> Pacing is a control problem on top of a forecast: you have a budget and a flight, you must not exhaust too early or underspend, and short-term performance can fight long-term delivery. I’d start from a forecast of remaining opportunity, a spend-rate policy under constraints, and an eval that penalizes the failure mode the business actually cares about — not MAPE on impressions.

---

## 4. Likely recruiter questions → short answers

| Question | Answer direction |
|----------|------------------|
| Walk me through your background | Chronology light → land on **forecasting / sequential ML** as current center of gravity |
| What are you looking for? | FT IC applied scientist; forecasting systems with product impact; Seattle / Eastside |
| Why leave academia / why now? | Want to ship forecasting into a product at scale; available FT (academic leave from Oct; available now) |
| Level / years? | PhD + post-academia research career; let them map Senior AS; don’t self-downgrade |
| Do you have ads / programmatic experience? | No. Forecasting + production-minded eval is the transfer; eager to learn auction/pacing constraints |
| Forecasting vs research papers? | Papers are the research arc; I also think in bakeoffs, baselines, and what I’d actually ship |
| Competing offers / process? | Optional: exploring a few applied-science roles (forecasting + GenAI); TTD Channel Growth is high priority given forecasting + Bellevue |
| Comp expectations? | Prefer to learn level/scope first; public range is known; happy to discuss later with full package (stock matters here) |
| Remote? / which office? | Role is Bellevue or San Jose; you’re **in Seattle** — **Bellevue** is the office |
| Management interest? | Looking for **IC** impact; will guide technical direction as needed, not seeking a people-manager seat |

---

## 5. Logistics pocket (say cleanly)

Same facts as Keystone / Apple — consistency across companies:

> I’m a US permanent resident. I’m based in Seattle. I’m looking for a full-time IC role. I’m employed at BGU through October on an academic timeline, but I can start a full-time industry role — available now / align start with the team. No visa sponsorship needed.

Office: **Bellevue is workable**; don’t open with remote as a demand. Don’t volunteer San Jose.

**Public base range** (only if they bring pay): [$124,900–$228,900](https://careers.thetradedesk.com/jobs/5021488007/senior-applied-scientist-channel-growth) + equity/benefits. Internally: this base band is **lower** than Apple’s public range; TTD total comp is stock-heavy. Don’t anchor a number unless pressed; if pressed: “I’d expect to land in a competitive band for the level you assess — happy to sync once we know the level and total package.”

---

## 6. Questions to ask them (pick 3)

**Role / team**
1. How is **Channel Growth** scoped versus the broader forecasting science org (there’s also a Deep Learning Forecasting req) — emerging-channel forecast/pacing vs platform-wide campaign forecasting?
2. What does “emerging channels” mean for this hire right now — CTV, podcasts, live events, something else — and what’s the first problem they’d want owned?
3. What does success in the first 6–12 months look like: a better forecast, a pacer in production, channel recs, or all three?

**Process**
4. What does the loop look like after this call (HM screen, tech screen, on-site)?
5. Is the hiring manager already identified — and is the seat Bellevue-based?

**Optional if rapport is good**
6. How do scientists here split time between research prototypes and always-on production (Spark / serving / monitoring)?

Avoid on first screen: “What’s your exact pacing controller?” / IP-probing auction questions / comp as question #1.

---

## 7. Anti-patterns (read once)

| Avoid | Do |
|-------|-----|
| Apple Health / VLM-first intro | Forecasting + sequential models first; DL-at-scale as backup evidence |
| “I run a lab / supervise students…” | “I designed the model and owned training + eval…” |
| Overclaiming programmatic / RTB expertise | Honest gap + constraint-aware forecasting bridge |
| Lecturing Kokai / Decision Power | Light product literacy; ask what Channel Growth owns |
| Chronos paper recap | When you’d use / reject a method under ads constraints |
| Negotiating RSUs on call 1 | Learn process + next step |
| Sounding like Keystone supply-chain | This is **ads planning/allocation**, not CPG inventory — same science muscles, different decisions |

---

## 8. If they ask “any concerns / fit gaps?”

> The JD’s strongest overlap with me is forecasting — statistical, ML, and deep learning — plus building custom models when generic ones don’t scale, and gating on eval. I don’t have programmatic-auction years. The learning curve I expect is TTD’s channel/pacing product constraints and the always-on serving stack. That’s a reason I want the role, not a reason to hesitate.

---

## 9. Close

> I’m very interested in this role and the Bellevue team. I’d love to meet the hiring manager or a scientist on Channel Growth next. Happy to send an updated CV or any materials that help.

After the call: write `2026-08-12_recruiter-debrief.md` (their questions, level signal, next step, any HM name) and update this README’s active thread.
