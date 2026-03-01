from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models import Category, User
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse
from app.api.admin.auth import get_current_user
from app.utils.slug import generate_unique_slug
from typing import List

router = APIRouter()


@router.get("", response_model=List[CategoryResponse])
async def list_categories(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    result = await db.execute(select(Category).order_by(Category.name))
    categories = result.scalars().all()
    return [CategoryResponse.model_validate(c) for c in categories]


@router.post("", response_model=CategoryResponse)
async def create_category(
    category_data: CategoryCreate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    # Check if name exists
    result = await db.execute(
        select(Category).where(Category.name == category_data.name)
    )
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Category with this name already exists")
    
    # Generate slug
    result = await db.execute(select(Category.slug))
    existing_slugs = set(row[0] for row in result.fetchall())
    slug = generate_unique_slug(category_data.name, existing_slugs)
    
    category = Category(
        name=category_data.name,
        slug=slug,
        description=category_data.description,
        color=category_data.color
    )
    
    db.add(category)
    await db.commit()
    await db.refresh(category)
    
    return CategoryResponse.model_validate(category)


@router.put("/{category_id}", response_model=CategoryResponse)
async def update_category(
    category_id: int,
    category_data: CategoryUpdate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Category).where(Category.id == category_id)
    )
    category = result.scalar_one_or_none()
    
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    update_data = category_data.model_dump(exclude_unset=True)
    
    # Check for name conflicts
    if 'name' in update_data and update_data['name'] != category.name:
        result = await db.execute(
            select(Category).where(Category.name == update_data['name'])
        )
        if result.scalar_one_or_none():
            raise HTTPException(status_code=400, detail="Category with this name already exists")
        
        # Update slug
        result = await db.execute(select(Category.slug))
        existing_slugs = set(row[0] for row in result.fetchall())
        existing_slugs.discard(category.slug)
        update_data['slug'] = generate_unique_slug(update_data['name'], existing_slugs)
    
    for field, value in update_data.items():
        setattr(category, field, value)
    
    await db.commit()
    await db.refresh(category)
    
    return CategoryResponse.model_validate(category)


@router.delete("/{category_id}")
async def delete_category(
    category_id: int,
    request: Request,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Category).where(Category.id == category_id)
    )
    category = result.scalar_one_or_none()
    
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    await db.delete(category)
    await db.commit()
    
    if request.headers.get("HX-Request"):
        return Response(status_code=200)
    return {"message": "Category deleted successfully"}