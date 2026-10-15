#!/usr/bin/env python3
"""Slide 3: one authentic-style item per official bench."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

MUTED = "#b7a99a"
ACCENT = "#d4783c"
GOLD = "#e8c07a"
PAPER = "#1c1814"
SPINE = "#3a322b"

OUT = Path(__file__).resolve().parent


def style_ax(ax):
    ax.set_facecolor(PAPER)
    ax.tick_params(colors=MUTED, labelsize=9, length=0)
    for sp in ax.spines.values():
        sp.set_color(SPINE)
    ax.set_xticks([])
    ax.set_ylabel("")
    ax.grid(color=SPINE, linewidth=0.5, alpha=0.9)


def save(fig, name):
    fig.savefig(
        OUT / name,
        dpi=160,
        facecolor=PAPER,
        bbox_inches="tight",
        pad_inches=0.12,
    )
    plt.close(fig)


def main():
    t = np.linspace(0, 8 * np.pi, 240)
    saw = (t / np.pi) % 2 - 1
    fig, ax = plt.subplots(figsize=(9.2, 2.05), facecolor=PAPER)
    style_ax(ax)
    ax.plot(saw, color=ACCENT, lw=1.6)
    save(fig, "slide3-tsexam.png")

    x = np.linspace(0, 1, 160)
    y = 12 + 1.4 * np.sin(2 * np.pi * x * 3)
    y[72:76] += np.array([4.0, 8.2, 8.0, 3.2])
    fig, ax = plt.subplots(figsize=(9.2, 2.05), facecolor=PAPER)
    style_ax(ax)
    ax.plot(y, color=GOLD, lw=1.45)
    ax.scatter([74], [y[74]], color=ACCENT, s=28, zorder=3)
    ax.annotate(
        "t",
        xy=(74, y[74]),
        xytext=(88, y[74] + 2.2),
        color=MUTED,
        fontsize=11,
        arrowprops=dict(arrowstyle="-", color=ACCENT, lw=1.0),
    )
    save(fig, "slide3-chatts.png")

    z = np.zeros(260)
    z += 0.08 * np.sin(np.linspace(0, 18 * np.pi, 260))
    # Burst first, then level drop, then a late spike — not the order named in the question.
    burst = np.linspace(0, 8 * np.pi, 36)
    z[48:84] += 0.55 * np.sin(burst * 3) * np.hanning(36)
    z[110:] -= 0.85
    z[198:204] += np.array([0.4, 1.35, 1.5, 0.9, 0.35, 0.1])
    fig, ax = plt.subplots(figsize=(9.2, 2.05), facecolor=PAPER)
    style_ax(ax)
    ax.plot(z, color=GOLD, lw=1.45)
    save(fig, "slide3-tsrbench.png")


if __name__ == "__main__":
    main()
