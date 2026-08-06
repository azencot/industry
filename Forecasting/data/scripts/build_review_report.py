#!/usr/bin/env python3
"""Build REVIEW.html + REVIEW.md with exemplar plots for manual sign-off."""

from __future__ import annotations

import base64
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "generated"
REVIEW = ROOT / "review"
FIGS = REVIEW / "figures"

REGIME_BLURB = {
    "smooth_seasonal": {
        "title": "Smooth seasonal",
        "expected_winner": "Seasonal Naive / ETS",
        "look_for": "Clear weekly seasonality; stable mean; low zeros.",
    },
    "mean_step": {
        "title": "Mean step (structural break)",
        "expected_winner": "ETS / LightGBM",
        "look_for": "Permanent jump in series mean at shift_date; SN will lag after the break.",
    },
    "promo_driven": {
        "title": "Promo / covariate-driven",
        "expected_winner": "LightGBM",
        "look_for": "Spikes aligned with promo=1; promo present in test horizon.",
    },
    "intermittent": {
        "title": "Intermittent discrete demand",
        "expected_winner": "Metric drama; Chronos vs local stats",
        "look_for": "Many exact zeros; integer bursts; MAPE-unfriendly.",
    },
    "cold_start": {
        "title": "Cold start / short history",
        "expected_winner": "Chronos-Bolt",
        "look_for": "Only ~30–60 train days before cutoff.",
    },
}


def regime_score(regime: str, g: pd.DataFrame, m: pd.Series) -> float:
    y = g.loc[g["in_train"], "y"].to_numpy()
    if regime == "smooth_seasonal":
        if len(y) < 14:
            return 0.0
        return float(np.corrcoef(y[:-7], y[7:])[0, 1])
    if regime == "mean_step":
        shift = pd.Timestamp(m["shift_date"])
        before = g.loc[g["ds"] < shift, "y"].mean()
        after = g.loc[(g["ds"] >= shift) & g["in_train"], "y"].mean()
        return float(after - before)
    if regime == "promo_driven":
        y1 = g.loc[g["promo"] == 1, "y"].mean()
        y0 = g.loc[g["promo"] == 0, "y"].mean()
        return float(y1 / y0) if y0 else 0.0
    if regime == "intermittent":
        return float(np.mean(y == 0))
    if regime == "cold_start":
        return -float(m["n_train_days"])  # shorter = more extreme
    return 0.0


def pick_exemplars(panel: pd.DataFrame, meta: pd.DataFrame) -> list[tuple[str, str]]:
    """First series id + highest regime-score series per regime."""
    picks: list[tuple[str, str]] = []
    for regime in REGIME_BLURB:
        sub = meta.loc[meta["regime"] == regime].sort_values("series_id")
        first = str(sub.iloc[0]["series_id"])
        scores = []
        for _, m in sub.iterrows():
            g = panel.loc[panel["series_id"] == m["series_id"]].copy()
            g["ds"] = pd.to_datetime(g["ds"])
            scores.append((regime_score(regime, g, m), str(m["series_id"])))
        best = max(scores)[1]
        picks.append((regime, first))
        if best != first:
            picks.append((regime, best))
    return picks


def plot_series(
    g: pd.DataFrame,
    m: pd.Series,
    cutoff: pd.Timestamp,
    out_path: Path,
) -> None:
    g = g.sort_values("ds")
    fig, ax = plt.subplots(figsize=(10, 3.2))
    train = g.loc[g["in_train"]]
    test = g.loc[~g["in_train"]]
    ax.plot(train["ds"], train["y"], color="#1f4e79", lw=1.2, label="train")
    ax.plot(test["ds"], test["y"], color="#c45911", lw=1.2, label="test (horizon)")
    ax.axvline(cutoff, color="#666", ls="--", lw=1, label="cutoff")
    if m["regime"] == "mean_step" and m.get("shift_date"):
        ax.axvline(pd.Timestamp(m["shift_date"]), color="#548235", ls=":", lw=1.5, label="shift_date")
    if m["regime"] in ("promo_driven", "cold_start") and g["promo"].sum() > 0:
        promo_days = g.loc[g["promo"] == 1]
        ax.scatter(
            promo_days["ds"],
            promo_days["y"],
            s=18,
            c="#e2a03f",
            zorder=3,
            label="promo=1",
        )
    ax.set_title(f"{m['series_id']}  ·  {m['regime']}")
    ax.set_ylabel("y")
    ax.legend(loc="upper left", fontsize=8, ncol=2)
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


def img_b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


def build() -> None:
    REVIEW.mkdir(parents=True, exist_ok=True)
    FIGS.mkdir(parents=True, exist_ok=True)

    panel = pd.read_parquet(GEN / "panel.parquet")
    panel["ds"] = pd.to_datetime(panel["ds"])
    meta = pd.read_csv(GEN / "series_meta.csv")
    cutoff_info = json.loads((GEN / "cutoff.json").read_text())
    cutoff = pd.Timestamp(cutoff_info["cutoff"])
    gold = pd.read_csv(GEN / "gold_checks.csv") if (GEN / "gold_checks.csv").exists() else None

    picks = pick_exemplars(panel, meta)
    fig_records = []
    for regime, sid in picks:
        m = meta.loc[meta["series_id"] == sid].iloc[0]
        g = panel.loc[panel["series_id"] == sid]
        fname = f"{regime}__{sid}.png"
        out = FIGS / fname
        plot_series(g, m, cutoff, out)
        fig_records.append(
            {
                "regime": regime,
                "series_id": sid,
                "path": out,
                "rel": f"figures/{fname}",
                "meta": m,
            }
        )

    # --- markdown ---
    md_lines = [
        "# Synthetic panel review",
        "",
        f"- Cutoff: `{cutoff_info['cutoff']}` · Horizon: `{cutoff_info['horizon']}` · Seed: `{cutoff_info['seed']}`",
        f"- Series: `{cutoff_info['n_series_total']}` · Rows: `{cutoff_info['n_rows']}`",
        "",
        "Primary view: [`REVIEW.html`](REVIEW.html) (open in browser).",
        "",
        "## Manual checklist",
        "",
        "- [ ] Seasonality visible on smooth",
        "- [ ] Clear permanent mean jump on mean_step (vline at shift_date)",
        "- [ ] Promo spikes align with promo flag",
        "- [ ] Intermittent looks sparse/discrete",
        "- [ ] Cold-start history is obviously short",
        "",
    ]
    if gold is not None:
        md_lines += ["## Gold checks", "", "| Check | Pass | Detail |", "|-------|------|--------|"]
        for _, r in gold.iterrows():
            md_lines.append(f"| `{r['check']}` | {'yes' if r['pass'] else 'NO'} | {r['detail']} |")
        md_lines.append("")

    md_lines += ["## Exemplars", ""]
    for rec in fig_records:
        b = REGIME_BLURB[rec["regime"]]
        m = rec["meta"]
        md_lines += [
            f"### {b['title']} — `{rec['series_id']}`",
            "",
            f"- Expected later winner: **{b['expected_winner']}**",
            f"- Look for: {b['look_for']}",
            f"- n_train_days={int(m['n_train_days'])}; parent_dgp={m['parent_dgp']}",
            f"- ![]({rec['rel']})",
            "",
        ]
    (REVIEW / "REVIEW.md").write_text("\n".join(md_lines) + "\n")

    # --- html ---
    gold_html = ""
    if gold is not None:
        cells = []
        for _, r in gold.iterrows():
            cls = "pass" if r["pass"] else "fail"
            cells.append(
                f"<tr class='{cls}'><td><code>{r['check']}</code></td>"
                f"<td>{'PASS' if r['pass'] else 'FAIL'}</td><td>{r['detail']}</td></tr>"
            )
        gold_html = (
            "<h2>Gold checks</h2><table><thead><tr><th>Check</th><th>Pass</th><th>Detail</th></tr></thead>"
            f"<tbody>{''.join(cells)}</tbody></table>"
        )

    sections = []
    for rec in fig_records:
        b = REGIME_BLURB[rec["regime"]]
        m = rec["meta"]
        b64 = img_b64(rec["path"])
        sections.append(
            f"""
<section>
  <h3>{b['title']} — <code>{rec['series_id']}</code></h3>
  <p><strong>Expected later winner:</strong> {b['expected_winner']}<br>
  <strong>Look for:</strong> {b['look_for']}<br>
  n_train_days={int(m['n_train_days'])}; parent_dgp={m['parent_dgp']};
  shift_date={m.get('shift_date') or '—'}; promo_lift={m.get('promo_lift')}</p>
  <img alt="{rec['series_id']}" src="data:image/png;base64,{b64}"/>
</section>
"""
        )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>Synthetic panel review</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
         max-width: 980px; margin: 2rem auto; padding: 0 1rem; color: #1a1a1a; line-height: 1.45; }}
  h1, h2, h3 {{ line-height: 1.2; }}
  table {{ border-collapse: collapse; width: 100%; font-size: 0.9rem; margin: 1rem 0; }}
  th, td {{ border: 1px solid #ccc; padding: 0.35rem 0.5rem; text-align: left; }}
  tr.fail {{ background: #fde8e8; }}
  tr.pass {{ background: #eef8ee; }}
  img {{ max-width: 100%; height: auto; border: 1px solid #ddd; }}
  ul.checklist {{ list-style: none; padding-left: 0; }}
  ul.checklist li {{ margin: 0.35rem 0; }}
  code {{ background: #f4f4f4; padding: 0.1rem 0.3rem; }}
  .meta {{ color: #444; }}
</style>
</head>
<body>
<h1>Synthetic panel review</h1>
<p class="meta">Cutoff: <code>{cutoff_info['cutoff']}</code> ·
Horizon: <code>{cutoff_info['horizon']}</code> ·
Seed: <code>{cutoff_info['seed']}</code> ·
Series: <code>{cutoff_info['n_series_total']}</code> ·
Rows: <code>{cutoff_info['n_rows']}</code></p>

<h2>Manual checklist</h2>
<ul class="checklist">
  <li>☐ Seasonality visible on smooth</li>
  <li>☐ Clear permanent mean jump on mean_step (vline at shift_date)</li>
  <li>☐ Promo spikes align with promo flag</li>
  <li>☐ Intermittent looks sparse/discrete</li>
  <li>☐ Cold-start history is obviously short</li>
</ul>

{gold_html}

<h2>Exemplars</h2>
{''.join(sections)}

<p class="meta">Regenerate: <code>python scripts/generate_panel.py && python scripts/verify_gold.py && python scripts/build_review_report.py</code></p>
</body>
</html>
"""
    (REVIEW / "REVIEW.html").write_text(html)
    print(f"Wrote {REVIEW / 'REVIEW.html'} and {REVIEW / 'REVIEW.md'} ({len(fig_records)} figures)")


if __name__ == "__main__":
    build()
