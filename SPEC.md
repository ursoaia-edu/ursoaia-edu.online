# Improvement Spec

Per-item implementation spec for items tracked in [TODO.md](./TODO.md).
Each section names the goal, the files to touch, key implementation notes, and the acceptance criteria.

---

## OG image (1200×630)

- **Goal.** Replace the square logo fallback with a proper Open Graph card so link previews on Facebook, Telegram, LinkedIn, Slack, and X look intentional rather than cropped.
- **Files.** `docs/assets/og-default.png` (new, 1200×630), `custom_theme/base.html` (`_og_image` line).
- **Implementation.** Design the card with the project name, tagline, and logo on the brand orange-amber gradient. Save as PNG ≤ 200 KB. Update `_og_image` in `base.html` to `config.site_url.rstrip('/') ~ '/assets/og-default.png'`. Optionally add per-page override via `page.meta.og_image`.
- **Acceptance.** Pasting any deployed page URL into [opengraph.xyz](https://www.opengraph.xyz) shows the new image; Telegram, X, and LinkedIn previews use it.

---

## BreadcrumbList JSON-LD

- **Goal.** Show hierarchical breadcrumbs in Google SERPs (e.g. `ursoaia-edu.online › Projects › ESP32 › Temperature`) instead of bare URLs.
- **Files.** `custom_theme/base.html` (add a conditional `<script type="application/ld+json">` block in `<head>`).
- **Implementation.** Render a `BreadcrumbList` from `page.ancestors|reverse` plus `page` itself, prefixed with the localized "Home" item. Skip on the homepage (`page.ancestors` empty). Use `|tojson` for any user-controlled string to avoid breaking the JSON. Sections without their own URL get `first_page_url(section)` as item.
- **Acceptance.** Inner page JSON-LD passes [Google Rich Results Test](https://search.google.com/test/rich-results). After re-indexing, breadcrumbs appear in SERPs for at least one inner page.

---

## Course / Article structured data

- **Goal.** Surface educational content as rich results: courses with description and provider, projects as articles with author and dates.
- **Files.** `custom_theme/base.html` (extend the existing `@graph` JSON-LD with conditional `Course` and `Article` entries).
- **Implementation.** Detect page type from `page.url`:
  - Starts with `courses/` → emit `Course` with `name`, `description`, `provider` (Organization), `inLanguage`, `educationalLevel: beginner`.
  - Starts with `projects/` → emit `Article` with `headline`, `description`, `image`, `datePublished` (from `page.meta.date` if present), `author: Organization`, `inLanguage`.
- **Acceptance.** Rich Results Test recognises `Course` on `/courses/python/01-...` and `Article` on `/projects/esp32/temperature_web/`. No validation errors.

---

## Per-page `description` frontmatter

- **Goal.** Unique meta description per page so Google snippets describe the actual page, not the homepage tagline.
- **Files.** All `docs/courses/python/*.md`, `docs/courses/web/*.md`, `docs/projects/**/*.md` (~80 files including i18n variants).
- **Implementation.** Add `description: "..."` (≤ 160 chars) to each file's frontmatter. Mirror RO and EN variants. The template already falls back `description → summary → site_description`, so files with `summary:` are fine — only add explicit `description:` where neither exists.
- **Acceptance.** `curl -s https://ursoaia-edu.online/projects/esp32/temperature/ | grep description` returns a unique value per page across the site.

---

## Replace Tailwind CDN with built CSS

- **Goal.** Remove the ~3 MB JS payload of `cdn.tailwindcss.com` and the in-browser JIT, fixing LCP and TBT.
- **Files.** `package.json` (new), `tailwind.config.js` (new), `docs/assets/css/tailwind.input.css` (new), `pyproject.toml` (`build` script), `custom_theme/base.html` (replace `<script src="cdn.tailwindcss.com">` with `<link>` to built CSS), `.gitignore` (ignore `node_modules/`).
- **Implementation.** Add `tailwindcss` + `@tailwindcss/typography` as npm devDependencies. Configure `content: ["./custom_theme/**/*.html", "./docs/**/*.md"]` in `tailwind.config.js`. Generate `docs/assets/css/tailwind.css` via `npx tailwindcss -i ... -o ... --minify`. Wire as a pre-step in the `build` script in `pyproject.toml` (or via a Makefile / `uv run` shim). CI must run `npm install && npm run build:css` before `mkdocs build`.
- **Acceptance.** Lighthouse mobile Performance score ≥ 85 on the homepage. No `cdn.tailwindcss.com` request in the production HTML. Bundle size of CSS ≤ 50 KB gzipped.

---

## Image optimization

- **Goal.** Smaller image bytes, faster LCP, lower bandwidth.
- **Files.** All `.png`/`.jpg` under `docs/assets/images/`.
- **Implementation.** Convert non-SVG assets to WebP using `cwebp -q 80`. Keep originals as fallback only if needed. Update Markdown image references to `.webp`. Add `loading="lazy"` to non-hero images via a Markdown extension or a simple post-process step. Optional: generate 480 / 960 / 1440 widths and use `srcset`.
- **Acceptance.** Total image bytes on `/projects/arduino/starter_kit/` drops by ≥ 50 %. Lighthouse "Properly size images" and "Serve images in modern formats" both pass.

---

## Self-host fonts

- **Goal.** Remove third-party render-blocking from `fonts.googleapis.com`; faster first paint and one less external dependency.
- **Files.** `docs/assets/fonts/` (new, woff2 files), `custom_theme/base.html` (replace Google Fonts `<link>` with `@font-face` block in `<style>`).
- **Implementation.** Download Inter (300/400/500/600/700) and JetBrains Mono (400/500) `.woff2` from [google-webfonts-helper](https://gwfh.mranftl.com). Add `@font-face` declarations with `font-display: swap`. Drop the Google Fonts `<link>`.
- **Acceptance.** Network tab shows zero requests to `fonts.googleapis.com` / `fonts.gstatic.com`. Fonts render unchanged.

---

## Google Search Console

- **Goal.** Get the site indexed and monitor search performance.
- **Files.** Optional: `custom_theme/base.html` (insert `<meta name="google-site-verification">` if HTML-tag verification is chosen).
- **Implementation.** Create URL-prefix property for `https://ursoaia-edu.online`. Verify via DNS TXT (preferred — no code change) or HTML meta tag. After verification, submit `https://ursoaia-edu.online/sitemap.xml` under Sitemaps.
- **Acceptance.** Property status is `Verified`. Sitemap status is `Success` with a non-zero URL count.

---

## GTM container tags

- **Goal.** GA4 pageviews flowing through the existing GTM container `GTM-WD9LXKB7`.
- **Files.** None in this repo. Configuration lives in the GTM web UI.
- **Implementation.** In Tag Manager: new tag → **Google tag** with `Tag ID: G-PQC2Y5KWP9` → trigger **All Pages** → publish version. No custom Data Layer required for v1.
- **Acceptance.** GA4 → Realtime shows live users when the deployed site is opened. GTM Preview Mode confirms the tag fires on every page view.

---

## GA4 verification

- **Goal.** Confirm Analytics is collecting after GTM publish.
- **Files.** None.
- **Implementation.** Open the deployed site in a new tab. In GA4 → Reports → Realtime → check "Users in last 30 minutes" > 0. Optionally trigger a `page_view` debug event via GTM Preview.
- **Acceptance.** Realtime card shows the visit within 30 seconds.

---

## Custom 404 page

- **Goal.** Friendly 404 with site nav and a search box instead of bare server error.
- **Files.** `docs/404.md` (new), optional `custom_theme/main.html` (route check).
- **Implementation.** Create `docs/404.md` with frontmatter `title: Page not found`. Body: short message, link to home, link to projects/courses index. MkDocs serves it as `/404.html` automatically when `nav` does not include it. GitHub Pages / Cloudflare Pages picks it up as the default 404 page.
- **Acceptance.** `https://ursoaia-edu.online/this-does-not-exist` returns the custom 404 with full nav and theme.

---

## `humans.txt`

- **Goal.** Acknowledge contributors; signal that the site is human-made.
- **Files.** `docs/humans.txt` (new).
- **Implementation.** Plain text following [humanstxt.org](https://humanstxt.org) conventions: `/* TEAM */`, `/* SITE */` blocks. List the circle members and the tech stack.
- **Acceptance.** `https://ursoaia-edu.online/humans.txt` returns `200`.

---

## `security.txt`

- **Goal.** Standardised vulnerability-disclosure contact per [RFC 9116](https://www.rfc-editor.org/rfc/rfc9116).
- **Files.** `docs/.well-known/security.txt` (new).
- **Implementation.** Plain text with `Contact:`, `Expires:`, `Preferred-Languages:`. Sign with PGP if a key exists. `Expires` should be ≤ 1 year out and renewed yearly.
- **Acceptance.** `https://ursoaia-edu.online/.well-known/security.txt` returns `200` and validates at [securitytxt.org](https://securitytxt.org).
