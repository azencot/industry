#!/usr/bin/env python3
"""Slide 13: multivariate contract vs .ravel() fake univariate.

N named series -> N <ts> markers -> N chart + N delay. Gluing channels in
time makes one bogus trajectory; delay geometry dies.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

INK = "#f3ece3"
MUTED = "#b7a99a"
ACCENT = "#d4783c"
TEAL = "#7eb8a8"
GOLD = "#e8c07a"
PAPER = "#1c1814"
SPINE = "#3a322b"

OUT = Path(__file__).resolve().parent
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Avenir Next", "Helvetica Neue", "DejaVu Sans"]
CMAP = LinearSegmentedColormap.from_list("de", ["#2a221c", TEAL, GOLD])


def save(fig, name):
    fig.savefig(OUT / name, dpi=170, facecolor=PAPER, bbox_inches="tight", pad_inches=0.10)
    plt.close(fig)


def delay_embed_2d(x, height=28, width=28):
    x = np.asarray(x, dtype=np.float32)
    length = int(x.size)
    l = max(8, min(length, int(np.floor(0.6 * length))))
    max_start = max(0, length - l)
    step = (max_start / float(width - 1)) if width > 1 else 0.0
    out = np.empty((height, width), dtype=np.float32)
    src = np.linspace(0.0, 1.0, num=l)
    dst = np.linspace(0.0, 1.0, num=height)
    for col in range(width):
        start = min(int(round(col * step)), max_start)
        window = x[start : start + l]
        out[:, col] = np.interp(dst, src, window)
    return out


def style_line(ax):
    ax.set_facecolor(PAPER)
    ax.tick_params(length=0, labelbottom=False, labelleft=False)
    for sp in ax.spines.values():
        sp.set_color(SPINE)
    ax.grid(color=SPINE, linewidth=0.5, alpha=0.9)


def style_img(ax, img):
    ax.set_facecolor(PAPER)
    ax.imshow(img, origin="lower", cmap=CMAP, aspect="auto", interpolation="nearest")
    ax.tick_params(length=0, labelbottom=False, labelleft=False)
    for sp in ax.spines.values():
        sp.set_color(SPINE)


def main():
    rng = np.random.default_rng(5)
    n = 80
    t = np.arange(n)
    ts1 = 1.4 * np.sin(2 * np.pi * t / 18) + rng.normal(0, 0.08, n)
    ts2 = 0.045 * t + rng.normal(0, 0.06, n)
    glued = np.concatenate([ts1, ts2])
    d1 = delay_embed_2d(ts1)
    d2 = delay_embed_2d(ts2)
    dg = delay_embed_2d(glued)

    fig = plt.figure(figsize=(13.6, 5.55), facecolor=PAPER)
    gs = fig.add_gridspec(
        2, 4,
        width_ratios=[1.15, 0.95, 0.18, 1.45],
        left=0.05, right=0.98, top=0.86, bottom=0.08,
        wspace=0.28, hspace=0.38,
    )

    ax_c1 = fig.add_subplot(gs[0, 0])
    ax_d1 = fig.add_subplot(gs[0, 1])
    ax_c2 = fig.add_subplot(gs[1, 0])
    ax_d2 = fig.add_subplot(gs[1, 1])
    ax_rv = fig.add_subplot(gs[0, 3])
    ax_rd = fig.add_subplot(gs[1, 3])

    style_line(ax_c1)
    ax_c1.plot(ts1, color=GOLD, lw=1.45)
    ax_c1.set_title("ts1  chart", color=MUTED, fontsize=9, pad=4, fontfamily="monospace")

    style_img(ax_d1, d1)
    ax_d1.set_title("ts1  delay", color=MUTED, fontsize=9, pad=4, fontfamily="monospace")

    style_line(ax_c2)
    ax_c2.plot(ts2, color=TEAL, lw=1.45)
    ax_c2.set_title("ts2  chart", color=MUTED, fontsize=9, pad=4, fontfamily="monospace")

    style_img(ax_d2, d2)
    ax_d2.set_title("ts2  delay", color=MUTED, fontsize=9, pad=4, fontfamily="monospace")

    style_line(ax_rv)
    ax_rv.plot(glued, color=ACCENT, lw=1.35)
    ax_rv.axvline(n - 0.5, color=SPINE, lw=1.15)
    ax_rv.set_title("channels glued in time", color=MUTED, fontsize=9, pad=4, fontfamily="monospace")

    style_img(ax_rd, dg)
    ax_rd.set_title("one delay  ·  garbage geometry", color=MUTED, fontsize=9, pad=4,
                    fontfamily="monospace")

    fig.text(0.28, 0.94, "CONTRACT", ha="center", va="center",
             color=GOLD, fontsize=11, fontfamily="monospace", fontweight="600")
    fig.text(0.28, 0.90, "N series  =  N markers  =  N dual views",
             ha="center", va="center", color=MUTED, fontsize=8.5, fontfamily="monospace")
    fig.text(0.78, 0.94, ".ravel()", ha="center", va="center",
             color=ACCENT, fontsize=11, fontfamily="monospace", fontweight="600")
    fig.text(0.78, 0.90, "one fake univariate",
             ha="center", va="center", color=MUTED, fontsize=8.5, fontfamily="monospace")

    save(fig, "slide13-ravel.png")


if __name__ == "__main__":
    main()
