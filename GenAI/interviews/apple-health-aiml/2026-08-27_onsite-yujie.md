# On-site — Yujie Li (Wed 10:05 PDT)

**Track:** multimodal arch + **time-series encoding** (behavioral, not only 100 Hz). **Conf:** high.  
**Who (private):** Senior MLE, Seattle; headline Apple health AI. Coauthor [Beyond Sensor Data / WBM](https://machinelearning.apple.com/research/beyond-sensor) — 2.5B hours, 162k people, **tokenization + architecture**, 57 health tasks. CV / representation background.  
**Hub:** [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md)

**Opens Wednesday.** First two minutes: encoding → stay here. Labels / 162k / missingness → Haraldur sheet (**5**).

Do **not** name WBM / ICML. Do **not** force TS-as-image onto PPG. Do **not** only talk PPG@100 Hz / IMU@50 Hz.

---

## Timescales (the upgrade)

Low-level: PPG, IMU, ECG.  
**Behavioral:** daily steps, sleep stages, workouts, resting HR, mobility, HealthKit events. Different **semantic clocks**.

Tokenize **three years** of mixed history — walk alternatives:

| Scheme | Preserves | Loses | Cost | Bias |
|--------|-----------|-------|------|------|
| Regular bins (hour/day) | Alignment | Fake grid; missing cells explode length | \(T\) huge | Clock-time |
| Event tokens `<SLEEP…>` | Sparsity, semantics | Discretization choices | Cheap if sparse | What you chose to name |
| Dense patches | Local waveform | Long-range unless hierarchy | Patches × Hz | Local stationarity |
| **Hierarchical** | Fine locally, coarse globally | Fusion design | Best if done honestly | Scale separation |

Preferred skeleton:

\[
\text{dense } x_m(t) \xrightarrow{\text{local } E_m} z_{\text{hour/day}} \rightarrow \text{longitudinal model}
\]

Do **not** dump 100 Hz IMU for 3 years into one Transformer.

**Fifth box** on every encoding:

**What temporal scale does the downstream question require?**  
Sleep next night ≠ 5-year diabetes risk ≠ a 10 s gait motif.

---

## Bakeoff: “just quantize everything into a Transformer”

Empirical, not philosophy:

- matched data / split / compute  
- tasks at **short and long** horizons  
- missingness slices  
- probe the representation (linear head)  
- **token utilization / throughput**

Then decide. Your text vs native encoder vs image story **fits as families**, not as “I would plot PPG.”

Year one: same eval, compare encoder families on **their** streams. Patched native encoder = honest bias if you have the data. Images = stolen visual prior when the LM couldn’t see a **short** series.

---

## Predicted questions

1. Three years of heterogeneous wearable history — how do you **tokenize**?  
2. Why not one grid at the fastest clock?  
3. Fuse IMU@100 Hz with daily sleep — where?  
4. Behavioral tokens vs raw PPG — when each wins.  
5. Quantize all continuous vars → Transformer. Why not?  
6. Token budget: what do you drop first?  
7. Half the streams missing that year.  
8. Sampling rate changes across device gens.  
9. Concat vs cross-attn vs native encoder — one discriminating experiment.  
10. Feng leftover: caption eval ≠ CE/ROUGE; multivariate ≠ “just concat” without identity / time.

---

## Traps

| Trap | Do instead |
|------|------------|
| Replay Shirley’s 2–3 min encodings | Clocks + token cost + timescale |
| LLaVA vs Flamingo as the whole hour | Wearable token design |
| “Images keep all information” | Own ablation |
| Recite 2.5B hours | She wrote it |

**Mock (35 min):** first Wed slot. Broad: add PPG + IMU + **behavioral** history. Drill: tokenize 3 years. Scenario: matched bakeoff, no matplotlib on PPG.
