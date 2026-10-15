#!/usr/bin/env python3
"""Worked example from TSLMTSEXAM presentation/make_figs.py (s0-champion-fix).

Replay the same Generator(7) draws as the lab script so the prediction
series matches the stored figure. Delay image is the history only
(Hankel / ImagenTime columns) — same construction as the explainer slide.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

MUTED = "#b7a99a"
PAPER = "#1c1814"
SPINE = "#3a322b"
GOLD = "#e8c07a"
TEAL = "#7eb8a8"
ACCENT = "#d4783c"
GRAY = "#8a8076"
RED = "#c0392b"

OUT = Path(__file__).resolve().parent


def hankel(y, delay, embedding):
    cols = []
    i = 0
    while i * delay + embedding <= len(y):
        cols.append(y[i * delay : i * delay + embedding])
        i += 1
    return np.stack(cols, axis=1)


def replay_prediction():
    """Same draws as presentation/make_figs.py up through the prediction block."""
    rng = np.random.default_rng(7)
    n = 336
    rng.normal(0, 0.8, n)  # perception
    rng.normal(0, 1.0, 35)  # reasoning (wind)

    nh = 200
    th = np.arange(nh)
    hist = 5 * np.sin(2 * np.pi * th / 50) + 0.01 * th + rng.normal(0, 0.5, nh)
    tf = np.arange(nh, nh + 60)
    cand_a = 5 * np.sin(2 * np.pi * tf / 50) + 0.01 * tf + rng.normal(0, 0.5, 60)
    cand_b = np.full(60, hist[-1]) + rng.normal(0, 0.3, 60)
    cand_c = hist[-1] + np.cumsum(rng.normal(0.15, 1.4, 60))
    return th, hist, tf, cand_a, cand_b, cand_c


def style_ax(ax):
    ax.set_facecolor(PAPER)
    ax.tick_params(colors=MUTED, labelsize=11, length=0)
    for sp in ax.spines.values():
        sp.set_color(SPINE)
    ax.grid(color=SPINE, linewidth=0.5, alpha=0.9)
    ax.set_xlabel("")
    ax.set_ylabel("")


def main():
    th, hist, tf, a, b, c = replay_prediction()

    fig, ax = plt.subplots(figsize=(10.4, 4.6), facecolor=PAPER)
    style_ax(ax)
    ax.plot(th, hist, color=GOLD, lw=2.1, zorder=3, label="history")
    ax.plot(tf, a, color=TEAL, lw=2.0, zorder=3)
    ax.plot(tf, b, color=GRAY, lw=1.8, zorder=2)
    ax.plot(tf, c, color=RED, lw=1.8, zorder=2)
    ax.axvline(th[-1], ls=":", lw=1.3, color=MUTED, zorder=1)
    ax.text(tf[-1] + 2.5, a[-1], "A", color=TEAL, fontsize=16, fontweight="bold", va="center")
    ax.text(tf[-1] + 2.5, b[-1], "B", color=GRAY, fontsize=16, fontweight="bold", va="center")
    ax.text(tf[-1] + 2.5, c[-1], "C", color=RED, fontsize=16, fontweight="bold", va="center")
    ax.text(th[-1] - 2, hist.max() + 0.35, "now", color=MUTED, fontsize=11, ha="right")
    ax.set_xlim(0, tf[-1] + 18)
    fig.tight_layout(pad=0.25)
    fig.savefig(OUT / "who-ex-pred.png", dpi=160, facecolor=PAPER, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)

    img = hankel(hist, delay=4, embedding=40)
    cmap = LinearSegmentedColormap.from_list(
        "de",
        ["#1c1814", "#3a322b", "#7a4a2c", "#d4783c", "#e8c07a", "#f3ece3"],
    )
    fig, ax = plt.subplots(figsize=(10.4, 3.2), facecolor=PAPER)
    ax.set_facecolor(PAPER)
    ax.imshow(img, aspect="auto", cmap=cmap, interpolation="nearest", origin="upper")
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_color(SPINE)
    fig.tight_layout(pad=0.05)
    fig.savefig(OUT / "who-ex-delay.png", dpi=160, facecolor=PAPER, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)


if __name__ == "__main__":
    main()
