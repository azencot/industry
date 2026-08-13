# Prep — Bosch HM screen with Shabnam Ghaffarzadegan

**When:** **Thursday, August 13, 2026 · 3:15–3:45 PM PDT** (30 min)  
**Role (use this title on the call):** [AI Research Scientist — Multimodal Foundational Models](https://jobs.smartrecruiters.com/BoschGroup/744000139447918-ai-research-scientist-multimodal-foundational-models-) (Sunnyvale, hybrid)  
**You first read:** [Senior TSFM](https://jobs.smartrecruiters.com/BoschGroup/744000135345769-senior-ai-research-scientist-time-series-foundational-models?trid=2d92f286-613b-4daf-9dfa-6340ffbecf73) — same group, almost the same JD. **Do not correct her to Senior TSFM.**  
**HM:** **Shabnam Ghaffarzadegan** (CR/RHI1-NA) — she emailed; she will be on Teams  
**HR:** GS/HRS-PAC-NA (may join)  
**Format:** Microsoft **Teams** · **fit** — “background and interest.” Not a coding round. Invite log: [`2026-08-12_hm-invite.md`](2026-08-12_hm-invite.md)

**Your goal:** she leaves thinking: *genuinely wants this sensor+vision FM team, already works beyond forecasting (classify / describe / fuse), can talk high-frequency signals without faking speech/ICASSP, IC not lab-PI, worth a technical loop.*

**Do not mix tracks:** TTD / Keystone stay parked. Apple Health scripts stay parked. Lead with **multimodal sensor FMs**, not SKU demand or Watch fitness.

---

## 0. Next-hour checklist (do this, in order)

1. Reply-all confirming the slot. Test Teams once.
2. **Say the 60s intro out loud twice** (§3) — IC verbs; kill lab-PI; **her job title**; **no** Chronos-vs-LightGBM.
3. **Lock three fit bridges:** classify/describe beyond forecast · high-freq (STFT) for audio/vibration · series + vision.
4. **Lock logistics pocket** (§5): Seattle → Sunnyvale hybrid · Green Card · FT. Don’t volunteer Apple.
5. **Pick 3 questions** (§6) aimed at **her** team (sensor FMs + vision), not a generic TSFM seminar.
6. **Skim anti-patterns** (§7) once — especially: don’t quiz SoundSee/ISS; don’t fake ICASSP.

Skip until a later technical round: radar PHY, TimesFM recap, ADAS product trivia.

---

## 1. What this call is

| Is | Isn’t |
|----|--------|
| HM **fit**: who you are, why **her** multimodal sensor-FM role | Recruiter logistics-only (she is the scientist) |
| Background walkthrough + interest | Coding, whiteboard, or paper quiz |
| Chance to sound like an **IC** who trains and evaluates models | Lab-PI / grant / student-count pitch |
| Light technical if she probes: frequency, fusion, eval | Claiming you shipped Bosch ADAS or speech systems |
| Mutual interest + next-step | Offer negotiation; fighting RS vs Senior title |

**Shabnam (public — don’t name-drop papers unless natural):** audio event/scene classification, weakly labeled audio, “Smart Ear,” SoundSee. [Hiring post](https://www.linkedin.com/posts/shabnam-ghaffarzadegan-42142a93_ai-research-scientist-multimodal-foundational-activity-7484753196805017600-8sO1): FMs on **audio, vibration, radar, IMU** + **vision** for robotics / autonomous / physical AI. [Expert page](https://www.bosch.com/research/about-bosch-research/our-research-experts/shabnam-ghaffarzadegan/).

If she goes technical: **ImagenTime STFT vs delay** (her high-freq sensors) + **VLM classify/describe/fuse** + honest gap (not a speech DSP engineer).

---

## 2. JD → you (fit map)

Headline for yourself: she asked for **multimodal FMs over sensors + vision**, **beyond forecasting**. That is the last 2–3 years of work. Audio/ADAS is the **deployment domain**, not a missing research stack.

### They want (from [her JD](https://jobs.smartrecruiters.com/BoschGroup/744000139447918-ai-research-scientist-multimodal-foundational-models-); Senior TSFM is the same bullets plus explicit low/high frequency)

| JD signal | Your evidence | How to say it |
|-----------|---------------|---------------|
| **TS FMs beyond forecasting** | VLM stack: MCQ, regression, captioning, open QA; ImagenTime generative + discriminative; irregular TS completion | “I don’t treat TSFMs as forecast heads. I train models that **classify, describe, and reason** over series — and I gate on task-level eval.” |
| **Label / predict / classify / cluster / describe / fuse** | Dual-encoding VLM; caption attr-recovery 0.72; TSExam ~0.90; TSRBench north star | Map verbs to tasks you actually ran. Clustering = representation learning / embeddings if asked — don’t invent a clustering paper. |
| **Multivariate TSFM + low and high frequency** | ImagenTime: **STFT** (long periodic / frequency structure) vs **delay embedding** (short + ultra-long topology) | This is the money line. One patch size / one encoding does not serve audio-like and telemetry-like sensors. |
| **Auxiliary video / image for context** | Chart ViT + delay-image DINOv3 → LLM; two-stage curriculum | “Vision is not a plot — it is a second encoder that supplies context the 1-D series loses.” |
| **Signal processing + DL** | Invertible STFT / delay maps; irregular sampling + masking; spectrogram-style thinking | Honest: strong on TS↔image/spectral transforms, not a radar/ultrasound DSP engineer. |
| **Python / PyTorch / Lightning-class stack** | PyTorch, PEFT/LoRA, DDP, eval harness; Slurm | Easy checkbox. Lightning: “I use PyTorch + config-first training; I can work in Lightning.” Don’t fake a Lightning-only resume. |
| **Pubs** | 40+ NeurIPS / ICML / ICLR | One sentence. They also list ICASSP / InterSpeech / CVPR — you are the ML-venue cluster, not speech. |
| **Data-centric / synthetic / agentic** (preferred) | Synthetic captions, CaTS, killed bad TR mixes, data-scarce +55% @ 5% | Lead **data-centric + synthetic**. Agentic: weak — “eval/tooling around training, not multi-agent products.” |
| **Slurm / Git / MLflow** | Slurm + DDP + YAML sweeps | MLflow: familiar with experiment tracking; don’t overclaim a production MLflow org. |
| **Lead small teams / mentor** | Technical direction on architecture + experiments | **Technical** leadership. Do not open with students. |
| **Expert input to management / R&D bets** | Kill decisions, multi-scale 9B↔27B, representation bets | Frame as **technical recommendation with evidence**, not org strategy. |
| **ADAS + Bosch products** | Same problem class: heterogeneous sensors + context modalities | Bridge; don’t fake vehicle programs. |

### Gaps — don’t hide; don’t over-explain

| Gap | Pocket |
|-----|--------|
| Not an ADAS / radar / lidar / ultrasound product owner | “Strongest overlap is multimodal TSFM + frequency-aware representations. I’d learn Bosch sensor stacks and safety constraints on the job — that’s why the role is interesting.” |
| Not ICASSP/speech | “My frequency work is STFT / delay embeddings on general sensors, not a speech-recognition career.” |
| Not 3+ years sitting in an industrial research lab as FTE | UCLA + ICSI + industry collabs; hands-on training systems. IC verbs. |
| PI title reads managerial | Designed, implemented, trained, debugged, killed mixes. |
| Seattle vs Sunnyvale hybrid | §5. Don’t volunteer “I won’t relocate.” |
| Bosch collab on profile is TBD | Use only if you can name it. Otherwise skip. |

---

## 3. Spoken scripts

### 60-second intro (practice this)

> I’m an applied ML research scientist focused on sequential and multimodal data — foundation models that go beyond forecasting. Most recently I’ve been building multimodal models that take a series, encode it two ways — a chart for trend and amplitude, a delay embedding for structure — fuse those into an LLM, and train so the model can classify, describe, and answer questions about the series, not just emit a forecast. Before that I worked on generative time series as images, including choosing STFT versus delay embeddings depending on whether the series is high-frequency periodic or long-range topological. I have a PhD from the Technion and publish in NeurIPS, ICML, and ICLR. I’m a US permanent resident, I’m currently based in Seattle, and I’m looking for a full-time IC research role where I own architecture, training, and eval. This role is a strong fit because it’s multimodal foundation models over industrial sensors — audio, vibration, telemetry — with vision as context. That’s the research line I’ve been on.

### Why Bosch / why this team (20–30s)

> I want to work on foundation models for **real sensors**, not only forecast heads on well-behaved series. Chronos-style models are the wrong abstraction when the signal is acoustics or vibration sitting next to a camera. Bosch RTC is one of the few industrial labs hiring exactly that — classify, describe, fuse, and transfer into products — and still publishing. I’m especially interested in this team because the mandate is multimodal perception for physical AI, not a forecasting-only charter.

### Flagship — VLM as TSFM (45–60s)

> I built a research stack to fine-tune multimodal LLMs on time-series reasoning. One visualization isn’t enough: line charts keep amplitude and trend; delay-embedding images keep topology. I fuse both into the LLM and train in two stages — first align vision so the model can *see* a series, then teach it to *answer*. Tasks are exam-style classification, numeric regression, captions, and open QA. We’re on Qwen3.5 at 9B and 27B, config-driven sweeps on multi-GPU, gated by a tiered eval. When a data mix hurt temporal-relation slices, I killed it and went back to data generation. That’s the working style: architecture plus data plus honest eval — a TSFM judged on many heads, not one forecast metric.

### Frequency split — ImagenTime (30–45s; use if they say “low and high frequency”)

> High-frequency sensors I think in spectrograms and STFT: local frequency structure, hop size versus time resolution. Low-frequency telemetry I think in delay embeddings and charts: trend, topology, long context. In ImagenTime I committed to two invertible maps — STFT won on long periodic series; delay embeddings won on short and ultra-long. A TSFM that uses one patch size for both is the failure mode I’d probe first on Bosch’s mix of acoustics, vibration, and slow telemetry.

### Motivation for ADAS / industrial sensors (don’t claim vehicle ownership)

> I’m not an ADAS stack owner. What I care about is foundation models that understand messy multivariate sensors and extra context from cameras, and that only get promoted when eval on the actual tasks — detect, classify, describe, fuse — supports it. Vehicles and factories are where that combination is expensive to get wrong.

---

## 4. Likely questions → short answers

| Question | Answer direction |
|----------|------------------|
| Walk me through your background | Chronology light → land on multimodal TSFM as current center of gravity |
| What are you looking for? | FT IC research scientist; multimodal / sensor FMs with product transfer; open on Sunnyvale hybrid |
| Why leave academia / why now? | Want TSFMs that have to work on real sensors and transfer; available FT (BGU through Oct; can start — align with team) |
| How is this different from forecasting FMs? | Forecasting is one head. Bosch’s verb list is the product. I already eval classify / describe / numeric / QA. |
| Chronos / TimesFM / MOMENT? | Know the map (§8). Position: useful baselines for *forecast*; insufficient alone for fusion + description + high-freq sensors. |
| LLM-for-TS vs native TSFM? | Tradeoff: LLM/VLM buys language + image context and instruction following; native TSFM buys efficiency and dense numeric fidelity. I’d bake off by **task**, not ideology. |
| How do you fuse video and time series? | Dual-encoder / cross-attention / shared LLM token space. I built chart + delay → LLM. For driving video I’d keep time-aligned context tokens; I would not dump raw lidar into a ViT without a sensor-specific encoder. |
| Signal processing experience? | STFT, delay embeddings, invertibility checks, irregular sampling. Not a radar PHY expert. |
| Publications? | 40+ top ML venues; cluster = generative TS, irregular TS, multimodal reasoning. |
| Industry experience / Bosch collab? | Only if named. Otherwise: applied research + ICSI; want to do this inside Bosch products. |
| Competing processes? | Exploring a few industry science roles. Don’t volunteer Apple unless asked. This team is high priority if the science + hybrid work. |
| Comp? | Prefer level/scope first; public base is $165–195K; happy to discuss total package later. Don’t raise RS vs Senior. |
| Management? | Looking for **IC research** impact; will guide technical direction / mentoring as needed. |
| Can you relocate? | §5. Open to discussing hybrid and relocation for the right team. |

---

## 5. Logistics pocket (say cleanly)

Reuse the same facts as other processes — consistency:

> I’m a US permanent resident. I’m currently based in Seattle. I’m looking for a full-time IC role. I’m employed at BGU through October on an academic timeline, but I can start a full-time industry role — available now / align start with the team. No visa sponsorship needed.

**Sunnyvale hybrid (the actual issue):**

> The role is Sunnyvale hybrid. I’m based in Seattle today. I’m interested enough in this team and problem that I want to understand the hybrid pattern — days on site, whether a start in Seattle then relocate is possible — and I’m open to relocation if the role is the right fit.

Do **not** open with remote-as-a-demand. Do **not** pretend you already live in the Bay.

**Public base range** (only if they bring pay): [$165,000–$195,000](https://jobs.smartrecruiters.com/BoschGroup/744000139447918-ai-research-scientist-multimodal-foundational-models-). Tight for Bay Area RS. Know it; don’t lead with it; if pressed: “I’d expect a competitive total package for the level you assess — happy to sync once we know bonus, LTI, and hybrid/relocation support.”

---

## 6. Questions to ask them (pick 3)

**Role / science (Shabnam)**
1. For this team, what are the north-star tasks for a multimodal sensor FM right now — event classification, anomaly, description, virtual sensing, fusion with vision?
2. How do you combine **high-frequency** audio/vibration with **vision** in practice — spectrogram towers, multi-rate patches, shared tokens?
3. What does success in the first 6–12 months look like — paper, patent, transfer to a business unit?

**Process / org**
4. What does the loop look like after this conversation?
5. How hybrid is Sunnyvale in practice, and how does the group work with ADAS / I4.0 product teams?

**Optional if rapport is good**
6. Labels are expensive on sensors — how do you think about synthetic data, weak labels, and eval slices? (Her public work is weakly labeled audio; don’t lecture.)

Avoid: “Tell me about SoundSee on the ISS” / IP-probing / comp as #1 / “I applied to the Senior TSFM req.”

---

## 7. Anti-patterns (read once)

| Avoid | Do |
|-------|-----|
| Keystone/TTD pitch: LightGBM vs Chronos, MAPE, intermittent demand | Sensor FM **tasks**: classify, describe, fuse, frequency |
| Apple Health pitch: Watch, fitness, clinical safety | Industrial sensors + physical AI / ADAS as the domain |
| “I run a lab / supervise students…” | “I designed the dual-tower stack and owned training + eval…” |
| Quizzing SoundSee / ISS | Bridge via STFT + classify/describe + vision; let her name the product |
| Claiming radar/lidar/ultrasound or speech DSP | Honest: STFT / delay / irregular TS; learning curve is Bosch sensor stacks |
| Correcting her to “Senior TSFM” | Use **Research Scientist, Multimodal Foundational Models** |
| Claiming Chronos-scale pretrain from scratch | Honest: multimodal training runs, curricula, representation FMs |
| Overclaiming the CV “Bosch AI” collab | Name it or omit it |
| Long paper list | One flagship (VLM) + frequency pocket (ImagenTime) |
| Negotiating $165K band on this call | Learn loop + hybrid + next step |

---

## 8. Technical depth (scientist / HM)

Use if they go deep. Do not dump this on a recruiter.

### 8.1 Landscape — where you sit

| Family | Examples | What they’re for | Your take for Bosch |
|--------|----------|------------------|---------------------|
| Forecast FMs | Chronos, TimesFM, Moirai | Zero-shot / few-shot **forecast** | Necessary baseline; **not** the JD. |
| Multi-task TSFMs | MOMENT, UniTS | Forecast + classify + impute from one backbone | Closer. Still weak on **language/description** and **video**. |
| LLM-for-TS | Time-LLM, GPT4TS, ChatTS | Prompt / patch TS into an LLM | Language interface; numeric fidelity and high-freq are the risks. |
| Vision-for-TS | ImagenTime; your dual-tower VLM | TS as images → vision / VLM stack | **Your wedge:** description, classification, image context. |

**Line to remember:** a foundation model is defined by **pretrain + many downstream heads**, not by “it’s a transformer that forecasts.”

### 8.2 Low vs high frequency (they wrote this in the JD)

| | High frequency | Low frequency |
|--|----------------|---------------|
| Bosch examples | Acoustic, vibration, ultrasound, (radar IF) | Telemetry, slow IoT, many vehicle logs |
| Representation | STFT / spectrogram / short windows | Delay embedding, charts, long context |
| Failure mode | Averaging away transients; huge sequences | Missing periodic / resonant structure |
| Your artifact | ImagenTime STFT path | ImagenTime DE path + VLM chart/DE towers |

If they ask “one model or two?”: start with **shared backbone, modality-specific tokenizers / patch rates**, bake off vs two specialists. Don’t religiously insist on one giant model.

### 8.3 Multimodal fusion (video/image + series)

Order of design, spoken:

1. **Time alignment** — sensors and frames must share a clock; otherwise fusion is leakage.
2. **Per-modality encoders** — don’t force lidar/radar through a natural-image ViT.
3. **Fusion site** — early concat vs cross-attention vs LLM token fusion. You implemented **token fusion into an LLM**.
4. **Eval** — ablate “series only” vs “series + image.” If the camera doesn’t move the slice metric, don’t ship the extra encoder.

### 8.4 Eval (your differentiator)

Same discipline as the VLM harness, retargeted:

- Task suite matching the JD verbs (not only MAE/WAPE).
- Slice by sensor type and frequency band.
- Parse/schema failures tracked separately from accuracy if there’s a language head.
- Kill data mixes that help the average and hurt the hard slice (your TR-bucket story).

### 8.5 Numbers you may say (don’t mix campaigns)

| Item | Number |
|------|--------|
| Current VLM scales | Qwen3.5 **9B / 27B** |
| Earlier TSExam (0.8B / 8B) | **0.890 / 0.901** |
| Caption attr-recovery | **0.72** macro |
| ImagenTime | **+58%** short / **+132%** long generative vs TS diffusion baselines |
| Irregular TS | ~**70%** discriminative gain, ~**85%** compute reduction (if asked) |
| Data-scarce | **+55%** with 5% data |

Refresh 9B/27B live numbers from the Apple 3C file if you cite current-run TSExam.

---

## 9. If they ask “any concerns / fit gaps?”

> The JD’s core — TSFMs beyond forecasting, frequency-aware representations, and image/video as context — is where I’ve been deepest. The learning curve I’d expect is Bosch’s specific sensor stacks and the transfer path into ADAS or I4.0 products. That’s a reason I want the role, not a reason to hesitate.

---

## 10. Close

> I’m very interested in this team and problem. I’d love to continue with the technical loop. Happy to send a short research summary if that’s useful.

After the call: write `YYYY-MM-DD_hm-screen-debrief.md` (her questions, hybrid signal, next step) and update [`README.md`](README.md).
