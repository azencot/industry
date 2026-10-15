#!/usr/bin/env python3
"""Six-year slide: overlapping first-page blob of BGU-era papers."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

PAPER = (28, 24, 20, 255)
OUT = Path(__file__).resolve().parent
PAGES = OUT / "papers" / "pages"

# Newest-ish toward front-right.
ORDER = [
    "2006.12070-01.png",
    "2303.17264-01.png",
    "2305.15924-01.png",
    "2310.02619-01.png",
    "2406.10914-01.png",
    "2406.18131-01.png",
    "2410.19538-01.png",
    "2505.13358-01.png",
    "2505.20446-01.png",
    "2510.05717-01.png",
    "2510.06699-01.png",
    "2510.20819-01.png",
]

# Loose 3×4 with overlap; slight tilt so it reads as a pile, not a table.
LAYOUT = [
    (40, 70, -8), (300, 40, 5), (560, 80, -4), (820, 50, 7),
    (20, 320, 6), (280, 300, -5), (540, 340, 4), (800, 310, -7),
    (50, 560, -3), (310, 540, 8), (570, 570, -6), (830, 550, 3),
]


def main():
    W, H = 1200, 900
    canvas = Image.new("RGBA", (W, H), PAPER)
    shadow_base = Image.new("RGBA", (W, H), (0, 0, 0, 0))

    for name, (x, y, ang) in zip(ORDER, LAYOUT):
        im = Image.open(PAGES / name).convert("RGBA")
        im.thumbnail((340, 440), Image.Resampling.LANCZOS)
        # faint warmth so white pages sit on the dark deck
        im = ImageEnhance.Color(im).enhance(0.92)
        im = ImageEnhance.Contrast(im).enhance(1.05)
        rot = im.rotate(ang, expand=True, resample=Image.Resampling.BICUBIC)
        # drop shadow
        sh = Image.new("RGBA", rot.size, (0, 0, 0, 0))
        sd = ImageDraw.Draw(sh)
        sd.rounded_rectangle(
            (6, 8, rot.size[0] - 2, rot.size[1] - 2),
            radius=4,
            fill=(0, 0, 0, 90),
        )
        sh = sh.filter(ImageFilter.GaussianBlur(6))
        canvas.alpha_composite(sh, (x + 4, y + 8))
        canvas.alpha_composite(rot, (x, y))

    rgb = Image.new("RGB", canvas.size, PAPER[:3])
    rgb.paste(canvas, mask=canvas.split()[-1])
    rgb.save(OUT / "who-papers.png", quality=92)


if __name__ == "__main__":
    main()
