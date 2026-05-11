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

Tests for the qrcat high-level API.
"""

from __future__ import annotations

from qrcat import HalfBlockRenderer, Renderer, render_qr


class _MarkerRenderer(Renderer):
    """Renderer that records arguments and returns a sentinel."""

    def __init__(self, sentinel: str = "MARKER") -> None:
        self.sentinel = sentinel
        self.calls: list[tuple[int, int, int]] = []

    def render(self, bitmap, *, border=2):
        self.calls.append((len(bitmap), len(bitmap[0]), border))
        return self.sentinel


class TestRenderQr:
    def test_returns_non_empty_string(self):
        out = render_qr("hello world")
        assert isinstance(out, str)
        assert out.strip()

    def test_default_renderer_is_half_block(self):
        out = render_qr("hi")
        assert set(out) <= set(" ▀▄█\n")

    def test_custom_renderer_invoked(self):
        marker = _MarkerRenderer()
        out = render_qr("hi", renderer=marker, border=3)
        assert out == "MARKER"
        assert len(marker.calls) == 1
        rows, cols, border = marker.calls[0]
        assert rows > 0 and cols > 0
        assert border == 3

    def test_deterministic(self):
        a = render_qr("payload", error="M", border=2)
        b = render_qr("payload", error="M", border=2)
        assert a == b

    def test_error_level_changes_output(self):
        low = render_qr("payload", error="L")
        high = render_qr("payload", error="H")
        assert low != high

    def test_explicit_half_block_matches_default(self):
        a = render_qr("same input", renderer=HalfBlockRenderer())
        b = render_qr("same input")
        assert a == b
