#!/usr/bin/env python3
"""Slide 12: three measured ablations (8B, grpo tables).

1. ChatTS numerical — delay vs chart vs dual (chatts-8b-* / dual-8b-chatts).
2. TSExam — delay wins anomaly, chart wins noise (qwen8b_ftmatplotlib / qwen8b_dino2stage).
3. Same delay images — native ViT LoRA vs DINOv3 (qwendelay-8b / dino8b-fp).
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

INK = "#f3ece3"
MUTED = "#b7a99a"
ACCENT = "#d4783c"
TEAL = "#7eb8a8"
GOLD = "#e8c07a"
PAPER = "#1c1814"
SPINE = "#3a322b"

OUT = Path(__file__).resolve().parent
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Avenir Next", "Helvetica Neue", "DejaVu Sans"]


def save(fig, name):
    fig.savefig(OUT / name, dpi=160, facecolor=PAPER, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)


def style(ax):
    ax.set_facecolor(PAPER)
    ax.tick_params(colors=MUTED, labelsize=8.2, length=0)
    for sp in ax.spines.values():
        sp.set_color(SPINE)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", color=SPINE, linewidth=0.6, alpha=0.9)
    ax.set_axisbelow(True)


def hbars(name, rows, xmax=1.0, fmt="{:.2f}"):
    """rows: (label, value, color). First row drawn at top."""
    fig, ax = plt.subplots(figsize=(9.2, 2.05), facecolor=PAPER)
    style(ax)
    labels = [r[0] for r in rows][::-1]
    vals = [r[1] for r in rows][::-1]
    cols = [r[2] for r in rows][::-1]
    y = np.arange(len(rows))
    h = 0.62 if len(rows) <= 3 else 0.48
    ax.barh(y, vals, color=cols, height=h, edgecolor=PAPER, linewidth=0.4)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, color=INK, fontsize=9.2)
    ax.set_xlim(0, xmax)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(["0", ".25", ".50", ".75", "1"], color=MUTED)
    for yi, v in zip(y, vals):
        ax.text(min(v + 0.025, xmax - 0.02), yi, fmt.format(v),
                va="center", ha="left", color=INK, fontsize=9.0, fontweight="600")
    save(fig, name)


def main():
    # ChatTS 8B 2-stage, dataset A numerical (B matches within 3 pp).
    hbars("slide12-num.png", [
        ("Delay only", 0.351, TEAL),
        ("Chart only", 0.709, GOLD),
        ("Dual", 0.787, ACCENT),
    ])
    # Complementary pair only: delay wins anomaly, chart wins noise.
    hbars("slide12-cats.png", [
        ("Anom · chart", 0.562, GOLD),
        ("Anom · delay", 0.824, TEAL),
        ("Noise · chart", 0.960, GOLD),
        ("Noise · delay", 0.762, TEAL),
    ])
    hbars("slide12-tower.png", [
        ("Native ViT on delay", 0.601, GOLD),
        ("DINOv3 on delay", 0.831, TEAL),
    ], fmt="{:.3f}")


if __name__ == "__main__":
    main()
