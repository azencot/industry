#!/usr/bin/env python3
"""Slide 1: one real series as a line chart and as a delay-embedding image.

Delay is the ImagenTime Hankel image (columns = delayed windows), not a
phase portrait. Data: Melbourne daily min temperatures (1981–1990).
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.collections import LineCollection

MUTED = "#b7a99a"
ACCENT = "#d4783c"
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


def hankel_delay(y, delay, embedding):
    cols = []
    i = 0
    while i * delay + embedding <= len(y):
        cols.append(y[i * delay : i * delay + embedding])
        i += 1
    x = np.stack(cols, axis=1)
    n = max(x.shape)
    img = np.full((n, n), np.nan)
    img[: x.shape[0], : x.shape[1]] = x
    return img


def style_ax(ax):
    ax.set_facecolor(PAPER)
    ax.tick_params(colors=MUTED, labelsize=11)
    for sp in ax.spines.values():
        sp.set_color(SPINE)
    ax.xaxis.label.set_color(MUTED)
    ax.yaxis.label.set_color(MUTED)


def colored_line(ax, x, y, cmap, lw):
    pts = np.column_stack([x, y]).reshape(-1, 1, 2)
    segs = np.concatenate([pts[:-1], pts[1:]], axis=1)
    lc = LineCollection(segs, cmap=cmap, norm=Normalize(0, 1))
    lc.set_array(np.linspace(0, 1, len(segs)))
    lc.set_linewidth(lw)
    ax.add_collection(lc)
    ax.autoscale_view()
    return lc


def save(fig, name):
    fig.savefig(
        OUT / name,
        dpi=160,
        facecolor=PAPER,
        bbox_inches="tight",
        pad_inches=0.18,
    )
    plt.close(fig)


def main():
    dates, y_all = load_temps()
    # Four calendar years — readable chart, same window for the Hankel image.
    mask = (dates >= "1985-01-01") & (dates < "1989-01-01")
    y = y_all[mask]
    t = np.arange(len(y))

    delay = 7
    embedding = int(round(len(y) / (delay + 1)))
    img = hankel_delay(y, delay=delay, embedding=embedding)

    cmap_chart = LinearSegmentedColormap.from_list("chart", [ACCENT, "#e8c07a"])

    fig, ax = plt.subplots(figsize=(8.4, 4.6), facecolor=PAPER)
    style_ax(ax)
    colored_line(ax, t, y, cmap_chart, lw=1.55)
    ax.set_xlabel("day")
    ax.set_ylabel("°C")
    ax.grid(color=SPINE, linewidth=0.6, alpha=0.9)
    save(fig, "slide1-chart.png")

    cmap_de = LinearSegmentedColormap.from_list(
        "de",
        ["#1c1814", "#3a322b", "#7a4a2c", "#d4783c", "#e8c07a", "#f3ece3"],
    )
    cmap_de.set_bad(PAPER)

    fig, ax = plt.subplots(figsize=(8.4, 4.6), facecolor=PAPER)
    ax.set_facecolor(PAPER)
    ax.imshow(img, aspect="equal", cmap=cmap_de, interpolation="nearest")
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    save(fig, "slide1-delay.png")


if __name__ == "__main__":
    main()
