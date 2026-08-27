# Debrief — 2026-08-26 — Bosch coding take-home submitted

**Type:** Take-home close-out (not a live drill)  
**When:** Wed 2026-08-26 midday PT  
**Loop:** [`README.md`](README.md) · interview **Thu 2026-08-27, 10:00–11:00 AM PT**  
**Working copy (not in `industry`):** `~/bosch-rtc-coding/lightning-hydra-uv-template`  
**Earlier WIP:** [`2026-08-24_take-home-debrief.md`](2026-08-24_take-home-debrief.md)

---

## Outcome

Zip emailed (or ready to email) from `~/bosch-rtc-coding/omri-azencot-bosch-coding.zip` (~6.1MB). Includes `.git/`; excludes `.venv`, `data/`, `logs/` / `.ckpt`. **Do not `git push`** assignment `origin` (Ivan Batalov’s GitHub).

`train.py` post-fit test and `eval.py` on **best** (`epoch_001.ckpt`) match bit-for-bit.

---

## Quote these (block-wise test)

| ckpt | steps (approx) | test/loss | test/ppl | ROUGE-L | BERTScore F1 |
|------|----------------|-----------|----------|---------|--------------|
| pretrained | 0 | 3.585 | 36.06 | 0.114 | 0.721 |
| **best** | **116** (`epoch_001`) | **3.366856** | **28.987** | **0.11584** | **0.72642** |
| last (165-step run) | 162 | 3.414 | 30.38 | 0.118 | 0.732 |
| last (330-step run) | 324 | 3.678 | 39.59 | 0.115 | 0.733 |

Best is **not** end of `max_steps: 165`. Both 165 and 330 runs picked **epoch 1 / global_step 116** as min `val/loss`. Extra steps **hurt** test PPL (overfit). Eval of both `epoch_001.ckpt` files was identical because `seed: 42` shares the first 116 steps.

Line-wise numbers (pretrained ~5.74 NLL / PPL ~310; 500-step val 4.23 on 8 batches) are **not** comparable — different packing.

---

## Discussion (15 min — NTP vs generation)

The experiments highlight several differences between intrinsic language-model evaluation and generation evaluation.

The clearest improvement from fine-tuning is in **held-out next-token likelihood**. The best validation checkpoint achieves substantially lower test loss and perplexity than the pretrained model, showing successful adaptation to TinyShakespeare.

At the same time, **sequence-level metrics improve only slightly**. Likely reasons:

1. The training objective optimizes next-token likelihood rather than ROUGE-L or BERTScore directly.
2. Small changes in token probabilities do not necessarily change the greedy argmax sequence.
3. Open-ended generation admits many valid continuations, while ROUGE-L and BERTScore compare the model output against only one reference continuation.
4. TinyShakespeare is very small relative to a 135M-parameter model, making overfitting likely.

The **degradation in test perplexity at step 330** supports the last point and motivates checkpoint selection based on validation performance rather than simply using the final training step.

### Possible improvements

With additional time:

- Tune learning rate and training duration using validation loss.
- Evaluate generation over a larger number of held-out prompts.
- Report a repetition or diversity metric to quantify the repetitive behavior visible in greedy generations.
- Compare greedy decoding with sampling-based decoding for qualitative analysis.
- Use multiple random seeds to quantify training variance.
- Explore stronger generation evaluation methods that are less dependent on a single reference continuation.
- To move ROUGE/BERTScore a lot on this protocol: kill greedy loops (no-repeat n-gram or sampling if collapse), and score a shorter continuation (16–32 tokens) as a diagnostic. More NTP steps will not; one ~128-token gold suffix is a hard ceiling.

The current implementation focuses on correctness, reproducibility, and a clear comparison between the pretrained and fine-tuned models.

---

## What shipped (assignment repo)

- `TINYSDataModule`: Karpathy blocks — raw text 80/10/10, encode, `block_size=256`, no pad.
- `SmolLMLitModule`: HF NTP, token-weighted PPL, greedy half-block generate, ROUGE-L + DistilBERT BERTScore on 64 rows, 4 printed samples. `setup()` loads HF **once** (do not wipe FT weights on `stage=test`).
- Hydra: `experiment=smollm_tinys`, `eval.py data=tinyshakespeare model=smollm`.
- README how-to + `results/blockwise_eval.txt` (and linewise appendix).

---

## Corrections to keep (15 min)

| Issue | Line |
|-------|------|
| `train.py` tests **best**, `eval last.ckpt` is a different point | Quote `epoch_001` vs `last` |
| `setup()` used to `from_pretrained` every time; `ckpt_path=None` → pretrained test | Guard is in; still say eval.py + named ckpt |
| Hydra `+trainer.limit_test_batches` | Key not in trainer struct |
| ROUGE-L | LCS overlap, **not** semantics; BERTScore is the semantic proxy (noisy on verse) |
| Greedy | Repeats; NTP ≠ “sounds like Shakespeare” |
| Packed collate | **No pad**; `-100` only if padded |
| HF shift | 255 NTP terms on a 256-token block |
| Pre-commit | `git add` clean, then one-line `-m`; do not ruff YAML |
| ARM `uv` | `(base)` conda is x86; do not mix |

---

## 15-min walkthrough spine

1. MNIST stays; `experiment=smollm_tinys` swaps data/model/callbacks (`val/loss`).  
2. Lines → blocks so context crosses verse; split **text** then tokenize (no leak).  
3. `training_step` = `self.model(**batch)`; labels = `input_ids`.  
4. Table: 0 → **116 best** → last 165/330 overfits.  
5. Gen: half-block greedy; ROUGE/BERTScore barely move — NTP ≠ one-reference generation (Discussion above).  
6. More time: val-tuned lr/duration, more prompts, repetition metric, sampling vs greedy, seeds, less single-reference gen eval. To move ROUGE a lot: stop greedy loops + shorter continuation; not more NTP.

No Apple Watch / RelCon. Reloc in-play. Don’t fight the title.

---

## Next session

Talk hard-stop 23 slides; then coding walkthrough with the table above. Deck: [`talks/ts-vlm/bosch-30min.html`](../../../talks/ts-vlm/bosch-30min.html).

```
@GenAI/interviews/bosch-rtc-tsfm/2026-08-26_take-home-submit.md
@talks/ts-vlm/bosch-30min.html
Bosch Thu 8/27 10:00 AM PT: 25 talk + 20 Q&A + 15 coding. Quote block-wise best @ step 116 (test PPL 28.99). last 165/330 worse. NTP moved; ROUGE/BERTScore barely. Val ckpt not last. Do not recap the zip. Do not mix Apple scripts.
```
