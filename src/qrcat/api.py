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

from .qr import ErrorLevel, make_matrix
from .renderers import HalfBlockRenderer, Renderer


def render_qr(
    data: str,
    *,
    error: ErrorLevel = "M",
    border: int = 2,
    renderer: Renderer | None = None,
) -> str:
    """Encode `data` as a QR code and render it to a string."""
    matrix = make_matrix(data, error=error)
    return (renderer or HalfBlockRenderer()).render(matrix, border=border)
