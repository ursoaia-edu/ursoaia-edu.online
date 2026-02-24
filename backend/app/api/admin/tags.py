from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models import Tag, User
from app.schemas.tag import TagCreate, TagUpdate, TagResponse
from app.api.admin.auth import get_current_user
from app.utils.slug import generate_unique_slug
from typing import List

router = APIRouter()


@router.get("", response_model=List[TagResponse])
async def list_tags(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    result = await db.execute(select(Tag).order_by(Tag.name))
    tags = result.scalars().all()
    return [TagResponse.model_validate(t) for t in tags]


@router.post("", response_model=TagResponse)
async def create_tag(
    tag_data: TagCreate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    result = await db.execute(select(Tag).where(Tag.name == tag_data.name))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Tag with this name already exists")
    
    result = await db.execute(select(Tag.slug))
    existing_slugs = set(row[0] for row in result.fetchall())
    slug = generate_unique_slug(tag_data.name, existing_slugs)
    
    tag = Tag(name=tag_data.name, slug=slug, color=tag_data.color)
    
    db.add(tag)
    await db.commit()
    await db.refresh(tag)
    
    return TagResponse.model_validate(tag)


@router.put("/{tag_id}", response_model=TagResponse)
async def update_tag(
    tag_id: int,
    tag_data: TagUpdate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    result = await db.execute(select(Tag).where(Tag.id == tag_id))
    tag = result.scalar_one_or_none()
    
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    
    update_data = tag_data.model_dump(exclude_unset=True)
    
    if 'name' in update_data and update_data['name'] != tag.name:
        result = await db.execute(select(Tag).where(Tag.name == update_data['name']))
        if result.scalar_one_or_none():
            raise HTTPException(status_code=400, detail="Tag with this name already exists")
        
        result = await db.execute(select(Tag.slug))
        existing_slugs = set(row[0] for row in result.fetchall())
        existing_slugs.discard(tag.slug)
        update_data['slug'] = generate_unique_slug(update_data['name'], existing_slugs)
    
    for field, value in update_data.items():
        setattr(tag, field, value)
    
    await db.commit()
    await db.refresh(tag)
    
    return TagResponse.model_validate(tag)


@router.delete("/{tag_id}")
async def delete_tag(
    tag_id: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    result = await db.execute(select(Tag).where(Tag.id == tag_id))
    tag = result.scalar_one_or_none()
    
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    
    await db.delete(tag)
    await db.commit()
    
    return {"message": "Tag deleted successfully"}