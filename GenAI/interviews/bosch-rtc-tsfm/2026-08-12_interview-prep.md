# Prep — Bosch HM screen with Shabnam Ghaffarzadegan

**When:** **Thursday, August 13, 2026 · 3:15–3:45 PM PDT** (30 min) — **done.** Debrief: [`2026-08-13_hm-screen-debrief.md`](2026-08-13_hm-screen-debrief.md).  
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
7. **Tonight:** say **§4A** Q1, Q3, Q5, Q9, Q11 out loud once. Stop. Don’t cram §8.

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

---

## 3. Spoken scripts

### 60-second intro (practice this)

> I’m an applied ML research scientist focused on sequential and multimodal data — foundation models that go beyond forecasting. Most recently I’ve been building multimodal models that take a series, encode it two ways — a chart for trend and amplitude, a delay embedding for structure — fuse those into an LLM, and train so the model can classify, describe, and answer questions about the series, not just emit a forecast. Before that I worked on generative time series as images, including choosing STFT versus delay embeddings depending on whether the series is high-frequency periodic or long-range topological. I have a PhD from the Technion and publish in NeurIPS, ICML, and ICLR. I’m a US permanent resident, I’m currently based in Seattle, and I’m looking for a full-time IC research role where I own architecture, training, and eval. This role is a strong fit because it’s multimodal foundation models over industrial sensors — audio, vibration, telemetry — with vision as context. That’s the research line I’ve been on.

### Why Bosch / why this team (20–30s)

> I want to work on foundation models for **real sensors**, not only forecast heads on well-behaved series. Chronos-style models are the wrong abstraction when the signal is acoustics or vibration sitting next to a camera. I’ve already published with Bosch Center for AI — synthetic frequency-driven time series, a general modality-translation diffusion bridge, and graph generation for traffic scenes — and I want to do that class of work inside RTC, with product transfer. This team’s mandate is multimodal perception for physical AI, not a forecasting-only charter.

### Bosch collab pocket (15–20s if she asks “have you worked with Bosch?”)

> Yes — with Bosch Center for AI in Haifa, three papers. The closest to this role is a NeurIPS 2025 modality-translation diffusion bridge: map between arbitrary modalities in a shared latent space, which is the same problem as fusing sensors and vision. Synth-FAR is synthetic frequency-plus-autoregressive data for time-series and foundation-model pipelines. The third is score-based graph generation with rich edge attributes, including traffic scenes. Different group from Sunnyvale — I want to bring that collaboration inside RTC.

Lead with **LDDBM** for her. Synth-FAR if she hits frequency / synthetic data. Graph paper if ADAS/traffic. Don’t list coauthor org charts. Don’t claim SoundSee.

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
| Industry experience / Bosch collab? | BCAI Haifa, three papers. Lead **LDDBM** (modality translation). Don’t imply you already work on her team. Shir = intro; don’t narrate a mix-up. |
| Competing processes? | Exploring a few industry science roles. Don’t volunteer Apple unless asked. This team is high priority if the science + hybrid work. |
| Comp? | Prefer level/scope first; public base is $165–195K; happy to discuss total package later. Don’t raise RS vs Senior. |
| Management? | Looking for **IC research** impact; will guide technical direction / mentoring as needed. |
| Can you relocate? | §5. Open to discussing hybrid and relocation for the right team. |

---

## 4A. Hard probes — say these out loud (tonight)

Fit is a good match. The failure mode is **sounding like a forecasting PI who wandered in**, or **overclaiming audio/ADAS**. These are the questions that create that failure. Each answer is **20–40s**. If she isn’t asking it, don’t volunteer the whole paragraph.

**Practice set (5):** Q1 · Q3 · Q5 · Q9 · Q11. Read the rest once.

### Q1. “Your papers look like forecasting and VLMs. Why this team?”

Trap: Chronos vs LightGBM, or “I like foundation models.”

> Forecasting is one head. What I actually build is models that **classify, describe, and fuse**. The VLM stack is exam-style classification, captions, and QA over series — not a forecast-only mandate. ImagenTime is a representation bet: STFT vs delay embeddings for different frequency regimes. This team is sensor FMs plus vision for physical AI. That’s the same problem with a harder sensor stack, which is why I want it.

### Q2. “You’re not an audio / ICASSP person. How would you work with acoustics and vibration?”

Trap: fake torchaudio production or speech ASR.

> I’m not a speech scientist. I am a representation-and-eval person for sequential signals. High-frequency sensors I treat as spectrograms / STFT — hop size vs time resolution, invertibility, not averaging away transients. Low-frequency telemetry I treat as delay embeddings and long context. I would start from that split, then learn Bosch’s mics, sample rates, and domain shift — hardware and rooms change the distribution, which is the real audio problem. Learned filterbanks are on the table; I wouldn’t pretend I’ve already shipped them.

### Q3. “How would you design a multimodal sensor foundation model in the first six months?”

Trap: “pretrain a 27B on all Bosch sensors.”

> I would not start with a giant pretrain. First: clocks, sensor list, label taxonomy, and a **task suite** that matches the product verbs — event detect, classify, describe, fuse — not MAE. Second: a representation bakeoff on **one** high-frequency task — STFT vs learned patches vs delay — with a frozen eval. Third: add vision only if an ablation moves the slice. Shared backbone with **modality-specific tokenizers** is the default; two specialists if the bakeoff says so. Pretrain scale comes after the eval and the data contract are real.

### Q4. “One model or two for low- and high-frequency sensors?”

> Default: one backbone, different tokenizers and patch rates. Forcing the same patch size on audio and slow telemetry is how you destroy transients or blow up sequence length. I’d bake that off against two specialists. I don’t have a religion about one giant model.

### Q5. “Labels are scarce and the sound vocabulary is open. How do you eval?”

This is **her** public challenge. Don’t lecture; show the same discipline.

> You cannot enumerate every sound. I would not wait for a perfect ontology. Weak labels and synthetic data to get a representation, then a **held-out event set** plus an abstain / unknown bucket — the model should know when it doesn’t know. Slice metrics by sensor, environment, and frequency band. If a data mix helps the average and hurts the hard slice, I kill it. I did that on temporal-relation buckets in the VLM work. Open vocabulary is an eval-and-abstention problem, not a bigger softmax.

### Q6. “When would you *not* fuse the camera?”

> If series-only already hits the slice, or the camera isn’t time-aligned, or the extra encoder doesn’t move the metric in an ablation. Fusion is a hypothesis. I would ship the cheaper unimodal model until vision pays for itself on the task that matters.

### Q7. “You have a diffusion modality-translation paper and a VLM. Which would you use here?”

> Different jobs. **LDDBM** is: map modality A to modality B in a shared latent space when you need translation or virtual sensing — audio to another signal, for example. The **VLM** is: language and image context, classification, description, instruction following. For Bosch I would not pick one ideology. Event detection on vibration might want a native encoder plus a small head. Description and fusion with video might want a VLM. Translation between sensors might want a bridge. Bake off by task.

### Q8. “Synthetic data is in our preferred quals. When does it hurt?”

> When it’s too clean or too simple — the model learns the generator, not the sensor. In the VLM work, synthetic captions that were too basic didn’t transfer to hard reasoning; I had to change the data, not stack more mixes. Synth-FAR is the other side: frequency-aware synthetics to cover regimes real data misses. I’d always keep a real held-out sensor set as the gate. Synthetic is a pretrain/augment tool, not the north star.

### Q9. “On the Bosch papers — what did *you* do?”

Trap: “we published with Dotan.” She will hear PI.

> I was the academic PI and a technical collaborator, not a Bosch FTE. On the modality-translation paper I owned the research framing — latent bridge, contrastive plus predictive losses — with Bosch scientists as coauthors. On Synth-FAR the frequency diagnosis and synthetic-generator design is the line I care about. I don’t claim I wrote every training loop. What I want now is to be the IC who owns architecture, experiments, and eval **inside** RTC, not to run a lab remotely.

If she pushes “so you didn’t implement it”: name one concrete decision you actually made. If you didn’t implement a piece, say so. Don’t inflate.

### Q10. “Will you miss running a lab? This is an IC role.”

> That’s why I’m here. I want to own models end-to-end again — architecture, data, training, gating — on sensors that have to transfer. Mentoring is fine as a side effect. I’m not looking for a people-manager seat.

### Q11. “You’re in Seattle. This is Sunnyvale hybrid.”

> I’m based in Seattle. I’m interested enough in this problem and team that I’m open to relocation. I want to understand the hybrid pattern — days on site — and then make that work. I’m not asking to be remote-first.

Don’t add “unless the pay is X.” Don’t mention Apple.

### Q12. “This posting is Research Scientist, not Senior. Are you overleveled?”

> I’m interested in **this** team’s problem. I’m happy to be mapped to the level you use. I operate as a senior IC on architecture and eval; I won’t fight the title on a first conversation.

### Q13. “Always-on audio has privacy issues. How do you think about that?”

Her public writing. Stay high-level; don’t design a product.

> Raw waveforms leaving the device is the wrong default. I’d rather work with on-device embeddings, short buffers, and explicit retention limits — and I’d treat “unknown sound” as abstain, not a cloud round-trip of everything. That’s an eval and systems constraint, not an afterthought. I’d follow Bosch’s product and legal bar; I wouldn’t freelance a privacy architecture in this call.

### Q14. “The JD mentions agentic AI. What’s your experience?”

> Weak. I’ve built training and eval loops, not multi-agent products. If the team means tool-using models around labeling or experiment automation, I can learn that. I wouldn’t claim an agents portfolio.

### Q15. “Tell me a result that didn’t work.”

> On the VLM stack I added data mixes aimed at temporal-relation reasoning. The average looked fine; the hard TR slice dropped. I had set the floor before training, so I killed the mix and went back to data generation instead of stacking more buckets. The lesson: slice metrics gate the work, not the headline number.

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
| Overclaiming you already work on Shabnam’s team | BCAI Haifa collab is real; RTC-NA is the move you want |
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
