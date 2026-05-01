"""MkDocs hook: add `loading="lazy" decoding="async"` to <img> tags in rendered pages.

Markdown-authored images don't carry these attributes by default, but they're
all below the fold (deep inside long-form articles) so lazy is always safe for
them. Template-emitted images keep whatever the template set, so a card marked
`loading="eager"` (e.g. the homepage LCP candidate) is preserved.
"""

from __future__ import annotations

import re

# Match <img ...> that does NOT already have a loading= attribute.
# Negative lookahead is sufficient — we only run on rendered HTML, not on
# arbitrary input that might contain `<img>` inside script/style.
_IMG_RE = re.compile(
    r"<img(?![^>]*\bloading=)([^>]*)>",
    flags=re.IGNORECASE,
)


def _inject(match: re.Match[str]) -> str:
    attrs = match.group(1)
    return f'<img loading="lazy" decoding="async"{attrs}>'


def on_post_page(output: str, **kwargs) -> str:
    return _IMG_RE.sub(_inject, output)
