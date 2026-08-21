# Tech-screen study code (not CoderPad)

Tyler locked **spoken** LLM training + multimodality. These files are for **shapes**. After you run them, close the tab and say the forward pass aloud.

| File | When | What |
|------|------|------|
| [`day1_attention.py`](day1_attention.py) | Fri/Sat | Causal MHA + next-token CE. Trace, then fill `CausalSelfAttentionFromMemory`. |
| `day2_multimodal.py` | Sun | Projector concat into an LM. Not written yet. |
| `day3_broken_attention.py` | Mon | Bugs to find. Not written yet. |

External read (Sat): [karpathy/nanoGPT `model.py`](https://github.com/karpathy/nanoGPT/blob/master/model.py) — `CausalSelfAttention` and `GPT.forward` (the `cross_entropy` call).

```bash
python3 day1_attention.py
```
