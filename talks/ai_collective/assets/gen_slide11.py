#!/usr/bin/env python3
"""Slide 11: dual-tower architecture, matched to TSLMTSEXAM `grpo`.

UnifiedDualCollator: each <ts> marker becomes an image span (matplotlib chart
through frozen Qwen ViT + native merger) then a video span (delay embed
through DINOv3 + trained merger, video_grid_thw t=1). Chart token count is a
budget cap (max_chart_tokens=114), not a fixed width. Delay is 64 tokens.
M-RoPE type-ids are Qwen3.5-only and are not drawn.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

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


def box(ax, x, y, w, h, title, sub=None, edge=SPINE, lw=1.25):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.012,rounding_size=0.06",
        linewidth=lw, edgecolor=edge, facecolor=BOX, zorder=2,
    ))
    if sub:
        ax.text(x + w / 2, y + h * 0.62, title, ha="center", va="center",
                color=INK, fontsize=10.0, fontweight="600", zorder=3)
        ax.text(x + w / 2, y + h * 0.28, sub, ha="center", va="center",
                color=MUTED, fontsize=7.6, zorder=3)
    else:
        ax.text(x + w / 2, y + h / 2, title, ha="center", va="center",
                color=INK, fontsize=10.0, fontweight="600", zorder=3)


def arrow(ax, p, q, color=MUTED, rad=0):
    ax.add_patch(FancyArrowPatch(
        p, q, arrowstyle="-|>", mutation_scale=11, lw=1.2,
        color=color, connectionstyle=f"arc3,rad={rad}", zorder=1,
        shrinkA=2, shrinkB=2,
    ))


def delay_embed_2d(x, height, width):
    """Match src/delay_embedding.py: sliding window, interpolate each column."""
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


def chips(ax, x, y, groups, h=0.62, w=0.18, gap=0.035, pack=0.12):
    x0 = x
    for color, n in groups:
        for _ in range(n):
            ax.add_patch(Rectangle(
                (x0, y), w, h, facecolor=color, edgecolor=PAPER,
                linewidth=0.5, zorder=4, alpha=0.92,
            ))
            x0 += w + gap
        x0 += pack
    return x0


def main():
    rng = np.random.default_rng(4)
    t = np.arange(64)
    y = 0.035 * t + 1.2 * np.sin(2 * np.pi * t / 16) + rng.normal(0, 0.07, 64)
    yn = (y - y.min()) / (y.max() - y.min())
    xn = (y - y.min()) / (np.ptp(y) + 1e-6)
    delay_img = delay_embed_2d(xn.astype(np.float32), 28, 28)
    cmap = LinearSegmentedColormap.from_list("de", ["#2a221c", TEAL, GOLD])

    fig, ax = plt.subplots(figsize=(13.6, 6.25), facecolor=PAPER)
    ax.set_xlim(0, 18.15)
    ax.set_ylim(0.0, 10.15)
    ax.set_axis_off()
    ax.set_facecolor(PAPER)

    box(ax, 0.20, 3.55, 2.45, 3.05, "", edge=GOLD, lw=1.35)
    ax.text(1.425, 6.25, r"$x \in \mathbb{R}^{T}$", ha="center", va="center",
            color=INK, fontsize=12, zorder=3)
    ax.text(1.425, 5.88, "named series", ha="center", va="center",
            color=MUTED, fontsize=7.6, zorder=3)
    ax.plot(0.42 + t / 63 * 2.02, 3.78 + yn * 1.65, color=GOLD, lw=1.35, zorder=3)

    ax.text(5.70, 9.78, "CHART TOWER", ha="center", va="center",
            color=GOLD, fontsize=8.6, fontfamily="monospace", fontweight="600")
    box(ax, 3.20, 7.15, 2.40, 2.20, "", edge=GOLD)
    ax.plot(3.38 + t / 63 * 2.04, 7.68 + yn * 1.22, color=GOLD, lw=1.15, zorder=4)
    ax.text(4.40, 7.38, "matplotlib chart", ha="center", va="center",
            color=INK, fontsize=9.6, fontweight="600", zorder=4)
    box(ax, 5.85, 7.35, 3.55, 1.80, "Qwen ViT + merger",
        "frozen  ·  image stream", GOLD)
    ax.text(7.62, 7.12, "<=114 image_pad   (budget cap)", ha="center", va="top",
            color=GOLD, fontsize=7.3, fontfamily="monospace")

    ax.text(5.70, 3.22, "DELAY TOWER", ha="center", va="center",
            color=TEAL, fontsize=8.6, fontfamily="monospace", fontweight="600")
    box(ax, 3.20, 0.70, 2.40, 2.20, "", edge=TEAL)
    ax.imshow(
        delay_img, origin="lower", cmap=cmap, aspect="auto",
        extent=(3.38, 5.42, 1.22, 2.58), zorder=3, interpolation="nearest",
    )
    ax.text(4.40, 0.92, "delay embed 256 x 256", ha="center", va="center",
            color=MUTED, fontsize=7.5, zorder=4)
    box(ax, 5.85, 0.92, 3.55, 1.80, "DINOv3 + merger",
        "LoRA in A  ·  video t=1  ·  64 tok", TEAL)

    arrow(ax, (2.65, 5.95), (3.20, 8.25), GOLD, rad=-0.10)
    arrow(ax, (2.65, 4.20), (3.20, 1.80), TEAL, rad=0.10)
    arrow(ax, (5.60, 8.25), (5.85, 8.25), GOLD)
    arrow(ax, (5.60, 1.82), (5.85, 1.82), TEAL)

    ax.text(14.05, 9.78, "ONE REASONER", ha="center", va="center",
            color=ACCENT, fontsize=8.6, fontfamily="monospace", fontweight="600")

    box(ax, 10.00, 6.55, 7.90, 2.40, "", edge=ACCENT, lw=1.35)
    ax.text(13.95, 8.60, "Each <ts> marker: chart span, then delay span",
            ha="center", va="center", color=INK, fontsize=10.0, fontweight="600", zorder=3)
    ax.text(13.95, 8.28, "interleaved in the question  ·  not a global concat",
            ha="center", va="center", color=MUTED, fontsize=7.5, fontfamily="monospace", zorder=3)

    groups = [
        (MUTED, 3), (GOLD, 5), (TEAL, 4),
        (MUTED, 2), (GOLD, 5), (TEAL, 4),
        (MUTED, 3),
    ]
    chips(ax, 10.35, 7.00, groups, h=0.62, w=0.175, gap=0.028, pack=0.10)
    ax.text(11.97, 6.68, "marker", ha="center", va="top", color=MUTED,
            fontsize=7.2, fontfamily="monospace", zorder=4)
    ax.text(14.37, 6.68, "marker", ha="center", va="top", color=MUTED,
            fontsize=7.2, fontfamily="monospace", zorder=4)

    box(ax, 10.00, 3.35, 7.90, 2.60, "", edge=ACCENT, lw=1.35)
    for i in range(3):
        yy = 5.28 - i * 0.60
        ax.add_patch(FancyBboxPatch(
            (10.55, yy), 6.80, 0.50,
            boxstyle="round,pad=0.008,rounding_size=0.04",
            linewidth=1.0, edgecolor=SPINE, facecolor="#1a1612", zorder=3,
        ))
        ax.text(13.95, yy + 0.25, "Nx   Qwen decoder block", ha="center", va="center",
                color=INK, fontsize=9.3, zorder=4)
    ax.text(13.95, 3.55, "LoRA in Stage B   ·   LLM frozen in A", ha="center", va="center",
            color=MUTED, fontsize=7.4, fontfamily="monospace", zorder=4)

    box(ax, 10.00, 1.40, 7.90, 1.32, "Answer", "MCQ  ·  caption  ·  open QA", ACCENT)

    arrow(ax, (9.40, 8.25), (10.00, 7.95), GOLD, rad=-0.06)
    arrow(ax, (9.40, 1.82), (10.00, 7.35), TEAL, rad=0.10)
    arrow(ax, (13.95, 6.55), (13.95, 5.95), ACCENT)
    arrow(ax, (13.95, 3.35), (13.95, 2.72), ACCENT)

    ax.text(9.55, 0.28, "N series  =  N markers  =  N dual views",
            ha="center", va="center", color=MUTED, fontsize=8.1,
            fontfamily="monospace")

    save(fig, "slide11-arch.png")


if __name__ == "__main__":
    main()
