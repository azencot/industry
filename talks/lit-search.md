# Lit search — TS reasoning VLMs (ongoing)

**Living file.** Append on each crawl; do not fork dated copies unless you need a frozen snapshot for a talk.  
**Facts (your stack):** [`.cursor/skills/debrief/vlm_multimodal_project.md`](../.cursor/skills/debrief/vlm_multimodal_project.md)  
**Spoken map:** [`ts-vlm/README.md`](ts-vlm/README.md)  
**First-pass snapshot (superseded):** [`ts-vlm/2026-08-19_lit-search-dual-tower.md`](ts-vlm/2026-08-19_lit-search-dual-tower.md)

| | |
|---|---|
| **Last crawl** | 2026-08-19 |
| **Seeds** | [Time-MQA](https://arxiv.org/abs/2503.01875) · [ChatTS](https://arxiv.org/abs/2412.03104) · [OpenTSLM](https://arxiv.org/abs/2510.02410) |
| **Method** | Semantic Scholar citation APIs (first 30 citing papers each) + arXiv HTML on the high-overlap hits + web search for delay/DINOv3/dual-ViT. S2 rate-limits; citation lists are **not** complete. |
| **Your recipe** | Line chart → frozen Qwen ViT; delay-embedding image → DINOv3 + merger; fuse into LLM. Data: improve TSExam / ChatTS / CaTS (synthetic captions, added patterns). Train: A perception → B QA+traces → C preference (WIP). Eval: TSExam, ChatTS, TSRBench. |

---

## Correction vs the first pass

The 2026-08-19 dual-tower note was **right about the three seeds** (none is chart + delay dual ViT) and **too strong on the field**.

Citing ChatTS / Time-MQA / OpenTSLM in 2026 is a **busy** TS-reasoning neighborhood (native TS-MLLMs, agentic tools, VLMs, routers, new benches). Searching only “delay embedding + DINOv3” made the field look empty. Searching **who cites those three** does not.

**Closest published dual-view VLM (missed on first pass):** [LLaTiSA](https://arxiv.org/abs/2604.17295) (ACL’26 Findings, arXiv Apr 2026). Cites ChatTS and Time-MQA. **Two images into one Qwen3-VL:** line plot + index–value **table** image; **three-stage curriculum SFT** (difficulty L1→L2→L3), not two specialized ViTs and not delay embeddings.

Honest talk line:

> Native TS-MLLMs add a series encoder. Chart VLMs add one plot. **LLaTiSA** already feeds **two pictures** (plot + numeric table) to one VLM. I run **two geometries** through **two towers** (chart ViT + delay DINOv3) into one reasoner.

Do **not** say “nobody uses two visual views.”

---

## The four contributions — overlap (this is the useful table)

| # | Your claim | Covered already? | What is still yours | Talk risk |
|---|----------------|------------------|---------------------|-----------|
| **1 Data** | Improve TSExam / ChatTS / CaTS: synthetic **captions**, **added patterns** | **High.** ChatTS *is* synthetic TS↔text (attribute generators + Evol-Instruct). Time-MQA is a 200k QA set. CaTS-Bench is Rose Yu’s caption bench. [Thoth](https://arxiv.org/abs/2603.01042) mid-trains Qwen3 on synthetic TS↔text. [CGTime](https://arxiv.org/abs/2608.05238) (Aug 2026, cites ChatTS) is **exactly** “code computes stats, LLM verbalizes” — same *idea* as your gold-feature captions. [HiTSR](https://arxiv.org/abs/2604.17295) (LLaTiSA) is 83k hierarchical QA + verified CoT. [TimeSeriesExamAgent](https://www.semanticscholar.org/paper/925f7cd748ac7ceca06b3d2948fe923cd9303688) automates TS-exam construction. | **Improving those specific repos** (captions + new pattern primitives from the TSRBench audit), not “we invented synthetic TS-text.” | Don’t open with “scarce aligned data.” ChatTS already owned that sentence. |
| **2 Arch** | Dual tower: chart ViT + delay DINOv3 → LLM | **Low for the exact recipe. Medium for “two views.”** Dual *modality* (TS encoder + LLM) is everywhere: ChatTS, OpenTSLM, ITFormer, PATRA. Dual *visual*: **LLaTiSA** = plot + **table image**, one Qwen3-VL. [TimeOmni-VL](https://arxiv.org/abs/2602.17149) = one fidelity TS-image (Bi-TSI) into a UMM. [MADI](https://arxiv.org/abs/2601.21436) = numerical patches + **one** line plot + captions, contrastive alignment. Time-VLM = one 3-channel freq image, **forecasting**. ViTs-TSAD tried line+STFT **and dropped it**. | **Delay embedding as the second geometry + a second ViT (DINOv3) + merger.** Not “two images.” Not “TS encoder + text.” | If they say “LLaTiSA already dual-view”: plot vs table is **readout precision**; delay vs chart is **dynamical topology**. Different bet. |
| **3 Train** | Own 3-stage: A perception (LLM frozen) → B QA + traces → C preference WIP | **High for staged SFT; medium for C.** LLaVA two-stage is the ancestor everyone copies. ChatTS: align then SFT. OpenTSLM: QA then CoT. **LLaTiSA: three-stage curriculum by difficulty**, CoT in the data. [PATRA](https://arxiv.org/abs/2602.23161) (ICML’26): SFT then **GRPO**. TimeOmni-1: multi-stage + **rewards**. VisAnomReasoner: SFT on **preferred reasoning traces**. CGTime uses stats as RL reward. | TS-specific **Stage A** (what a series *is* + **components**, LLM frozen, DINO LoRA). Traces in B as *your* mix. C is not a finished paper — don’t claim unique RL. | “Own three-stage recipe” will get a PATRA / LLaTiSA follow-up. Name the **content** of A (components, frozen LLM), not the integer 3. |
| **4 Results** | Same **official protocol** on each of TSExam, ChatTS, TSRBench: **SOTA or on par**; TSRBench still behind **proprietary**. **No prior paper reports that triple.** | **Holds on this crawl.** LLaTiSA trains/evals on **HiTSR** (their suite); OOD tables are BEDTime / MMTS-Bench / MCQ2 samples + ECG after extra SFT — **not** TSExam, **not** ChatTS official, **not** TSRBench. ChatTS appears as a *baseline model* on HiTSR, not as “we beat ChatTS on the ChatTS bench.” PATRA/Thoth/TimeOmni-1 each live on their own or one public suite. TSRBench paper’s own open ceiling is Qwen3-VL-32B **44.9** overall; your 8B **~45.4** official-protocol is on par and still below GPT-5 (T+V) **55.6**. | First (known) stack at/near SOTA **across those three public protocols**. Dual-view cousins that mint a new bench are not a results rebuttal. Label **8B vs 9B/27B**. | Spoken: first to show it on TSExam + ChatTS + TSRBench; TSRBench is where closed models still win. If they name LLaTiSA: architecture cousin, **different benches**. Don’t say “LLaTiSA only works on HiTSR” as a proof — they have some OOD — say **they didn’t report these three**. |

---

## Citation graph (Semantic Scholar, 2026-08-19)

First **30** citing papers per seed. Lists below are **filtered to TS-reasoning / multimodal**, not the full dump (industrial scheduling, website fingerprinting, etc. dropped).

### ChatTS ([2412.03104](https://arxiv.org/abs/2412.03104)) — ≥30 citing (API `next: 30`)

| Paper | Why it matters |
|-------|----------------|
| **[LLaTiSA](https://arxiv.org/abs/2604.17295)** | Dual-image VLM (plot + table); 3-stage curriculum. **Results: HiTSR + BEDTime/MMTS/MCQ2/ECG — not TSExam/ChatTS/TSRBench.** Architecture cousin, not a three-bench competitor. |
| **[PATRA](https://arxiv.org/abs/2602.23161)** | Dual encoder **text + TS** (not two ViTs); SFT → **GRPO**. Pattern-aware alignment. |
| **[Thoth](https://arxiv.org/abs/2603.01042)** | Mid-training Qwen3 on synthetic TS↔text. Data-overlap, not visual dual tower. |
| **[CGTime](https://arxiv.org/abs/2608.05238)** | Captions from **computed** stats, not LLM-looking-at-the-series. Same family as your gold-feature captions. |
| **[TSRouter](https://arxiv.org/abs/2607.08940)** | Routes **LLM vs VLM vs mix** per query (COLM’26). Does not train a dual tower; assumes modalities are complementary. |
| **[Tiny but Trusted / VisAnom](https://arxiv.org/abs/2605.30344)** | **One plot** → Qwen2.5-VL; anomaly intervals + traces. Chart-only VLM, traces overlap B. |
| **TimeSage-EV, TimeART, TSQAgent, ARFBench, TS-Skill, CAN-QA, CLIR-Bench** | Benches / agents on TS QA. Landscape, not your arch. |
| **TimeSeriesExamAgent** | Automated TS-exam construction — data-overlap with TSExam. |
| **Beyond Tokenization / Direct Timestep Embedding** | Native TS tokens + contrastive alignment, not vision. |
| **Grammar of the Wave** | Neuro-symbolic **VLM agents** on plots. Chart-only. |
| **Rethinking Post-Training Recipes for Multimodal Time-Series Forecasting** | Post-train for **forecasting** VLMs. Wrong task family. |
| **How Well Do Multimodal Models Reason on ECG Signals?** | Domain eval; OpenTSLM/ChatTS as context. |

### Time-MQA ([2503.01875](https://arxiv.org/abs/2503.01875)) — ≥30 citing

Heavy overlap with the ChatTS list (LLaTiSA, Thoth, TSRouter, CGTime, Tiny/Trusted, TimeSage-EV, ARFBench, …) plus:

| Paper | Why it matters |
|-------|----------------|
| **TRACE-TS** | Attribution-grounded sensor-language reasoning. Native / language, not dual visual. |
| **TimeOmni-1** (cites the suite; [2509.24803](https://arxiv.org/abs/2509.24803), ICLR’26) | Text-token TSRM; multi-stage + rewards. TSRBench Table 2 **overall 36.7%** (the **49.4** is the **EP** task, not overall). Does not beat an ~45% official-protocol 8B. |
| **ITFormer** ([2506.20093](https://arxiv.org/abs/2506.20093), ICML’25) | PatchTST + Instruct-Time Attention into **frozen** LLM. Native TS, not two ViTs. |
| **Representing Time Series as Structured Programs** | Program-like TS for LLM reasoning. |
| **FinSTaR** | Financial TS reasoning models. Domain, not dual visual. |

### OpenTSLM ([2510.02410](https://arxiv.org/abs/2510.02410)) — ~22 citing (shorter graph; more medical/wearable)

| Paper | Why it matters |
|-------|----------------|
| **[TSRBench](https://arxiv.org/abs/2601.18744)** | Evaluates OpenTSLM variants, ChatTS-14B, TimeOmni-1, TS-Reasoner. Official numbers above. |
| **AutoTSLM** | Automotive telemetry TSLM. Native TS-MLLM, domain. |
| **MILM** | Multimodal **irregular** TS + informative sampling. Not dual visual. |
| **ECG-Reasoning-Benchmark, SleepLM, How Well … ECG** | Waveform / clinical reasoning evals. |
| **TS-Haystack** | Long-context retrieval for TSLMs. |
| **Adaptive Time Series Reasoning via Segment Selection** | Segment routing, not two ViTs. |
| **Toward Reasoning-Centric Time-Series Analysis** (2025 position) | Agenda, not a method clone. |

**Not in the first 30 ChatTS cites, still load-bearing:** TimeOmni-VL (one TS-image, generation+understanding); MADI (number + plot alignment); UDE (delay patches, forecast FM); Time-VLM (3-channel one ViT, forecast).

---

## Architecture map (updated)

```
How a series becomes tokens for reasoning
├── Text tokens            Time-MQA, TimeOmni-1, Thoth, LLM dumps
├── Native TS encoder      ChatTS (patch MLP), OpenTSLM (SoftPrompt/Flamingo),
│                          ITFormer (PatchTST+ITA), PATRA (TS+text encoders), TS-Reasoner
├── One plot → one VLM     InsightMiner, VL-Time, VisAnomReasoner, OpenTSLM plot baseline,
│                          TimeOmni-VL (single TS-image), CaTS-style line plots
├── Two views, one VLM     LLaTiSA (plot + table image); MADI (numbers + one plot, not two ViTs)
└── Two geometries, two ViTs → LLM     ← this work (still no published clone in this crawl)
```

---

## Papers that cover *any* of the four (expanded, not just citers)

| Work | 1 Data | 2 Arch | 3 Train | 4 Results | One-liner |
|------|:------:|:------:|:-------:|:---------:|-----------|
| ChatTS | ● | native TS | align→SFT | own QA benches vs GPT-4o | Substrate you *improve*, not a dual tower |
| Time-MQA | ● (TSQA) | text | CPT+LoRA | MQA tasks | Text-LLM family |
| OpenTSLM | medical QA | native TS | QA→CoT | health CoT | Plot is a baseline they beat |
| **LLaTiSA** | ● HiTSR | **dual image** | **3-stage SFT** | HiTSR; OOD ≠ your three | Arch cousin. Did not post TSExam / ChatTS / TSRBench. |
| PATRA | pattern align | TS+text encoders | SFT→**GRPO** | TSQA | Stage C cousin |
| Thoth | ● synthesis | text mid-train | mid-train | understanding | Data cousin |
| TimeOmni-1 | TSR-Suite | text | multi-stage + **rewards** | TSRBench overall **36.7** (EP 49.4) | Train-recipe cousin; not ahead on official overall |
| TimeOmni-VL | TSUMM-Suite | **one** TS-image | CoT then generate | understanding+generation | Single visual mapping |
| ITFormer | EngineMT-QA | PatchTST+LLM | freeze LLM | engine QA | Native connector |
| CGTime | ● code→captions | language align | + RL on facts | caption fact-score | Stage A *labeling* cousin |
| VisAnomReasoner | traces on plots | one plot VLM | SFT on traces | anomaly F1 | Stage B traces, chart-only |
| TSRouter | — | **routing** LLM/VLM | — | TSRBench routing | Complementary modalities, not fusion |
| TSRBench | eval set | T / V / T+V | — | leaderboard | Your north star; they do **one** plot |
| MADI | captions+plots | number↔plot align | contrastive+VQ | TSUR | Dual *modality*, one plot |
| Time-VLM | — | 3-ch **one** ViT | — | **forecast** | Wrong task |
| UDE | — | delay **patches** | — | **forecast FM** | Delay without LLM/chart tower |

● = material overlap.

---

## How to talk (until the map is edited)

1. **Related-work slide:** keep text · native TS-MLLM · chart VLM. Add a half-clause: *recent dual-view is plot+table (LLaTiSA); we do chart+delay through two towers.*
2. **Data:** “open repos as substrate” is correct. Do not imply you introduced synthetic TS-text.
3. **Train:** say perception → traces → (WIP) preference. Do not brand “the three-stage recipe” as unique.
4. **Results:** first known stack at/near SOTA on **TSExam + ChatTS + TSRBench** (official protocol each). TSRBench still behind proprietary. LLaTiSA is not a counterexample — they shipped **HiTSR**, not those three. Backup table: GPT-5 (T+V) 55.6 · your 8B ~45.4 · Qwen3-VL-32B 44.9 · TimeOmni-1-7B **36.7 overall**.

---

## Open / next crawl

- [ ] Semantic Scholar page 2 (`offset=30`) for ChatTS and Time-MQA.
- [ ] Confirm LLaTiSA does **not** use a second backbone (current read: one Qwen3-VL, two images).
- [ ] Optional: one backup slide with TSRBench paper Table 2 overalls vs your official-protocol 8B (and 9B/27B when they land). 12-task JSONL is a **training gate**, not the SOTA claim.
- [ ] Search arXiv for `delay embedding` + `VLM` / `vision-language` / `DINOv3` after this date.
- [ ] Time-VLM / ImagenTime citers (forecasting graph; only if someone asks “isn’t that Time-VLM?”).
- [ ] Google Scholar “Cited by” as a second source (S2 is incomplete).

---

## Changelog

| Date | What |
|------|------|
| 2026-08-19 | First dual-tower search: no chart+delay clone; three seeds correctly classified. **Overclaimed emptiness of dual-visual.** |
| 2026-08-19 | Recrawl via **citing papers**. Living file created. **LLaTiSA** dual-view + 3-stage; PATRA GRPO; CGTime caption-from-code. Four-contribution overlap table. |
| 2026-08-19 | **Results correction:** TimeOmni 49.4 was **EP**, overall is **36.7**. SOTA claim is official protocol on TSExam, ChatTS, TSRBench separately; TSRBench still loses to proprietary. Do not treat the 12-task gate as a different bench. |
| 2026-08-19 | **Three-bench first:** no citing paper (incl. LLaTiSA) reports TSExam + ChatTS + TSRBench. LLaTiSA = HiTSR (+ other OOD), not a results clone. |
