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

Tests for HalfBlockRenderer.
"""

from __future__ import annotations

import pytest

from qrcat.renderers import HalfBlockRenderer


class TestPad:
    def test_zero_border_unchanged_size(self):
        r = HalfBlockRenderer()
        padded = r._pad([[1, 0], [0, 1]], 0)
        assert padded == [[1, 0], [0, 1]]

    def test_border_adds_rings(self):
        r = HalfBlockRenderer()
        padded = r._pad([[1]], 1)
        assert padded == [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]

    def test_empty_bitmap(self):
        r = HalfBlockRenderer()
        padded = r._pad([], 2)
        assert len(padded) == 4
        assert all(row == [0, 0, 0, 0] for row in padded)


class TestRender:
    def test_negative_border_rejected(self):
        with pytest.raises(ValueError):
            HalfBlockRenderer().render([[1]], border=-1)

    def test_single_dark_module_no_border(self):
        # 1x1 dark module → padded to 1 row, made even → 2 rows → "▀".
        out = HalfBlockRenderer().render([[1]], border=0)
        assert out == "▀"

    def test_single_light_module_no_border(self):
        out = HalfBlockRenderer().render([[0]], border=0)
        assert out == " "

    def test_two_row_pair_glyphs(self):
        # Two rows of two modules: top=(1,0), bot=(0,1) → "▀▄".
        out = HalfBlockRenderer().render([[1, 0], [0, 1]], border=0)
        assert out == "▀▄"

    def test_full_block_pair(self):
        out = HalfBlockRenderer().render([[1], [1]], border=0)
        assert out == "█"

    def test_border_one_around_single_module(self):
        # 1x1 dark, border=1 → 3x3 padded → odd rows → pad to 4 rows.
        # Row 0 = all light, row 1 = light,dark,light, row 2 = all light,
        # row 3 = appended pad (all light).
        # Pairs: rows 0+1 → "▄ ▄"? no: glyphs map (top,bot) of each col.
        # Col 0: (0,0) → " "; col 1: (0,1) → "▄"; col 2: (0,0) → " ".
        # Pairs: rows 2+3 all light → "   ".
        out = HalfBlockRenderer().render([[1]], border=1)
        assert out.split("\n") == [" ▄ ", "   "]

    def test_output_width_matches_padded_module_count(self):
        bitmap = [[1, 0, 1], [0, 1, 0], [1, 1, 0]]
        border = 2
        out = HalfBlockRenderer().render(bitmap, border=border)
        expected_width = len(bitmap[0]) + 2 * border
        for line in out.split("\n"):
            assert len(line) == expected_width

    def test_uses_only_known_glyphs(self):
        out = HalfBlockRenderer().render([[1, 0], [0, 1], [1, 1]], border=1)
        assert set(out) <= set(" ▀▄█\n")
