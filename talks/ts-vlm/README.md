# Talk — multimodal time-series VLMs

**Working deck:** [`bosch-30min.html`](bosch-30min.html) — synced to the spoken map (2026-08-19). Open in a browser. **← →** or click · **L** speaker notes · **B** backup slides (hidden by default; **24** spoken). Facts still win if a number drifts.

| | |
|---|---|
| **Now** | Bosch RTC-NA — **one 1h technical**: 30-min talk + panel Q&A + take-home discussion. Invite: [`../../GenAI/interviews/bosch-rtc-tsfm/2026-08-19_next-round-invite.md`](../../GenAI/interviews/bosch-rtc-tsfm/2026-08-19_next-round-invite.md) |
| **Later** | Israeli AI community, Seattle area — **2026-09-07**. Same spine; extra lineage / results / open problems. Do **not** fork a second deck until Bosch is locked. |
| **Facts** | [`.cursor/skills/debrief/vlm_multimodal_project.md`](../../.cursor/skills/debrief/vlm_multimodal_project.md) |
| **Bosch fit** | [`../../GenAI/interviews/bosch-rtc-tsfm/2026-08-13_hm-screen-debrief.md`](../../GenAI/interviews/bosch-rtc-tsfm/2026-08-13_hm-screen-debrief.md) |

## Frame (lock)

**This is a multimodal *reasoning* talk.** Say it in *your* terms (questions about a series, captions, exam-style answers, two visual views). Do **not** recast the JD on a title slide. They will map it to their sensor+vision charter themselves.

**Four contributions (the spine after problem + related work):**

| # | Contribution | What to say |
|---|--------------|-------------|
| **1 Data** | Open repos as substrate (TSExam, ChatTS, CaTS) — the work is **improving** them, especially **synthetic** captions and **added patterns** | Not “I downloaded three datasets.” |
| **2 Arch** | **Dual tower**: chart + delay embedding into one LLM | Complementary views, not a bigger ViT on one plot. **N series → N markers → N dual views** (don’t flatten channels). |
| **3 Train** | LLaVA-inspired, **own three-stage recipe** | **A** perception: what a time series is and its components · **B** reasoning: QA + **reasoning traces** · **C** post-adaptation (**in progress**): encourage good answers, discourage bad ones |
| **4 Results** | Same **official protocol** on each of TSExam, ChatTS, TSRBench: **SOTA or on par**; **first** to show that triple | TSRBench is where **proprietary** still wins. **Quote 8B** for TSExam (**0.926**) / TSRBench (**~45.6%**); **27B** for ChatTS cat. Don’t lead with 9B/27B as better on the north star. LLaTiSA reports **HiTSR**, not these three. Numbers: facts file (`grpo` §21–28). |

| | |
|---|---|
| **Bosch** | Don’t parrot detect/classify/describe/fuse. Don’t replay the HM screen. Transfer slides are *your* 6-month plan, in your language. |
| **HM questions (Shabnam)** | **Do not address them as her questions** on the spoken path. Substance lives in the dual tower. If they ask by name, that’s **panel Q&A after the talk** (and maybe the only technical, if the next hold is one hour). Explicit “one model / mixed rates” stays **backup**. |
| **Related work (main)** | TS / multimodal **reasoning** interfaces: (1) series as **text tokens** ([Time-MQA](https://arxiv.org/abs/2503.01875)); (2) **native TS encoder** into an LLM ([ChatTS](https://arxiv.org/abs/2412.03104), [OpenTSLM](https://arxiv.org/abs/2510.02410)); (3) **chart VLMs** — including **dual-view plot+table** ([LLaTiSA](https://arxiv.org/abs/2604.17295)), still one VLM. **This work:** two *geometries* (chart ViT + delay DINOv3). Lit: [`../lit-search.md`](../lit-search.md). Do **not** mention forecast FMs. |

## How this is built

1. Spoken map (locked).
2. HTML matches this map; copy/numbers from the facts file.
3. **Sep 7 extend** without densifying the 30-min path.

## Senior bar (Bosch)

**~1 slide per minute** · **24 spoken slides**.

Not: paper tour, student/lab-PI, FinTech analogies, claiming Haifa papers shipped, **replaying the HM Q&A on slides**, **any forecast-head framing**.

Shabnam’s bar: **BU transfer**. Results prove the stack; last three slides are what you’d do next.

**Do not use their verb list on the problem slides.** Reciting “classify, describe, fuse” reads as you read the posting. Let MCQ / caption / QA + dual vision do the mapping.

**Stage C:** on the spoken path as *in progress* — idea + status, not a finished RL paper. Don’t lead with it; don’t hide it.

## Spoken map (30 min · ~1 min / slide)

| # | Beat | Slide | Job |
|---|------|-------|-----|
| 1 | Open | Title | VLM **reasoning** over series — not a CV dump. IC identity is **spoken**, not a slide. |
| 2 | Problem | What I mean by reasoning | A model that can **see** a series and **answer** about it — describe, compare, explain |
| 3 | Problem | What I actually eval | TSExam · ChatTS · TSRBench — one authentic question each. Not captions as a third column. |
| 4 | Related | How people do TS *reasoning* | Three families: **text-LLM** · **native TS-MLLM** · **chart VLM** (incl. plot+table dual-view). **This work:** two geometries, two towers |
| 5 | Related | Series as text tokens | [Time-MQA](https://arxiv.org/abs/2503.01875): QA over numbers + text context |
| 6 | Related | Native TS into the LLM | [ChatTS](https://arxiv.org/abs/2412.03104) patch-MLP; [OpenTSLM](https://arxiv.org/abs/2510.02410) SoftPrompt/Flamingo. One series encoder. If they push “two views already exist”: [LLaTiSA](https://arxiv.org/abs/2604.17295) is plot+**table**, one VLM — not delay DINOv3 |
| 7 | Spine | Four contributions | Data · dual tower · three-stage recipe · three-benchmark results |
| 8 | Data | Substrate: open repos | TSExam, ChatTS, CaTS — starting point, not the contribution |
| 9 | Data | What I changed | Synthetic **captions**, **added patterns**, other hardening of those repos |
| 10 | Arch | Dual tower | **One** reasoner, **two** views — not two models, not one plot |
| 11 | Arch | Why two views | Delay **throws away amplitude** (ChatTS num collapses); chart keeps axes. Native ViT **cannot** learn delay. Complementary categories. They will hear high vs low frequency without a FAQ slide. |
| 12 | Arch | What I implemented | Towers, collator, merge, DDP — *I* verbs. Multivariate: **N series = N markers = N dual views**. Student ChatTS stored `[C, T]`; TSExam used `ts1`/`ts2`. Mixing them + `.ravel()` **concatenated channels in time** — one fake univariate. Caught in the collator, not a bigger model. |
| 13 | Train | Own recipe, LLaVA as ancestor | Three stages. Not “we followed LLaVA.” |
| 14 | Train | Stage A — perception | Teach *what a time series is* and its **components** (LLM frozen) |
| 15 | Train | Stage B — reasoning | QA + **reasoning traces** — how to answer about a series |
| 16 | Train | Stage C — post-adaptation | In progress: upweight good responses, downweight bad ones |
| 17 | Results | Three benchmarks | TSExam · ChatTS · TSRBench — first to be at/near SOTA on **all three** official protocols |
| 18 | Results | TSRBench vs proprietary | Open model; second to giant closed systems; still headroom |
| 19 | Results | How I know it isn’t fake | Kill a mix that helped the average and hurt the hard **reasoning** slice; missing primitives, not more buckets |
| 20 | Results | Scale | 0.8B to choose; **8B still TSExam/TSRBench ceiling**; 27B wins ChatTS; don’t mix unlabeled |
| 21 | Transfer | 6-month bakeoff | One frozen **reasoning** task suite on their sensors, then scale — not a giant pretrain |
| 22 | Transfer | Extra vision is a hypothesis | Ablate the camera on that suite |
| 23 | Transfer | Success is use, not a paper | vLLM 9B dual **parity gate** — a unit can run it. Don’t quote her “business impact” line. Don’t slide 122B. |
| 24 | Close | Four takeaways = four contributions | Data · dual tower · see-then-reason(-then-adapt) · three-bench results + transfer |

**24 slides.** IC identity is a 10s spoken line on the title, not a slide. If the room is slow, drop 20 or merge 22–23. If it runs fast, parse-miss is the only backup worth promoting.

**Takeaways (draft):** (1) Open data is not enough — synthetic captions and patterns are the work. (2) One reasoner, two views — different geometries, not two models. (3) Perception, then reasoning traces, then (in progress) preference. (4) One stack, three benchmarks, open weights vs giant proprietary — then transfer to sensors.

Backup (Q&A / technical hour): full numbers table; **one backbone vs two specialists**; **don’t upsample mixed rates**; LDDBM vs VLM; irregular sampling; Stage C mechanics; parse-miss; multivariate format (`ts1`/`ts2` vs ChatTS `[C,T]`; ChatTS eval fallback to one stacked chart on marker mismatch).
