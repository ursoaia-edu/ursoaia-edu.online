from sqlalchemy import String, Text, Boolean, Integer, DateTime, ForeignKey, JSON, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Table, Column
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime
from app.database import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.category import Category
    from app.models.tag import Tag


article_categories = Table(
    "article_categories",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("articles.id", ondelete="CASCADE"), primary_key=True),
    Column("category_id", Integer, ForeignKey("categories.id", ondelete="CASCADE"), primary_key=True)
)


class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    slug: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    content: Mapped[dict] = mapped_column(JSON, default=dict)  # TipTap JSON
    excerpt: Mapped[str] = mapped_column(Text, default="")
    cover_image: Mapped[str] = mapped_column(String(500), nullable=True)
    is_published: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    is_featured: Mapped[bool] = mapped_column(Boolean, default=False)
    views_count: Mapped[int] = mapped_column(Integer, default=0)
    reading_time: Mapped[int] = mapped_column(Integer, default=0)  # in minutes
    
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    published_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    author: Mapped["User"] = relationship(back_populates="articles")
    categories: Mapped[List["Category"]] = relationship(
        secondary=article_categories,
        back_populates="articles"
    )
    tags: Mapped[List["Tag"]] = relationship(
        secondary="article_tags",
        back_populates="articles"
    )

    def __repr__(self) -> str:
        return f"<Article(id={self.id}, title={self.title})>"