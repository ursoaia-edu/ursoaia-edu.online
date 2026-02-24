# Ursoaia Edu - Educational Portal

A modern blog/news website with admin panel built on Python (FastAPI) + PostgreSQL + Docker.

## Features

- 🚀 **FastAPI Backend** - High-performance async Python web framework
- 🎨 **daisyUI + Tailwind CSS** - Beautiful dark theme with Chain App Dev style
- ✍️ **TipTap Editor** - Rich text editor with custom blocks
- 🌐 **Astro Frontend** - Static site generation for public blog
- 🐘 **PostgreSQL** - Robust relational database
- 🐳 **Docker** - Containerized deployment
- 🔐 **JWT Authentication** - Secure admin access
- 📁 **Media Management** - Image upload and optimization

## Tech Stack

### Backend
- Python 3.12
- FastAPI 0.109
- SQLAlchemy 2.0 (async)
- PostgreSQL 16
- Alembic (migrations)
- Pydantic 2.5

### Frontend
- Astro 4.4
- Tailwind CSS 3.4
- daisyUI 4.7

### Admin Panel
- Jinja2 templates
- HTMX 1.9
- TipTap editor

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Node.js 20+ (for local development)
- Python 3.12+ (for local development)

### Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ursoaia-edu.online.git
cd ursoaia-edu.online
```

2. Create environment file:
```bash
cp .env.example .env
# Edit .env with your settings
```

3. Start development servers:
```bash
docker-compose -f docker-compose.dev.yml up -d
```

4. Access the application:
- Frontend: http://localhost:4321
- Admin Panel: http://localhost:8000/admin
- API: http://localhost:8000/api

### Production

1. Configure environment variables in `.env`
2. Run database migrations:
```bash
docker-compose run backend alembic upgrade head
```

3. Start services:
```bash
docker-compose up -d
```

## Project Structure

```
ursoaia-edu.online/
├── backend/                    # FastAPI application
│   ├── app/
│   │   ├── api/               # API routes (public & admin)
│   │   ├── admin/             # Admin panel templates
│   │   ├── models/            # SQLAlchemy models
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── services/          # Business logic
│   │   └── utils/             # Utilities
│   ├── alembic/               # Database migrations
│   └── requirements.txt
├── frontend/                   # Astro application
│   ├── src/
│   │   ├── pages/             # Astro pages
│   │   ├── components/        # UI components
│   │   └── layouts/           # Page layouts
│   └── package.json
├── nginx/                      # Nginx configuration
├── uploads/                    # Uploaded media files
├── docker-compose.yml          # Production Docker config
└── docker-compose.dev.yml      # Development Docker config
```

## API Endpoints

### Public API
- `GET /api/articles` - List published articles
- `GET /api/articles/{slug}` - Get article by slug
- `GET /api/categories` - List categories
- `GET /api/tags` - List tags
- `GET /api/search?q=query` - Search articles

### Admin API
- `POST /api/admin/auth/login` - Admin login
- `GET /api/admin/auth/me` - Current user
- `CRUD /api/admin/articles` - Article management
- `CRUD /api/admin/categories` - Category management
- `CRUD /api/admin/tags` - Tag management
- `POST /api/admin/media` - Upload media

## Default Admin Credentials

After first run, a default admin user is created:
- Email: `admin@ursoaia-edu.online`
- Password: `admin123`

**Important:** Change these credentials in production!

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | - |
| `SECRET_KEY` | JWT secret key | - |
| `ADMIN_EMAIL` | Admin user email | `admin@ursoaia-edu.online` |
| `ADMIN_PASSWORD` | Admin user password | `admin123` |
| `DEBUG` | Enable debug mode | `false` |
| `FRONTEND_URL` | Frontend URL for CORS | - |

## Database Migrations

Create a new migration:
```bash
alembic revision --autogenerate -m "Description"
```

Apply migrations:
```bash
alembic upgrade head
```

Rollback:
```bash
alembic downgrade -1
```

## License

MIT License - See LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request