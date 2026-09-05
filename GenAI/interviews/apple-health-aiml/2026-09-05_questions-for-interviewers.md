# Questions for interviewers — Apple Health AIML on-site

**When:** Tue 2026-09-08, last 3–5 min of each slot.  
**Order:** Jonathan 11:05 → Yujie 1:05 → Chung-Cheng 2:05 → Haraldur 3:05 → Vincent 4:05 PDT.  
**Hub:** [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md)

Pick **1–2** per person. Do not dump all five. If they already answered it while grilling you, skip.

**Spoken rule:** ask about the *problem*, not their CV. Do **not** name RelCon, WBM, periodicity, AXLearn, AFM, Workout Buddy, hypertension posts, or the cycle-tracking patent. Private notes below are for you only.

**Shape:** one sentence of context from *your* work, then the question. Stop. Let them talk.

---

## How seniority is used here

| Person | Question height | Why |
|--------|-----------------|-----|
| **Jonathan** | Concrete: pipelines, eval, what is hard day-to-day | ARE / SWE; almost no public research trail |
| **Haraldur** | Concrete: labels, operating points, when simple models win | Applied IC; product-adjacent sensing. Not org strategy |
| **Yujie** | Architecture: tokens, fusion, complementary views | Senior MLE; representation / wearable-behavior FM |
| **Chung-Cheng** | Training systems: scale, modularity, on-device vs server | Principal RE; cross-org FM / trainer (not Health) |
| **Vincent** | Program: what to bet on, year-one bar, cross-functional ownership | Eng manager; last slot; strategy + leadership |

---

## 1. Jonathan — 11:05–11:50 PDT

**Seat:** Applied Research Engineer, Health AI, Seattle. Self-describes as a software engineer. Opens the day.

No public papers. Ask about current work, product interest, and the research→code path. Your hook: dual-tower collator, staged training, eval gates — you have lived the engineering of a multimodal run.

**Default picks:** 1 and 2.

### 1. Turning a second view into something that trains

> I’ve spent a lot of time on the unglamorous part of multimodal work — collating two encodings, keeping stages from leaking, and making eval match the claim. When a new representation shows up on this team, what’s been the hardest part of making it actually train and evaluate: alignment, the data path, or the eval harness?

*Private:* ARE seat. Maps to your dual-tower collator / Stage A→B merge / parse-miss ≠ accuracy. Tests whether he lives in the same stack.

### 2. What looks like modeling until you open the pipeline

> What’s a current challenge on the team that people underestimate — something that looks like a modeling problem until you get into the pipeline?

*Private:* No paper to cite. Lets him tell you what is actually on fire (missingness, device generations, labeling, serving). Junior-appropriate; high signal.

### 3. Where the product is interesting

> From your seat, what part of the health or fitness product is most interesting to work on right now — and where does adding a language or multimodal layer actually help versus get in the way?

*Private:* Product-interest question. Workout Buddy–class language-over-series is the org surface; do not name it. Hear whether he wants models that talk vs models that detect.

### 4. Notebook vs real eval

> How do you tell that a prototype is ready to leave a notebook? What does a “real” eval look like here — slices, held-out people, a kill gate — versus a metric that moved once?

*Private:* Your TR mix 26.9→21.9 is the story if he asks back. You want his bar, not to pitch.

### 5. How scientists and engineers split a new representation

> When you’re trying a new encoder or a second modality, how do research scientists and research engineers split the work? What do you wish the scientist had already decided before it hit the training stack?

*Private:* Collaboration / day-to-day. Signals whether this hire is expected to own YAML-to-eval, not only ideas.

---

## 2. Yujie — 1:05–1:50 PDT

**Seat:** Senior MLE, Seattle; health AI. Public work: wearable **behavioral** foundation model — tokenize long irregular series, bake off architectures, complementary to a raw-sensor (PPG) model. Earlier: computer vision (image–text, 3D).

Senior questions: encoding, fusion, evidence that both views are used. Do not recite 2.5B hours / 57 tasks / Mamba.

**Default picks:** 1 and 2.

### 1. What actually decided the encoding

> When you’ve compared ways of turning long, irregular wearable series into tokens, what actually decided the encoding — information you couldn’t afford to drop, sequence length, or how missingness is represented?

*Private:* WBM: TST hourly patches + missingness mask beat fancier tokenizers; architecture bakeoff was real. Your analog: chart vs delay vs dual; patch size = temporal resolution. Senior: she owns this tradeoff.

### 2. Two views help on average and fail a slice

> I’ve seen two complementary views of the same series help the average and still fail an important slice — so I don’t treat “dual > single” as proof both are used. When you fuse a slower behavioral view with a raw-sensor view, how do you check that both are actually contributing, and what would make you drop one?

*Private:* WBM + PPG is their complementarity claim. Yours: delay-only ChatTS ~0.17 vs chart ~0.71 vs dual ~0.79; shuffle/corrupt/remove. This is the highest-leverage question for her.

### 3. Clocks and token budget

> Wearables don’t share a clock — high-rate optical, hourly behavior, sparse events, occasional text. How do you choose the fusion timescale so one modality doesn’t dominate the token budget?

*Private:* Yujie sheet: physical time ≠ token index; audio-dominates-tokens injection. Her FM lives at hourly behavior, not 100 Hz PPG. Your dual tower also has a token tax.

### 4. Missingness as signal

> When is missingness something you should encode rather than impute away — and when does encoding it become a shortcut around the physiology?

*Private:* WBM concatenates missingness indicators; periodicity paper (Feng/Haraldur) showed missingness correlates with the label. She may send this to Haraldur; if she stays, go deep on representation, not PPV.

### 5. Steal a vision prior vs train a native temporal encoder

> I used visual encodings to steal a pretrained prior when the language model couldn’t see the series — not because plots are the true wearable representation. From a vision background, when would you still steal a pretrained encoder for a wearable problem, and when is a native temporal encoder the honest bias?

*Private:* Her Zillow/CV line + WBM native behavioral encoder. Matches Feng’s arch / encoder / no-data triangle and your “I would not reprint charts on PPG.” Senior: she can disagree with you productively.

---

## 3. Chung-Cheng — 2:05–2:50 PDT

**Seat:** Principal RE, Apple AI/ML (Mountain View). Cross-org, **not** Health. Public: large-scale FM training, modular hardware-agnostic trainer, Apple Intelligence FMs; earlier speech/ASR (end-to-end listen-attend-spell, spectrogram augmentation).

Senior questions: diagnosis at scale, modularity when the *input* stops being text, on-device vs server. Do not ask “do you use AXLearn.” Do not volunteer AFM.

**Default picks:** 1 and 2.

### 1. Throughput dies after a high-rate encoder

> When I add a second encoder in front of an LLM, the language model still fits and throughput still dies. When you’ve seen that, what was the actual bottleneck — token count and attention, packing that assumed text-shaped sequences, or the input pipeline stalling?

*Private:* His A7 scenario and your dual-tower / DINO tower token tax. Principal-level: he wants diagnosis, not FlashAttention as a noun. Best multimodal bridge in this hour.

### 2. Keep the trainer modular when the input changes

> I’ve had to change collators and towers without rewriting the training loop. When the input stops being language-only — variable-length sensor tokens, two towers, staged freeze/unfreeze — what’s the piece that’s hardest to keep modular: the input pipeline, sharding, or checkpointing?

*Private:* AXLearn’s pitch is modular input/ckpt/loop on heterogeneous hardware. Ask the *problem*. Honest: you run Slurm/DDP, not GSPMD on 1k chips.

### 3. Speech was already time series + language

> Speech is already a time-series encoder into a language model. What from that world still applies when the stream is a wearable instead of audio — and what breaks because wearables are sparse, missing, and not phonemes?

*Private:* LAS / SpecAugment / Conformer lineage; Health also probes speech FMs on wearables (Narain/Ren — do not name). Senior: he can talk mechanism (filterbanks, masking, encoder warmup) without a Health paper recap.

### 4. On-device vs server fusion

> On-device and server models have very different sequence and memory budgets. How does that change whether you’d fuse modalities in the backbone versus keep a small encoder and a thin language head?

*Private:* AFM-on-device ~3B vs server. Health RelCon encoder is ~4M on purpose. Your 8B dual is a research ceiling, not a Watch budget. Lets him set the constraint you should internalize.

### 5. Slow multimodal run: systems or collate?

> When a multimodal job is slow, how do you decide it’s a systems problem versus a bad packing or collation assumption — same token budget, totally different step time?

*Private:* Your 8→64 global-batch miss lives here if he flips it. Asking *his* debug order is the close already on his sheet.

---

## 4. Haraldur — 3:05–3:50 PDT

**Seat:** Senior Applied RS, Health AI, Seattle. Public: motion/sensor FMs, TS-reasoning with LLMs, multimodal mood/periodicity work; LinkedIn (do not cite) on sensor FMs contributing to Watch hypertension notifications and AirPods calorie estimation.

Keep questions **applied and concrete** — labels, robustness, operating points — not a three-year agenda.

**Default picks:** 1 and 4.

### 1. Small sensor representation vs language layer

> When is a small sensor representation enough for the decision, and when do you actually need a language layer on top of the series? What evidence would make you *not* reach for the LLM?

*Private:* RelCon ~3.9M frozen encoder vs TS-LLM (he is coauthor). Your work is the language layer. You want his kill criterion. Do not name either paper.

### 2. Perception first, then language

> I’ve been treating “learn to see the series” as a separate stage from “learn to answer.” In health series, what’s gone wrong when people skip perception and jump to an LLM — and how do you know perception is actually the bottleneck?

*Private:* TS-LLM: most models fail at perception; two-stage encoder warmup then LoRA. Same shape as your Stage A/B. Concrete, not strategic.

### 3. When the simple model is more robust

> There’s a temptation to assume a deep sequence model wins. When have simpler periodic features or tree models been more robust, and what was the missingness or shift that exposed the deep model?

*Private:* Periodicity + GBDT held up under missingness; CNN dropped. Cultural signal of this group. Do not recite Table 1. If he goes here, stay on robustness, not architecture flex.

### 4. AUROC vs a user-facing decision

> When a model has to become a user-facing decision — notify or not — what surprised you about the gap between a good discrimination number and a usable operating point?

*Private:* Hypertension notification: Se ~41%, Sp ~92%, PPV depends on prevalence; FDA-cleared screening, not a BP reading. Do **not** mention the feature or the post. This is the applied question he is qualified to answer and you need before Vincent.

### 5. Hardest problem on the sensing side right now

> What’s currently the hardest applied problem on the sensing side — the labels, naturalistic missingness, or the fact that the people you can label are not the people you deploy to?

*Private:* His advanced-sheet failure classes (label quality, selection/verification bias, decision utility). Junior-height: current work, not “set the roadmap.”

---

## 5. Vincent — 4:05–4:50 PDT

**Seat:** Eng Manager, Health AIML. Recruits multimodal LLMs / fusion / VLMs. Stats PhD. Named on a cycle-tracking/prediction patent (HR + calendar-like signals). Thanked on the TS-LLM paper. Last of five — energy; this is the program question.

Senior questions: what to bet on, what year one is, who owns the hard tradeoff. Do not name the patent or intern posting.

**Default picks:** 1 and 3.

### 1. Language/VLM layer vs better sensor representation

> How do you decide whether the next stretch of work should be a language or VLM layer on health series versus a better sensor representation? What evidence would change that bet?

*Private:* He is hiring for agentic / multimodal LLMs / VLMs. Guillermo (private, do not cite): ~1-year product, not an open FM lab. Your honest stance: perception first, bake off encoder families, don’t reprint matplotlib on PPG.

### 2. Sparse self-report + physiology + privacy

> For problems that mix sparse self-report with physiological streams and a high privacy bar, where does multimodal modeling actually earn its complexity — and where does a simpler longitudinal model win?

*Private:* Cycle tracking: logs + Watch HR → period/fertile-window predictions. Same *shape* as mood/periodicity (weak labels, missingness, population). Don’t say “your patent.” Senior: he thinks in product constraints, not RoPE.

### 3. What strong looks like in year one

> This seat sits between foundational multimodal research and something that has to ship. What does strong look like in the first year — a bakeoff on your signals, an eval harness, a model component in a feature, or something else?

*Private:* Same question you asked Shirley, now to the EM who has to live with the hire. Best close of the day. Listen; don’t negotiate.

### 4. What the research scientist owns

> When research, clinical, privacy, and product disagree on a label or an operating point, what does the research scientist own — and what do they *not* get to decide?

*Private:* L5/L6 cross-functional. IC verbs if he flips it (“what did *you* own on Bosch / dual-tower eval”). Don’t tell a PI/lab story.

### 5. Failure mode he is hiring against

> When you hire for multimodal fusion, what’s the failure mode you most want this person to avoid: overbuilding the architecture, underbuilding the eval, or ignoring which population the model has to work for?

*Private:* His intern/role posts name VLMs and multimodal sensing. Your differentiator is eval gates + killing a mix that hurt a slice. Lets him name the bar in his words.

---

## If time is almost gone (one line each)

| Person | One line |
|--------|----------|
| Jonathan | What’s currently hard that people treat as a modeling problem? |
| Yujie | How do you know a second view is used, not just extra capacity? |
| Chung-Cheng | When a high-rate encoder kills throughput, what do you profile first? |
| Haraldur | When is a small sensor model enough and the LLM is the wrong layer? |
| Vincent | What does strong look like in year one in this seat? |

---

## Do not ask

- Paper titles, venues, “I read your LinkedIn,” Watch model internals  
- Comp, competing-candidate count, “will I get to publish” as question #1  
- “Do you use AXLearn / FSDP / Mamba?”  
- Anything that forces them to confirm they are the person on a paper  
- A second why-Apple speech (already locked; only if *they* pull it)

---

## After the day

Log what you asked and what they said in [`2026-09-08_onsite-debrief.md`](2026-09-08_onsite-debrief.md) (create that night).
