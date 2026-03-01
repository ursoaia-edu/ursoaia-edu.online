from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Query, Request
from fastapi.responses import Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models import Media, User
from app.schemas.media import MediaResponse
from app.api.admin.auth import get_current_user
from app.config import settings
from typing import List
import aiofiles
import os
import uuid
from datetime import datetime
from PIL import Image
import io

router = APIRouter()


def generate_filename(original_filename: str) -> str:
    ext = original_filename.rsplit('.', 1)[-1].lower()
    if ext not in settings.ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="File type not allowed")
    
    return f"{datetime.now().strftime('%Y%m%d')}_{uuid.uuid4().hex[:8]}.{ext}"


async def process_image(file_content: bytes, filename: str) -> tuple[bytes, int, int]:
    try:
        img = Image.open(io.BytesIO(file_content))
        width, height = img.size
        
        # Resize if too large
        max_dimension = 1920
        if max(width, height) > max_dimension:
            if width > height:
                new_width = max_dimension
                new_height = int(height * max_dimension / width)
            else:
                new_height = max_dimension
                new_width = int(width * max_dimension / height)
            
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            width, height = new_width, new_height
        
        # Convert to RGB if necessary
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        
        output = io.BytesIO()
        img.save(output, format='JPEG', quality=85, optimize=True)
        return output.getvalue(), width, height
    
    except Exception:
        return file_content, 0, 0


@router.post("", response_model=MediaResponse)
async def upload_media(
    file: UploadFile = File(...),
    alt_text: str = Query(None),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    if file.size > settings.MAX_UPLOAD_SIZE:
        raise HTTPException(status_code=400, detail="File too large")
    
    filename = generate_filename(file.filename)
    file_content = await file.read()
    
    # Process image
    processed_content, width, height = await process_image(file_content, filename)
    
    # Save file
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    filepath = os.path.join(settings.UPLOAD_DIR, filename)
    
    async with aiofiles.open(filepath, 'wb') as f:
        await f.write(processed_content)
    
    # Create media record
    media = Media(
        filename=filename,
        original_filename=file.filename,
        url=f"/uploads/{filename}",
        mime_type=file.content_type or "image/jpeg",
        size=len(processed_content),
        width=width,
        height=height,
        alt_text=alt_text
    )
    
    db.add(media)
    await db.commit()
    await db.refresh(media)
    
    return MediaResponse.model_validate(media)


@router.get("", response_model=List[MediaResponse])
async def list_media(
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    offset = (page - 1) * per_page
    result = await db.execute(
        select(Media).order_by(Media.uploaded_at.desc()).offset(offset).limit(per_page)
    )
    media = result.scalars().all()
    return [MediaResponse.model_validate(m) for m in media]


@router.delete("/{media_id}")
async def delete_media(
    media_id: int,
    request: Request,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    result = await db.execute(select(Media).where(Media.id == media_id))
    media = result.scalar_one_or_none()
    
    if not media:
        raise HTTPException(status_code=404, detail="Media not found")
    
    # Delete file
    filepath = os.path.join(settings.UPLOAD_DIR, media.filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    
    await db.delete(media)
    await db.commit()
    
    if request.headers.get("HX-Request"):
        return Response(status_code=200)
    return {"message": "Media deleted successfully"}