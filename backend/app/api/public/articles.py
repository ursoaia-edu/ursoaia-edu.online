from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from typing import Optional
from app.database import get_db
from app.models import Article, Category, Tag
from app.schemas.article import ArticleResponse, ArticleListResponse, ArticlePreview

router = APIRouter()


@router.get("", response_model=ArticleListResponse)
async def get_articles(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100),
    category: Optional[str] = None,
    tag: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Article).options(
        selectinload(Article.categories),
        selectinload(Article.tags)
    ).where(Article.is_published == True)
    
    if category:
        query = query.join(Article.categories).where(Category.slug == category)
    
    if tag:
        query = query.join(Article.tags).where(Tag.slug == tag)
    
    # Count total
    count_query = select(func.count()).select_from(query.subquery())
    total = await db.scalar(count_query)
    
    # Paginate
    offset = (page - 1) * per_page
    query = query.order_by(Article.published_at.desc()).offset(offset).limit(per_page)
    
    result = await db.execute(query)
    articles = result.scalars().all()
    
    return ArticleListResponse(
        items=[ArticlePreview.model_validate(a) for a in articles],
        total=total or 0,
        page=page,
        per_page=per_page,
        pages=(total + per_page - 1) // per_page if total else 0
    )


@router.get("/{slug}", response_model=ArticleResponse)
async def get_article(slug: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Article)
        .options(selectinload(Article.categories), selectinload(Article.tags))
        .where(Article.slug == slug, Article.is_published == True)
    )
    article = result.scalar_one_or_none()
    
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    
    # Increment views
    article.views_count += 1
    await db.commit()
    
    result = await db.execute(
        select(Article)
        .options(selectinload(Article.categories), selectinload(Article.tags))
        .where(Article.id == article.id)
    )
    article = result.scalar_one()
    
    return ArticleResponse.model_validate(article)