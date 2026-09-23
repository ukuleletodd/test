# Tidewave: Luno prompt pack

**Luno settings:** project "Duskhaven Product Images", model **Google Nano Banana Pro**, **4:5**, **4K**. The bar reads `Google · 4:5 · 4K` and the cost button shows `0` while the free counter lasts; drop to 2K when it runs out.

**Run folder:** `Tidewave_NanoBananaPro_Luno_NN`, where NN is the next unused number for Tidewave.

## Reference files

Upload references in the order listed for each shot. Product references go first. Light references (x1–x4) always go last.

| Code | File | What it is |
|---|---|---|
| A | `tidewave-ref-g06-studio-unlit-cable.jpg` | Supplier studio shot, unlit: cube, base, touch icon, white USB cable (labels removed) |
| B | `tidewave-ref-g03-studio-warm-ripple.jpg` | Supplier studio shot: ripple texture, base, touch icon (dimension lines removed) |
| C | `tidewave-ref-g01-cyan-lit.jpg` | Supplier shot of the cube lit in aqua |
| D | `tidewave-ref-g03-remote-24key.jpg` | The included 24-key remote |
| E | `tidewave-ref-x5-docos-unlit-texture-closeup.jpg` | Other seller, real photo: close-up of the unlit ripple embossing |
| x1 | `tidewave-ref-x1-docos-white-wall-ripple.jpg` | Other seller, real photo: white light fanning up a wall, room partly lit |
| x2 | `tidewave-ref-x2-docos-coolwhite-wall-ripple.jpg` | Other seller, real photo: cool-white ripple fan on a wall |
| x3 | `tidewave-ref-x3-docos-amber-wall-ripple.jpg` | Other seller, real photo: amber ripple fan on a wall |
| x4 | `tidewave-ref-x4-aquaticvita-blue-dark-room.jpg` | Other seller, real photo: blue light filling a wall and ceiling in a fully dark room |

**What the real photos show.** The ripple embossing throws streaky, flame-like caustic rays. They fan up and out onto the wall behind the lamp, brightest just above it, and break into soft rippling cells that fade with height. In a fully dark room, a softer wash also reaches the ceiling. The crisp, even network of lines in the current store image is not how this lamp's light looks.

**Add this line to any prompt that uses x1–x4:**

> The last reference photo is a real photo of this same lamp design from another seller (a slightly larger size). Use it only for how the light projects onto the wall and ceiling: the pattern's shape, softness, spread and falloff. Do not copy its furniture, clock, plants, ornaments, room or the lamp's size.

## Product block (start of every generation prompt)

> Use the exact product from these reference photos: the Tidewave water-ripple projector lamp, one single small lamp. It is a clear, colorless crystal-look cube about 9.5 cm wide, every face covered in an irregular embossed water-ripple texture, sitting on a slightly wider square base with softly rounded corners in a pale natural-oak wood-grain finish. Overall it is 11.2 cm wide x 11.2 cm deep x 11.2 cm tall (4.4 in), a small tabletop object only a little taller than a coffee mug. A small circular touch power icon is embossed on the front edge of the base, and a thin white USB cable leaves the side of the base toward the back. It has no shade, stem, feet, speaker, screen or other hardware. When on, the LED inside lights the whole textured cube in one color with a brighter core low in the middle, and the ripple texture throws streaky, flame-like water-caustic rays that fan upward and outward onto the wall behind and above the lamp: brightest just above the lamp, broken into soft rippling cells, fading with height and distance.

Below, `[PRODUCT]` means that block and `[LIGHT-REF LINE]` means the line above. Every prompt ends with `No text, no logo, no watermark.`

---

## 03: head-on, room lights on (pilot; generate and review this first)
Environment: **Contemporary city apartment** bedroom. References: A, B, C, x1

> [PRODUCT] Setting: a compact contemporary city-apartment bedroom at night: a queen bed with a low upholstered headboard in charcoal-gray linen, white sheets and a slate-blue duvet with natural folds, two matching light-walnut nightstands 55 cm high with slim tapered legs placed at the same depth either side of the bed, walls painted a muted blue-gray, one simple framed abstract print in muted tones centered above the headboard, an oatmeal wool rug on a pale oak floor, and a window at the far right with sheer curtains showing distant city lights. The Tidewave stands on the left nightstand, 10 cm from the wall, next to a plain white ceramic mug 9.5 cm tall at the same depth; the lamp is about one fifth of the nightstand's 55 cm height and only slightly taller than the mug. The right nightstand holds ordinary decor only: two stacked hardback books and a small potted pothos, no lamp. Centered, straight-on, level camera, natural perspective, straight verticals, about 3.5 m back at 1.1 m height, framing the whole bed, the headboard, both nightstands and enough floor to judge furniture height. Time: night, after dark. The Tidewave is on at full brightness in aqua-blue; the room's ceiling flush-mount light and a warm-white floor lamp in the right corner are also on, so the room is evenly and warmly lit and the lamp's aqua ripple fan on the wall just behind and above it is visible but softened by the room light. Photorealistic interior photography, believable exposure, natural textures, restrained color. [LIGHT-REF LINE] No text, no logo, no watermark.

**Scale check:** lamp height ÷ nightstand height should be about 0.20 (11.2 / 55). The lamp should read slightly taller than the mug (11.2 vs 9.5 cm).

## 04: head-on, room lights off (edit of the accepted 03)
References: **accepted 03 first**, then C, A, B, x4

> Edit the first reference image. Switch off only the room's other artificial lights (the ceiling flush-mount light and the warm-white floor lamp in the right corner). Keep the Tidewave on at exactly the same brightness and aqua-blue light color. Change nothing else: same furniture, bedding folds, wall color, window view, weather, time of day, product position, cords, camera and crop. Show the product's real local glow, shadows and falloff: the cube glows aqua with a brighter core, streaky aqua ripple rays fan up the wall behind the left nightstand, and a softer aqua wash with rippling cells reaches the nearby ceiling and headboard, fading toward the right side of the room. Let unlit areas go genuinely dark. The other references show the exact product. [LIGHT-REF LINE] No text, no logo, no watermark.

**Pair check:** build a side-by-side and a 50/50 overlay. Reject any movement, ghosting, or an evenly re-lit dark frame.

## 01: signature hero
Environment: **Modern garden house**. References: A, B, C, x1

> [PRODUCT] Setting: a modern garden house at dusk. The Tidewave stands on a warm-timber floating shelf against a pale limewashed plaster wall; beside it a small hand-thrown stoneware vase with one olive branch. At the edge of the frame, a large steel-framed window shows a landscaped courtyard garden in deep blue dusk. The lamp is on in aqua-blue; streaky aqua ripple rays fan up the plaster wall just above and behind it, brightest near the lamp and fading with height. Close, product-led medium shot at shelf height, slight three-quarter view so the front and one side of the cube and the base with its touch icon read clearly; the lamp fills about a third of the frame width. Photorealistic, natural materials, believable dusk exposure, no heavy bloom. [LIGHT-REF LINE] No text, no logo, no watermark.

## 02: name-and-symbol photo (overlay added afterwards)
Environment: **Collected antique-inspired home**. References: A, B, C, x2

> [PRODUCT] Setting: a collected antique-inspired home at night. The Tidewave stands on top of a vintage walnut chest of drawers with softly worn edges, against a deep olive-green painted wall with restrained traditional molding; beside it two old cloth-bound books. The lamp is on in aqua-blue and throws streaky aqua ripple rays up the olive wall above it, fading with height. Straight-on, level camera at chest-top height; the lamp sits in the upper-middle of the frame, and the lower third of the image is a calm, dark, empty walnut drawer front with no handles, objects or bright details, leaving quiet space for a caption. Photorealistic, moody but believable exposure. [LIGHT-REF LINE] No text, no logo, no watermark.

Overlay: `python tidewave_overlays.py name-symbol <raw> 02-tidewave-name-symbol.jpg`

## 05: alternate view (unlit, construction)
Environment: **Everyday warm-modern home** office. References: A, B, E

> [PRODUCT] The lamp is switched off, so the clear textured cube and its ripple embossing, the pale wood-grain base with its touch power icon, and the white USB cable are all clearly visible. Setting: an everyday warm-modern home office in soft morning daylight: the lamp stands on a light oak desk near a linen-curtained window, with a closed notebook and a ceramic pencil cup nearby. Camera: elevated three-quarter view looking down at about 35 degrees, showing the top face and two side faces of the cube and the white cable running off the back of the desk. Photorealistic, natural daylight shadows. No text, no logo, no watermark.

## 06: material detail
References: E, A, B, x1

> [PRODUCT] Macro close-up detail of the lower front corner of the lamp: the embossed water-ripple texture of the clear cube glowing softly in warm white from inside, and the front edge of the pale oak-look wood-grain base with the small circular touch power icon, in sharp focus. The lamp stands on a dark stained oak surface in a dim room; the background falls off into soft darkness with a faint warm ripple pattern on the wall behind. Shallow depth of field, crisp texture, true-to-life materials; the crop may cut the top of the cube. [LIGHT-REF LINE] No text, no logo, no watermark.

## 07: second lifestyle (movie night)
Environment: **Quiet woodland retreat**. References: A, B, C, x4

> [PRODUCT] Setting: a quiet woodland-retreat living room during a relaxed movie night: warm knotty-pine wall paneling, a comfortable rust-brown corduroy sofa with a knitted throw, a low rustic oak side table at the sofa's arm holding the Tidewave and a small ceramic bowl of popcorn, a dark window showing silhouetted pine trees, and the soft glow of an off-frame TV. The room lights are off; the lamp is on in deep ocean blue at medium brightness and throws streaky blue ripple rays up the paneling behind it, with a softer blue wash reaching the ceiling corner and fading with distance; the rest of the room is dim but readable. Medium shot, camera at seated eye level, the side table and lamp in the foreground third, sofa behind. Photorealistic, believable low-light exposure, no heavy bloom. [LIGHT-REF LINE] No text, no logo, no watermark.

## 08: dimensions studio shot (finished as a card)
References: A, B, C

> [PRODUCT] Clean studio product photo for a dimension diagram: the lamp stands alone on a plain dark charcoal-gray seamless backdrop that is far behind it, straight-on front view with a level camera at the height of the cube's center so the front face is square to camera and the base's front edge is horizontal. The lamp is on at low brightness in aqua-blue so the ripple texture reads; only a faint glow reaches the distant backdrop. The white USB cable runs straight back out of view. The lamp occupies about 45 percent of the frame width, centered, with generous empty margins on all sides. Soft even studio light. No text, no logo, no watermark.

Overlay: `python tidewave_overlays.py dimensions <raw> 08-tidewave-dimensions.jpg`

## Features (after the core shots; single variant, so no variant images)

### 09: remote control (kids' room)
Environment: **Everyday warm-modern home** (a calm kid's bedroom). References: A, B, C, D

> [PRODUCT] The final reference image shows the included remote control exactly: a slim white remote with brightness up and down, OFF and ON keys, R G B W keys, twelve colored color keys and FLASH, STROBE, FADE and SMOOTH keys. Setting: a calm kid's bedroom at night in an everyday warm-modern home: soft sage-green walls, a small white-oak nightstand beside a single bed with a patterned quilt, a knitted toy rabbit on the bed. An adult hand holds the remote pointed at the Tidewave, which glows violet-purple on the nightstand and throws soft violet ripple rays up the wall behind it. Medium close shot, the remote sharp in the foreground left, the lamp sharp in the midground right, a calm lower-left area. Photorealistic. No text, no logo, no watermark.

Label: `"16 COLORS · REMOTE CONTROL"` / `"24-key remote: color, brightness, flash, strobe, fade, smooth"`

### 10: colors (three edits of the accepted 01, composited 2×2)
References for each edit: **accepted 01 first**, then C, A, plus x3 for the amber edit.

> Edit the first reference image. Change only the Tidewave lamp's light color from aqua-blue to {warm amber | emerald green | magenta-pink}, at the same brightness. The glow inside the cube and the ripple rays on the wall change to that color; everything else stays identical: same shelf, vase, wall, window view, time of day, product position, camera and crop. The other references show the exact product. No text, no logo, no watermark.

Composite: `python tidewave_overlays.py colors 01-aqua.jpg amber.jpg green.jpg pink.jpg 10-tidewave-colors.jpg`

### 11: dimming (edit of the accepted 07)
References: **accepted 07 first**, then C, A

> Edit the first reference image. Dim only the Tidewave lamp to about 20 percent brightness, keeping the same deep ocean-blue color: the cube glows faintly and the blue ripple rays on the paneling become much fainter and shorter. Change nothing else: same sofa, throw, side table, popcorn, TV glow, walls, window, camera and crop. The other references show the exact product. No text, no logo, no watermark.

Label: `"STEPLESS DIMMING"` / `"Adjust brightness from 10% to 100% with the remote"`

### 12: touch switch + USB power
Environment: **Everyday warm-modern home** bedroom. References: A, B, E, x1

> [PRODUCT] Close-up: a fingertip gently touching the circular touch power icon on the front of the lamp's pale wood-grain base; the cube glows soft warm white and throws gentle warm ripple rays on the wall behind. The thin white USB cable runs from the base across a light oak dresser top toward the back. An everyday warm-modern bedroom in the evening, background softly out of focus. Photorealistic, natural skin and materials. [LIGHT-REF LINE] No text, no logo, no watermark.

Label: `"TOUCH SWITCH · USB POWERED"` / `"136 cm (53.5 in) USB cable"`
