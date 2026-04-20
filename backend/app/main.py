from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
import os
import bcrypt as _bcrypt

# passlib 1.7.4 compatibility shim for bcrypt >= 4.x
if not hasattr(_bcrypt, '__about__'):
    _bcrypt.__about__ = type('about', (), {'__version__': _bcrypt.__version__})()

from app.config import settings
from app.database import init_db
from app.api import api_router
from app.admin import admin_router
from app.models import User
from app.utils.security import hash_password
from app.utils.limiter import limiter
from sqlalchemy import select


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    
    # Create admin user if not exists
    from app.database import async_session_maker
    async with async_session_maker() as db:
        result = await db.execute(select(User).where(User.email == settings.ADMIN_EMAIL))
        if not result.scalar_one_or_none():
            admin = User(
                email=settings.ADMIN_EMAIL,
                password_hash=hash_password(settings.ADMIN_PASSWORD),
                is_admin=True,
                is_active=True
            )
            db.add(admin)
            await db.commit()
            print(f"Admin user created: {settings.ADMIN_EMAIL}")
    
    yield
    
    # Shutdown
    pass


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan
)

# Rate limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS
_origins = [settings.FRONTEND_URL]
if settings.DEBUG:
    _origins += ["http://localhost:4321", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

# Static files
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
os.makedirs("app/static", exist_ok=True)
app.mount("/uploads", StaticFiles(directory=settings.UPLOAD_DIR), name="uploads")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# API routes
app.include_router(api_router, prefix="/api")

# Admin panel routes
app.include_router(admin_router, prefix="/admin")


@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": settings.APP_VERSION}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=settings.DEBUG)