# Tidewave Aurora Projector Light: product-image run pack

Prepared 2026-09-23 with the Duskhaven product-image skill (Luno Studio, Nano Banana Pro, 4K, 4:5).

**Status: no images generated yet.** This session ran in a cloud container. It had no access to Todd's Chrome, where Luno is signed in, or to the `C:\Users\Todd\...` folders. Luno redirects everything to a login page and has no public API. The skill never signs in on Todd's behalf, so generation stopped at the prompt stage. Everything needed to generate is here:

- `prompts.md`: shot plan, reference upload order and the exact prompt for every slot
- `tidewave_overlays.py`: name-and-symbol, dimension card, feature labels and the 2×2 colors composite (tested on stand-in images)
- The reference images are **not** in this public repo because some come from other sellers. They were sent separately as `tidewave-refs.zip`.

## Product (Shopify)
- **Tidewave Aurora Projector Light**, SKU DH-TIDE-01, one variant ("Default Title"), vendor Duskhaven
- Supplier: `custom.aliexpress_url` = https://www.aliexpress.com/item/1005009888234857.html
- Established mark (from the "branded product photo"): a one-period sine-wave stroke + `TIDEWAVE` in spaced medium caps, cream

## Verified facts (the only ones allowed in labels)
| Fact | Value | Source |
|---|---|---|
| Overall size | 11.2 × 11.2 × 11.2 cm (4.4 in) | Supplier "Product Size" card |
| Crystal cube | about 9.5 cm (3.74 in) wide | Supplier gallery dimension image |
| Base | Square, pale wood-grain finish, touch power icon on the front | Supplier gallery |
| Cable | White USB-A, 136 cm (53.5 in) | Supplier "Product Size" card |
| Remote | 24-key IR: brightness +/−, OFF, ON, R/G/B/W, 12 color keys, FLASH/STROBE/FADE/SMOOTH | Supplier gallery |
| Colors | 16 | Supplier gallery + Shopify listing |
| Dimming | Stepless, 10–100% via remote | Supplier gallery |
| Light effect | Dynamic water-ripple projection on walls and ceiling | Supplier gallery + Shopify listing |

**Flagged; don't guess:**
- **Height conflict:** one supplier image says 11 cm / 4.33 in high with an 11 cm base; the size card says 11.2 cm. The dimension card uses 11.2 cm. Confirm with the supplier if exactness matters.
- **Not verified:** wattage, cube material (acrylic vs glass), whether a power adapter is included, full package contents, and remote battery. No label mentions these.
- **Remote casing:** shown white in two supplier images and black-framed in one.
- **Not collected:** AliExpress showed a reCAPTCHA, so the description images, specification table, review photos and SKU images were not collected. Only the 6 gallery images came through. Re-check reviews from Chrome if needed.

## Reference vetting
**Kept (supplier, text removed):**
- g06: studio shot, unlit, with cable. Labels, arrows and remote inpainted out.
- g03: studio shot and remote. Dimension lines and callouts removed.
- g01: lit aqua cube, cropped away from the exaggerated room collage.

**Kept (other sellers, same design; you approved this):**
- x1–x3 (docos.us listing): real photos of white, cool-white and amber light on a wall.
- x4 (aquaticvita.com listing): real photo of blue light in a fully dark room.
- x5 (docos.us listing): real close-up of the unlit texture.
- These are for light behaviour and texture only. The docos.us version is a larger 13 × 14 cm size.

**Rejected:**
- g02: charcoal base, a finish the store doesn't sell, plus promotional text
- g05: dark walnut base (different finish); kept as facts only (dimming 10–100%)
- g04: color-chart infographic; facts only (16 colors)
- g07: a business-license image, not the product
- Shopify supplier image S4ec1…: white base (different finish) plus promotional text
- Duskhaven's own clean, branded and features images: these are store assets, not supplier evidence. The branded photo was used only to copy the mark.
- Other-seller extras: promotional infographics, a larger-size dimension drawing, and photos with clocks, turntables or plants that a model would copy

## Environment plan and log rows
`environment-log.md` is on Todd's PC and couldn't be read. Check these rooms against recent products before generating. After the run, append:

```
| 2026-09-23 | Tidewave | Tidewave_NanoBananaPro_Luno_NN | 03, 04 | Contemporary city apartment | queen bed, low charcoal-linen upholstered headboard, slate-blue duvet; two 55 cm light-walnut tapered-leg nightstands; muted blue-gray walls; one muted abstract print; oatmeal wool rug; right-hand window, sheer curtains, city lights at night |
| 2026-09-23 | Tidewave | Tidewave_NanoBananaPro_Luno_NN | 01, 10 | Modern garden house | warm-timber floating shelf; limewashed plaster wall; stoneware vase with olive branch; steel-framed window onto dusk courtyard |
| 2026-09-23 | Tidewave | Tidewave_NanoBananaPro_Luno_NN | 02 | Collected antique-inspired home | vintage walnut chest of drawers; deep olive walls with traditional molding; cloth-bound books |
| 2026-09-23 | Tidewave | Tidewave_NanoBananaPro_Luno_NN | 05 | Everyday warm-modern home | light oak desk; linen curtains; morning daylight; notebook, ceramic pencil cup |
| 2026-09-23 | Tidewave | Tidewave_NanoBananaPro_Luno_NN | 07, 11 | Quiet woodland retreat | knotty-pine paneling; rust corduroy sofa, knitted throw; rustic oak side table; pine silhouettes through window |
| 2026-09-23 | Tidewave | Tidewave_NanoBananaPro_Luno_NN | 09 | Everyday warm-modern home | kid's bedroom; sage walls; white-oak nightstand; single bed with patterned quilt; knitted toy rabbit |
| 2026-09-23 | Tidewave | Tidewave_NanoBananaPro_Luno_NN | 12 | Everyday warm-modern home | light oak dresser top; evening bedroom, background soft |
```

## Shot list (14 Luno jobs: 9 new generations + 5 edits, then overlays)
| # | Shot | Built by |
|---|---|---|
| 01 | Signature hero | generate |
| 02 | Name + symbol | generate + overlay |
| 03 | Head-on, room lights on (pilot) | generate first |
| 04 | Head-on, room lights off | edit of accepted 03 |
| 05 | Alternate view (unlit) | generate |
| 06 | Material detail | generate |
| 07 | Second lifestyle | generate |
| 08 | Dimensions | generate + card overlay |
| 09 | Remote / 16 colors | generate + label |
| 10 | Colors 2×2 | 3 edits of 01 + composite |
| 11 | Stepless dimming | edit of 07 + label |
| 12 | Touch switch + USB | generate + label |

These will be AI-generated, reference-grounded lifestyle images. They are not measured evidence of brightness, coverage or exact dimensions.
