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

from typing import Literal

ErrorLevel = Literal["L", "M", "Q", "H"]


def make_matrix(data: str, *, error: ErrorLevel = "M") -> list[list[int]]:
    """Encode `data` and return a 2D matrix of ints (1 = dark, 0 = light)."""
    import segno  # lazy: only loaded when a QR is actually generated

    qr = segno.make(data, error=error)
    return [[1 if cell else 0 for cell in row] for row in qr.matrix]
