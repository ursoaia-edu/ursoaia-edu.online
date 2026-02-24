# Ursoaia Edu — Спецификация проекта

## Цель

Современный блог/новостной сайт с админкой для образовательного портала.

- **Backend**: Python (FastAPI) + PostgreSQL
- **Frontend**: Astro 5 (SSR) + Tailwind CSS + daisyUI
- **Admin Panel**: Jinja2 + HTMX (серверный рендеринг)
- **Редактор**: TipTap (JSON-контент)
- **Инфраструктура**: Docker Compose + Nginx reverse proxy
- **Дизайн**: тёмно-синие градиенты + красно-оранжевые акценты

---

## Стек технологий

### Backend

| Компонент | Версия |
|-----------|--------|
| Python | 3.12 |
| FastAPI | 0.129.0 |
| SQLAlchemy (async) | 2.0.46 |
| asyncpg | 0.30.0 |
| Alembic | 1.17.2 |
| Pydantic | 2.12.5 |
| python-jose (JWT) | 3.5.0 |
| passlib (bcrypt) | 1.7.4 |
| Jinja2 | 3.1.6 |
| bleach | 6.1.0 |
| Pillow | 12.1.1 |
| slowapi | 0.1.9 |
| python-slugify | 8.0.4 |

### Frontend

| Компонент | Версия |
|-----------|--------|
| Astro | 5.17 |
| @astrojs/node | 9.x |
| @astrojs/sitemap | 3.x |
| @astrojs/rss | 4.x |
| @astrojs/tailwind | 6.x |
| @tailwindcss/typography | 0.5.x |
| Tailwind CSS | 3.4 |
| daisyUI | 4.12 |

### Инфраструктура

| Компонент | Версия |
|-----------|--------|
| PostgreSQL | 16 (Alpine) |
| Nginx | Alpine |
| Node.js | 20 (Alpine) |
| Docker Compose | v2 |

---

## Структура проекта

```
ursoaia-edu.online/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI app + lifespan (auto-create admin)
│   │   ├── config.py               # pydantic-settings (env vars)
│   │   ├── database.py             # AsyncSession + engine + Base
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py             # User (email, password_hash, is_admin, is_active)
│   │   │   ├── article.py          # Article (TipTap JSON content) + article_categories
│   │   │   ├── category.py         # Category (name, slug, color)
│   │   │   ├── tag.py              # Tag (name, slug, color) + article_tags
│   │   │   └── media.py            # Media (filename, url, mime, dimensions)
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── article.py          # ArticleCreate/Update/Preview/Response/ListResponse
│   │   │   ├── category.py
│   │   │   ├── tag.py
│   │   │   └── media.py
│   │   ├── api/
│   │   │   ├── __init__.py         # api_router (монтирует все sub-routers)
│   │   │   ├── public/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── articles.py     # GET /articles, GET /articles/{slug}
│   │   │   │   ├── categories.py   # GET /categories, GET /categories/{slug}
│   │   │   │   ├── tags.py         # GET /tags
│   │   │   │   └── search.py       # GET /search?q=
│   │   │   └── admin/
│   │   │       ├── __init__.py
│   │   │       ├── auth.py         # POST login/logout, GET /me, get_current_user dep
│   │   │       ├── articles.py     # CRUD /admin/articles
│   │   │       ├── categories.py   # CRUD /admin/categories
│   │   │       ├── tags.py         # CRUD /admin/tags
│   │   │       └── media.py        # GET/POST /admin/media, DELETE
│   │   ├── admin/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py           # Jinja2 HTML pages (dashboard, articles, etc.)
│   │   │   └── templates/
│   │   │       ├── base.html
│   │   │       ├── login.html
│   │   │       ├── dashboard.html
│   │   │       ├── articles/       # list, create, edit
│   │   │       ├── categories/
│   │   │       ├── tags/
│   │   │       └── media/
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── security.py         # JWT (HS256), bcrypt, verify_token()
│   │   │   ├── slug.py             # python-slugify + unique suffix
│   │   │   └── sanitization.py     # bleach (HTML + TipTap JSON sanitization)
│   │   └── static/
│   │       ├── css/
│   │       └── js/
│   ├── alembic/
│   │   ├── versions/
│   │   └── env.py                  # Overrides sqlalchemy.url from settings.DATABASE_URL
│   ├── alembic.ini
│   ├── requirements.txt
│   └── Dockerfile                  # python:3.12-slim
├── frontend/
│   ├── src/
│   │   ├── types/
│   │   │   └── api.ts              # Category, Tag, ArticlePreview, ArticleResponse, etc.
│   │   ├── lib/
│   │   │   ├── api.ts              # fetchApi<T>() — centralized API client
│   │   │   └── tiptap.ts           # renderTipTapContent() — JSON → HTML
│   │   ├── pages/
│   │   │   ├── index.astro         # Главная (категории + последние статьи)
│   │   │   ├── 404.astro           # Страница ошибки
│   │   │   ├── search.astro        # Поиск по статьям
│   │   │   ├── rss.xml.ts          # RSS лента (@astrojs/rss)
│   │   │   ├── articles/
│   │   │   │   ├── index.astro     # Список статей (пагинация)
│   │   │   │   └── [slug].astro    # Одна статья (TipTap рендеринг)
│   │   │   ├── categories/
│   │   │   │   ├── index.astro     # Все категории
│   │   │   │   └── [slug].astro    # Статьи по категории
│   │   │   └── tags/
│   │   │       ├── index.astro     # Все теги
│   │   │       └── [slug].astro    # Статьи по тегу
│   │   ├── layouts/
│   │   │   └── BaseLayout.astro    # HTML shell, nav, footer
│   │   ├── components/
│   │   │   ├── Header.astro        # Hero section
│   │   │   ├── Footer.astro        # CTA section
│   │   │   ├── ArticleCard.astro   # Карточка статьи
│   │   │   └── Pagination.astro    # Пагинация с ellipsis
│   │   └── styles/
│   │       └── global.css          # Tailwind directives + custom utilities
│   ├── astro.config.mjs            # output: 'server', @astrojs/node standalone
│   ├── tailwind.config.mjs         # typography + daisyUI (dark/light themes)
│   ├── package.json
│   ├── package-lock.json
│   ├── Dockerfile                  # Multi-stage: build → node:20-alpine runtime
│   ├── Dockerfile.dev              # node:20-alpine + npm run dev --host
│   └── nginx.conf                  # (legacy, unused — SSR теперь через Node)
├── uploads/                        # Загруженные медиа файлы
├── nginx/
│   └── nginx.conf                  # Reverse proxy: /admin, /api → backend; / → frontend
├── docker-compose.yml              # Production (postgres + backend + frontend + nginx)
├── docker-compose.dev.yml          # Development (hot reload, mounted volumes)
├── .env.example
├── .dockerignore
├── .gitignore
├── README.md
├── plan.md
├── task.md
└── spec.md
```

---

## Модели базы данных

### User

```python
class User(Base):
    __tablename__ = "users"

    id: Mapped[int]                    # PK
    email: Mapped[str]                 # unique, indexed
    password_hash: Mapped[str]
    is_admin: Mapped[bool]             # default=True
    is_active: Mapped[bool]            # default=True
    created_at: Mapped[datetime]       # server_default=now(), timezone=True
    updated_at: Mapped[datetime]       # onupdate=now(), timezone=True

    articles → List[Article]           # cascade="all, delete-orphan"
```

### Article

```python
class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int]                    # PK
    title: Mapped[str]                 # max 255
    slug: Mapped[str]                  # unique, indexed
    content: Mapped[dict]              # JSON (TipTap document)
    excerpt: Mapped[str]               # Text
    cover_image: Mapped[str]           # nullable
    is_published: Mapped[bool]         # default=False, indexed
    is_featured: Mapped[bool]          # default=False
    views_count: Mapped[int]           # default=0
    reading_time: Mapped[int]          # minutes, default=0
    author_id: Mapped[int]             # FK → users.id (CASCADE)
    created_at: Mapped[datetime]       # timezone=True
    updated_at: Mapped[datetime]       # onupdate, timezone=True
    published_at: Mapped[datetime]     # nullable, timezone=True

    author → User
    categories → List[Category]        # M2M через article_categories
    tags → List[Tag]                   # M2M через article_tags
```

### Category

```python
class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int]                    # PK
    name: Mapped[str]                  # max 100, unique
    slug: Mapped[str]                  # max 100, unique, indexed
    description: Mapped[str]           # nullable
    color: Mapped[str]                 # hex, default="#3B82F6"

    articles → List[Article]           # M2M
```

### Tag

```python
class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int]                    # PK
    name: Mapped[str]                  # max 50, unique
    slug: Mapped[str]                  # max 50, unique, indexed
    color: Mapped[str]                 # hex, default="#10B981"

    articles → List[Article]           # M2M
```

### Media

```python
class Media(Base):
    __tablename__ = "media"

    id: Mapped[int]                    # PK
    filename: Mapped[str]              # сгенерированное имя
    original_filename: Mapped[str]     # оригинальное имя
    url: Mapped[str]                   # путь к файлу
    mime_type: Mapped[str]
    size: Mapped[int]                  # bytes
    width: Mapped[int]                 # nullable
    height: Mapped[int]                # nullable
    alt_text: Mapped[str]              # nullable
    uploaded_at: Mapped[datetime]      # timezone=True
```

### Связующие таблицы

- `article_categories` (article_id PK, category_id PK) — CASCADE
- `article_tags` (article_id PK, tag_id PK) — CASCADE

---

## API Endpoints

### Публичное API (`/api`)

| Метод | Endpoint | Описание | Параметры |
|-------|----------|----------|-----------|
| `GET` | `/articles` | Список статей | `page`, `per_page`, `category`, `tag` |
| `GET` | `/articles/{slug}` | Одна статья | — |
| `GET` | `/categories` | Все категории | — |
| `GET` | `/categories/{slug}` | Одна категория | — |
| `GET` | `/tags` | Все теги | — |
| `GET` | `/search` | Поиск по статьям | `q`, `page`, `per_page` |

### Admin API (`/api/admin`)

| Метод | Endpoint | Описание |
|-------|----------|----------|
| `POST` | `/admin/auth/login` | Авторизация (JWT → HttpOnly cookie) |
| `POST` | `/admin/auth/logout` | Выход |
| `GET` | `/admin/auth/me` | Текущий пользователь |
| `GET/POST` | `/admin/articles` | Список / создание статей |
| `GET/PUT/DELETE` | `/admin/articles/{id}` | Чтение / обновление / удаление |
| `GET/POST` | `/admin/categories` | Список / создание категорий |
| `PUT/DELETE` | `/admin/categories/{id}` | Обновление / удаление |
| `GET/POST` | `/admin/tags` | Список / создание тегов |
| `PUT/DELETE` | `/admin/tags/{id}` | Обновление / удаление |
| `GET/POST` | `/admin/media` | Список / загрузка медиа |
| `DELETE` | `/admin/media/{id}` | Удаление медиа |

### Admin Panel (`/admin`)

| URL | Описание |
|-----|----------|
| `/admin/login` | Страница входа |
| `/admin/` | Dashboard (статистика + последние статьи) |
| `/admin/articles` | Список статей |
| `/admin/articles/create` | Создание статьи |
| `/admin/articles/{id}/edit` | Редактирование статьи |
| `/admin/categories` | Управление категориями |
| `/admin/tags` | Управление тегами |
| `/admin/media` | Медиа библиотека |

### Прочее

| URL | Описание |
|-----|----------|
| `GET /health` | Health check |
| `GET /rss.xml` | RSS лента (frontend) |
| `GET /sitemap-index.xml` | Sitemap (auto-generated) |

---

## Безопасность

### Аутентификация

- **JWT** (HS256) в HttpOnly cookie `access_token`
- Срок действия: 24 часа
- `verify_token()` для валидации (не только проверка наличия cookie)
- `datetime.now(timezone.utc)` вместо deprecated `datetime.utcnow()`
- Авто-создание admin пользователя при первом запуске

### Санитизация

- **HTML**: bleach с белым списком тегов и атрибутов (включая table, thead, tbody)
- **TipTap JSON**: рекурсивная санитизация узлов — очистка текста, валидация URL в link marks
- **Поиск**: экранирование `%` и `_` в LIKE-запросах

### Nginx

- Rate limiting: API (`10r/s`), login (`5r/m`)
- Security headers: `X-Frame-Options`, `X-Content-Type-Options`, `X-XSS-Protection`, `Referrer-Policy`
- Uploads: только image-расширения, проверка referer
- Gzip сжатие

### Конфигурация

- `DEBUG: bool = False` по умолчанию (безопасен при отсутствии `.env`)
- Credentials в `alembic.ini` удалены (env.py переопределяет из `settings.DATABASE_URL`)
- Все секреты через переменные окружения

---

## Frontend архитектура

### Режим рендеринга

- **SSR** (`output: 'server'`) с `@astrojs/node` adapter (standalone)
- Все страницы рендерятся на сервере при каждом запросе
- Динамические роуты (`[slug].astro`) работают без `getStaticPaths()`
- Поиск и пагинация через `Astro.url.searchParams`

### Типизация

- `src/types/api.ts` — интерфейсы для всех API-ответов
- `src/lib/api.ts` — `fetchApi<T>(path)` — единый клиент с error handling
- `src/lib/tiptap.ts` — `renderTipTapContent(doc)` — JSON → HTML рендерер

### Стили

- **Tailwind CSS 3.4** + **@tailwindcss/typography** (`prose prose-invert`)
- **daisyUI** — только через Tailwind plugin (CDN убран)
- Кастомная тема `dark` с цветами проекта
- Утилиты: `.btn-gradient`, `.card-gradient`, `.hero-gradient`, `.text-gradient`

### Интеграции

- `@astrojs/sitemap` — автоматическая генерация sitemap
- `@astrojs/rss` — RSS лента (`/rss.xml`)

---

## Docker

### Production (`docker-compose.yml`)

| Сервис | Образ | Память | Порты |
|--------|-------|--------|-------|
| postgres | postgres:16-alpine | 200M | — |
| backend | python:3.12-slim | 300M | — |
| frontend | node:20-alpine (SSR) | 200M | — |
| nginx | nginx:alpine | 50M | 80, 443 |

**Общая сеть**: `ursoaia-network` (bridge)

### Development (`docker-compose.dev.yml`)

| Сервис | Особенности |
|--------|-------------|
| postgres | Порт `65432` (избежание конфликтов) |
| backend | Hot reload (`--reload`), mounted `./backend/app` |
| frontend | `Dockerfile.dev`, mounted `./frontend`, hot reload |

**Общая сеть**: `ursoaia-dev-network` (bridge) — все сервисы подключены

### Dockerfiles

**Backend** (`python:3.12-slim`):
```dockerfile
FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p /app/uploads
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Frontend Production** (multi-stage, Node SSR):
```dockerfile
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/package.json ./
ENV HOST=0.0.0.0
ENV PORT=4321
EXPOSE 4321
CMD ["node", "./dist/server/entry.mjs"]
```

**Frontend Dev**:
```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 4321
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
```

---

## Nginx конфигурация

```
/ → frontend:4321              # Astro SSR
/admin → backend:8000          # Admin Panel (Jinja2)
/api → backend:8000            # REST API
/api/admin/auth/login           # Rate limit: 5r/m
/uploads → /var/www/uploads     # Static files (images only)
/health → backend:8000          # Health check
```

---

## Цветовая схема

| Переменная | Цвет | Использование |
|------------|------|---------------|
| `primary-dark` | `#2b2d42` | Фон, base-100 |
| `primary-light` | `#8d99ae` | Вторичный текст |
| `accent` / `primary` | `#ef233c` | Акцент, ссылки, кнопки |
| `accent-secondary` / `secondary` | `#ff6b35` | Градиенты |
| `base-200` / `neutral` | `#1a1b2e` | Тёмный фон |
| `base-300` | `#16171f` | Самый тёмный фон |

---

## Локализация

- Язык интерфейса: **румынский** (`lang="ro"`)
- Форматирование дат: `ro-RO` (`toLocaleDateString`)
- UI тексты: Acasă, Articole, Categorii, Căutare, Tag-uri и т.д.
