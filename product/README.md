# The Fruit-Powered Life — $20 Digital Product

A fruitarian lifestyle guide that synthesizes the best, most actionable lessons commonly
associated with **Loren Lockman** (physiology & Natural Hygiene simplicity), **Ted Carr**
(long-term, sustainable practice), and **Shane Sterling** (calorie/numbers discipline)
into one practical framework.

## Files

- **`The-Fruit-Powered-Life.pdf`** — the finished, sellable ebook (15 pages: cover, table of
  contents, 5 core sections, 30-day transition plan, troubleshooting, appendices, back cover).
- **`src/content.md`** — the finalized written content in plain Markdown (source of truth for wording).
- **`src/book.html`** — the styled HTML source used to render the PDF (fonts, layout, palette).

## Regenerating the PDF

The PDF is built from `src/book.html` using headless Chromium's print-to-PDF:

```bash
chromium --headless --disable-gpu --no-sandbox \
  --print-to-pdf="product/The-Fruit-Powered-Life.pdf" \
  --print-to-pdf-no-header --no-pdf-header-footer \
  "file://$(pwd)/product/src/book.html"
```

If you edit the content, update `src/content.md` first, then mirror the change into the
corresponding section of `src/book.html`, then re-render.

## Content & attribution note

This guide is an **independent, original synthesis** of publicly discussed philosophies
associated with these three practitioners. It is not officially affiliated with, endorsed
by, or reviewed by Loren Lockman, Tanglewood Wellness Center, Ted Carr, or Shane Sterling,
and it is not medical advice — this is stated explicitly inside the product (welcome page
and back cover).
