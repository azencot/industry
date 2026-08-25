# Debrief — 2026-08-24 — Bosch coding take-home (in progress)

**Type:** Take-home implementation in their Lightning–Hydra–uv template (not a live code drill)  
**When:** Mon 2026-08-24 afternoon–evening PT (into Tue AM notes)  
**Loop:** [`README.md`](README.md) · agenda [`2026-08-20_technical-agenda.md`](2026-08-20_technical-agenda.md)  
**Working copy (not in `industry`):** `~/bosch-rtc-coding/lightning-hydra-uv-template`  
**Checklist:** [`code_assignment/TODO.md`](code_assignment/TODO.md)  
**Interview:** **Thu 2026-08-27, 10:00–11:00 AM PT** — 15 min coding walkthrough at the end of the hour

---

## What shipped

Data + model + short FT are in. Generation eval is **started in the LightningModule but not finished** (`test_step` calls `_generate_and_score`, method not defined yet).

| Piece | Where |
|-------|--------|
| `TINYSDataModule` | download-if-missing, nonempty **lines**, contiguous 80/10/10, SmolLM tokenizer, pad=`eos`, labels `-100` |
| `SmolLMLitModule` | `from_pretrained` in `setup`, `_shared_step` NLL+PPL, AdamW, no extra CE, no `net` |
| Configs | `data/tinyshakespeare.yaml`, `model/smollm.yaml`, `experiment/smollm_tinys.yaml` |
| Train | `uv run src/train.py experiment=smollm_tinys` |

**Do not push** the assignment `origin` (Ivan’s GitHub). Zip that folder later, exclude `data/`, `.venv`, `logs/` (~1.6GB ckpts).

Assignment commits (local): `212c29b` datamodule → `5bf69f8` tokenize → `78186e0` module+YAMLs → `34f5740` experiment. `main` is 4 ahead of their template origin.

---

## Numbers (quote these)

Smoke (pretrained, one train batch): **~5.74 NLL / PPL ~310**.

From ckpt `ModelCheckpoint.best_model_score` (`val/loss`, 8 val batches — noisy):

| Run | Steps | `val/loss` | PPL ≈ e^NLL |
|-----|-------|------------|-------------|
| `logs/train/runs/2026-08-24_18-33-05` | 100 | **4.52** | **~92** |
| `logs/train/runs/2026-08-24_18-37-18` | 500 | **4.23** | **~69** |

Use the **500-step** ckpt for FT eval:  
`logs/train/runs/2026-08-24_18-37-18/checkpoints/epoch_000.ckpt`

Most of the drop is 0→100 steps (domain shift). 100→500 is smaller. **No LoRA** — 135M already fits; PDF asked for a few steps.

---

## What went well

- Isolated the template **outside** Google Drive / `industry` so the zip has a clean `.git`.
- Deleted leftover local branch `feat/aniruddha-interview` **without opening it** (prior candidate solution in the zip they sent).
- Native ARM `uv` (`~/.local/bin`); Intel Homebrew `uv` was resolving `macosx_x86_64` and could not install torch 2.6.
- Kept MNIST; **added** Shakespeare/SmolLM. Hydra experiment overrides instead of rewriting `train.yaml`.
- Causal LM wiring is correct: tokenizer = model name; HF `out.loss`; pad ignored via `-100`.

---

## What broke / corrections

| Issue | Fix / say in 15 min |
|-------|---------------------|
| Intel `uv` + x86 `.venv` | ARM `uv`; delete x86 venv; `uv python install 3.12` arm64 |
| `(base)` Anaconda is x86 | `conda deactivate` for this project |
| Pre-commit stash | Stage a **clean** file (`git add` with nothing unstaged); hook auto-fix + leftover hunk = rollback |
| `ruff check file.yaml` | Ruff is Python-only; YAML = `check-yaml` hook |
| `torch.optim.lr_scheduler \| None` | That’s a **module**; use `LRScheduler \| None` |
| `max_steps` + EarlyStopping `val/loss` | Val is epoch-end by default; 100 steps never finish an epoch. `val_check_interval`; `early_stopping: null` |
| No CSV logger | Metrics not in `train.log`; numbers live on the ckpt |
| `compile:` in YAML | `torch.compile`, left **false** — not “build from nn.Linear” |
| PPL vs NLL | Same story (\(e^{\mathrm{NLL}}\)); generation metric is the extra one they asked for |

---

## 15-min walkthrough spine

1. Template MNIST stays; experiment `smollm_tinys` swaps data/model/trainer/callbacks.  
2. Line split (contiguous) so no speech leaks into test; verse lines are short (~40 chars) — packing is “with more time.”  
3. `training_step` = `self.model(**batch)`; labels already in the collator.  
4. Table: pretrained ~5.7 NLL vs 100-step 4.5 vs 500-step 4.2.  
5. Then generation (once `_generate_and_score` lands): greedy half-line continuation, ROUGE-L as a **noisy** literary proxy; 2–3 printed samples.  
6. More time: pack lines, CSV logger, MPS, LoRA if memory, better decoding.

Do **not** recap Apple Watch / RelCon. Reloc still in-play. Don’t fight the title.

---

## Still open (after Apple Tue)

1. Finish `_generate_and_score` in `smollm_module.py` (currently **called but missing** — will crash test/eval).  
2. `uv run src/eval.py data=tinyshakespeare model=smollm ckpt_path=... trainer.limit_test_batches=8`  
3. Pretrained vs FT table + a few samples (text file OK; no weights).  
4. `ASSIGNMENT.md` / README how-to; `pytest` still green; zip without logs/data/venv.  
5. Commit eval from **Terminal** in the assignment repo (no Cursor trailers).

Apple Health tech screen is **Tue 2026-08-25 1:35–2:20 PM PDT** — that is first. Bosch coding polish is after that call.

---

## Hand-off prompt

```
@GenAI/interviews/bosch-rtc-tsfm/2026-08-24_take-home-debrief.md
@GenAI/interviews/bosch-rtc-tsfm/code_assignment/TODO.md
Bosch take-home: data+FT done at ~/bosch-rtc-coding/lightning-hydra-uv-template. 500-step val/loss 4.23. Next: implement missing _generate_and_score, eval.py CLI, pretrained vs FT table. Do not push assignment origin. Do not zip ckpts. Apple Feng is Tue 8/25 first; Bosch walkthrough Thu 8/27.
```
