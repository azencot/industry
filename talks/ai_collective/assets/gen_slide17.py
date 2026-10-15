#!/usr/bin/env python3
"""Slide 17: Stage C — why letter-GRPO failed, why gold traces first.

From TSLMTSEXAM `grpo` RUN_SUMMARY §7 and §27: letter GRPO on saturated SFT
is a no-op (zero group-std). Format GRPO regresses. C-RS gold TR SFT is what
moved 9B accuracy; later GRPO is format/boxing.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

INK = "#f3ece3"
MUTED = "#b7a99a"
ACCENT = "#d4783c"
GOLD = "#e8c07a"
PAPER = "#1c1814"
SPINE = "#3a322b"
BOX = "#241f1a"

OUT = Path(__file__).resolve().parent
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Avenir Next", "Helvetica Neue", "DejaVu Sans"]


def save(fig, name):
    fig.savefig(OUT / name, dpi=170, facecolor=PAPER, bbox_inches="tight", pad_inches=0.10)
    plt.close(fig)


def rbox(ax, x, y, w, h, edge=SPINE, lw=1.25, fc=BOX):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.012,rounding_size=0.05",
        linewidth=lw, edgecolor=edge, facecolor=fc, zorder=2,
    ))


def arrow(ax, p, q, color=MUTED):
    ax.add_patch(FancyArrowPatch(
        p, q, arrowstyle="-|>", mutation_scale=12, lw=1.25,
        color=color, zorder=1, shrinkA=1.5, shrinkB=1.5,
    ))


def chip(ax, x, y, w, h, text, edge=SPINE, fc=BOX, tc=INK):
    rbox(ax, x, y, w, h, edge=edge, lw=1.05, fc=fc)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            color=tc, fontsize=10.0, fontweight="600", zorder=3)


def main():
    fig, ax = plt.subplots(figsize=(9.6, 6.15), facecolor=PAPER)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.15)
    ax.axis("off")
    ax.set_facecolor(PAPER)

    ax.text(5.0, 6.88, "Prefer needs disagreement. A true why is not a format trick.",
            ha="center", va="center", color=MUTED, fontsize=8.6)

    # --- fail band ---
    rbox(ax, 0.35, 3.85, 9.3, 2.55, edge=SPINE, lw=1.1, fc="#201b17")
    ax.text(0.58, 6.08, "Tried · letter GRPO on a saturated SFT",
            ha="left", va="center", color=MUTED, fontsize=8.2, zorder=3)
    cw, ch = 0.78, 0.72
    x0, y0 = 0.70, 4.55
    for i in range(8):
        chip(ax, x0 + i * 0.92, y0, cw, ch, "B", edge=SPINE, fc="#2c2620", tc=MUTED)
    ax.text(8.55, 4.91, "G = 8", ha="center", va="center",
            color=MUTED, fontsize=7.8, zorder=3)
    ax.text(5.0, 4.22, "all correct  ·  reward-std = 0  ·  no gradient",
            ha="center", va="center", color=MUTED, fontsize=9.0, zorder=3)

    # --- work band ---
    rbox(ax, 0.35, 0.35, 9.3, 3.15, edge=ACCENT, lw=1.45, fc="#241c16")
    ax.text(0.58, 3.18, "Worked · gold traces first, then format GRPO",
            ha="left", va="center", color=ACCENT, fontsize=8.2, zorder=3)

    rbox(ax, 0.70, 1.45, 3.35, 1.35, edge=GOLD, lw=1.4)
    ax.text(2.375, 2.38, "Gold why", ha="center", va="center",
            color=INK, fontsize=12.0, fontweight="600", zorder=4)
    ax.text(2.375, 1.88, "TR traces from the generator",
            ha="center", va="center", color=MUTED, fontsize=8.0, zorder=4)

    arrow(ax, (4.15, 2.12), (4.85, 2.12), GOLD)

    rbox(ax, 4.85, 1.45, 4.45, 1.35, edge=ACCENT, lw=1.5)
    ax.text(7.075, 2.38, "SFT on the LLM", ha="center", va="center",
            color=INK, fontsize=12.0, fontweight="600", zorder=4)
    ax.text(7.075, 1.88, "true chain, then the letter",
            ha="center", va="center", color=MUTED, fontsize=8.0, zorder=4)

    ax.text(5.0, 0.78, "GRPO after that teaches boxing. Accuracy already moved.",
            ha="center", va="center", color=MUTED, fontsize=8.4, zorder=3)

    save(fig, "slide17-prefer.png")


if __name__ == "__main__":
    main()
