#!/usr/bin/env python3
"""Panel: high- vs low-frequency — clocks align, do not upsample.

Naive: resample onto the fast clock → sparse slow channel, sequence explodes.
Do: STFT / short windows for the mic; chart+delay or coarse patches for
telemetry; fuse on a coarser grid. Same backbone as slide 24; different rates.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

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
        p, q, arrowstyle="-|>", mutation_scale=11, lw=1.3,
        color=color, zorder=3, shrinkA=2, shrinkB=2,
    ))


def mini(fig, ax, x, y, w, h):
    ins = inset_axes(
        ax, width="100%", height="100%",
        bbox_to_anchor=(x, y, w, h),
        bbox_transform=ax.transData, loc="center", borderpad=0,
    )
    ins.set_xticks([])
    ins.set_yticks([])
    ins.set_facecolor(PAPER)
    for sp in ins.spines.values():
        sp.set_color(SPINE)
        sp.set_linewidth(0.7)
    return ins


def main():
    fig, ax = plt.subplots(figsize=(9.6, 6.15), facecolor=PAPER)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.15)
    ax.axis("off")
    ax.set_facecolor(PAPER)

    ax.text(5.0, 6.88, "Clocks must agree. Do not upsample the slow channel onto the audio grid.",
            ha="center", va="center", color=MUTED, fontsize=8.6)

    # --- don't ---
    rbox(ax, 0.35, 3.55, 9.3, 2.95, edge=SPINE, lw=1.15, fc="#201b17")
    ax.text(0.58, 6.18, "Naive — one shared sample clock",
            ha="left", va="center", color=MUTED, fontsize=8.3, zorder=3)

    rbox(ax, 0.55, 3.75, 2.55, 2.05, edge=SPINE, lw=1.05)
    ax.text(1.82, 5.55, "Audio", ha="center", color=MUTED, fontsize=8.0, zorder=4)
    w_fast = mini(fig, ax, 0.70, 3.90, 2.25, 1.35)
    t = np.linspace(0, 1, 220)
    w_fast.plot(t, 0.7 * np.sin(2 * np.pi * 18 * t), color=GOLD, lw=1.05)
    w_fast.set_xlim(0, 1)
    w_fast.set_ylim(-1.2, 1.2)

    rbox(ax, 3.30, 3.75, 2.55, 2.05, edge=SPINE, lw=1.05)
    ax.text(4.57, 5.55, "Telemetry, upsampled", ha="center", color=MUTED, fontsize=8.0, zorder=4)
    w_slow = mini(fig, ax, 3.45, 3.90, 2.25, 1.35)
    ts = np.linspace(0, 1, 12)
    ys = 0.45 * np.sin(2 * np.pi * 1.5 * ts)
    w_slow.step(ts, ys, where="mid", color=TEAL, lw=1.35)
    w_slow.set_xlim(0, 1)
    w_slow.set_ylim(-1.2, 1.2)

    arrow(ax, (5.95, 4.78), (6.85, 4.78), ACCENT)
    rbox(ax, 6.90, 3.85, 2.45, 1.85, edge=ACCENT, lw=1.35, fc="#2c221c")
    ax.text(8.12, 5.22, "Concat", ha="center", color=INK, fontsize=12.5,
            fontweight="600", zorder=4)
    ax.text(8.12, 4.55, "sparse + explode", ha="center", color=ACCENT, fontsize=8.4, zorder=4)
    ax.plot([7.25, 8.95], [4.78, 4.78], color=ACCENT, lw=1.5, zorder=5)

    # --- do ---
    rbox(ax, 0.35, 0.28, 9.3, 3.05, edge=ACCENT, lw=1.45, fc="#241c16")
    ax.text(0.58, 3.02, "Encode at native rate, fuse coarser",
            ha="left", va="center", color=ACCENT, fontsize=8.3, zorder=3)

    rbox(ax, 0.55, 0.50, 2.70, 2.20, edge=GOLD, lw=1.3, fc="#2a2018")
    ax.text(1.90, 2.42, "STFT", ha="center", color=INK, fontsize=13.0,
            fontweight="600", zorder=4)
    ax.text(1.90, 1.95, "mic / shaker", ha="center", color=GOLD, fontsize=8.2, zorder=4)
    spec = mini(fig, ax, 0.78, 0.65, 2.25, 1.05)
    f = np.abs(np.sin(np.linspace(0, 4 * np.pi, 48)[:, None] + np.linspace(0, 2, 28)))
    spec.imshow(f.T, aspect="auto", cmap="magma", origin="lower")
    spec.set_xticks([])
    spec.set_yticks([])

    rbox(ax, 3.45, 0.50, 2.70, 2.20, edge=TEAL, lw=1.3)
    ax.text(4.80, 2.42, "Chart + delay", ha="center", color=INK, fontsize=12.5,
            fontweight="600", zorder=4)
    ax.text(4.80, 1.95, "slow telemetry", ha="center", color=TEAL, fontsize=8.2, zorder=4)
    ch = mini(fig, ax, 3.68, 0.65, 2.25, 1.05)
    tt = np.linspace(0, 1, 80)
    ch.plot(tt, 0.55 * np.sin(2 * np.pi * 2 * tt) + 0.15 * tt, color=TEAL, lw=1.4)
    ch.set_xlim(0, 1)
    ch.set_ylim(-1.0, 1.2)

    arrow(ax, (6.25, 1.60), (7.05, 1.60), GOLD)
    rbox(ax, 7.10, 0.55, 2.25, 2.10, edge=GOLD, lw=1.5)
    ax.text(8.22, 1.95, "One VLM", ha="center", color=INK, fontsize=14.0,
            fontweight="600", zorder=4)
    ax.text(8.22, 1.35, "shared backbone", ha="center", color=MUTED, fontsize=8.4, zorder=4)
    ax.text(8.22, 0.88, "different rates", ha="center", color=GOLD, fontsize=8.4, zorder=4)

    save(fig, "slide25-rates.png")


if __name__ == "__main__":
    main()
