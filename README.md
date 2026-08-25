# Legends Awakened — Shopify Store

A custom Shopify theme for the **Legends Awakened** merch store, built on top of Shopify's
free [Dawn](https://github.com/Shopify/dawn) theme and reskinned with a dark-fantasy,
black/gold brand: original channel art on tees, hoodies, and posters.

This repo is the **theme code**, not a live store — Shopify stores are hosted and configured
in Shopify's own admin (products, payments, domain, POD fulfillment, etc.), which isn't
something that can be created from a git repo. Follow **[store-setup/SETUP.md](store-setup/SETUP.md)**
to turn this theme into a real, live store.

## What's in here

- Full Dawn theme structure (`sections/`, `snippets/`, `templates/`, `assets/`, `config/`, `locales/`)
- `config/settings_data.json` — rebranded color schemes (black/charcoal background, gold accent,
  deep-red hero scheme) and typography (Cinzel display font for headings, Work Sans for body)
- `templates/index.json` — a branded homepage: hero, shop-by-category, new drops, "our story", email signup
- `assets/legends-awakened.css` — ornamental gold accents (section dividers, hero corner marks,
  hover glow on product cards) layered on top of Dawn's base styles
- `sections/header-group.json` / `footer-group.json` — gold announcement bar, dark header/footer,
  footer blocks (about text, quick links, social icons)
- `store-setup/products-import.csv` — a placeholder catalog (tee, hoodie, poster with size/color
  variants) formatted for Shopify's product CSV importer, so you have a real catalog structure to
  start from instead of an empty store
- `store-setup/SETUP.md` — step-by-step guide: create the Shopify account, upload this theme,
  import the placeholder products, swap in your art, connect a print-on-demand fulfiller, set up
  payments/domain, and launch

## Customizing further

Once the theme is uploaded to a Shopify store, most day-to-day changes (homepage layout, colors,
menus, adding products/collections) can be done in **Shopify's theme editor and admin** — you
don't need to edit this code for routine updates. Come back to this repo when you want to change
structure/behavior beyond what the theme editor exposes (custom sections, layout logic, etc.).
