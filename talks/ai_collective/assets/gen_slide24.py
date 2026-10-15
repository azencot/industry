#!/usr/bin/env python3
"""Panel Q1: one model, not one renderer.

Shared LLM / VLM backbone. STFT for frequency-rich sensors; chart+delay
for slow series. Do not upsample onto one grid. Not a Bosch run.
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
        p, q, arrowstyle="-|>", mutation_scale=12, lw=1.35,
        color=color, zorder=3, shrinkA=2, shrinkB=2,
    ))


def chip(ax, x, y, w, h, title, sub, edge=SPINE, fc=BOX, tc=INK, sc=MUTED, lw=1.2):
    rbox(ax, x, y, w, h, edge=edge, lw=lw, fc=fc)
    ax.text(x + w / 2, y + h * 0.62, title, ha="center", va="center",
            color=tc, fontsize=12.5, fontweight="600", zorder=4)
    ax.text(x + w / 2, y + h * 0.28, sub, ha="center", va="center",
            color=sc, fontsize=8.2, zorder=4)


def main():
    fig, ax = plt.subplots(figsize=(9.6, 6.15), facecolor=PAPER)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.15)
    ax.axis("off")
    ax.set_facecolor(PAPER)

    ax.text(5.0, 6.88, "Unified architecture. Not a unified tokenizer.",
            ha="center", va="center", color=MUTED, fontsize=8.6)

    rbox(ax, 0.35, 4.05, 9.3, 2.45, edge=SPINE, lw=1.1, fc="#201b17")
    ax.text(0.58, 6.18, "What I do not do",
            ha="left", va="center", color=MUTED, fontsize=8.2, zorder=3)
    chip(ax, 0.70, 4.35, 4.00, 1.35, "One patch, one rate",
         "audio and telemetry alike", fc="#2c2620", tc=MUTED, sc=MUTED)
    chip(ax, 5.30, 4.35, 4.00, 1.35, "Upsample onto one grid",
         "slow channel sparse, fast explodes", fc="#2c2620", tc=MUTED, sc=MUTED)
    ax.plot([0.95, 4.45], [5.02, 5.02], color=ACCENT, lw=1.7, zorder=5, solid_capstyle="round")
    ax.plot([5.55, 9.05], [5.02, 5.02], color=ACCENT, lw=1.7, zorder=5, solid_capstyle="round")

    rbox(ax, 0.35, 0.35, 9.3, 3.40, edge=ACCENT, lw=1.45, fc="#241c16")
    ax.text(0.58, 3.42, "What I do",
            ha="left", va="center", color=ACCENT, fontsize=8.2, zorder=3)

    chip(ax, 0.70, 1.55, 3.35, 1.45, "STFT", "mic, shaker, …",
         edge=ACCENT, lw=1.4, fc="#2a2018", tc=INK, sc=GOLD)
    chip(ax, 0.70, 0.55, 3.35, 0.85, "Chart + delay", "slow series",
         edge=TEAL, lw=1.3, fc=BOX, tc=INK, sc=TEAL)

    arrow(ax, (4.15, 2.28), (5.35, 1.85), GOLD)
    arrow(ax, (4.15, 0.98), (5.35, 1.70), TEAL)

    rbox(ax, 5.35, 0.70, 3.90, 2.15, edge=GOLD, lw=1.5)
    ax.text(7.30, 2.15, "One VLM", ha="center", va="center",
            color=INK, fontsize=16.0, fontweight="600", zorder=4)
    ax.text(7.30, 1.45, "shared backbone", ha="center", va="center",
            color=MUTED, fontsize=9.0, zorder=4)

    save(fig, "slide24-onemodel.png")


if __name__ == "__main__":
    main()
