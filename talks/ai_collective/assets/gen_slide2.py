#!/usr/bin/env python3
"""Slide 2: describe / compare / explain on the same real series."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

MUTED = "#b7a99a"
ACCENT = "#d4783c"
TEAL = "#7eb8a8"
GOLD = "#e8c07a"
PAPER = "#1c1814"
SPINE = "#3a322b"

OUT = Path(__file__).resolve().parent
CSV = OUT / "daily-min-temperatures.csv"


def load_temps():
    dates, vals = [], []
    with CSV.open() as f:
        next(f)
        for line in f:
            d, t = line.strip().replace('"', "").split(",")
            dates.append(d)
            vals.append(float(t))
    return np.array(dates), np.array(vals, dtype=float)


def year(dates, y, start):
    m = (dates >= start) & (dates < f"{int(start[:4]) + 1}-01-01")
    return y[m]


def style_ax(ax, ylabel=True):
    ax.set_facecolor(PAPER)
    ax.tick_params(colors=MUTED, labelsize=10, length=0)
    for sp in ax.spines.values():
        sp.set_color(SPINE)
    ax.set_xlabel("")
    if ylabel:
        ax.set_ylabel("°C", color=MUTED)
    else:
        ax.set_ylabel("")
    ax.grid(color=SPINE, linewidth=0.5, alpha=0.9)
    ax.set_xticks([])


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
    dates, y = load_temps()
    y85 = year(dates, y, "1985-01-01")
    y87 = year(dates, y, "1987-01-01")
    n = min(len(y85), len(y87))
    y85, y87 = y85[:n], y87[:n]

    fig, ax = plt.subplots(figsize=(9.2, 2.05), facecolor=PAPER)
    style_ax(ax)
    ax.plot(y85, color=ACCENT, lw=1.35)
    save(fig, "slide2-describe.png")

    fig, ax = plt.subplots(figsize=(9.2, 2.05), facecolor=PAPER)
    style_ax(ax)
    ax.plot(y85, color=ACCENT, lw=1.25, alpha=0.95)
    ax.plot(y87, color=TEAL, lw=1.25, alpha=0.95)
    save(fig, "slide2-compare.png")

    w = y85[90:250]
    d = np.diff(w)
    drop = int(np.argmin(d)) + 1
    fig, ax = plt.subplots(figsize=(9.2, 2.05), facecolor=PAPER)
    style_ax(ax)
    ax.plot(w, color=GOLD, lw=1.4)
    ax.scatter([drop - 1], [w[drop - 1]], color=ACCENT, s=36, zorder=3)
    ax.scatter([drop], [w[drop]], color=ACCENT, s=36, zorder=3)
    ax.annotate(
        "",
        xy=(drop, w[drop]),
        xytext=(drop - 1, w[drop - 1]),
        arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.4),
    )
    save(fig, "slide2-explain.png")


if __name__ == "__main__":
    main()
