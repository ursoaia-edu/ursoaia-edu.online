"""MkDocs hook: copy `docs/.well-known/` into the build output.

MkDocs skips dotfile directories by default, so static files placed under
`docs/.well-known/` (e.g. `security.txt` per RFC 9116) never reach the build.
This hook copies that directory verbatim after the build completes.
"""

from __future__ import annotations

import shutil
from pathlib import Path


def on_post_build(config) -> None:
    docs_dir = Path(config["docs_dir"])
    site_dir = Path(config["site_dir"])
    src = docs_dir / ".well-known"
    if not src.is_dir():
        return
    dest = site_dir / ".well-known"
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)
