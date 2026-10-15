#!/usr/bin/env python3
"""Slide 20: kill the mix that helped the average.

Ownership numbers from the TR-synth promotion gate (not the slide-19
8B champion board): reasoning avg 29.5 → 31.2, AR/IR +7 pp, TR 26.9 → 21.9.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

INK = "#f3ece3"
MUTED = "#b7a99a"
ACCENT = "#d4783c"
TEAL = "#7eb8a8"
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
        p, q, arrowstyle="-|>", mutation_scale=13, lw=1.4,
        color=color, zorder=3, shrinkA=0, shrinkB=0,
    ))


def readout(ax, y, lab, left, right, color):
    ax.text(0.85, y + 0.72, lab, ha="left", va="center",
            color=MUTED, fontsize=8.4, zorder=4)
    ax.text(2.55, y + 0.28, left, ha="center", va="center",
            color=INK, fontsize=15.5, fontweight="600", zorder=4)
    arrow(ax, (3.45, y + 0.28), (5.15, y + 0.28), color)
    ax.text(6.05, y + 0.28, right, ha="center", va="center",
            color=color, fontsize=15.5, fontweight="600", zorder=4)


def main():
    fig, ax = plt.subplots(figsize=(9.6, 6.15), facecolor=PAPER)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.15)
    ax.axis("off")
    ax.set_facecolor(PAPER)

    ax.text(5.0, 6.88, "Same mix. Three readouts. The headline is not the slice.",
            ha="center", va="center", color=MUTED, fontsize=8.6)

    rbox(ax, 0.35, 3.55, 9.3, 2.95, edge=SPINE, lw=1.1, fc="#201b17")
    ax.text(0.58, 6.15, "Looked like a win",
            ha="left", va="center", color=MUTED, fontsize=8.2, zorder=3)
    readout(ax, 5.05, "Reasoning average", "29.5", "31.2", TEAL)
    ax.text(8.55, 5.33, "+1.8 pp", ha="center", va="center",
            color=TEAL, fontsize=9.2, fontweight="600", zorder=4)

    rbox(ax, 0.70, 3.78, 8.55, 0.95, edge=SPINE, lw=1.0, fc="#2c2620")
    ax.text(0.95, 4.25, "AR / IR", ha="left", va="center",
            color=MUTED, fontsize=8.4, zorder=4)
    ax.text(5.0, 4.25, "+7 pp each", ha="center", va="center",
            color=GOLD, fontsize=15.0, fontweight="600", zorder=4)
    ax.text(8.55, 4.25, "shipped?", ha="center", va="center",
            color=MUTED, fontsize=8.4, zorder=4)

    rbox(ax, 0.35, 0.35, 9.3, 2.90, edge=ACCENT, lw=1.45, fc="#241c16")
    ax.text(0.58, 2.90, "The slice I built the data for",
            ha="left", va="center", color=ACCENT, fontsize=8.2, zorder=3)
    readout(ax, 1.55, "Temporal relation", "26.9", "21.9", ACCENT)
    ax.text(5.0, 0.78, "−5 pp. Gate written before the run. Kill.",
            ha="center", va="center", color=MUTED, fontsize=9.0, zorder=3)

    save(fig, "slide20-kill.png")


if __name__ == "__main__":
    main()
