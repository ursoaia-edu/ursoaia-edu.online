from fastapi import APIRouter, Request, Depends, HTTPException, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from app.database import get_db
from app.models import User, Article, Category, Tag, Media
from app.utils.security import verify_token
from app.config import settings
from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory="app/admin/templates")


def is_authenticated(request: Request) -> bool:
    token = request.cookies.get("access_token")
    if not token:
        return False
    return verify_token(token) is not None


async def require_admin(request: Request, db: AsyncSession = Depends(get_db)) -> User:
    from app.api.admin.auth import get_current_user
    try:
        return await get_current_user(request, db)
    except HTTPException:
        raise HTTPException(status_code=302, headers={"Location": "/admin/login"})


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    if is_authenticated(request):
        return RedirectResponse(url="/admin", status_code=302)
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/", response_class=HTMLResponse)
async def dashboard(
    request: Request,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_admin)
):
    # Get stats
    articles_count = await db.scalar(
        select(func.count()).select_from(Article)
    )
    published_count = await db.scalar(
        select(func.count()).select_from(Article).where(Article.is_published == True)
    )
    categories_count = await db.scalar(
        select(func.count()).select_from(Category)
    )
    tags_count = await db.scalar(
        select(func.count()).select_from(Tag)
    )
    
    # Recent articles
    result = await db.execute(
        select(Article)
        .options(selectinload(Article.categories))
        .order_by(Article.updated_at.desc())
        .limit(5)
    )
    recent_articles = result.scalars().all()
    
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "user": user,
        "stats": {
            "articles": articles_count or 0,
            "published": published_count or 0,
            "categories": categories_count or 0,
            "tags": tags_count or 0
        },
        "recent_articles": recent_articles
    })


# Articles pages
@router.get("/articles", response_class=HTMLResponse)
async def articles_list(
    request: Request,
    page: int = 1,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_admin)
):
    per_page = 20
    offset = (page - 1) * per_page
    
    result = await db.execute(
        select(Article)
        .options(selectinload(Article.categories), selectinload(Article.tags))
        .order_by(Article.updated_at.desc())
        .offset(offset)
        .limit(per_page)
    )
    articles = result.scalars().all()
    
    total = await db.scalar(select(func.count()).select_from(Article))
    pages = (total + per_page - 1) // per_page if total else 0
    
    return templates.TemplateResponse("articles/list.html", {
        "request": request,
        "user": user,
        "articles": articles,
        "page": page,
        "pages": pages
    })


@router.get("/articles/create", response_class=HTMLResponse)
async def create_article_page(
    request: Request,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_admin)
):
    categories = (await db.execute(select(Category))).scalars().all()
    tags = (await db.execute(select(Tag))).scalars().all()
    
    return templates.TemplateResponse("articles/create.html", {
        "request": request,
        "user": user,
        "categories": categories,
        "tags": tags
    })


@router.get("/articles/{article_id}/edit", response_class=HTMLResponse)
async def edit_article_page(
    request: Request,
    article_id: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_admin)
):
    result = await db.execute(
        select(Article)
        .options(selectinload(Article.categories), selectinload(Article.tags))
        .where(Article.id == article_id)
    )
    article = result.scalar_one_or_none()
    
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    
    categories = (await db.execute(select(Category))).scalars().all()
    tags = (await db.execute(select(Tag))).scalars().all()
    
    return templates.TemplateResponse("articles/edit.html", {
        "request": request,
        "user": user,
        "article": article,
        "categories": categories,
        "tags": tags,
        "selected_categories": [c.id for c in article.categories],
        "selected_tags": [t.id for t in article.tags]
    })


# Categories pages
@router.get("/categories", response_class=HTMLResponse)
async def categories_list(
    request: Request,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_admin)
):
    categories = (await db.execute(select(Category).order_by(Category.name))).scalars().all()
    return templates.TemplateResponse("categories/list.html", {
        "request": request,
        "user": user,
        "categories": categories
    })


# Tags pages
@router.get("/tags", response_class=HTMLResponse)
async def tags_list(
    request: Request,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_admin)
):
    tags = (await db.execute(select(Tag).order_by(Tag.name))).scalars().all()
    return templates.TemplateResponse("tags/list.html", {
        "request": request,
        "user": user,
        "tags": tags
    })


# Media page
@router.get("/media", response_class=HTMLResponse)
async def media_page(
    request: Request,
    page: int = 1,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_admin)
):
    per_page = 30
    offset = (page - 1) * per_page
    
    result = await db.execute(
        select(Media).order_by(Media.uploaded_at.desc()).offset(offset).limit(per_page)
    )
    media = result.scalars().all()
    
    return templates.TemplateResponse("media/list.html", {
        "request": request,
        "user": user,
        "media": media,
        "page": page
    })