# Debrief — 2026-06-21 — continual pre-training blog (Day 2 start)

## Session

- **Type:** exploration (Day 2 ML/LLM depth)
- **Duration:** ~30 min read (results section skipped)
- **Prior context:** Day 1 complete — elevator pitch, anchor cheat sheet ([`elevator-pitch.md`](../elevator-pitch.md), [`anchor-cheat-sheet.md`](../anchor-cheat-sheet.md))
- **Source:** [Efficient continual pre-training LLMs for financial domains](https://aws.amazon.com/blogs/machine-learning/efficient-continual-pre-training-llms-for-financial-domains/) (Karan Aggarwal et al., Mar 2024); paper: *Efficient Continual Pre-training for Building Domain Specific Large Language Models*

---

## Blog summary (methodology — results skipped)

### Why domain continual pre-training?

General LLMs (CommonCrawl, C4, Wikipedia, ArXiv) are strong on broad tasks but weak on finance-specific knowledge and language. **BloombergGPT** used ~51% finance documents (news, filings, etc.) and beat general models on finance benchmarks — e.g., correctly naming CEOs where GPT-NeoX / FLAN-T5 hallucinated or repeated wrong names. Domain corpus matters for both **facts** and **style**.

### Data collection & preparation

Pipeline: **identify sources → domain filters → preprocessing**.

| Source | Coverage | Scale | Access |
|--------|----------|-------|--------|
| News CommonCrawl | 2016–2022 | ~25.8B words | S3 `commoncrawl/crawl-data/CC-NEWS/` |
| SEC filings (EDGAR) | 1993–2022 | ~5.1B words | EDGAR scrape or SageMaker SEC APIs |

**Financial news filtering:** simple URL + keyword rules — whitelist financial outlets *or* finance keywords in URL. Catches finance sections of general news sites, not just dedicated outlets.

**Preprocessing highlights:**

- SEC filings: drop short sentences that are table/figure artifacts after HTML/table stripping
- **Deduplication:** locality-sensitive hashing; SEC deduped at **section** level (not whole doc)
- **Throughput trick:** concatenate docs → tokenize → chunk to max sequence length (reduces padding waste, lowers training cost)

### Four ways to add domain capability

| Method | Role | Cost | Limitation |
|--------|------|------|------------|
| **Train from scratch** | Full domain model | Prohibitive ($100M+ class) | Overkill when open weights exist |
| **Continual pre-training** | Adapt open LLM on domain corpus | Middle | Needs large curated corpus; still cheaper than scratch |
| **Instruction fine-tuning** | Task behavior | Lowest of pre-training options | **Does not** inject broad domain knowledge unless dataset is huge; task interference across tasks |
| **RAG** | Ground answers in retrieved facts | Inference + index cost | Best for **grounding**; model still speaks in general-domain style — doesn't internalize finance language |

**Blog's positioning:** continual pre-training = cost-effective path to **domain knowledge + language style**, then optional instruction FT on top. Best when downstream task set is **large or unknown** and labeled instruction data is **scarce**. RAG or instruction FT alone may suffice when tasks are narrow and well-defined.

### Methodology taxonomy (paper / FinPythia)

Base model: **Pythia** suite → finance-adapted **FinPythia**.

| Acronym | What it does | When |
|---------|--------------|------|
| **DACP** (Domain-Adaptive Continual Pre-training) | Pre-train on **full** curated finance corpus | Build a general **financial foundation** model |
| **TACP** (Task-Adaptive Continual Pre-training) | Further pre-train on **unlabeled task tokens** (no labels) | Boost specific in-domain tasks; yields task-specialized models, not a broad foundation |
| **ETS-DACP** (Efficient Task-**Similar** DACP) | Subsample corpus **closest to task data** (embedding similarity) | Have target task data (even unlabeled); want efficiency |
| **ETA-DACP** (Efficient Task-**Agnostic** DACP) | Subsample by **perplexity** (novelty — what base model hasn't seen) and **token-type entropy** (diversity) | No task data; want versatile domain model cheaply |

**Efficiency claim (conceptual):** smart subset selection targets ~**10% of corpus** while aiming to match or beat full-corpus DACP — task-similar selection (ETS) best when task tokens exist; task-agnostic entropy/perplexity (ETA) close second.

**Sampling schemes:** **hard** = rank by metric, take top-k; **soft** = weight by metric, sample k points.

Eval tasks mentioned in blog (for context only): Financial Phrase Bank, FiQA SA, Headline classification, financial NER on SEC credit-risk sections — evaluated 5-shot after instruction tuning.

### AWS / team angle

- Co-authored by **Amazon FinTech applied science** + AWS financial industry specialists
- Production path: SageMaker Training, Bedrock
- Reinforces Amazon's view: finance LLMs need **curated domain corpus + efficient adaptation**, not just prompting

---

## Interview hooks (for Karan PS1)

**If asked "RAG vs fine-tuning vs continual pre-training":**

> RAG grounds responses in fresh facts but doesn't teach the model finance syntax and implicit knowledge. Instruction FT shapes behavior on labeled tasks but won't absorb broad domain knowledge from small datasets. Continual pre-training is the middle-cost path to internalize finance language and facts on an open base model; we'd still layer eval gates, RAG for compliance-critical facts, and routing to SLMs for cost.

**Connect to your VLM anchor (without over-claiming finance):**

- Same **release gating** mindset: domain adaptation only ships after task eval + regression on general capability (blog notes no adverse effect on generic benchmarks — worth asking Karan how FinTelligence validates that in production)
- **Low-label:** ETS-DACP uses **unlabeled task tokens** — parallels weak supervision / synthetic data themes in JD
- **Tiered inference:** foundation domain model (FinPythia-class) + task heads / RAG / smaller routed models

**Smart questions for Karan (pick 1–2):**

1. In production, how do you choose between ETA-DACP-style corpus selection vs RAG for a new payments doc task?
2. What eval suite gates continual pre-training before ship — finance tasks only, or general regression too?
3. How do user corrections feed back — instruction FT, data selection for next CPT round, or both?

---

## What went well / gaps

- **Well:** Started Day 2 on Karan's own work — strong PS1 signal
- **Skipped:** Results section — revisit briefly before PS1 for headline numbers (FinPythia +10% avg on 6.9B; efficient methods at 10% data)
- **Still open (Day 2):** 3-min spoken drills; RAG vs FT vs CPT comparison aloud

---

## ECG-QALM (abstract only — 2026-06-21)

- **Problem:** scarce NER labels, entity under-representation, privacy constraints on sensitive training data
- **Method:** entity-controlled synthetic text via contextual Q&A with PLMs; augment small labeled sets for downstream NER
- **Claim:** 75–140% gains in low-label regimes (full paper skipped for PS1)
- **Parallel to VLM work:** synthetic caption lane (TSExam + ChatTS, CaTS) is closer than TSExam **operator extension** — latter is benchmark coverage audit, not text generation
- **PS1 bridge:** *"ECG-QALM fills label gaps with controlled synthetic text; I audited which primitives TSRBench needs and extended TSExam ops instead of stacking training buckets."*

Full CPT paper (blog underlying work): [arxiv:2311.08545](https://arxiv.org/abs/2311.08545)

---

## Decisions / artifacts updated

- [x] This debrief → [`Amazon_FinTech/debrief/`](.)
- [x] [`INDEX.md`](../INDEX.md) debrief row
- [x] [`prep-plan.md`](../prep-plan.md) — Day 2 Karan reads
- [ ] Results skim before PS1 ([arxiv:2311.08545](https://arxiv.org/abs/2311.08545))

---

## Next session (one prompt for session B)

> @Files Amazon_FinTech/debrief/2026-06-21_continual-pretraining-blog.md Amazon_FinTech/anchor-cheat-sheet.md
> Run `/ml-deep-dive`: "Walk through RAG vs instruction fine-tuning vs continual pre-training for payment document extraction — 3 minutes, FinTech compliance lens."
