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

Renderer protocol and shared types.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Sequence

Bitmap = Sequence[Sequence[int]]


class Renderer(ABC):
    """Render a 2D bitmap (1 = dark module, 0 = light) to a string.

    Subclasses pick a glyph strategy (half-blocks, quadrants, ascii, ...).
    """

    @abstractmethod
    def render(self, bitmap: Bitmap, *, border: int = 2) -> str:
        """Return the rendered QR as a multi-line string."""
        raise NotImplementedError
