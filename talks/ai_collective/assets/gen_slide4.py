#!/usr/bin/env python3
"""Slide 4: same short series, three interfaces, side by side."""
from pathlib import Path

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

OUT = Path(__file__).resolve().parent
Y = np.array([2.1, 2.4, 2.8, 3.1, 2.9, 3.4, 3.6, 3.3, 3.8, 4.1, 3.9, 4.4, 4.7, 4.5, 5.0, 5.2])
PATCH_C = [ACCENT, GOLD, TEAL, "#c48a62"]


def save(fig, name):
    fig.savefig(OUT / name, dpi=160, facecolor=PAPER, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)


def text_board():
    fig, ax = plt.subplots(figsize=(5.4, 3.6), facecolor=PAPER)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_axis_off()
    ax.set_facecolor(PAPER)
    box = FancyBboxPatch(
        (0.04, 0.08), 0.92, 0.84,
        boxstyle="round,pad=0.02,rounding_size=0.04",
        facecolor="#14110e", edgecolor=SPINE, linewidth=1.2,
    )
    ax.add_patch(box)
    prompt = (
        "Q: Is the series increasing?\n\n"
        "ts: 2.1, 2.4, 2.8, 3.1,\n"
        "    2.9, 3.4, 3.6, 3.3,\n"
        "    3.8, 4.1, 3.9, 4.4,\n"
        "    4.7, 4.5, 5.0, 5.2"
    )
    ax.text(
        0.10, 0.86, prompt,
        va="top", ha="left",
        fontfamily="monospace", fontsize=10.5, color=INK, linespacing=1.45,
    )
    save(fig, "slide4-text.png")


def patch_board():
    fig, ax = plt.subplots(figsize=(5.4, 3.6), facecolor=PAPER)
    ax.set_facecolor(PAPER)
    ax.set_xlim(-0.6, 15.6)
    ax.set_ylim(-1.35, 6.4)
    ax.set_axis_off()
    n = len(Y)
    pw = n // 4
    for p in range(4):
        x0 = p * pw - 0.45
        ax.add_patch(Rectangle(
            (x0, 1.7), pw - 0.1, 4.0,
            facecolor=PATCH_C[p], alpha=0.18, edgecolor=PATCH_C[p], linewidth=1.0, zorder=0,
        ))
    ax.plot(np.arange(n), Y, color=GOLD, lw=1.8, zorder=2)
    ax.scatter(np.arange(n), Y, s=12, color=INK, zorder=3)
    for p in range(4):
        cx = p * pw + (pw - 1) / 2
        ax.annotate(
            "", xy=(cx, 0.55), xytext=(cx, 1.65),
            arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.1),
        )
        ax.add_patch(FancyBboxPatch(
            (cx - 1.15, -0.85), 2.3, 1.15,
            boxstyle="round,pad=0.02,rounding_size=0.12",
            facecolor="#14110e", edgecolor=PATCH_C[p], linewidth=1.2,
        ))
        ax.text(cx, -0.22, "enc", ha="center", va="center",
                fontfamily="monospace", fontsize=9, color=INK)
    save(fig, "slide4-patch.png")


def chart_table_board():
    fig = plt.figure(figsize=(5.4, 3.6), facecolor=PAPER)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.15, 0.85], wspace=0.12)
    ax = fig.add_subplot(gs[0])
    ax.set_facecolor(PAPER)
    ax.plot(np.arange(len(Y)), Y, color=ACCENT, lw=1.8)
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_color(SPINE)
    ax.set_title("plot", color=MUTED, fontsize=10, pad=6, fontfamily="monospace")

    ax2 = fig.add_subplot(gs[1])
    ax2.set_facecolor(PAPER)
    ax2.set_axis_off()
    ax2.set_title("table", color=MUTED, fontsize=10, pad=6, fontfamily="monospace")
    rows = [["t", "x"]] + [[str(i), f"{v:.1f}"] for i, v in enumerate(Y[:8])]
    table = ax2.table(
        cellText=rows, loc="center", cellLoc="center",
        colWidths=[0.38, 0.5],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8.5)
    table.scale(1.05, 1.28)
    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor(SPINE)
        cell.set_facecolor("#14110e" if r else "#2a221c")
        cell.set_text_props(color=GOLD if r == 0 else INK, fontfamily="monospace")
    save(fig, "slide4-charttable.png")


if __name__ == "__main__":
    text_board()
    patch_board()
    chart_table_board()
