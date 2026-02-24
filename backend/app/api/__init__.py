from fastapi import APIRouter
from app.api.public import articles, categories, tags, search
from app.api.admin import auth, articles as admin_articles, categories as admin_categories, tags as admin_tags, media

api_router = APIRouter()

# Public API
api_router.include_router(articles.router, prefix="/articles", tags=["public-articles"])
api_router.include_router(categories.router, prefix="/categories", tags=["public-categories"])
api_router.include_router(tags.router, prefix="/tags", tags=["public-tags"])
api_router.include_router(search.router, prefix="/search", tags=["search"])

# Admin API
api_router.include_router(auth.router, prefix="/admin/auth", tags=["admin-auth"])
api_router.include_router(admin_articles.router, prefix="/admin/articles", tags=["admin-articles"])
api_router.include_router(admin_categories.router, prefix="/admin/categories", tags=["admin-categories"])
api_router.include_router(admin_tags.router, prefix="/admin/tags", tags=["admin-tags"])
api_router.include_router(media.router, prefix="/admin/media", tags=["admin-media"])