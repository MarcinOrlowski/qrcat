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

Tests for the qrcat CLI argument parser and entry point.
"""

from __future__ import annotations

import pytest

from qrcat import __version__
from qrcat.cli import _build_parser, main


class TestParser:
    def test_data_optional(self):
        parser = _build_parser()
        ns = parser.parse_args([])
        assert ns.data is None

    def test_defaults(self):
        parser = _build_parser()
        ns = parser.parse_args(["hello"])
        assert ns.data == "hello"
        assert ns.border == 2
        assert ns.version is False

    def test_border_int(self):
        parser = _build_parser()
        ns = parser.parse_args(["x", "-b", "5"])
        assert ns.border == 5

    def test_border_rejects_non_int(self):
        parser = _build_parser()
        with pytest.raises(SystemExit):
            parser.parse_args(["x", "-b", "huge"])


class TestMain:
    def test_version_flag(self, capsys):
        rc = main(["--version"])
        assert rc == 0
        out = capsys.readouterr().out.strip()
        assert out == __version__

    def test_help_includes_about_and_qr(self, capsys):
        from qrcat import __author__, __url__

        with pytest.raises(SystemExit) as exc:
            main(["--help"])
        assert exc.value.code == 0
        out = capsys.readouterr().out
        # Standard argparse content still present.
        assert "usage:" in out
        # Project info appended.
        assert f"qrcat v{__version__}" in out
        assert __author__ in out
        assert __url__ in out
        # Rendered QR (half-block glyphs).
        assert any(ch in out for ch in "▀▄█")

    def test_render_prints_output(self, capsys):
        rc = main(["hello"])
        assert rc == 0
        out = capsys.readouterr().out
        assert out.strip(), "expected non-empty render"
        # Half-block renderer must use only its known glyphs plus newline.
        allowed = set(" ▀▄█\n")
        assert set(out) <= allowed, f"unexpected glyphs: {set(out) - allowed!r}"

    def test_stdin_dash_reads_input(self, capsys, monkeypatch):
        import io

        stream = io.StringIO("https://example.com\n")
        stream.isatty = lambda: False  # type: ignore[method-assign]
        monkeypatch.setattr("sys.stdin", stream)
        rc = main(["-"])
        assert rc == 0
        assert capsys.readouterr().out.strip()

    def test_no_arg_reads_piped_stdin(self, capsys, monkeypatch):
        import io

        stream = io.StringIO("hello\n")
        stream.isatty = lambda: False  # type: ignore[method-assign]
        monkeypatch.setattr("sys.stdin", stream)
        rc = main([])
        assert rc == 0
        assert capsys.readouterr().out.strip()

    def test_no_arg_with_tty_stdin_errors(self, monkeypatch):
        import io

        stream = io.StringIO("")
        stream.isatty = lambda: True  # type: ignore[method-assign]
        monkeypatch.setattr("sys.stdin", stream)
        with pytest.raises(SystemExit):
            main([])

    def test_empty_stdin_errors(self, monkeypatch):
        import io

        stream = io.StringIO("")
        stream.isatty = lambda: False  # type: ignore[method-assign]
        monkeypatch.setattr("sys.stdin", stream)
        with pytest.raises(SystemExit):
            main(["-"])
