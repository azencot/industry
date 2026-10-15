#!/usr/bin/env python3
"""Delay-embedding explainer: windows of a series become columns of an image.

Hankel construction (ImagenTime), not a 2D phase portrait.
Wide canvas — matches the slide panel, no stray-label padding.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle

MUTED = "#b7a99a"
PAPER = "#1c1814"
SPINE = "#3a322b"
GOLD = "#e8c07a"
WIN = ["#d4783c", "#e8c07a", "#7eb8a8", "#c48a62"]

OUT = Path(__file__).resolve().parent


def hankel(y, delay, embedding):
    cols = []
    i = 0
    while i * delay + embedding <= len(y):
        cols.append(y[i * delay : i * delay + embedding])
        i += 1
    return np.stack(cols, axis=1)


def main():
    n, period, delay, m = 80, 16, 4, 20
    t = np.arange(n, dtype=float)
    y = np.sin(2 * np.pi * t / period)
    img = hankel(y, delay=delay, embedding=m)
    starts = [0, delay, 2 * delay, 3 * delay]

    fig, axes = plt.subplots(
        2, 1,
        figsize=(14.4, 7.2),
        facecolor=PAPER,
        gridspec_kw={"height_ratios": [0.55, 2.45], "hspace": 0.045},
    )
    ax, ax2 = axes
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)

    ax.set_facecolor(PAPER)
    for i, s in enumerate(starts):
        ax.axvspan(s - 0.35, s + m - 0.65, color=WIN[i], alpha=0.28, zorder=0)
        ax.axvline(s - 0.35, color=WIN[i], lw=1.6, zorder=1)
        ax.axvline(s + m - 0.65, color=WIN[i], lw=1.6, zorder=1)
    ax.plot(t, y, color=GOLD, lw=3.2, zorder=2)
    ax.fill_between(t, y, 0, color=GOLD, alpha=0.12, zorder=1)
    ax.set_xlim(0, n - 1)
    ax.set_ylim(-1.15, 1.15)
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_color(SPINE)
    ax.text(
        0.008, 0.90, "series  ·  each tinted span is one window",
        transform=ax.transAxes, color=MUTED, fontsize=12, va="top",
    )

    cmap = LinearSegmentedColormap.from_list(
        "de",
        ["#1c1814", "#3a322b", "#7a4a2c", "#d4783c", "#e8c07a", "#f3ece3"],
    )
    ax2.set_facecolor(PAPER)
    ax2.imshow(img, aspect="auto", cmap=cmap, interpolation="nearest", origin="upper")
    for i, _s in enumerate(starts):
        ax2.add_patch(Rectangle(
            (i - 0.5, -0.5), 1.0, img.shape[0],
            fill=False, edgecolor=WIN[i], lw=2.4, zorder=3,
        ))
    ax2.set_xticks([])
    ax2.set_yticks([])
    for sp in ax2.spines.values():
        sp.set_color(SPINE)
    ax2.text(
        0.008, 0.96, "delay image  ·  that window is now a column",
        transform=ax2.transAxes, color=MUTED, fontsize=12, va="top",
    )

    fig.savefig(OUT / "who-de-how.png", dpi=150, facecolor=PAPER, pad_inches=0)
    plt.close(fig)


if __name__ == "__main__":
    main()
