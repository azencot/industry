# Talk — multimodal time-series VLMs

**Working deck:** [`bosch-30min.html`](bosch-30min.html) — synced to the spoken map (2026-08-19). Open in a browser. **← →** or click · **L** speaker notes · **B** backup slides (hidden by default; **23** spoken + **2** panel). Facts still win if a number drifts.

| | |
|---|---|
| **Now** | Bosch RTC-NA — **one 1h technical**: **25 min** talk + **20 min** previous-work Q&A + **15 min** coding discuss. Agenda: [`../../GenAI/interviews/bosch-rtc-tsfm/2026-08-20_technical-agenda.md`](../../GenAI/interviews/bosch-rtc-tsfm/2026-08-20_technical-agenda.md). **Hard stop on slide 23.** |
| **Later** | Israeli AI community, Seattle area — **2026-09-07**. Same spine; extra lineage / results / open problems. Do **not** fork a second deck until Bosch is locked. |
| **Facts** | [`.cursor/skills/debrief/vlm_multimodal_project.md`](../../.cursor/skills/debrief/vlm_multimodal_project.md) |
| **Bosch fit** | [`../../GenAI/interviews/bosch-rtc-tsfm/2026-08-13_hm-screen-debrief.md`](../../GenAI/interviews/bosch-rtc-tsfm/2026-08-13_hm-screen-debrief.md) |

## Frame (lock)

**This is a multimodal *reasoning* talk.** Say it in *your* terms (questions about a series, captions, exam-style answers, two visual views). Do **not** recast the JD on a title slide. They will map it to their sensor+vision charter themselves.

**Four contributions (the spine after problem + related work):**

| # | Contribution | What to say |
|---|--------------|-------------|
| **1 Data** | Open repos as substrate (TSExam, ChatTS, CaTS). **Improve TSExam / ChatTS** — synthetic captions and added patterns. **CaTS used as-is** (helped the mix, not the only driver) | Not “I downloaded three datasets.” Not “I rewrote CaTS.” |
| **2 Arch** | **Dual tower**: chart + delay embedding into one LLM | Complementary views, not a bigger ViT on one plot. **N series → N markers → N dual views** (don’t flatten channels). |
| **3 Train** | LLaVA-inspired, **own three-stage recipe** | **A** perception: what a time series is and its components · **B** reasoning: QA + **reasoning traces** · **C** post-adaptation (**in progress**): encourage good answers, discourage bad ones |
| **4 Results** | Same **official protocol** on each of TSExam, ChatTS, TSRBench: **SOTA or on par**; **first** to show that triple | TSRBench is where **proprietary** still wins. **Quote 8B** for TSExam (**0.926**) / TSRBench (**~45.6%**); **27B** for ChatTS cat. Don’t lead with 9B/27B as better on the north star. LLaTiSA reports **HiTSR**, not these three. Numbers: facts file (`grpo` §21–28). |

| | |
|---|---|
| **Bosch** | Don’t parrot detect/classify/describe/fuse. Don’t replay the HM screen. Transfer is **method**, not a 6-month program: if a sensor admits an image (chart, delay, STFT), it enters this VLM. Serve is backup. Panel slides 24–25 if they ask one-model / camera. |
| **HM questions (Shabnam)** | **Do not address them as her questions** on the 25-min path. If they ask in the 20-min Q&A: **24** one backbone ≠ one renderer; **25** scene camera is a third stream. Don’t name her. |
| **Related work (main)** | TS / multimodal **reasoning** interfaces: (1) series as **text tokens** ([Time-MQA](https://arxiv.org/abs/2503.01875)); (2) **native TS encoder** into an LLM ([ChatTS](https://arxiv.org/abs/2412.03104), [OpenTSLM](https://arxiv.org/abs/2510.02410)); (3) **chart VLMs** — including **dual-view plot+table** ([LLaTiSA](https://arxiv.org/abs/2604.17295)), still one VLM. **This work:** two *geometries* (chart ViT + delay DINOv3). Lit: [`../lit-search.md`](../lit-search.md). Do **not** mention forecast FMs. |

## How this is built

1. Spoken map (locked).
2. HTML matches this map; copy/numbers from the facts file.
3. **Sep 7 extend** without densifying the Bosch 25-min path.

## Senior bar (Bosch)

**~1 slide per minute** · **23 spoken slides** + **2 panel**.

Not: paper tour, student/lab-PI, FinTech analogies, claiming Haifa papers shipped, **replaying the HM Q&A on slides**, **any forecast-head framing**.

Shabnam’s bar: **BU transfer**. Results prove the stack; the last transfer slide is how the idea moves — if a sensor admits an image, it enters this VLM. One-model and camera wait for the panel (24–25).

**Do not use their verb list on the problem slides.** Reciting “classify, describe, fuse” reads as you read the posting. Let MCQ / caption / QA + dual vision do the mapping.

**Stage C:** on the spoken path as *in progress* — idea + status, not a finished RL paper. Don’t lead with it; don’t hide it.

## Spoken map (Bosch **25 min** · ~1 min / slide · 23 slides already fit)

| # | Beat | Slide | Job |
|---|------|-------|-----|
| 1 | Open | Title | VLM **reasoning** over series — not a CV dump. IC identity is **spoken**, not a slide. |
| 2 | Problem | What I mean by reasoning | A model that can **see** a series and **answer** about it — describe, compare, explain |
| 3 | Problem | What I actually eval | TSExam · ChatTS · TSRBench — one authentic question each. Not captions as a third column. |
| 4 | Related | How people do TS *reasoning* | Three families: **text-LLM** · **native TS-MLLM** · **chart VLM** (incl. plot+table dual-view). **This work:** two geometries, two towers |
| 5 | Related | Series as text tokens | [Time-MQA](https://arxiv.org/abs/2503.01875) dumps digits in the prompt. Dive: [OpenTSLM](https://arxiv.org/abs/2510.02410) **Fig 17–18** — extra tokens in the LLM explode with N and L (SoftPrompt). Digit text is worse: 12-lead 10s ECG → **80k tokens**, **>100 GB**, OOM; models repeat/count; GPT-4o **2.95** F1 as text vs **10.83** as plot. Do **not** sell Flamingo on this slide. |
| 6 | Related | Patch, encode, feed the LLM | [ChatTS](https://arxiv.org/abs/2412.03104) / [OpenTSLM](https://arxiv.org/abs/2510.02410): windows → encoder → extra tokens. Respect it (beats digits; many people use this). Tax: you **leave the VLM stack** — no pretrained ViT, no VLM instruction-tuning, next backbone drop is not a free upgrade. Still one 1D geometry. Do **not** unpack LLaTiSA here (slide 4 board 3; if they push, slide 12). |
| 7 | Spine | Four contributions | 2×2, **challenge first**: Data = toy / domain-locked / scarce · Arch = two views × N channels · Train = what, how long, when to stop · Results = beat them on their official benches. No numbers. Close still repeats the four contributions. |
| 8 | Data | Substrate: what’s in the repos | Stacked. **TSExam:** 11 base objects, 3 compositions, length 128, optional lagged/Granger pair. **ChatTS:** 4/7/3/19 attribute pool + 567 metrics → exact series; UTS + MTS-shape/local + Evol-Instruct Q&amp;A. **CaTS:** 11 real domains, triplet = numeric crop + metadata + plot, ~16k captions. Ignore benches. CaTS = use. |
| 9 | Data | Captions (shipped) | TSEXAMPP: gold by construction. One example. Attributes from the generator, no LLM labeler. The caption is the gold answer. |
| 10 | Data | Reasoning (ongoing) | Lagged pair (injection contract) + **segment order** (tid 210: concat trend → sine → flat). Gold answer and gold trace. Don’t unpack Stage C or quote TSRBench scores. |
| 11 | Arch | Dual tower | Paper figure matched to `grpo`: matplotlib chart → frozen Qwen ViT+merger (image, **≤114 cap**) · delay embed 256² → DINOv3+merger (video t=1, **64 tok**). Each `<ts>` = chart span then delay span, interleaved in the question. **N series = N dual views.** No M-RoPE type-ids (Q35-only). |
| 12 | Arch | Why two views | Stacked 8B ablations, all left–right bars. (1) ChatTS num: delay **0.35** / chart **0.71** / dual **0.79**. (2) Anom delay **0.82** vs chart **0.56**; noise chart **0.96** vs delay **0.76**. (3) Same delay images: qwendelay **0.601** vs DINOv3 **0.831**. Don’t mix 32B 0.17. Dual-beats-32B (0.886 vs 0.849) is a spare sentence. |
| 13 | Arch | What I implemented | One picture: **N series = N markers = N dual views** vs `.ravel()` gluing channels in time (fake univariate, garbage delay). Caught in the collator. Not towers/DDP laundry. |
| 14 | Train | Own recipe, LLaVA as ancestor | Three columns from `grpo` YAMLs: **A** gold captions + ChatTS align + CaTS, delay-tower LoRA, LLM frozen · **B** exam MCQ / ChatTS QA / numeric; traces on the exam mix (0.926), caption holdout on the TSRBench mix (45.6%) · **C** gold TR traces, 9B, not the 8B three-bench. 61.8% and GRPO stay on 15/17. |
| 15 | Train | Stage A — perception | Freeze diagram + **61.8%** stall. Captions (gold / ChatTS align / CaTS), delay-tower LoRA, LLM frozen. Don’t quote 0.926 or caption 0.72. |
| 16 | Train | Stage B — reasoning | Freeze invert of 15: LLM LoRA always; **8B generalist freezes vision**, 9B/27B also LoRA DINO. Questions (exam / ChatTS / numeric). Traces on the exam mix only. Don’t quote 0.926. ICL-UCR backup. |
| 17 | Train | Stage C — post-adaptation | Letter GRPO no-op (zero group-std). Format GRPO −11 pp. Gold TR traces first, then boxing. 9B in progress. Not the 8B three-bench. Don’t quote 0.9316 as the headline. |
| 18 | Results | Three benchmarks | **Our 8B** TSExam **0.926** vs paper GPT-4o **0.87** / Gemini **0.76** / MiniCPM **0.55** (plots, round 0, weighted). **Our 27B** ChatTS cat **0.92 / 0.90** vs ChatTS-14B **0.89 / 0.86** and GPT-4o vision **0.61 / 0.47** (Table 3). TSRBench: GPT-5 **55.6** · Our 8B **45.6** · Qwen3-VL-32B **44.9** · TimeOmni-7B **36.7**. Don’t claim a GPT-4o re-run. Don’t quote TimeOmni 49.4. |
| 19 | Results | TSRBench groups | Perception **0.87** · prediction **0.50** · decision **0.37** · reasoning **0.29**. Closed gap is the hard slice, not perception. |
| 20 | Results | How I know it isn’t fake | Kill a mix that helped the average and hurt TR: avg **29.5→31.2**, AR/IR **+7**, TR **26.9→21.9**. Missing primitives, not more buckets. Not the 0.27 on 19. |
| 21 | Results | Scale | 0.8B to choose; **8B still TSExam/TSRBench ceiling**; 27B wins ChatTS; 9B/27B TSRBench **~0.41–0.43**. Don’t mix unlabeled. Don’t slide 122B. Drop if slow. |
| 22 | Transfer | Image renderers | If a sensor admits an image, the VLM stack transfers. Chart + delay here; **STFT** on a mic/shaker. Not a 6-month plan. Don’t claim a Bosch run. |
| 23 | Close | Four takeaways = four contributions | Data · one reasoner, **more views if they pay** · see-then-reason(-then-adapt) · three benches, then an image. No new numbers. |
| 24 | Panel | One model? | Shared backbone, **different renderers**. Not one patch. Don’t upsample. Don’t claim STFT is already in this VLM. |
| 25 | Panel | Scene camera? | Picture of the **room**, not another plot of the signal. Add when sensor-only is wrong (crack, in-band vibration). Leave off when the frame is the label (warning light). Train both; keep the cheaper if they match. |

**23 spoken + 2 panel.** Bosch: **hard stop on 23** (25 min). If the room is slow, drop 21. If it runs fast, do **not** promote backups — leave the 20 min for previous-work Q&A. Sep 7 can go longer.

**Takeaways (draft):** (1) Open data is not enough — synthetic captions and patterns are the work. (2) One reasoner — more views if they pay; another geometry is another tower, not another model. (3) Perception, then reasoning traces, then (in progress) preference. (4) One stack, three official benches — then if it admits an image, the stack transfers.

Backup (Q&A / technical hour): full numbers table; **serve the trained model** (vLLM 9B 100/100 — the server, not “vision LLM”); **one backbone vs two specialists**; **don’t upsample mixed rates**; LDDBM vs VLM; irregular sampling; Stage C mechanics; parse-miss; multivariate format (`ts1`/`ts2` vs ChatTS `[C,T]`; ChatTS eval fallback to one stacked chart on marker mismatch).
