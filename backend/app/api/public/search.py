from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from app.database import get_db
from app.models import Article
from app.schemas.article import ArticlePreview, ArticleListResponse
from typing import List

router = APIRouter()


@router.get("", response_model=ArticleListResponse)
async def search_articles(
    q: str = Query(..., min_length=1),
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    search_term = f"%{q}%"
    
    query = select(Article).where(
        Article.is_published == True,
        or_(
            Article.title.ilike(search_term),
            Article.excerpt.ilike(search_term)
        )
    ).order_by(Article.published_at.desc())
    
    # Count
    from sqlalchemy import func
    count_query = select(func.count()).select_from(query.subquery())
    total = await db.scalar(count_query)
    
    # Paginate
    offset = (page - 1) * per_page
    query = query.offset(offset).limit(per_page)
    
    result = await db.execute(query)
    articles = result.scalars().all()
    
    return ArticleListResponse(
        items=[ArticlePreview.model_validate(a) for a in articles],
        total=total or 0,
        page=page,
        per_page=per_page,
        pages=(total + per_page - 1) // per_page if total else 0
    )