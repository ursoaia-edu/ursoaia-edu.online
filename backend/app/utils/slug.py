import re
from unicodedata import normalize
from slugify import slugify


def generate_unique_slug(title: str, existing_slugs: set = None) -> str:
    base_slug = slugify(title)
    if not base_slug:
        base_slug = "untitled"
    
    if existing_slugs is None:
        return base_slug
    
    slug = base_slug
    counter = 1
    while slug in existing_slugs:
        slug = f"{base_slug}-{counter}"
        counter += 1
    
    return slug