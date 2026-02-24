# Ursoaia EDU — Blog Platform

Static prototype / design specification for the Ursoaia EDU blog platform — a Medium-like educational blog for Odoo School students.

## Pages

| File | Description |
|---|---|
| `home.html` | Main feed — article list, featured post, sidebar |
| `article.html` | Sample article page with full typography |
| `reference.html` | External resources & Google Drive links |
| `base_of_html.html` | Web course — video lessons |
| `spec.html` | Full technical architecture specification |

## Features

- **Dark / Light theme** — CSS custom properties + `localStorage` persistence
- **Responsive** — mobile-first, works on all screen sizes
- **Medium-like design** — Georgia serif typography, clean layout
- **No JavaScript frameworks** — vanilla JS only

## Architecture (planned backend)

See [`spec.html`](spec.html) for full technical specifications:

- **Backend:** Python 3.12 + Django 5.x + Wagtail CMS 6.x
- **Database:** PostgreSQL 16
- **Server:** Nginx + Gunicorn + Docker Compose
- **SSL:** Let's Encrypt (auto-renewal)
- **RAM budget:** ~520 MB / 1024 MB on a 1 GB VPS
