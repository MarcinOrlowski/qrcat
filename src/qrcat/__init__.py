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

from .api import render_qr
from .renderers import HalfBlockRenderer, Renderer

__version__ = "1.0.1"
__author__ = "Marcin Orlowski"
__url__ = "https://github.com/MarcinOrlowski/qrcat"
__all__ = [
    "render_qr",
    "Renderer",
    "HalfBlockRenderer",
    "__version__",
    "__author__",
    "__url__",
]
