"""Console-script wrappers so `uv run serve` / `uv run build` invoke mkdocs."""
from __future__ import annotations

import sys

from mkdocs.__main__ import cli


def serve() -> None:
    cli.main(args=["serve", *sys.argv[1:]], prog_name="uv run serve", standalone_mode=True)


def build() -> None:
    cli.main(args=["build", *sys.argv[1:]], prog_name="uv run build", standalone_mode=True)
