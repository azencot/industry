#!/usr/bin/env python3
"""Slide 21: scale is three jobs, not a ladder.

0.8B chooses; 8B is still the TSExam/TSRBench quote; 27B wins ChatTS cat.
9B/27B do not beat 8B on TSRBench (~0.41–0.43). Do not put 122B or 0.9316
on the figure. Don't mix unlabeled campaigns into one ranking.
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
        p, q, arrowstyle="-|>", mutation_scale=12, lw=1.25,
        color=color, zorder=3, shrinkA=1.5, shrinkB=1.5,
    ))


def chip(ax, x, y, w, h, title, sub, edge=SPINE, fc=BOX, tc=INK, sc=MUTED, lw=1.2):
    rbox(ax, x, y, w, h, edge=edge, lw=lw, fc=fc)
    ax.text(x + w / 2, y + h * 0.62, title, ha="center", va="center",
            color=tc, fontsize=13.0, fontweight="600", zorder=4)
    ax.text(x + w / 2, y + h * 0.28, sub, ha="center", va="center",
            color=sc, fontsize=8.2, zorder=4)


def main():
    fig, ax = plt.subplots(figsize=(9.6, 6.15), facecolor=PAPER)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.15)
    ax.axis("off")
    ax.set_facecolor(PAPER)

    ax.text(5.0, 6.88, "Different campaigns. Not one ranking.",
            ha="center", va="center", color=MUTED, fontsize=8.6)

    rbox(ax, 0.35, 3.85, 9.3, 2.65, edge=SPINE, lw=1.1, fc="#201b17")
    ax.text(0.58, 6.15, "The ladder people want",
            ha="left", va="center", color=MUTED, fontsize=8.2, zorder=3)

    cw, ch = 1.85, 1.05
    y = 4.55
    chip(ax, 0.85, y, cw, ch, "0.8B", "pilot", fc="#2c2620", tc=MUTED, sc=MUTED)
    chip(ax, 4.08, y, cw, ch, "8B", "then bigger", fc="#2c2620", tc=MUTED, sc=MUTED)
    chip(ax, 7.30, y, cw, ch, "27B", "wins everything", fc="#2c2620", tc=MUTED, sc=MUTED)
    arrow(ax, (2.75, y + ch / 2), (4.03, y + ch / 2))
    arrow(ax, (5.98, y + ch / 2), (7.25, y + ch / 2))

    ax.text(5.0, 4.18, "who wins everything",
            ha="center", va="center", color=MUTED, fontsize=9.2, zorder=4)
    ax.plot([3.15, 6.85], [4.18, 4.18], color=ACCENT, lw=1.7, zorder=5, solid_capstyle="round")

    rbox(ax, 0.35, 0.35, 9.3, 3.20, edge=ACCENT, lw=1.45, fc="#241c16")
    ax.text(0.58, 3.20, "What I actually quote",
            ha="left", va="center", color=ACCENT, fontsize=8.2, zorder=3)

    jw, jh = 2.70, 1.55
    jy = 1.25
    chip(ax, 0.70, jy, jw, jh, "0.8B", "choose the recipe",
         edge=SPINE, fc=BOX, tc=INK, sc=MUTED)
    chip(ax, 3.65, jy, jw, jh, "8B", "exam + TSRBench",
         edge=ACCENT, lw=1.5, fc="#2a2018", tc=INK, sc=GOLD)
    chip(ax, 6.60, jy, jw, jh, "27B", "ChatTS cat",
         edge=GOLD, lw=1.3, fc=BOX, tc=INK, sc=GOLD)

    ax.text(5.0, 0.78, "9B / 27B TSRBench  ~0.41–0.43.  Not a bigger north star.",
            ha="center", va="center", color=MUTED, fontsize=8.6, zorder=3)

    save(fig, "slide21-scale.png")


if __name__ == "__main__":
    main()
