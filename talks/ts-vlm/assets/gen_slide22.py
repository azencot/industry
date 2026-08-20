#!/usr/bin/env python3
"""Slide 22: the stack transfers if the signal admits an image.

Same 1-D series rendered three ways: matplotlib chart, delay embedding
(this talk), STFT (the sensor hop). Do not claim a Bosch run. Do not
draw a 6-month program.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import FancyBboxPatch
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
CMAP = LinearSegmentedColormap.from_list("de", ["#2a221c", TEAL, GOLD])


def save(fig, name):
    fig.savefig(OUT / name, dpi=170, facecolor=PAPER, bbox_inches="tight", pad_inches=0.10)
    plt.close(fig)


def rbox(ax, x, y, w, h, edge=SPINE, lw=1.25, fc=BOX):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.012,rounding_size=0.05",
        linewidth=lw, edgecolor=edge, facecolor=fc, zorder=2,
    ))


def delay_embed_2d(x, height, width):
    length = int(x.size)
    l = int(np.floor(0.6 * length))
    l = max(8, min(l, length))
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


def stft_mag(x, nperseg=96, hop=24):
    win = np.hanning(nperseg)
    cols = []
    for start in range(0, len(x) - nperseg + 1, hop):
        cols.append(np.abs(np.fft.rfft(x[start : start + nperseg] * win)))
    spec = np.stack(cols, axis=1)
    return np.log1p(spec)


def panel(fig, ax, x, y, w, h, img, kind, title, sub, edge):
    rbox(ax, x, y, w, h, edge=edge, lw=1.35)
    ax.text(x + 0.18, y + h - 0.28, title, ha="left", va="center",
            color=edge, fontsize=8.2, zorder=4)
    ax.text(x + w - 0.18, y + h - 0.28, sub, ha="right", va="center",
            color=MUTED, fontsize=8.0, zorder=4)
    ins = inset_axes(
        ax, width="88%", height="62%",
        bbox_to_anchor=(x, y + 0.12, w, h - 0.42),
        bbox_transform=ax.transData, loc="center", borderpad=0,
    )
    ins.set_facecolor(PAPER)
    for sp in ins.spines.values():
        sp.set_visible(False)
    ins.set_xticks([])
    ins.set_yticks([])
    if kind == "line":
        ins.plot(np.arange(img.size), img, color=GOLD, lw=1.15)
        ins.set_xlim(0, img.size - 1)
        pad = 0.12 * np.ptp(img)
        ins.set_ylim(img.min() - pad, img.max() + pad)
    else:
        ins.imshow(img, origin="lower", cmap=CMAP, aspect="auto", interpolation="nearest")
    return ins


def main():
    t = np.linspace(0, 1, 512)
    y = np.sin(2 * np.pi * (8 + 70 * t) * t)
    yn = (y - y.min()) / (np.ptp(y) + 1e-6)
    delay = delay_embed_2d(yn.astype(np.float32), 48, 48)
    spec = stft_mag(yn.astype(np.float32))

    fig, ax = plt.subplots(figsize=(9.6, 6.15), facecolor=PAPER)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.15)
    ax.axis("off")
    ax.set_facecolor(PAPER)

    ax.text(5.0, 6.88, "Same series. Swap the renderer. The VLM still sees an image.",
            ha="center", va="center", color=MUTED, fontsize=8.6)

    panel(fig, ax, 0.45, 4.55, 9.10, 2.00, y, "line",
          "Chart", "this talk", GOLD)
    panel(fig, ax, 0.45, 2.40, 9.10, 2.00, delay, "img",
          "Delay", "this talk", TEAL)
    panel(fig, ax, 0.45, 0.55, 9.10, 1.70, spec, "img",
          "STFT", "a mic, a shaker, …", ACCENT)

    save(fig, "slide22-render.png")


if __name__ == "__main__":
    main()
