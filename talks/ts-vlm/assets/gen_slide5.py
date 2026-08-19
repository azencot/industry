#!/usr/bin/env python3
"""Slide 5: OpenTSLM Fig 17 / 18 restyled — tokens in the LLM context."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

INK = "#f3ece3"
MUTED = "#b7a99a"
ACCENT = "#d4783c"
TEAL = "#7eb8a8"
GOLD = "#e8c07a"
PAPER = "#1c1814"
SPINE = "#3a322b"
OOM = "#e07070"

OUT = Path(__file__).resolve().parent
N = np.array([1, 2, 3, 4, 5])
LS = (10, 100, 1000, 10000)

# Table 11, OpenTSLM. nan = OOM.
SP = {
    "Gemma-3-270M": {
        10: [2.3, 2.3, 2.3, 2.3, 2.3],
        100: [2.3, 2.3, 2.3, 2.4, 2.4],
        1000: [2.4, 3.4, 4.8, 5.5, 7.0],
        10000: [13.7, 32.1, 56.1, 85.6, 118.4],
    },
    "Gemma-3-1B": {
        10: [5.0, 5.0, 4.9, 5.0, 5.0],
        100: [4.9, 5.0, 5.0, 5.0, 5.0],
        1000: [5.0, 4.9, 7.4, 8.7, 10.2],
        10000: [19.2, 43.6, 76.0, 116.4, 164.5],
    },
    "Llama-3.2-1B": {
        10: [2.6, 2.6, 2.7, 2.7, 2.8],
        100: [2.7, 2.8, 2.9, 3.0, 3.2],
        1000: [3.6, 5.0, 6.9, 9.2, 12.0],
        10000: [29.5, 93.3, np.nan, np.nan, np.nan],
    },
    "Llama-3.2-3B": {
        10: [6.3, 6.4, 6.4, 6.5, 6.7],
        100: [6.4, 6.6, 6.8, 7.0, 7.3],
        1000: [8.0, 9.8, 12.3, 15.4, 19.1],
        10000: [42.7, 191.4, np.nan, np.nan, np.nan],
    },
}
FL = {
    "Gemma-3-270M": {
        10: [5.7, 5.7, 5.8, 5.8, 5.8],
        100: [5.7, 5.7, 5.8, 5.8, 5.7],
        1000: [5.7, 5.7, 5.8, 5.8, 5.7],
        10000: [5.7, 5.7, 5.8, 6.4, 6.4],
    },
    "Gemma-3-1B": {
        10: [15.4, 15.5, 15.5, 15.5, 15.6],
        100: [15.4, 15.5, 15.5, 15.5, 15.5],
        1000: [15.4, 15.4, 15.5, 15.6, 15.6],
        10000: [15.4, 15.4, 15.5, 15.5, 15.5],
    },
    "Llama-3.2-1B": {
        10: [20.4, 20.4, 20.4, 20.5, 20.5],
        100: [20.4, 20.4, 20.5, 20.5, 20.5],
        1000: [20.4, 20.4, 20.4, 20.5, 20.6],
        10000: [20.4, 20.4, 20.6, 20.8, 21.0],
    },
    "Llama-3.2-3B": {
        10: [61.0, 60.9, 60.7, 60.7, 60.8],
        100: [61.0, 60.9, 60.7, 60.7, 60.8],
        1000: [61.0, 61.0, 60.7, 60.7, 60.7],
        10000: [61.0, 61.0, 60.7, 60.8, 61.1],
    },
}
COLOR = {
    "Gemma-3-270M": TEAL,
    "Gemma-3-1B": GOLD,
    "Llama-3.2-1B": ACCENT,
    "Llama-3.2-3B": "#c48a62",
}
MODELS = list(COLOR)


def save(fig, name):
    fig.savefig(OUT / name, dpi=160, facecolor=PAPER, bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)


def style(ax):
    ax.set_facecolor(PAPER)
    ax.tick_params(colors=MUTED, labelsize=8, length=3, width=0.6)
    for sp in ax.spines.values():
        sp.set_color(SPINE)
    ax.grid(color=SPINE, linewidth=0.5, alpha=0.55)
    ax.set_axisbelow(True)


def fig17():
    fig, axes = plt.subplots(2, 4, figsize=(11.4, 5.6), facecolor=PAPER)
    fig.subplots_adjust(left=0.11, right=0.99, top=0.82, bottom=0.14, wspace=0.22, hspace=0.38)

    for c, L in enumerate(LS):
        ax = axes[0, c]
        style(ax)
        ymax = 25 if L < 10000 else 200
        ax.set_ylim(0, ymax)
        ax.set_xlim(0.7, 5.3)
        ax.set_xticks(N)
        ax.set_title(f"L = {L:,}" if L < 10000 else "L = 10,000",
                     color=MUTED, fontsize=10, pad=6, fontfamily="monospace")
        for name in MODELS:
            y = np.asarray(SP[name][L], dtype=float)
            ok = np.isfinite(y)
            ax.plot(N[ok], y[ok], color=COLOR[name], marker="o", ms=4.2, lw=1.55)
            miss = np.where(~ok)[0]
            if len(miss):
                ax.scatter(N[miss], np.full(len(miss), ymax * 0.93),
                           marker="x", s=36, color=OOM, linewidths=1.5, zorder=4)
        if c == 0:
            ax.set_ylabel("SoftPrompt", color=ACCENT, fontsize=10, fontfamily="sans-serif")

        ax = axes[1, c]
        style(ax)
        ax.set_ylim(0, 70)
        ax.set_xlim(0.7, 5.3)
        ax.set_xticks(N)
        for name in MODELS:
            y = np.asarray(FL[name][L], dtype=float)
            ax.plot(N, y, color=COLOR[name], marker="s", ms=3.8, lw=1.55)
        if c == 0:
            ax.set_ylabel("Flamingo", color=TEAL, fontsize=10, fontfamily="sans-serif")

    fig.supxlabel("Number of series  N", color=MUTED, fontsize=10, y=0.02)
    fig.text(0.015, 0.48, "Peak memory (GB)", rotation=90, va="center", color=MUTED, fontsize=10)

    handles = [
        Line2D([0], [0], color=COLOR[m], marker="o", lw=1.5, ms=5, label=m)
        for m in MODELS
    ]
    handles.append(Line2D([0], [0], color=OOM, marker="x", lw=0, ms=8, label="OOM"))
    fig.legend(
        handles=handles, loc="upper center", ncol=5, frameon=False,
        bbox_to_anchor=(0.55, 1.02), labelcolor=MUTED, fontsize=8.5,
        handlelength=1.6, columnspacing=1.1,
    )
    save(fig, "slide5-fig17.png")


def fig18():
    fig, axes = plt.subplots(1, 4, figsize=(11.4, 3.55), facecolor=PAPER, sharey=False)
    fig.subplots_adjust(left=0.06, right=0.99, top=0.78, bottom=0.22, wspace=0.22)

    for ax, name in zip(axes, MODELS):
        style(ax)
        ax.set_title(name, color=MUTED, fontsize=10, pad=6, fontfamily="monospace")
        xs, ys = [], []
        xf, yf = [], []
        oom_x = []
        for L in LS:
            for n, v in zip(N, SP[name][L]):
                if np.isfinite(v):
                    xs.append(n * L)
                    ys.append(v)
                else:
                    oom_x.append(n * L)
            for n, v in zip(N, FL[name][L]):
                xf.append(n * L)
                yf.append(v)
        order = np.argsort(xs)
        xs, ys = np.asarray(xs)[order], np.asarray(ys)[order]
        of = np.argsort(xf)
        xf, yf = np.asarray(xf)[of], np.asarray(yf)[of]
        ax.plot(xs, ys, color=ACCENT, marker="o", ms=4.2, lw=1.6, label="SoftPrompt")
        ax.plot(xf, yf, color=TEAL, marker="s", ms=3.6, lw=1.6, label="Flamingo")
        ymax = max(180, (max(ys) if len(ys) else 20) * 1.15)
        ax.set_ylim(0, ymax)
        ax.set_xlim(-1500, 52000)
        if oom_x:
            ax.scatter(oom_x, np.full(len(oom_x), ymax * 0.92),
                       marker="x", s=42, color=OOM, linewidths=1.6, zorder=4)
        ax.tick_params(axis="x", labelsize=7.5)
        ax.set_xticks([0, 20000, 40000])
        ax.set_xticklabels(["0", "20k", "40k"])

    axes[0].set_ylabel("Peak VRAM (GB)", color=MUTED, fontsize=9)
    fig.supxlabel("Total size  N × L", color=MUTED, fontsize=10, y=0.04)
    handles = [
        Line2D([0], [0], color=ACCENT, marker="o", lw=1.5, ms=5, label="SoftPrompt"),
        Line2D([0], [0], color=TEAL, marker="s", lw=1.5, ms=5, label="Flamingo"),
        Line2D([0], [0], color=OOM, marker="x", lw=0, ms=8, label="OOM"),
    ]
    fig.legend(
        handles=handles, loc="upper center", ncol=3, frameon=False,
        bbox_to_anchor=(0.55, 1.04), labelcolor=MUTED, fontsize=8.5,
        handlelength=1.6, columnspacing=1.4,
    )
    save(fig, "slide5-fig18.png")


if __name__ == "__main__":
    fig17()
    fig18()
