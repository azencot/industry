#!/usr/bin/env python3
"""Postdoc slide: von Kármán street past a cylinder, deck palette.

Schematic vorticity (staggered Gaussian vortices), not a paper figure
and not a live CFD run. The picture is the testbed, not the theorem.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle

PAPER = "#1c1814"
SPINE = "#3a322b"
ACCENT = "#d4783c"
TEAL = "#7eb8a8"
GOLD = "#e8c07a"

OUT = Path(__file__).resolve().parent


def vortex(x, y, x0, y0, circ, sig):
    return circ * np.exp(-((x - x0) ** 2 + (y - y0) ** 2) / (2 * sig ** 2))


def main():
    nx, ny = 900, 320
    x = np.linspace(0.0, 9.2, nx)
    y = np.linspace(-1.55, 1.55, ny)
    X, Y = np.meshgrid(x, y)

    vort = np.zeros_like(X)
    spacing, half, sig = 1.12, 0.34, 0.18
    x0 = 2.05
    for n in range(7):
        vort += vortex(X, Y, x0 + n * spacing, half, 1.0, sig)
        vort += vortex(X, Y, x0 + (n + 0.5) * spacing, -half, -1.0, sig)

    # shear attached to the cylinder so the street has a source
    cx, cy, radius = 1.15, 0.0, 0.48
    ang = np.arctan2(Y - cy, X - cx)
    dist = np.sqrt((X - cx) ** 2 + (Y - cy) ** 2)
    shell = np.exp(-((dist - radius) ** 2) / (2 * 0.07 ** 2))
    vort += 0.55 * np.sin(ang) * shell

    obstacle = dist <= radius
    vort[obstacle] = np.nan

    vmax = np.nanpercentile(np.abs(vort), 99)
    cmap = LinearSegmentedColormap.from_list(
        "vort",
        [TEAL, "#3d6a64", PAPER, "#6b3d24", ACCENT, GOLD],
    )
    cmap.set_bad(PAPER)

    fig, ax = plt.subplots(figsize=(8.6, 3.55), facecolor=PAPER)
    ax.set_facecolor(PAPER)
    ax.imshow(
        vort,
        origin="lower",
        extent=[x[0], x[-1], y[0], y[-1]],
        cmap=cmap,
        vmin=-vmax,
        vmax=vmax,
        interpolation="bilinear",
        aspect="auto",
    )
    ax.add_patch(Circle((cx, cy), radius, facecolor=PAPER, edgecolor=SPINE, lw=1.35, zorder=3))
    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(y[0], y[-1])
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    fig.savefig(
        OUT / "who-cylinder.png",
        dpi=170,
        facecolor=PAPER,
        bbox_inches="tight",
        pad_inches=0.08,
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
