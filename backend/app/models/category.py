from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING
from app.database import Base

if TYPE_CHECKING:
    from app.models.article import Article


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    slug: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    color: Mapped[str] = mapped_column(String(7), default="#3B82F6")  # Hex color

    articles: Mapped[List["Article"]] = relationship(
        secondary="article_categories",
        back_populates="categories"
    )

    def __repr__(self) -> str:
        return f"<Category(id={self.id}, name={self.name})>"