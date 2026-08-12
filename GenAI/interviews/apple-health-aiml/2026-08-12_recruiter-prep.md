# Prep — Apple recruiter screen (Health AIML)

**When:** ~2026-08-12 (phone, ~30–45 min typical)  
**Role:** [ML Research Scientist — Health AIML](https://jobs.apple.com/en-us/details/200670570-3337/machine-learning-research-scientist-health-aiml?team=MLAI) (req `200670570-3337`, Seattle)  
**Format:** Recruiter screen — **fit + story + logistics**, not a research seminar.

**Your goal:** clear the soft gate so you meet a hiring manager / scientist. Leave them able to say: *strong multimodal + time-series researcher, publishes SOTA, hands-on training/eval, in Seattle, available FT, genuinely interested in health/fitness GenAI.*

---

## 0. Next-hour checklist (do this, in order)

1. **Say the 60s intro out loud twice** (§3) — fix anything that sounds managerial.
2. **Lock logistics pocket** (§5): Seattle · Green Card · FT available · BGU leave Oct.
3. **Memorize 3 fit bridges** (§2): multimodal VLM · time series / cross-modal · eval + safe deployment.
4. **Pick 3 questions** (§6) — don’t ask compensation first.
5. **Skim anti-patterns** (§7) once.

Skip: paper deep-dives, Apple Watch product trivia, compensation strategy beyond “happy to discuss later when we know level/team.”

---

## 1. What this call is

| Is | Isn’t |
|----|--------|
| Soft screen: who you are, why this role, location/auth/timing | Coding, whiteboard, or paper quiz |
| Recruiter mapping you to **level + team fit** | Health-domain clinical interview |
| Chance to sound like an **IC research scientist who ships models** | Lab-PI / grant / mentoring pitch |
| Mutual interest + next-step logistics | Offer negotiation |

Recruiters often probe: walkthrough of recent work, why Apple/Health, publication signal, training experience, Seattle/relocation, work auth, timeline, competing processes (optional honesty).

---

## 2. JD → you (fit map)

### They want (from [JD](https://jobs.apple.com/en-us/details/200670570-3337/machine-learning-research-scientist-health-aiml?team=MLAI))

| JD signal | Your evidence | How to say it |
|-----------|---------------|---------------|
| **Large multimodal models** | Qwen3.5 VLM stack (**9B** / **27B**); dual visual encodings → LLM; LoRA / PEFT / DDP | “I build and train multimodal LLMs end-to-end — not just apply APIs.” |
| **Health/fitness representation + multimodal** | TS as images + language; representation learning under scarcity | “Same problem class: heterogeneous physiological / activity-like **time series** + language/vision → shared representations.” Don’t fake clinical claims. |
| **Time-series, SSL, cross-modal** (preferred) | ImagenTime, irregular TS, dual-tower cross-modal alignment | Preferred quals are your **strongest** match — lead here. |
| **Train + evaluate multimodal** | Tiered eval, pilots, ablations, multi-scale **9B↔27B** | Eval rigor is a differentiator; Apple cares about **safe** health LLMs. |
| **PhD + SOTA pubs** | PhD Technion; 40+ NeurIPS/ICML/ICLR | One sentence; don’t list papers unless asked. |
| **Major LLM training runs** | Hands-on multi-GPU fine-tunes / curricula at **9B / 27B** class, not foundation pretrain from scratch | Frame honestly: **contributed to / owned** large multimodal **training runs** (DDP, LoRA, multi-stage). Don’t claim GPT-scale pretraining. |
| **Research lead / guide multimodality** | Technical leadership on architecture + experiments | Lead with **technical** leadership of research direction — not people management. |
| **Safe LLM deployment in health** | Eval gates, negative results, abstention thinking | Motivation + discipline: “wrong answer in health is costly; I gate on eval before claiming progress.” |
| **Industry experience** | UCLA faculty; ICSI Berkeley affiliate; industry collabs (Google/NVIDIA/Bosch — keep light unless they ask for detail) | “Industry + applied research experience beyond academia.” |
| **PyTorch** | Primary stack | Easy checkbox. |

### Gaps — don’t hide; don’t over-explain

| Gap | Pocket |
|-----|--------|
| Not a clinical / Apple Health product insider | “Strongest overlap is multimodal + time-series foundations; I’m motivated to apply that to health/fitness under Apple’s privacy and safety bar.” |
| Not multi-trillion-token LLM pretrain lead | “My recent work is multimodal LLM **training and eval at the fine-tune / adapter / curriculum** scale on multi-GPU clusters — architecture, data, and gating, not only inference demos.” |
| PI title can read managerial | Force IC verbs: designed, implemented, trained, debugged, killed bad mixes. |

**Headline fit (one sentence for yourself):**  
They asked for multimodal + time series + cross-modal + eval — that is your last 2–3 years of work; health is the **deployment domain**, not a missing research stack.

---

## 3. Spoken scripts

### 60-second intro (practice this)

> I’m an applied ML research scientist focused on sequential and multimodal data. Most recently I’ve been building end-to-end systems that teach vision-language models to reason over time series — dual visual encodings into an LLM, multi-stage training curricula, and a strict eval harness so we only keep changes that actually move the metrics. Before that, my work was generative and representation learning for time series — including image-based transforms and irregular sampling. I have a PhD from the Technion and publish in NeurIPS, ICML, and ICLR. I’m a US permanent resident, I’m based in Seattle, and I’m looking for a full-time IC research scientist role where multimodal models meet real user impact. Health AIML is a strong fit because the job is essentially foundational multimodal models over health and fitness signals at Apple scale — and I’m motivated by doing that carefully, with eval and safety first.

### Why Apple / why this role (20–30s)

> Apple sits at the intersection of devices people already trust with health and fitness data and world-class on-device / platform ML. This role is explicitly about multimodal foundational models for health and fitness experiences, including representation learning and time series — which matches what I’ve been building. I want to do that research where it reaches millions of users and where getting it wrong has real cost, so safety and evaluation matter as much as model cleverness.

### Flagship project (45–60s if they ask “tell me about a recent project”)

> I built a research stack to fine-tune multimodal LLMs on time-series reasoning. The core idea: one visualization isn’t enough — I use a line-chart encoding for trend/amplitude semantics and a delay-embedding image for structure, fuse both into the LLM, and train in two stages: first align vision to “see” series, then teach the language model to answer. We’re on **Qwen3.5** at **9B and 27B** scales — large config-driven sweeps on multi-GPU clusters with LoRA, gated by a tiered eval so cheap pilots happen before expensive full benchmarks. When a data-mix idea hurt temporal reasoning, I killed it and went back to data generation instead of stacking more training. That’s the working style I’d bring: architecture + data + honest eval.

### Motivation for health (don’t claim MD expertise)

> I’m not a clinician. What I care about is multimodal models that understand messy longitudinal signals — activity, physiological-like time series, text context — and only ship when evaluation supports it. Health and fitness is exactly where that combination matters, and where overconfident LLMs are unacceptable.

---

## 4. Likely recruiter questions → short answers

| Question | Answer direction |
|----------|------------------|
| Walk me through your background | Chronology light → land on multimodal TS VLM as current center of gravity |
| What are you looking for? | FT IC research scientist; multimodal / foundation-model research with product impact; Seattle |
| Why leave academia / why now? | Want to ship foundational multimodal tech at scale; available FT (academic leave from Oct; available now) |
| Level / years? | PhD + post-academia research career; publications + hands-on training systems — let them map level; don’t self-downgrade |
| Publications? | 40+ top venues; highlight multimodal / TS / generative as relevant cluster if asked for examples |
| LLM training experience? | Owned multimodal training runs: multi-GPU DDP, LoRA curricula, eval gates — honest about fine-tune vs pretrain-from-scratch |
| Competing offers / process? | Optional: exploring a few industry GenAI / science roles; Apple Health AIML is high priority given multimodal + TS + Seattle |
| Comp expectations? | Prefer to learn level/scope first; public range is known; happy to discuss later with full package |
| Remote? | Role is Seattle; you’re **already in Seattle** — on-site is fine |
| Management interest? | Looking for **IC research** impact; will guide technical direction / mentoring as needed, not seeking a people-manager seat |

---

## 5. Logistics pocket (say cleanly)

Reuse the same facts as Keystone/Boris — consistency across companies:

> I’m a US permanent resident. I’m based in Seattle. I’m looking for a full-time IC role. I’m employed at BGU through October on an academic timeline, but I can start a full-time industry role — available now / align start with the team. No visa sponsorship needed.

If they ask remote vs office: **Seattle on-site is workable**; don’t open with remote as a demand.

**Public base range** (only if they bring pay): [$175,000–$308,500](https://jobs.apple.com/en-us/details/200670570-3337/machine-learning-research-scientist-health-aiml?team=MLAI) + equity/benefits. Don’t anchor a number unless pressed; if pressed: “I’d expect to land in a competitive band for the level you assess — happy to sync once we know the level and total package.”

---

## 6. Questions to ask them (pick 3)

**Role / team**
1. How is Health AIML organized relative to other AIML / health teams — and what does “research lead for multimodality” mean day-to-day (IC depth vs coordinating others)?
2. What problems is the team focused on right now — representation learning, on-device constraints, multimodal fusion, eval for safety?
3. What does success in the first 6–12 months look like for this hire?

**Process**
4. What does the interview loop typically look like after this call (HM screen, research talk, coding)?
5. Is this an active open req with a hiring manager already identified?

**Optional if rapport is good**
6. How does the team think about **safe** LLM behavior for health/fitness — eval gates, abstention, human review?

Avoid on first screen: “What’s the exact model Apple Watch uses?” / IP-probing product questions / comp as question #1.

---

## 7. Anti-patterns (read once)

| Avoid | Do |
|-------|-----|
| “I run a lab / supervise students…” | “I designed the dual-tower stack and owned the training + eval loop…” |
| Overclaiming clinical health expertise | Bridge via multimodal + time series + eval/safety motivation |
| Claiming foundation-model pretrain ownership you don’t have | Accurate: multimodal LLM training runs, curricula, infra contribution |
| Forecasting-company pitch (Keystone/Chronos) | This is **GenAI / multimodal health** — keep forecasting only as TS credibility if asked |
| Long paper list | One flagship + offer to go deeper |
| Negotiating RSUs on call 1 | Learn process + next step |

---

## 8. If they ask “any concerns / fit gaps?”

> The JD’s preferred qualifications — multimodal training/eval, time series, self-supervised and cross-modal learning — are where I’ve been deepest. The main learning curve I’d expect is Apple’s health/fitness product constraints and the bar for safely deploying models in that space. That’s a reason I want the role, not a reason to hesitate.

---

## 9. Close

> I’m very interested in this role and team. I’d love to meet the hiring manager or a scientist on Health AIML next. Happy to send an updated CV or any materials that help.

After the call: write `2026-08-12_recruiter-debrief.md` (their questions, level signal, next step, any HM name) and update this README’s active thread.
