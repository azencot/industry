# Group papers (local PDFs)

PDFs of Shirley’s Health AI / Health & Fitness public papers. **Read to understand the stack. Do not name-drop on the tech screen** unless Feng goes there.

Spoken briefing (no paper quiz): [`../2026-08-20_shirley-group-briefing.md`](../2026-08-20_shirley-group-briefing.md).

| File | Paper | Authors (Apple-relevant) | Why it is here |
|------|--------|--------------------------|----------------|
| [`2411.18822v5.pdf`](2411.18822v5.pdf) | **RelCon** — relative contrastive motion FM for wearable accel (ICLR 2025) | Xu, **Narain**, Darnell, Hallgrímsson, … **Ren** | Sensor / motion layer. 1B **segments**, encoder **~3.9M** params. Not Feng. |
| [`2509.00221v3.pdf`](2509.00221v3.pdf) | **Speech FMs** generalize to wearable TS tasks | **Narain**, Aldeneh, **Ren** | Steal a pretrained encoder under scarcity (HuBERT / wav2vec 2.0 probes). |
| [`2409.11376v2.pdf`](2409.11376v2.pdf) | **Towards Time-Series Reasoning with LLMs** | Chow, Gardiner, Hallgrímsson, Xu, **Ren** (thanks: Vincent Chan, **Feng Zhu**) | Closest to your bet: patch TS encoder → Mistral, two-stage, perception first. |
| [`25_Leveraging_Periodicity_for_.pdf`](25_Leveraging_Periodicity_for_.pdf) | **Leveraging Periodicity** — multi-modal mood pattern models | **Narain**, Sun, Elachqar, Hallgrímsson, **Zhu**, **Ren** | **Feng’s paper.** 12 wearable streams, naturalistic **missingness**, periodicity + GBDT beat a deep TS model. |

**Bakeoff** = compare a few candidates under **one** eval/gate, then keep or kill. Not three separate papers. Not an ablation (ablation = drop a piece of *one* model).

## Periodicity paper (skim lock — do not recap Tue)

NeurIPS 2024 TS workshop. Mood-pattern **classification** (binarized PHQ2 / GAD2 items, not diagnoses). \(n=\)116,819 people, ~414k windows, **12 HealthKit streams** (HR family, steps, sleep, stand, …). Already **events**, not 100 Hz PPG/IMU.

**Collapse to hourly/daily:** bin timestamps → **one scalar per stream per bin** (or empty). Rates (HR, HRV, walking speed) = **mean** in the window. Counts/durations (steps, exercise, stand time) = **sum**. Stand-hour / sleep = **binary** at hourly. Empty bins stay missing. That is *their* representation. It is **not** Q12 “resample IMU@100 Hz and nightly sleep onto one grid.”

**Representations they compared:** 7/14-day temporal stats (no clock); weekend–weekday; 24h clock-hour profile; FFT **power** (routine regularity) + **phase** (timing); **periodic combined** = 24h profile + a few FFT bins (0, ~weekly 0.14, 1/2/3 cycles/day); raw daily/hourly grid → 1D CNN. XGB on aggregates vs CNN on the series.

**Results:** periodic combined + XGB ≈ hourly CNN on the **full** set (~0.71 AUC). Periodicity beats naive temporal stats. Adding demo still moves GAD. **Robustness is the claim:** periodic + GBDT holds up under missingness filters and smaller \(N\); CNN drops if you train on complete-ish rows and test on full missingness. Training **without** dropping high-missing rows is generally best (missingness correlates with the label). Tiny eval sets overstate AUC.

**Q12 translation (say this, not Table 1):** keep subset rows; don’t invent a complete tensor; encode what is present; mix missingness; one gate that includes incomplete people. Periodicity here = routine regularity/timing on **summaries**, not a spectrogram you reprint as an image.

## How to use before Tue (Feng)

1. **Stop reading PDFs.** If he says your benches aren’t Watch data, land: longitudinal, missing days, multi-stream — not UCR plots, not matplotlib on PPG. **Not** “periodic combined got 0.708.”
2. **TS-LLM PDF** only if you need encoder-family comparison: native encoder vs images; don’t recite Mistral-7B unprompted.
3. RelCon / speech-FM: already in the briefing. Don’t recap 1B segments.

Not in this folder (optional, not required for Feng): 2023 npj heart-rate (Ren + **Sapiro**); ICLR 2025 instruction-following (Ren / Narain / Miller; thanks Sapiro).
