from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING
from app.database import Base

if TYPE_CHECKING:
    from app.models.article import Article


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    articles: Mapped[List["Article"]] = relationship(back_populates="author", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email={self.email})>"