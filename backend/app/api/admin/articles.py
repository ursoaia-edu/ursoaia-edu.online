from fastapi import APIRouter, Depends, HTTPException, Query, Request
from fastapi.responses import Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from typing import Optional
from datetime import datetime, timezone
from app.database import get_db
from app.models import Article, Category, Tag, User
from app.schemas.article import (
    ArticleCreate, ArticleUpdate, ArticleResponse, ArticleListResponse, ArticlePreview
)
from app.api.admin.auth import get_current_user
from app.utils.slug import generate_unique_slug

router = APIRouter()


@router.get("", response_model=ArticleListResponse)
async def list_articles(
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100),
    is_published: Optional[bool] = None,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    query = select(Article).options(
        selectinload(Article.categories),
        selectinload(Article.tags)
    )
    
    if is_published is not None:
        query = query.where(Article.is_published == is_published)
    
    # Count
    count_query = select(func.count()).select_from(query.subquery())
    total = await db.scalar(count_query)
    
    # Paginate
    offset = (page - 1) * per_page
    query = query.order_by(Article.updated_at.desc()).offset(offset).limit(per_page)
    
    result = await db.execute(query)
    articles = result.scalars().all()
    
    return ArticleListResponse(
        items=[ArticlePreview.model_validate(a) for a in articles],
        total=total or 0,
        page=page,
        per_page=per_page,
        pages=(total + per_page - 1) // per_page if total else 0
    )


@router.post("", response_model=ArticleResponse)
async def create_article(
    article_data: ArticleCreate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    # Generate slug
    result = await db.execute(select(Article.slug))
    existing_slugs = set(row[0] for row in result.fetchall())
    slug = generate_unique_slug(article_data.title, existing_slugs)
    
    article = Article(
        title=article_data.title,
        slug=slug,
        excerpt=article_data.excerpt,
        content=article_data.content,
        cover_image=article_data.cover_image,
        is_featured=article_data.is_featured,
        author_id=user.id
    )
    
    # Add categories
    if article_data.category_ids:
        result = await db.execute(
            select(Category).where(Category.id.in_(article_data.category_ids))
        )
        article.categories = list(result.scalars().all())
    
    # Add tags
    if article_data.tag_ids:
        result = await db.execute(
            select(Tag).where(Tag.id.in_(article_data.tag_ids))
        )
        article.tags = list(result.scalars().all())
    
    if article_data.is_published:
        article.is_published = True
        article.published_at = datetime.now(timezone.utc)
    
    db.add(article)
    await db.commit()
    
    result = await db.execute(
        select(Article)
        .options(selectinload(Article.categories), selectinload(Article.tags))
        .where(Article.id == article.id)
    )
    article = result.scalar_one()
    
    return ArticleResponse.model_validate(article)


@router.get("/{article_id}", response_model=ArticleResponse)
async def get_article(
    article_id: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Article)
        .options(selectinload(Article.categories), selectinload(Article.tags))
        .where(Article.id == article_id)
    )
    article = result.scalar_one_or_none()
    
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    
    return ArticleResponse.model_validate(article)


@router.put("/{article_id}", response_model=ArticleResponse)
async def update_article(
    article_id: int,
    article_data: ArticleUpdate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Article)
        .options(selectinload(Article.categories), selectinload(Article.tags))
        .where(Article.id == article_id)
    )
    article = result.scalar_one_or_none()
    
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    
    # Update fields
    update_data = article_data.model_dump(exclude_unset=True)
    
    # Handle category/tag updates separately
    if 'category_ids' in update_data:
        category_ids = update_data.pop('category_ids')
        if category_ids is not None:
            result = await db.execute(
                select(Category).where(Category.id.in_(category_ids))
            )
            article.categories = list(result.scalars().all())
    
    if 'tag_ids' in update_data:
        tag_ids = update_data.pop('tag_ids')
        if tag_ids is not None:
            result = await db.execute(
                select(Tag).where(Tag.id.in_(tag_ids))
            )
            article.tags = list(result.scalars().all())
    
    # Update other fields
    was_published = article.is_published
    for field, value in update_data.items():
        setattr(article, field, value)
    
    # Handle publishing
    if article_data.is_published and not was_published:
        article.is_published = True
        article.published_at = datetime.now(timezone.utc)
    
    await db.commit()
    
    result = await db.execute(
        select(Article)
        .options(selectinload(Article.categories), selectinload(Article.tags))
        .where(Article.id == article.id)
    )
    article = result.scalar_one()
    
    return ArticleResponse.model_validate(article)


@router.delete("/{article_id}")
async def delete_article(
    article_id: int,
    request: Request,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Article).where(Article.id == article_id)
    )
    article = result.scalar_one_or_none()
    
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    
    await db.delete(article)
    await db.commit()
    
    if request.headers.get("HX-Request"):
        return Response(status_code=200)
    return {"message": "Article deleted successfully"}