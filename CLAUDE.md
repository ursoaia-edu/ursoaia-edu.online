# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Stack

- **Backend**: FastAPI 0.129 + SQLAlchemy 2.0 (async) + PostgreSQL 16 + Alembic migrations
- **Frontend**: Astro 5 SSR (Node adapter) + Tailwind CSS 3.4 + daisyUI 4.12
- **Proxy**: Nginx → routes `/` to frontend:4321, `/api` and `/admin` to backend:8000, `/uploads` served as static files
- **Auth**: JWT (HS256) in HttpOnly cookies, 24h expiry, admin-only endpoints under `/api/admin/*`
- **Content**: TipTap rich-text JSON stored in DB; frontend has a custom JSON→HTML renderer

## Development

```bash
# Start all services (hot reload enabled)
docker compose -f docker-compose.dev.yml up -d

# Frontend:  http://localhost:4321
# Admin UI:  http://localhost:8000/admin
# API:       http://localhost:8000/api
# DB:        localhost:65432  (ursoaia / ursoaia123)
```

### Database migrations

```bash
# Inside the backend container or venv:
alembic revision --autogenerate -m "description"
alembic upgrade head
alembic downgrade -1
```

### Frontend only

```bash
cd frontend
npm run dev      # dev server
npm run build    # production build
```

### Backend only

```bash
cd backend
uvicorn app.main:app --reload
```

## Architecture

### Request flow

```
Browser → Nginx (80/443)
  /            → frontend:4321  (Astro SSR, all pages dynamic)
  /api/*       → backend:8000   (rate-limited REST API)
  /admin/*     → backend:8000   (Jinja2 server-rendered admin panel)
  /uploads/*   → static files   (images only, 30-day cache, referer-validated)
```

### Backend layout (`backend/app/`)

- `main.py` — app factory, router registration, startup (creates admin user from env)
- `config.py` — Pydantic Settings; all env vars loaded here
- `models/` — SQLAlchemy ORM models (User, Article, Category, Tag, Media + M2M tables)
- `routers/` — FastAPI route handlers; `admin/` prefix = admin API/UI, `public/` = public API
- `schemas/` — Pydantic request/response schemas
- `services/` — business logic layer called by routers
- `dependencies.py` — shared FastAPI `Depends` (DB session, current user)
- `database.py` — async engine + session factory

### Frontend layout (`frontend/src/`)

- `pages/` — Astro pages (SSR); file-based routing
- `components/` — Astro/HTML components
- `lib/api.ts` — `fetchApi<T>()` centralised API client (all backend calls go through here)
- `lib/tiptap.ts` — TipTap JSON → HTML renderer for article content

### Key design decisions

- All Astro pages use SSR (`output: 'server'`); there is no static generation.
- TipTap content is stored as JSON in the DB and rendered to HTML at request time in the frontend.
- The admin panel is Jinja2 (server-rendered by FastAPI), not part of the Astro frontend.
- File uploads are validated server-side (10 MB max, allowed: jpg/jpeg/png/gif/webp/svg) and served by Nginx directly from `/uploads/`.

## Environment variables

Copy `.env.example` → `.env`. Critical production values:

| Variable | Purpose |
|---|---|
| `SECRET_KEY` | JWT signing key — must be set |
| `ADMIN_EMAIL` / `ADMIN_PASSWORD` | Bootstrapped admin account |
| `FRONTEND_URL` | Used for CORS and links in admin panel |
| `API_URL` | Frontend → backend URL (default `http://backend:8000/api`) |

## Language & locale

UI is in **Romanian** (`lang="ro"`). Keep all user-visible strings in Romanian.
