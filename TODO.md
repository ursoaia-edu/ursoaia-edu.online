# TODO

Pending improvements for [ursoaia-edu.online](https://ursoaia-edu.online).
Tracked here so they don't fall through the cracks. PRs welcome.

## SEO — markup & metadata

- [ ] **OG image (1200×630).** Currently `assets/logo.png` is used as fallback in `custom_theme/base.html`. Create `docs/assets/og-default.png` (1200×630, project tagline + logo) and update `_og_image` path in `base.html`.
- [x] **BreadcrumbList JSON-LD** on inner pages. Generate from `page.ancestors` in `custom_theme/base.html` so Google shows hierarchical breadcrumbs in SERPs.
- [x] **Course / Article structured data.** Add `Course` schema on `docs/courses/python/*` and `docs/courses/web/*` pages, `Article` schema on `docs/projects/**/*` pages. Conditional in `base.html` based on `page.url`.
- [ ] **Per-page `description` frontmatter** on inner pages. Currently only homepage RO/EN, `courses/index.*`, and `projects/index.*` have descriptions/summaries. Add ~140-160 char `description:` to each course lesson and project page so Google shows unique snippets per page.

## Performance — Core Web Vitals

- [ ] **Replace Tailwind CDN with built CSS.** `<script src="https://cdn.tailwindcss.com">` in `custom_theme/base.html` ships ~3 MB of JS and runs JIT in the browser, killing LCP. Switch to Tailwind CLI: add a `package.json` with `tailwindcss`, generate `docs/assets/css/tailwind.css`, hook into `uv run build`.
- [ ] **Image optimization.** Convert heavy `.png`/`.jpg` under `docs/assets/images/` to WebP. Add `loading="lazy"` to non-hero images. Consider `srcset` for responsive sizes.
- [ ] **Self-host fonts.** Inter and JetBrains Mono are loaded from `fonts.googleapis.com`. Self-host or `preconnect` to reduce render-blocking.

## Operations — external accounts

- [ ] **Google Search Console** verification + sitemap submission for `https://ursoaia-edu.online/sitemap.xml`. Choose verification method (HTML tag in `base.html` or DNS TXT). After verification, submit sitemap.
- [ ] **GTM container tags.** Container `GTM-WD9LXKB7` is wired into the site but empty. Create GA4 Configuration tag in [tagmanager.google.com](https://tagmanager.google.com) using Measurement ID `G-PQC2Y5KWP9`, fire on All Pages, publish.
- [ ] **GA4 verification.** After GTM publishes, confirm Realtime reports show traffic.

## Nice-to-haves

- [x] **Custom 404 page** with site nav and search.
- [x] **`humans.txt`** — small but meaningful for an open-source educational site.
- [x] **`security.txt`** — contact for vulnerability disclosure (under `docs/.well-known/security.txt`). Wired via `hooks/copy_well_known.py` since MkDocs skips dotfile dirs by default.
