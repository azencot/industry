#!/usr/bin/env python3
"""Panel Q2: when a scene camera helps vs when it is the label.

Plain: a camera is a picture of the room, not another plot of the signal.
Helps when the series looks fine and the scene does not. Cheats when the
frame already shows the answer (warning light) so the model never listens.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
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


def wave_ax(ax, y, color, spike=False):
    t = np.linspace(0, 1, 180)
    s = 0.55 * np.sin(2 * np.pi * 4 * t)
    if spike:
        s = s.copy()
        s[88:96] += 1.35
    ax.plot(t, s, color=color, lw=1.35)
    ax.set_xlim(0, 1)
    ax.set_ylim(-2.1, 2.1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor(PAPER)
    for sp in ax.spines.values():
        sp.set_color(SPINE)
        sp.set_linewidth(0.8)


def panel_axes(fig, ax, x, y, w, h):
    ins = inset_axes(
        ax, width="100%", height="100%",
        bbox_to_anchor=(x, y, w, h),
        bbox_transform=ax.transData, loc="center", borderpad=0,
    )
    ins.set_xticks([])
    ins.set_yticks([])
    for sp in ins.spines.values():
        sp.set_visible(False)
    ins.set_facecolor(PAPER)
    return ins


def main():
    fig, ax = plt.subplots(figsize=(9.6, 6.15), facecolor=PAPER)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.15)
    ax.axis("off")
    ax.set_facecolor(PAPER)

    ax.text(5.0, 6.88, "A camera is a picture of the room, not another plot of the signal.",
            ha="center", va="center", color=MUTED, fontsize=8.6)

    rbox(ax, 0.35, 3.55, 9.3, 2.95, edge=TEAL, lw=1.35, fc="#1c221f")
    ax.text(0.58, 6.18, "Adds a fact the series does not have",
            ha="left", va="center", color=TEAL, fontsize=8.4, zorder=3)

    rbox(ax, 0.70, 3.80, 3.85, 1.95, edge=SPINE, lw=1.05)
    ax.text(2.625, 5.52, "Vibration", ha="center", va="center",
            color=MUTED, fontsize=8.0, zorder=4)
    w1 = panel_axes(fig, ax, 0.95, 3.95, 3.35, 1.25)
    wave_ax(w1, None, GOLD, spike=False)

    rbox(ax, 5.05, 3.80, 4.20, 1.95, edge=SPINE, lw=1.05)
    ax.text(7.15, 5.52, "Housing", ha="center", va="center",
            color=MUTED, fontsize=8.0, zorder=4)
    # Physical casing, not a second waveform.
    ax.add_patch(Rectangle((5.70, 4.00), 2.90, 1.28, linewidth=1.35,
                           edgecolor=GOLD, facecolor="#2a221c", zorder=3))
    ax.plot([6.55, 6.40, 6.72, 6.58, 6.90], [4.00, 4.38, 4.62, 4.95, 5.28],
            color=ACCENT, lw=2.2, zorder=4, solid_capstyle="round")
    ax.text(8.22, 4.58, "crack", ha="left", va="center",
            color=ACCENT, fontsize=8.2, zorder=5)

    rbox(ax, 0.35, 0.35, 9.3, 2.90, edge=ACCENT, lw=1.45, fc="#241c16")
    ax.text(0.58, 2.92, "Is the answer — the model never has to listen",
            ha="left", va="center", color=ACCENT, fontsize=8.4, zorder=3)

    rbox(ax, 0.70, 0.60, 3.85, 1.90, edge=SPINE, lw=1.05)
    ax.text(2.625, 2.28, "Knock", ha="center", va="center",
            color=MUTED, fontsize=8.0, zorder=4)
    w2 = panel_axes(fig, ax, 0.95, 0.75, 3.35, 1.20)
    wave_ax(w2, None, GOLD, spike=True)

    rbox(ax, 5.05, 0.60, 4.20, 1.90, edge=SPINE, lw=1.05)
    ax.text(7.15, 2.28, "Warning light already on", ha="center", va="center",
            color=MUTED, fontsize=8.0, zorder=4)
    ax.add_patch(Circle((7.15, 1.28), 0.42, facecolor=ACCENT, edgecolor=GOLD,
                        linewidth=1.2, zorder=4))
    ax.text(7.15, 1.28, "ON", ha="center", va="center",
            color=PAPER, fontsize=9.5, fontweight="600", zorder=5)

    save(fig, "slide25-camera.png")


if __name__ == "__main__":
    main()
