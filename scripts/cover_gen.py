# -*- coding: utf-8 -*-
"""Generate zh/en covers for the Tathagata self-distillation essay.
Design: deep-ink vertical gradient, gold enso mark, serif typography."""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 900
INK_TOP, INK_BOT = (26, 23, 37), (16, 14, 24)
GOLD = (212, 175, 55)
GOLD_DIM = (212, 175, 55, 110)
FG = (238, 234, 226)
FG_DIM = (178, 172, 186)

FONTS = r"C:\Windows\Fonts"

def pick(names, size):
    for n in names:
        p = os.path.join(FONTS, n)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    raise FileNotFoundError(names)

def serif_zh(size):  return pick(["msyhbd.ttc", "msyh.ttc", "simsun.ttc"], size)
def serif_en(size):  return pick(["georgia.ttf", "cambria.ttc", "times.ttf"], size)

def canvas():
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        t = y / H
        c = tuple(round(a + (b - a) * t) for a, b in zip(INK_TOP, INK_BOT))
        for x in range(W):
            px[x, y] = c
    return img

def enso(d, cx, cy, r):
    d.arc([cx - r, cy - r, cx + r, cy + r], start=95, end=430, fill=GOLD, width=7)

def center(d, cy, text, font, fill, ls=0):
    if ls:  # manual letter-spacing for small caps lines
        widths = [d.textlength(ch, font=font) for ch in text]
        total = sum(widths) + ls * (len(text) - 1)
        x = (W - total) / 2
        for ch, w in zip(text, widths):
            d.text((x, cy), ch, font=font, fill=fill)
            x += w + ls
    else:
        w = d.textlength(text, font=font)
        d.text(((W - w) / 2, cy), text, font=font, fill=fill)

def rule(d, cy, half=90, color=GOLD, width=2):
    d.line([(W/2 - half, cy), (W/2 + half, cy)], fill=color, width=width)

def cover_zh(path):
    img = canvas(); d = ImageDraw.Draw(img)
    enso(d, W/2, 210, 92)
    center(d, 355, "如来的自我蒸馏", serif_zh(118), FG)
    center(d, 520, "两千五百年前的破幻觉算法", serif_zh(44), GOLD)
    center(d, 588, "The Self-Distillation of the Tathagata", serif_en(30), FG_DIM)
    rule(d, 660)
    center(d, 700, "破除幻觉 · 蒸馏正觉", serif_zh(26), FG_DIM, ls=8)
    center(d, 762, "BREAKING HALLUCINATION  ·  DISTILLING RIGHT AWAKENING", serif_en(18), FG_DIM, ls=4)
    center(d, 820, "2026 · wynn", serif_en(18), GOLD)
    img.save(path)

def cover_en(path):
    img = canvas(); d = ImageDraw.Draw(img)
    enso(d, W/2, 205, 92)
    f1 = serif_en(84)
    center(d, 340, "The Self-Distillation", f1, FG)
    center(d, 440, "of the Tathagata", f1, FG)
    center(d, 570, "A 2,500-Year-Old Anti-Hallucination Algorithm", serif_en(36), GOLD)
    center(d, 630, "如来的自我蒸馏 · 两千五百年前的破幻觉算法", serif_zh(26), FG_DIM)
    rule(d, 690)
    center(d, 728, "BREAKING HALLUCINATION  ·  DISTILLING RIGHT AWAKENING", serif_en(18), FG_DIM, ls=4)
    center(d, 820, "2026 · wynn", serif_en(18), GOLD)
    img.save(path)

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "assets")
    os.makedirs(out, exist_ok=True)
    cover_zh(os.path.join(out, "cover-zh.png"))
    cover_en(os.path.join(out, "cover-en.png"))
    print("covers written to", os.path.abspath(out))
