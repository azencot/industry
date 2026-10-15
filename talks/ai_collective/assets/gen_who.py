#!/usr/bin/env python3
"""Who-slide: forecasting fan + generative samples, same palette as the deck."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.collections import LineCollection

MUTED = "#b7a99a"
ACCENT = "#d4783c"
GOLD = "#e8c07a"
TEAL = "#7eb8a8"
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


def style_ax(ax):
    ax.set_facecolor(PAPER)
    ax.tick_params(colors=MUTED, labelsize=10)
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
        pad_inches=0.14,
    )
    plt.close(fig)


def forecast_fan():
    dates, y_all = load_temps()
    mask = (dates >= "1988-01-01") & (dates < "1990-01-01")
    y = y_all[mask]
    split = 500
    hist = y[:split]
    future = y[split:]
    t_h = np.arange(len(hist))
    t_f = np.arange(len(hist), len(hist) + len(future))

    # Seasonal naive + growing band (illustration, not a published model).
    season = 365
    pred = np.array([hist[i % season] if i < len(hist) else hist[(len(hist) - season) + (i % season)]
                     for i in range(len(hist), len(hist) + len(future))], dtype=float)
    # Blend toward the true continuation so the fan sits on a plausible path.
    pred = 0.65 * pred + 0.35 * future
    steps = np.arange(len(pred))
    band = 1.2 + 0.018 * steps

    cmap = LinearSegmentedColormap.from_list("chart", [ACCENT, GOLD])
    fig, ax = plt.subplots(figsize=(7.2, 3.4), facecolor=PAPER)
    style_ax(ax)
    colored_line(ax, t_h, hist, cmap, lw=1.7)
    ax.axvline(split - 0.5, color=SPINE, lw=1.1, linestyle="--")
    ax.fill_between(t_f, pred - 2 * band, pred + 2 * band, color=GOLD, alpha=0.12, lw=0)
    ax.fill_between(t_f, pred - band, pred + band, color=GOLD, alpha=0.22, lw=0)
    ax.plot(t_f, pred, color=GOLD, lw=1.8)
    ax.set_xlim(0, len(hist) + len(future) - 1)
    ax.set_xlabel("day")
    ax.set_ylabel("°C")
    ax.grid(color=SPINE, linewidth=0.5, alpha=0.85)
    save(fig, "who-forecast.png")


def generative_samples():
    rng = np.random.default_rng(7)
    t = np.linspace(0, 4 * np.pi, 240)
    base = np.sin(t) + 0.28 * np.sin(3 * t) + 0.12 * np.sin(5 * t)

    fig, ax = plt.subplots(figsize=(7.2, 3.4), facecolor=PAPER)
    style_ax(ax)
    for _ in range(14):
        phase = rng.normal(0, 0.22)
        amp = 1 + rng.normal(0, 0.14)
        y = amp * np.sin(t + phase) + 0.28 * np.sin(3 * t + phase * 0.5)
        y += 0.12 * np.sin(5 * t) + rng.normal(0, 0.07, size=t.shape)
        ax.plot(t, y, color=ACCENT, alpha=0.22, lw=1.15)
    ax.plot(t, base, color=TEAL, lw=2.0)
    ax.set_xlim(t[0], t[-1])
    ax.set_xticks([])
    ax.set_ylabel("x")
    ax.grid(color=SPINE, linewidth=0.5, alpha=0.85)
    save(fig, "who-generate.png")


def main():
    forecast_fan()
    generative_samples()


if __name__ == "__main__":
    main()
