#!/usr/bin/env python3
"""Motivation slide: the expert object is a wall of numbers."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

INK = "#f3ece3"
MUTED = "#b7a99a"
PAPER = "#1c1814"
SPINE = "#3a322b"

OUT = Path(__file__).resolve().parent
CSV = OUT / "daily-min-temperatures.csv"


def load_temps():
    vals = []
    with CSV.open() as f:
        next(f)
        for line in f:
            vals.append(float(line.strip().replace('"', "").split(",")[1]))
    return np.array(vals, dtype=float)


def main():
    y = load_temps()[:168]  # 24 weeks
    rows = ["  ".join(f"{v:4.1f}" for v in y[i : i + 12]) for i in range(0, len(y), 12)]
    text = "ts  daily min °C\n\n" + "\n".join(rows)

    fig, ax = plt.subplots(figsize=(8.4, 4.6), facecolor=PAPER)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_axis_off()
    ax.set_facecolor(PAPER)
    ax.add_patch(FancyBboxPatch(
        (0.03, 0.05), 0.94, 0.90,
        boxstyle="round,pad=0.012,rounding_size=0.03",
        facecolor="#14110e", edgecolor=SPINE, linewidth=1.15,
    ))
    ax.text(
        0.07, 0.90, text,
        va="top", ha="left",
        fontfamily="monospace", fontsize=8.4, color=MUTED, linespacing=1.38,
    )
    fig.savefig(
        OUT / "who-motive-numbers.png",
        dpi=160,
        facecolor=PAPER,
        bbox_inches="tight",
        pad_inches=0.12,
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
