"""MkDocs hook: lazy-load + WebP-wrap <img> tags in rendered pages.

Two transforms run in this order on every page's HTML:

1. Add ``loading="lazy" decoding="async"`` to <img> tags that don't already
   have a ``loading=`` attribute. Template-emitted images keep whatever the
   template set, so a card marked ``loading="eager"`` (e.g. the homepage LCP
   candidate) is preserved.

2. Wrap any <img> whose src ends in jpg/jpeg/png with a <picture> element so
   browsers prefer the same-named .webp sibling. The .webp files are produced
   by ``build_images()`` (see src/ursoaia_edu_online/__init__.py) before
   MkDocs runs, so the sibling always exists at request time.
"""

from __future__ import annotations

import re

# Match <img ...> that does NOT already have a loading= attribute.
_LAZY_RE = re.compile(
    r"<img(?![^>]*\bloading=)([^>]*)>",
    flags=re.IGNORECASE | re.DOTALL,
)

# Match <img ... src="X.{jpg,jpeg,png}" ...> not already inside a <picture>.
# Negative lookbehind for `<picture>...<source...>` is regex-impractical, so
# we instead skip when the tag carries a marker we add (data-no-webp).
_RASTER_IMG_RE = re.compile(
    r'<img(?![^>]*\bdata-no-webp\b)([^>]*?)\bsrc="([^"]+\.(?:jpe?g|png))"([^>]*)>',
    flags=re.IGNORECASE | re.DOTALL,
)


def _add_lazy(match: re.Match[str]) -> str:
    return f'<img loading="lazy" decoding="async"{match.group(1)}>'


def _wrap_picture(match: re.Match[str]) -> str:
    pre, src, post = match.group(1), match.group(2), match.group(3)
    webp_src = re.sub(r"\.(?:jpe?g|png)$", ".webp", src, flags=re.IGNORECASE)
    img_tag = f'<img{pre}src="{src}"{post}>'
    return f'<picture><source srcset="{webp_src}" type="image/webp">{img_tag}</picture>'


def on_post_page(output: str, **kwargs) -> str:
    output = _LAZY_RE.sub(_add_lazy, output)
    output = _RASTER_IMG_RE.sub(_wrap_picture, output)
    return output
