"""
##################################################################################
#
# qrcat by Marcin Orlowski
# QR codes for cats who live in terminal.
#
# @author    Marcin Orlowski <mail@marcinOrlowski.com>
# Copyright  ©2026 Marcin Orlowski <MarcinOrlowski.com>
# @link      https://github.com/MarcinOrlowski/qrcat
#
##################################################################################
"""

from __future__ import annotations

import argparse
import sys
from typing import Sequence


class _QrcatParser(argparse.ArgumentParser):
    """ArgumentParser that appends project info + QR to --help output.

    The QR (and thus segno) is rendered lazily, so it only loads when
    help is actually requested — not on every CLI invocation.
    """

    def format_help(self) -> str:
        return _about_text() + "\n" + super().format_help() + "\n"


def _about_text() -> str:
    """Return project info plus a QR code pointing to the project URL."""
    from . import __author__, __url__, __version__
    from .api import render_qr

    return "\n".join(
        [
            f"qrcat v{__version__}",
            f"Author:  {__author__}",
            render_qr(__url__),
            f" {__url__}",
            "",
        ]
    )


def _build_parser() -> argparse.ArgumentParser:
    p = _QrcatParser(
        prog="qrcat",
        description="Render a QR code to the terminal using unicode blocks.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "data",
        nargs="?",
        default=None,
        help="String to encode as QR code. Omit (or use '-') to read from stdin.",
    )
    p.add_argument(
        "-b",
        "--border",
        type=int,
        default=2,
        help="Width of the margin around the QR code, in QR cells (default: 2).",
    )
    p.add_argument(
        "--version",
        action="store_true",
        help="Print version and exit.",
    )
    return p


def main(argv: Sequence[str] | None = None) -> int:
    """qrcat CLI entry point."""
    parser = _build_parser()

    if argv is None:
        argv = sys.argv[1:]

    if argv and argv[0] == "--version":
        from . import __version__

        print(__version__)
        return 0

    args = parser.parse_args(argv)

    if args.data is None or args.data == "-":
        if sys.stdin.isatty():
            parser.error("no data given and stdin is a terminal")
        data = sys.stdin.read().rstrip("\n")
    else:
        data = args.data

    if not data:
        parser.error("data is empty")

    # Lazy import: segno + renderer only loaded when actually rendering.
    from .api import render_qr

    print(render_qr(data, border=args.border))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
