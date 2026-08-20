#!/usr/bin/env python3
"""Slide 16: Stage B — freeze inverted from Stage A.

Matched to dual_*_capall_*_stageB.yaml: merge Stage A (vision frozen),
LM-only LoRA. Target is QA, with TR traces on the exam mix only.
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


def module(ax, x, y, w, h, title, sub, badge, train=False):
    edge = ACCENT if train else SPINE
    rbox(ax, x, y, w, h, edge=edge, lw=1.6 if train else 1.15)
    ax.text(x + w / 2, y + h * 0.68, title, ha="center", va="center",
            color=INK, fontsize=11.2, fontweight="600", zorder=3)
    ax.text(x + w / 2, y + h * 0.42, sub, ha="center", va="center",
            color=MUTED, fontsize=8.0, zorder=3)
    bw, bh = 0.72, 0.22
    bx = x + (w - bw) / 2
    by = y + 0.10
    rbox(ax, bx, by, bw, bh, edge=ACCENT if train else SPINE, lw=0,
         fc=ACCENT if train else "#2c2620")
    ax.text(bx + bw / 2, by + bh / 2, badge, ha="center", va="center",
            color=INK if train else MUTED, fontsize=7.6, fontweight="700",
            zorder=4)


def main():
    fig, ax = plt.subplots(figsize=(9.6, 6.15), facecolor=PAPER)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.15)
    ax.axis("off")
    ax.set_facecolor(PAPER)

    ax.text(5.0, 6.88, "Stage A is merged in. The LLM LoRAs. Delay LoRA is optional.",
            ha="center", va="center", color=MUTED, fontsize=8.6)

    tw, th = 3.15, 1.58
    y_tow = 4.85
    module(ax, 0.85, y_tow, tw, th, "Chart ViT", "still frozen", "FROZEN", False)
    module(ax, 6.00, y_tow, tw, th, "Delay DINOv3", "frozen on 8B generalist", "FROZEN", False)

    lw, lh = 5.4, 1.42
    lx, ly = 2.3, 2.72
    module(ax, lx, ly, lw, lh, "Language model", "fresh LoRA on the LLM", "TRAINS", True)

    arrow(ax, (0.85 + tw / 2, y_tow), (lx + lw * 0.32, ly + lh), MUTED)
    arrow(ax, (6.00 + tw / 2, y_tow), (lx + lw * 0.68, ly + lh), MUTED)

    cx, cy, cw, ch = 1.5, 1.18, 7.0, 1.05
    rbox(ax, cx, cy, cw, ch, edge=GOLD, lw=1.35)
    ax.text(5.0, cy + ch * 0.68, "Target · an answer", ha="center", va="center",
            color=GOLD, fontsize=8.2, fontweight="600", zorder=3)
    ax.text(5.0, cy + ch * 0.32, "letter   ·   number   ·   why, then the letter",
            ha="center", va="center", color=INK, fontsize=11.2, zorder=3)
    arrow(ax, (5.0, ly), (5.0, cy + ch), ACCENT)

    chips = [
        (0.55, "Exam MCQ"),
        (3.55, "ChatTS QA"),
        (6.85, "Numeric"),
    ]
    for x, lab in chips:
        rbox(ax, x, 0.22, 2.6, 0.68, edge=SPINE, lw=1.0)
        ax.text(x + 1.3, 0.56, lab, ha="center", va="center",
                color=MUTED, fontsize=8.4, zorder=3)

    save(fig, "slide16-unfreeze.png")


if __name__ == "__main__":
    main()
