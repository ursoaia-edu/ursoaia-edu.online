from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class MediaBase(BaseModel):
    alt_text: Optional[str] = None


class MediaUpload(MediaBase):
    pass


class MediaResponse(MediaBase):
    id: int
    filename: str
    original_filename: str
    url: str
    mime_type: str
    size: int
    width: Optional[int]
    height: Optional[int]
    uploaded_at: datetime

    class Config:
        from_attributes = True