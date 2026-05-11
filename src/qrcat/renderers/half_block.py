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

Half-block renderer: 2 vertical modules per character cell.
"""

from __future__ import annotations

from .base import Bitmap, Renderer

# (top, bottom) -> glyph
_GLYPHS = {
    (0, 0): " ",
    (1, 0): "▀",  # ▀
    (0, 1): "▄",  # ▄
    (1, 1): "█",  # █
}


class HalfBlockRenderer(Renderer):
    """Pack 2 vertical modules into one terminal cell via half-block glyphs.

    Width stays equal to the QR module count; height is halved.
    A quiet-zone border of `border` modules is added on all sides.
    """

    def __init__(self, *, dark: str = "", light: str = "") -> None:
        # Optional ANSI escape wrappers; empty by default for portability.
        self._dark = dark
        self._light = light

    def render(self, bitmap: Bitmap, *, border: int = 2) -> str:
        if border < 0:
            raise ValueError("border must be >= 0")

        padded = self._pad(bitmap, border)
        # Ensure even row count so pairing works without a special last row.
        if len(padded) % 2:
            padded.append([0] * len(padded[0]))

        lines = []
        for y in range(0, len(padded), 2):
            top_row = padded[y]
            bot_row = padded[y + 1]
            line = "".join(
                _GLYPHS[(top_row[x], bot_row[x])] for x in range(len(top_row))
            )
            lines.append(line)
        return "\n".join(lines)

    @staticmethod
    def _pad(bitmap: Bitmap, border: int) -> list[list[int]]:
        if not bitmap:
            return [[0] * (border * 2) for _ in range(border * 2)]

        width = len(bitmap[0])
        pad_row = [0] * (width + border * 2)
        out: list[list[int]] = [list(pad_row) for _ in range(border)]
        for row in bitmap:
            out.append([0] * border + list(row) + [0] * border)
        out.extend(list(pad_row) for _ in range(border))
        return out
