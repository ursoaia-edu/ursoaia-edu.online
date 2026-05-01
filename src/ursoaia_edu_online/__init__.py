"""Console-script wrappers so `uv run serve` / `uv run build` invoke mkdocs.

`build_css` compiles Tailwind via the standalone CLI. `serve` and `build` run it
first so the bundled stylesheet at ``custom_theme/assets/tailwind.css`` is always
fresh before MkDocs copies it into the site.
"""
from __future__ import annotations

import os
import platform
import stat
import subprocess
import sys
import urllib.request
from pathlib import Path

from mkdocs.__main__ import cli

TAILWIND_VERSION = "v3.4.17"
PROJECT_ROOT = Path(__file__).resolve().parents[2]
TAILWIND_DIR = PROJECT_ROOT / "tailwind"
TAILWIND_BIN = TAILWIND_DIR / "bin" / "tailwindcss"
TAILWIND_CONFIG = TAILWIND_DIR / "tailwind.config.js"
TAILWIND_INPUT = TAILWIND_DIR / "input.css"
TAILWIND_OUTPUT = PROJECT_ROOT / "custom_theme" / "assets" / "tailwind.css"


def _tailwind_asset() -> str:
    machine = platform.machine().lower()
    system = platform.system().lower()
    if system == "linux":
        return "tailwindcss-linux-x64" if machine in {"x86_64", "amd64"} else "tailwindcss-linux-arm64"
    if system == "darwin":
        return "tailwindcss-macos-arm64" if machine in {"arm64", "aarch64"} else "tailwindcss-macos-x64"
    if system == "windows":
        return "tailwindcss-windows-x64.exe"
    raise RuntimeError(f"Unsupported platform: {system}/{machine}")


def _ensure_binary() -> Path:
    if TAILWIND_BIN.exists():
        return TAILWIND_BIN
    TAILWIND_BIN.parent.mkdir(parents=True, exist_ok=True)
    asset = _tailwind_asset()
    url = f"https://github.com/tailwindlabs/tailwindcss/releases/download/{TAILWIND_VERSION}/{asset}"
    print(f"Downloading Tailwind CLI {TAILWIND_VERSION} ({asset})...", file=sys.stderr)
    urllib.request.urlretrieve(url, TAILWIND_BIN)  # noqa: S310 — pinned vendor URL
    TAILWIND_BIN.chmod(TAILWIND_BIN.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    return TAILWIND_BIN


def build_css() -> None:
    binary = _ensure_binary()
    cmd = [
        str(binary),
        "-c", str(TAILWIND_CONFIG),
        "-i", str(TAILWIND_INPUT),
        "-o", str(TAILWIND_OUTPUT),
        "--minify",
    ]
    if "--watch" in sys.argv[1:]:
        cmd.append("--watch")
    TAILWIND_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(cmd, cwd=PROJECT_ROOT, check=True)


def serve() -> None:
    if os.environ.get("URSOAIA_SKIP_CSS") != "1":
        build_css()
    cli.main(args=["serve", *sys.argv[1:]], prog_name="uv run serve", standalone_mode=True)


def build() -> None:
    if os.environ.get("URSOAIA_SKIP_CSS") != "1":
        build_css()
    cli.main(args=["build", *sys.argv[1:]], prog_name="uv run build", standalone_mode=True)
