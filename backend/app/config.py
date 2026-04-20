from pydantic_settings import BaseSettings
from pydantic import model_validator
from functools import lru_cache

_INSECURE_SECRET = "your-secret-key-change-in-production"
_INSECURE_PASSWORD = "admin123"


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/ursoaia"

    # Security
    SECRET_KEY: str = _INSECURE_SECRET
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    # Admin
    ADMIN_EMAIL: str = "admin@ursoaia-edu.online"
    ADMIN_PASSWORD: str = _INSECURE_PASSWORD

    # App
    APP_NAME: str = "Ursoaia Edu"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # Uploads
    UPLOAD_DIR: str = "/app/uploads"
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS: set = {"jpg", "jpeg", "png", "gif", "webp", "svg"}

    # Frontend URL for CORS
    FRONTEND_URL: str = "http://localhost:4321"

    @model_validator(mode="after")
    def validate_security(self) -> "Settings":
        errors = []
        if self.SECRET_KEY == _INSECURE_SECRET:
            errors.append("SECRET_KEY is set to the insecure default — generate a random value (e.g. openssl rand -hex 32)")
        if len(self.SECRET_KEY) < 32:
            errors.append("SECRET_KEY must be at least 32 characters")
        if self.ADMIN_PASSWORD == _INSECURE_PASSWORD:
            errors.append("ADMIN_PASSWORD is set to the insecure default 'admin123'")
        if errors:
            raise ValueError("Insecure configuration:\n" + "\n".join(f"  • {e}" for e in errors))
        return self

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()