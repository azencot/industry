#!/usr/bin/env python3
"""Slide 6: patchify → encode → LLM tokens."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

INK = "#f3ece3"
MUTED = "#b7a99a"
ACCENT = "#d4783c"
TEAL = "#7eb8a8"
GOLD = "#e8c07a"
PAPER = "#1c1814"
SPINE = "#3a322b"
PATCH_C = [ACCENT, GOLD, TEAL, "#c48a62"]

OUT = Path(__file__).resolve().parent
Y = np.array([2.1, 2.4, 2.8, 3.1, 2.9, 3.4, 3.6, 3.3, 3.8, 4.1, 3.9, 4.4, 4.7, 4.5, 5.0, 5.2])


def save(fig, name):
    fig.savefig(OUT / name, dpi=160, facecolor=PAPER, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)


def pipeline():
    fig, ax = plt.subplots(figsize=(6.2, 7.0), facecolor=PAPER)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.set_axis_off()
    ax.set_facecolor(PAPER)
    n = len(Y)
    pw = n // 4
    xs = np.linspace(1.1, 8.9, n)
    ys = 8.55 + (Y - Y.min()) / (Y.max() - Y.min()) * 2.35

    ax.text(0.45, 11.55, "1 · windows", color=ACCENT, fontsize=11,
            fontfamily="monospace", fontweight="600")
    for p in range(4):
        i0, i1 = p * pw, min((p + 1) * pw, n)
        x0, x1 = xs[i0] - 0.18, xs[i1 - 1] + 0.18
        ax.add_patch(Rectangle(
            (x0, 8.35), x1 - x0, 2.75,
            facecolor=PATCH_C[p], alpha=0.18, edgecolor=PATCH_C[p], linewidth=1.1,
        ))
    ax.plot(xs, ys, color=GOLD, lw=1.9, zorder=3)
    ax.scatter(xs, ys, s=14, color=INK, zorder=4)

    ax.annotate("", xy=(5, 7.15), xytext=(5, 8.15),
                arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.2))

    ax.text(0.45, 6.85, "2 · encode", color=ACCENT, fontsize=11,
            fontfamily="monospace", fontweight="600")
    for p in range(4):
        cx = 1.55 + p * 2.15
        ax.add_patch(FancyBboxPatch(
            (cx - 0.85, 5.15), 1.7, 1.35,
            boxstyle="round,pad=0.02,rounding_size=0.12",
            facecolor="#14110e", edgecolor=PATCH_C[p], linewidth=1.3,
        ))
        ax.text(cx, 5.82, "enc", ha="center", va="center",
                fontfamily="monospace", fontsize=13, color=INK)

    ax.annotate("", xy=(5, 4.05), xytext=(5, 4.95),
                arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.2))

    ax.text(0.45, 3.75, "3 · LLM tokens", color=ACCENT, fontsize=11,
            fontfamily="monospace", fontweight="600")
    ax.add_patch(FancyBboxPatch(
        (0.7, 0.55), 8.6, 2.85,
        boxstyle="round,pad=0.02,rounding_size=0.14",
        facecolor="#14110e", edgecolor=SPINE, linewidth=1.2,
    ))
    ax.text(1.05, 2.85, "LLM", color=MUTED, fontsize=10, fontfamily="monospace")
    for p in range(4):
        cx = 2.05 + p * 1.85
        ax.add_patch(FancyBboxPatch(
            (cx - 0.7, 1.05), 1.4, 1.25,
            boxstyle="round,pad=0.02,rounding_size=0.1",
            facecolor="#1c1814", edgecolor=PATCH_C[p], linewidth=1.2,
        ))
        ax.text(cx, 1.68, f"z{p+1}", ha="center", va="center",
                fontfamily="monospace", fontsize=12, color=INK)
    ax.text(8.55, 1.68, "…", ha="center", va="center", color=MUTED, fontsize=16)
    save(fig, "slide6-patch.png")


if __name__ == "__main__":
    pipeline()
