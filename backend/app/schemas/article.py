from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from app.schemas.category import CategoryResponse
from app.schemas.tag import TagResponse


class ArticleBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    excerpt: str = Field(default="", max_length=500)
    content: dict = Field(default_factory=dict)
    cover_image: Optional[str] = None
    is_featured: bool = False


class ArticleCreate(ArticleBase):
    category_ids: List[int] = Field(default_factory=list)
    tag_ids: List[int] = Field(default_factory=list)
    is_published: bool = False


class ArticleUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    excerpt: Optional[str] = Field(None, max_length=500)
    content: Optional[dict] = None
    cover_image: Optional[str] = None
    is_published: Optional[bool] = None
    is_featured: Optional[bool] = None
    category_ids: Optional[List[int]] = None
    tag_ids: Optional[List[int]] = None


class ArticlePreview(BaseModel):
    id: int
    title: str
    slug: str
    excerpt: str
    cover_image: Optional[str]
    is_featured: bool
    is_published: bool
    views_count: int
    reading_time: int
    published_at: Optional[datetime]
    categories: List[CategoryResponse] = []
    tags: List[TagResponse] = []

    class Config:
        from_attributes = True


class ArticleResponse(ArticlePreview):
    content: dict
    author_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ArticleListResponse(BaseModel):
    items: List[ArticlePreview]
    total: int
    page: int
    per_page: int
    pages: int


class ArticleSearchParams(BaseModel):
    q: Optional[str] = None
    category: Optional[str] = None
    tag: Optional[str] = None
    is_published: Optional[bool] = True
    page: int = 1
    per_page: int = 10