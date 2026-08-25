# Launching the Legends Awakened store

This is the step-by-step path from "theme code in a repo" to "live store taking orders." Nothing
here requires coding — it's all done in Shopify's admin. Budget an afternoon for the first pass.

## 1. Create the Shopify account

1. Go to shopify.com and start a trial (or your existing plan).
2. Pick a store name — doesn't have to be final, you can change it later. Use something you can
   also get as a domain, e.g. `legendsawakenedshop`.
3. Shopify plans start around $25–40/mo (checked at signup, pricing changes). You need at least
   the **Basic** plan to sell; don't pay for a plan until your trial is ending and you're ready
   to launch.

## 2. Upload this theme

You have two options:

**Option A — zip upload (no tools needed)**
1. Download this repo as a `.zip` (GitHub → Code → Download ZIP), or `git clone` it locally.
2. Zip the **contents** of the repo (not a folder containing them) — `assets/`, `config/`,
   `layout/`, `locales/`, `sections/`, `snippets/`, `templates/` should be at the top level of
   the zip.
3. In Shopify admin: **Online Store → Themes → Add theme → Upload zip file**.
4. Once uploaded, click **Actions → Publish** to make it live (or preview it first — see below).

**Option B — Shopify CLI (if you're comfortable with a terminal)**
```
npm install -g @shopify/cli
shopify theme dev    # live preview while you edit
shopify theme push   # push this code to your store
```
Requires Node.js and logging into your Shopify store via the CLI (`shopify auth login`).

Either way, **preview before publishing**: Shopify gives every uploaded theme a preview link so
you can click through the store before it's visible to customers.

## 3. Add your logo

The theme currently falls back to your store name in the Cinzel gold display font — that already
looks on-brand, so a logo isn't required to launch. When you have one:
**Online Store → Themes → Customize → Header → Logo**, upload a PNG/SVG (transparent background
recommended). Keep it simple — it'll be small in the header.

## 4. Add your products

You put your own art on the merch, so there are two ways to go:

### Option A — Print-on-demand (recommended for a YouTuber)
No inventory, no shipping, no upfront cost — you upload art, a POD partner prints and ships each
order, Shopify handles the storefront/checkout. Standard setup:
1. Install **Printful** or **Printify** from the Shopify App Store.
2. In the app, create products (t-shirt, hoodie, poster, etc.), pick the blank garment/color, and
   upload your artwork as the print file (each app has resolution/placement guides per product).
3. Set your retail price — the app shows you the base cost, you set the markup.
4. Push the product to Shopify. It creates a real product with real variants automatically —
   you can skip the CSV import below for anything you create this way.

This is the lowest-risk way to sell merch with original art and is what most channels use.

### Option B — Start from the placeholder catalog (this repo)
`store-setup/products-import.csv` has 3 draft products already structured (Awakened Sigil Tee,
Legends Awakened Hoodie, The Awakening Print — with size/color variants, prices, and SKUs) so you
aren't starting from a blank product list.
1. **Products → Import** in Shopify admin, upload `products-import.csv`.
2. Products land as **drafts** — edit each one to: upload real product photos of your art on the
   actual garment, adjust price/description if needed, then set status to **Active**.
3. If you're doing your own printing/fulfillment (not POD), also set **Variant Inventory Qty**
   and **Fulfillment Service** correctly for each variant before going live.

You can mix both — e.g. posters self-fulfilled, apparel via Printful.

## 5. Organize into collections

Create collections for **Tees**, **Hoodies**, and **Posters** (Products → Collections → Create
collection, automated by product type/tag works well since the CSV already tags things
`apparel`/`poster`). Then in **Online Store → Themes → Customize → Home page → Shop by category**
section, assign each of the 3 collection blocks to the matching collection — right now they're
placeholders pointing at nothing.

## 6. Set up payments

**Settings → Payments**. Shopify Payments is the simplest option (no separate account, but
availability depends on your country) — otherwise connect PayPal, Stripe, etc. Without this step
customers can't check out.

## 7. Connect a domain

**Settings → Domains**. Buy one through Shopify or connect one you already own (e.g. from
Namecheap/Google Domains) and point its DNS at Shopify per their instructions. Something like
`legendsawakenedshop.com` or `.shop` ties it back to the channel.

## 8. Update the placeholders before launch

A few things in this theme are intentionally placeholder and need your real info:
- **YouTube link**: `config/settings_data.json` → `social_youtube_link` is set to a guessed URL —
  update it in **Online Store → Themes → Customize → Theme settings → Social media** to your real
  channel URL (or any other socials you run).
- **Announcement bar text** ("Free shipping over $60", "New drop") — edit in
  **Customize → Header → Announcement bar** to match your actual shipping policy/promo.
- **Footer "About" text** and **brand description** — tune the copy in **Customize → Footer** and
  **Theme settings → Brand** to sound like you, not a generic placeholder.
- **Footer menu**: the footer's "Quick links" block points at a menu handle called `footer` —
  Shopify creates this by default; add/edit its links under **Online Store → Navigation**.

## 9. Legal/policy pages

**Settings → Policies** — Shopify can auto-generate a refund, privacy, terms of service, and
shipping policy template for you to review and adjust.

## 10. Launch checklist

- [ ] Theme published and previewed on desktop + mobile
- [ ] At least one collection live with real product photos (not blank placeholders)
- [ ] Payments connected and tested with a real or test order
- [ ] Domain connected
- [ ] Social links point to your actual channel/socials
- [ ] Password/coming-soon page turned off (**Online Store → Preferences** → disable password
      protection) when you're ready for the public to see it

## Notes on the theme code itself

If you want to change layout/structure beyond what the Shopify theme editor exposes (custom
sections, new page templates, deeper styling), edit the files in this repo and re-upload/push —
see the main [README.md](../README.md) for what's already customized.
