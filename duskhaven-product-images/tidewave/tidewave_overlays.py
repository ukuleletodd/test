"""Tidewave overlay finishing (Duskhaven product-image skill, step 7).

Run after the Luno generations are accepted:

  python tidewave_overlays.py name-symbol  02-raw.jpg  02-tidewave-name-symbol.jpg
  python tidewave_overlays.py dimensions   08-raw.jpg  08-tidewave-dimensions.jpg
  python tidewave_overlays.py label        in.jpg out.jpg "STEPLESS DIMMING" "Remote brightness control, 10-100%"
  python tidewave_overlays.py colors       aqua.jpg amber.jpg green.jpg pink.jpg 10-tidewave-colors.jpg

Needs Pillow + numpy and Poppins (set POPPINS_DIR if it is not in a standard font folder).
Every number printed on a card comes from FACTS below (verified supplier facts only).
"""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

CREAM = (236, 214, 170)  # #ECD6AA
CARD = (12, 11, 11)      # #0C0B0B

FACTS = {
    "name": "TIDEWAVE",
    "finish": "Clear ripple cube · Pale wood-grain base",
    "size": "11.2 cm cube lamp",
    "height_cm": 11.2,
    "width_cm": 11.2,
    "footer": "Crystal cube 9.5 cm (3.7 in)  ·  USB cable 136 cm (53.5 in)  ·  16 colors  ·  Remote control",
}


def font(weight, size):
    dirs = [os.environ.get("POPPINS_DIR", ""), "/usr/share/fonts/truetype/google-fonts",
            os.path.expanduser("~/.fonts"), "C:/Windows/Fonts"]
    for d in dirs:
        p = os.path.join(d, f"Poppins-{weight}.ttf")
        if d and os.path.exists(p):
            return ImageFont.truetype(p, size)
    raise SystemExit("Poppins not found; set POPPINS_DIR")


def spaced(draw, xy, text, fnt, fill, tracking, anchor_center=False):
    """Draw letter-spaced caps; returns total width."""
    widths = [draw.textlength(ch, font=fnt) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x, y = xy
    if anchor_center:
        x -= total / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += w + tracking
    return total


def wave_glyph(draw, cx, cy, w, h, stroke, fill):
    """One-period sine stroke, the Tidewave symbol."""
    pts = [(cx - w / 2 + w * t / 200, cy - (h / 2) * np.sin(2 * np.pi * t / 200)) for t in range(201)]
    draw.line(pts, fill=fill, width=stroke, joint="curve")
    r = stroke / 2
    for px, py in (pts[0], pts[-1]):
        draw.ellipse((px - r, py - r, px + r, py + r), fill=fill)


def name_symbol(src, dst):
    im = Image.open(src).convert("RGB")
    W, H = im.size
    # soft dark scrim over the lower third
    scrim = Image.new("L", (W, H), 0)
    ys = np.linspace(0, 1, H)
    ramp = np.clip((ys - 0.58) / 0.30, 0, 1) ** 1.4 * 170
    scrim = Image.fromarray(np.repeat(ramp[:, None], W, 1).astype(np.uint8))
    im = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), im, scrim)
    d = ImageDraw.Draw(im)
    size = int(W * 0.046)
    f = font("Medium", size)
    track = size * 0.42
    text_w = sum(d.textlength(c, font=f) for c in FACTS["name"]) + track * (len(FACTS["name"]) - 1)
    glyph_w = size * 1.15
    gap = size * 0.9
    total = glyph_w + gap + text_w
    x0 = (W - total) / 2
    cy = H * 0.84
    wave_glyph(d, x0 + glyph_w / 2, cy, glyph_w, size * 0.62, max(3, int(size * 0.075)), CREAM)
    asc, desc = f.getmetrics()
    spaced(d, (x0 + glyph_w + gap, cy - asc * 0.62), FACTS["name"], f, CREAM, track)
    im.save(dst, quality=95)


def product_bounds(img, thresh=38):
    a = np.asarray(img.convert("RGB")).astype(int)
    border = np.concatenate([a[:8].reshape(-1, 3), a[-8:].reshape(-1, 3), a[:, :8].reshape(-1, 3), a[:, -8:].reshape(-1, 3)])
    bg = np.median(border, 0)
    mask = np.abs(a - bg).sum(2) > thresh
    rows, cols = np.where(mask.any(1))[0], np.where(mask.any(0))[0]
    # trim thin stragglers (cable, noise): keep rows/cols with a meaningful share of pixels
    rs = mask.sum(1); cs = mask.sum(0)
    rows = np.where(rs > rs.max() * 0.15)[0]
    cols = np.where(cs > cs.max() * 0.15)[0]
    return cols.min(), rows.min(), cols.max(), rows.max()


def dashed(d, p0, p1, fill, width, dash=18, gapl=12):
    x0, y0 = p0; x1, y1 = p1
    L = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    n = int(L // (dash + gapl)) + 1
    for i in range(n):
        s = i * (dash + gapl) / L; e = min(1, (i * (dash + gapl) + dash) / L)
        d.line([(x0 + (x1 - x0) * s, y0 + (y1 - y0) * s), (x0 + (x1 - x0) * e, y0 + (y1 - y0) * e)], fill=fill, width=width)


def dimensions(src, dst, bounds=None):
    shot = Image.open(src).convert("RGB")
    W, H = 3712, 4608
    card = Image.new("RGB", (W, H), CARD)
    # soft gray glow behind the product
    glow = Image.new("L", (W, H), 0)
    ImageDraw.Draw(glow).ellipse((W * 0.18, H * 0.20, W * 0.82, H * 0.72), fill=70)
    glow = glow.filter(ImageFilter.GaussianBlur(W * 0.08))
    card = Image.composite(Image.new("RGB", (W, H), (58, 58, 60)), card, glow)
    # studio shot at ~70% with an elliptical feathered mask
    sw = int(W * 0.70); sh = int(shot.height * sw / shot.width)
    shot_r = shot.resize((sw, sh), Image.LANCZOS)
    m = Image.new("L", (sw, sh), 0)
    ImageDraw.Draw(m).ellipse((sw * 0.06, sh * 0.06, sw * 0.94, sh * 0.94), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(sw * 0.06))
    ox, oy = (W - sw) // 2, int(H * 0.47 - sh / 2)
    card.paste(shot_r, (ox, oy), m)
    # product bounds in card coordinates
    bx0, by0, bx1, by1 = bounds or product_bounds(shot)
    k = sw / shot.width
    x0, y0, x1, y1 = ox + bx0 * k, oy + by0 * k, ox + bx1 * k, oy + by1 * k
    d = ImageDraw.Draw(card)
    lw = 6; tick = 34; grey = (150, 146, 140)
    big = font("Medium", 118); small = font("Regular", 70)
    # height line on the right
    hx = x1 + 170
    for yy in (y0, y1):
        dashed(d, (x1 + 25, yy), (hx + tick, yy), grey, 4)
    d.line([(hx, y0), (hx, y1)], fill=CREAM, width=lw)
    for yy in (y0, y1):
        d.line([(hx - tick, yy), (hx + tick, yy)], fill=CREAM, width=lw)
    hin = FACTS["height_cm"] / 2.54
    d.text((hx + 70, (y0 + y1) / 2 - 95), f"{hin:.1f} in", font=big, fill=CREAM)
    d.text((hx + 74, (y0 + y1) / 2 + 45), f"{FACTS['height_cm']:g} cm", font=small, fill=grey)
    # width line below
    wy = y1 + 170
    for xx in (x0, x1):
        dashed(d, (xx, y1 + 25), (xx, wy + tick), grey, 4)
    d.line([(x0, wy), (x1, wy)], fill=CREAM, width=lw)
    for xx in (x0, x1):
        d.line([(xx, wy - tick), (xx, wy + tick)], fill=CREAM, width=lw)
    win = FACTS["width_cm"] / 2.54
    t = f"{win:.1f} in"; tw = d.textlength(t, font=big)
    d.text(((x0 + x1) / 2 - tw / 2, wy + 60), t, font=big, fill=CREAM)
    t = f"{FACTS['width_cm']:g} cm"; tw = d.textlength(t, font=small)
    d.text(((x0 + x1) / 2 - tw / 2, wy + 200), t, font=small, fill=grey)
    # title, subtitle, footer
    spaced(d, (W / 2, H * 0.055), f"{FACTS['name']} · DIMENSIONS", font("Medium", 150), CREAM, 34, anchor_center=True)
    sub = f"{FACTS['finish']} · {FACTS['size']}"
    d.text((W / 2 - d.textlength(sub, font=font("Light", 84)) / 2, H * 0.055 + 230), sub, font=font("Light", 84), fill=grey)
    ff = font("Regular", 66)
    d.text((W / 2 - d.textlength(FACTS["footer"], font=ff) / 2, H * 0.925), FACTS["footer"], font=ff, fill=grey)
    card.save(dst, quality=95)


def label(src, dst, title, line):
    im = Image.open(src).convert("RGB")
    W, H = im.size
    ys = np.linspace(0, 1, H)[:, None]; xs = np.linspace(0, 1, W)[None, :]
    a = np.clip((ys - 0.70) / 0.3, 0, 1) * np.clip((0.75 - xs) / 0.75, 0, 1) * 150
    im = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), im, Image.fromarray(a.astype(np.uint8)))
    d = ImageDraw.Draw(im)
    s = int(W * 0.036)
    spaced(d, (W * 0.06, H * 0.865), title.upper(), font("Medium", s), CREAM, s * 0.3)
    d.text((W * 0.06, H * 0.865 + s * 1.6), line, font=font("Light", int(s * 0.62)), fill=CREAM)
    im.save(dst, quality=95)


def colors(paths, dst):
    ims = [Image.open(p).convert("RGB") for p in paths]
    W, H = 3712, 4608; g = 24
    tw, th = (W - g) // 2, (H - g) // 2
    out = Image.new("RGB", (W, H), CARD)
    for i, im in enumerate(ims):
        s = max(tw / im.width, th / im.height)
        r = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
        l, t = (r.width - tw) // 2, (r.height - th) // 2
        out.paste(r.crop((l, t, l + tw, t + th)), ((i % 2) * (tw + g), (i // 2) * (th + g)))
    tmp = dst + ".tmp.jpg"; out.save(tmp, quality=95)
    label(tmp, dst, "16 COLORS", "Choose from 16 colors with the included remote")
    os.remove(tmp)


if __name__ == "__main__":
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "name-symbol":
        name_symbol(*args)
    elif cmd == "dimensions":
        dimensions(*args)
    elif cmd == "label":
        label(*args)
    elif cmd == "colors":
        colors(args[:4], args[4])
    else:
        raise SystemExit(__doc__)
