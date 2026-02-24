from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/ursoaia"
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    
    # Admin
    ADMIN_EMAIL: str = "admin@ursoaia-edu.online"
    ADMIN_PASSWORD: str = "admin123"
    
    # App
    APP_NAME: str = "Ursoaia Edu"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # Uploads
    UPLOAD_DIR: str = "/app/uploads"
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS: set = {"jpg", "jpeg", "png", "gif", "webp", "svg"}
    
    # Frontend URL for CORS
    FRONTEND_URL: str = "http://localhost:4321"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()