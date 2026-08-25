# Bosch take-home TODO (industry copy)

Working tree: `~/bosch-rtc-coding/lightning-hydra-uv-template`  
Copy a cleaned version of this into that repo if you want a local checklist. Do **not** commit Cursor/industry paths, Apple notes, or “deleted leftover branch” into the zip.

PDF: [`Interview coding task.pdf`](Interview%20coding%20task.pdf)

---

## Verdict on the plan

The spine is right: data → model → train → eval, all **added** to the template (do not rip out MNIST). Three corrections:

1. **Do not embed in the datamodule.** Tokenize only. `input_ids` / `attention_mask` / `labels` go to the model; **SmolLM’s embedding table** maps tokens → vectors inside `forward`. “Verify the embedding fits” = use **the same tokenizer as the checkpoint** (`HuggingFaceTB/SmolLM-135M`), not a separate embedder.
2. **Do not write a new next-token loss** unless HF’s is wrong. `AutoModelForCausalLM` already does shifted CE when `labels` are passed (pad tokens set to `-100`). Training work is wiring `labels`, logging loss/PPL, and pointing Lightning at `val/loss` instead of MNIST `val/acc`.
3. **Skip 3.5 as a phase.** They said a few steps is enough. Val is for **reporting PPL** (and maybe early stop), not Optuna. Template already has `hparams_search`; using it burns the two days. One experiment YAML with a sane `lr` / `max_steps` / `block_size`. If val PPL is nonsense, change one knob, don’t sweep.

Eval is the part they grade. Train a short run so the loop is real; the write-up is pretrained vs few-step FT + one generation metric.

---

## Done

- [x] Isolated working copy outside `industry` (`~/bosch-rtc-coding/lightning-hydra-uv-template`)
- [x] Deleted leftover solution branch (`feat/aniruddha-interview`) — do not look at it
- [x] Native ARM `uv`; ARM `.venv`; `uv sync` / pre-commit / pytest / template `train.py` as required
- [x] Data: `TINYSDataModule` — download-if-missing, nonempty **lines**, contiguous 80/10/10 (not MNIST `random_split`)
- [x] Tokenize + collate: SmolLM tokenizer, `pad_token = eos_token`, labels pad → `-100`, dict batches
- [x] Smoke data: 26221 / 3277 / 3279 lines; batch `[16, 13]`
- [x] Model: `SmolLMLitModule` — `from_pretrained` in `setup`, `_shared_step`, NLL + PPL, `on_train_start` resets `val_loss`, no extra CE, no `net`
- [x] Smoke model: pretrained forward ≈ **5.74 NLL / PPL ~310** (domain shift; finite)
- [x] YAML: `configs/data/tinyshakespeare.yaml`, `configs/model/smollm.yaml`
- [x] Experiment: `configs/experiment/smollm_tinys.yaml` — `val/loss` checkpoint, `early_stopping: null`, `val_check_interval` (max_steps would skip epoch-end val)
- [x] Train: `uv run src/train.py experiment=smollm_tinys` — ckpt under `logs/train/runs/2026-08-24_18-33-05/checkpoints/` (`last.ckpt`, `epoch_000.ckpt`). **Do not zip logs.**
- [x] Local commits (do not push origin): `212c29b` datamodule · `5bf69f8` tokenize · `78186e0` SmolLM module + data/model configs · `34f5740` experiment. Eval helper **in progress** (`test_step` calls `_generate_and_score` — **method still missing**).

**Now (after Apple Tue):** implement `_generate_and_score`, `eval.py` CLI, pretrained vs FT table. Assignment `main` is 4 ahead of Ivan’s origin — do not `git push` that remote.

---

## 1. Data — TinyShakespeare DataModule

Mirror `src/data/mnist_datamodule.py`. **Add**, don’t replace.

- [x] `prepare_data`: download if missing (Karpathy raw). Cache under `data/` (gitignored)
- [x] `setup`: contiguous **line** split 80/10/10. No shuffle across the cut
- [ ] Pack consecutive lines to ~256 chars (deferred; verse lines are short — optional)
- [x] Tokenize with `AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM-135M")`
- [x] Collate: pad, `labels = input_ids.clone()`, pad/`attention_mask==0` → `-100`
- [x] Dataloaders return a **dict** (`input_ids`, `attention_mask`, `labels`)
- [x] Smoke: batch keys + shapes; decoded line looks like verse

Skipped: embeddings / a separate embedder.

---

## 2. Model — LightningModule around SmolLM

Mirror `src/models/mnist_module.py`. Hydra instantiates the class from YAML (`_target_`), same as MNIST.

- [x] `SmolLMLitModule(LightningModule)`
- [x] `AutoModelForCausalLM.from_pretrained` in `setup` (not `__init__`)
- [x] `_shared_step` → train/val/test; log `*/loss` and `*/ppl`
- [x] `configure_optimizers`: AdamW via Hydra `_partial_`; `scheduler: null`
- [ ] `_generate_and_score` (called from `test_step` when `batch_idx < 2` — **not implemented yet**; will crash)
- [x] No `SimpleDenseNet` / `net:` block

`compile` in YAML is `torch.compile`, left **false**.

---

## 3. Training — wire Hydra, don’t invent a new loop

`src/train.py` / `src/eval.py` stay. Default `train.yaml` still points at MNIST.

- [x] `configs/data/tinyshakespeare.yaml`
- [x] `configs/model/smollm.yaml`
- [x] `configs/experiment/smollm_tinys.yaml` — data/model overrides, `max_steps`, `val_check_interval`, `monitor: val/loss`
- [x] Callbacks: `val/loss` / `min`; early stopping off for the short run
- [x] Trainer: `cpu`; `max_steps=500`; `val_check_interval=100`; `limit_val_batches=8`
- [x] Run: `uv run src/train.py experiment=smollm_tinys`
- [x] `.ckpt` at `logs/train/runs/2026-08-24_18-37-18/checkpoints/` (500-step; use this). 100-step run: `18-33-05`. Gitignored; exclude from zip.

NTP loss: `out.loss` only. Don’t add a second CE.

---

## 4. Eval — this is the actual assignment

They said: training-aligned NTP is the objective; **at least one sequence-generation metric**; optional reference-based metric. You may eval **off-the-shelf HF weights** (no ckpt). Report **test**.

- [x] **PPL / NLL** logged in `test_step` (teacher forcing). Still need a **pretrained vs FT** table on test
- [ ] **Generation quality** — `test_step` calls `_generate_and_score` for `batch_idx < 2`; **method missing**
- [ ] **ROUGE-L** vs held-out continuation (noisy on verse; say so)
- [ ] `test_step` logs the metrics so `uv run src/eval.py data=tinyshakespeare model=smollm ckpt_path=...` just works (same pattern as MNIST)
- [ ] Also run eval **without** FT (load HF weights, skip ckpt or a “pretrained” path) so the 15-min table is pretrained vs FT
- [ ] Save a few generated samples in a small `outputs/samples.md` (text only, not weights)

Do not: FID, BERTScore-as-the-only-metric, LLM-as-judge, full BLEU suite.

---

## Packages

Already in `pyproject.toml`: `torch`, `pytorch-lightning`, `torchmetrics`, `hydra-*`, `transformers`, `huggingface-hub`, `datasets`.

- [ ] `uv add evaluate rouge-score` (or only `sacrebleu` if you pick chrF). That’s enough
- [ ] Do **not** add TRL, PEFT, unsloth, wandb-required, accelerate-as-a-second-trainer
- [ ] After add: `uv lock` is fine; commit `pyproject.toml` + `uv.lock`

Tokenizer/model download: HF cache (`~/.cache/huggingface`), **not** the repo.

---

## Tests and template hygiene

- [ ] Keep MNIST tests green (`uv run pytest`)
- [ ] Add a fast test: datamodule yields a batch with the right keys; optional 1-step train with `fast_dev_run` if it stays cheap
- [ ] `uv run pre-commit run --all-files` before zip
- [ ] Short **How to run** at the top of the template README (or `ASSIGNMENT.md`): train command, eval command, what the metrics mean

---

## Out of scope (say this in the 15 min, don’t build)

- Full epoch / SOTA Shakespeare
- LoRA / QLoRA (mention as “with more time / memory”)
- Optuna (`configs/hparams_search`)
- Custom architecture, extra encoder, contrastive loss
- Logging to a personal W&B that they can’t run

---

## Interview (15 min) — produce artifacts, not slides

- [ ] Table: pretrained vs FT — test PPL, generation metric, 2–3 decoded samples
- [ ] One failure: e.g. PPL dropped but samples still generic / repetition — why NTP ≠ “sounds like Shakespeare”
- [ ] What you’d do with more time: longer train, packing, decoding (temp/top-p), LoRA, better literary metrics
- [ ] Be ready to walk `training_step` (labels, `-100`, shift inside HF) and the Hydra experiment YAML

---

## Zip

- [ ] Working tree clean; no `.venv`, `data/`, `logs/` checkpoints, HF weights
- [ ] Include `.git/`, `.github/`, `pyproject.toml`, `uv.lock`, source, configs, tests
- [ ] Commits from **Terminal**, your name/email, no Cursor trailers
- [ ] Zip **`lightning-hydra-uv-template/`** only, not `code_assignment/` and not `industry`

```bash
cd ~/bosch-rtc-coding
git -C lightning-hydra-uv-template status
git -C lightning-hydra-uv-template clean -fdx
zip -r omri-azencot-bosch-coding.zip lightning-hydra-uv-template -x "*.DS_Store"
```

---

## Suggested commit chunks (local repo only)

1. [x] `feat: add TinyShakespeare datamodule`
2. [x] `feat: tokenize TinyShakespeare batches`
3. [x] `feat: add SmolLM Lightning module; config: data and model`
4. [x] `feat: add smollm_tinys experiment` (`34f5740`)
5. [x] short train + checkpoint (local `logs/`; do not commit weights)
6. [ ] `feat: generation eval (PPL + ROUGE-L / samples)`
7. [ ] `docs: how to train and evaluate`

---

## Copying this file

If you paste into `~/bosch-rtc-coding/.../TODO.md`, drop this industry header, the leftover-branch line, and the zip/AI-trace notes. Bosch can see that file.
