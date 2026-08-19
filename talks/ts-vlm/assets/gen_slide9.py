#!/usr/bin/env python3
"""Slide 9: TSExam caption + two reasoning items (TSEXAMPP)."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

MUTED = "#b7a99a"
ACCENT = "#d4783c"
TEAL = "#7eb8a8"
GOLD = "#e8c07a"
PAPER = "#1c1814"
SPINE = "#3a322b"

OUT = Path(__file__).resolve().parent
N = 128
T = np.arange(N, dtype=float)


def style_ax(ax):
    ax.set_facecolor(PAPER)
    ax.tick_params(colors=MUTED, labelsize=8, length=0)
    for sp in ax.spines.values():
        sp.set_color(SPINE)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(color=SPINE, linewidth=0.5, alpha=0.9)


def save(fig, name):
    fig.savefig(OUT / name, dpi=160, facecolor=PAPER, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)


def caption_series():
    # Matches TSEXAMPP worked example: LinearTrend + SineWave + GWN.
    y = 0.045 * T + 2.5 * np.sin(2 * np.pi * T / 32)
    rng = np.random.default_rng(0)
    y = y + rng.normal(0, 0.35, N)
    fig, ax = plt.subplots(figsize=(7.4, 4.4), facecolor=PAPER)
    style_ax(ax)
    ax.plot(y, color=GOLD, lw=1.8)
    save(fig, "slide9-caption.png")


def lag_pair():
    rng = np.random.default_rng(1)
    base = np.cumsum(rng.normal(0, 0.35, N + 40))
    ts1 = base[:N]
    ts2 = base[36:36 + N]
    fig, ax = plt.subplots(figsize=(9.2, 2.05), facecolor=PAPER)
    style_ax(ax)
    ax.plot(ts1, color=GOLD, lw=1.45, label="ts1")
    ax.plot(ts2, color=ACCENT, lw=1.45, label="ts2")
    ax.legend(
        loc="upper right", frameon=False, fontsize=8, labelcolor=MUTED,
        handlelength=1.4,
    )
    save(fig, "slide9-lag.png")


def flip_pair():
    rng = np.random.default_rng(2)
    ts1 = 2.2 * np.sin(2 * np.pi * T / 22) + 0.04 * T
    ts2 = -ts1 + rng.normal(0, 0.12, N)
    fig, ax = plt.subplots(figsize=(9.2, 2.05), facecolor=PAPER)
    style_ax(ax)
    ax.plot(ts1, color=GOLD, lw=1.45, label="ts1")
    ax.plot(ts2, color=TEAL, lw=1.45, label="ts2")
    ax.legend(
        loc="upper right", frameon=False, fontsize=8, labelcolor=MUTED,
        handlelength=1.4,
    )
    save(fig, "slide9-flip.png")


if __name__ == "__main__":
    caption_series()
    lag_pair()
    flip_pair()
