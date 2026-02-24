from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models import Tag
from app.schemas.tag import TagResponse
from typing import List

router = APIRouter()


@router.get("", response_model=List[TagResponse])
async def get_tags(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Tag).order_by(Tag.name)
    )
    tags = result.scalars().all()
    return [TagResponse.model_validate(t) for t in tags]