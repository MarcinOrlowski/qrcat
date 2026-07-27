![qrcat logo](logo.webp)

# Installation

* [As command line too](#command-line-tool)
* [Use as library in your code](#use-as-library)

---

## Command line tool

### Usage examples

```bash
$ qrcat https://MarcinOrlowski.com

█▀▀▀▀▀█  ██▀ █▄▄▀ █▀▀▀▀▀█
█ ███ █ █▄▄ █▄█▀▀ █ ███ █
█ ▀▀▀ █ █▄▀█▄▄█▄▀ █ ▀▀▀ █
▀▀▀▀▀▀▀ █▄█▄█ █ ▀ ▀▀▀▀▀▀▀
▀▄██▀▀▀▄▄▀█ █▀█▀█ ▀█▀▀▀▄
█▄▀█ █▀▀▀  █ ▀▄▀█▄██▄▀ ▀█
▄▄ ▀▄█▀▀█▄▀▀██▀▄▄█▀▄ ▄▀█▀
█  █ ▄▀  █▀  ▀▄▀▄ ▀██▀ ▀█
▀ ▀▀  ▀▀██ █▀█▀▄█▀▀▀█▄▀
█▀▀▀▀▀█ ▄▄▀▄  ▄ █ ▀ █▄▀▀▀
█ ███ █ ██▀█▀█ ▀▀██▀█▄█▄▄
█ ▀▀▀ █ ▀▄█▄▄▀▀██ ▄▄▄█▀ █
▀▀▀▀▀▀▀ ▀▀  ▀▀▀  ▀ ▀▀▀▀▀▀
```

`qrcat` can also read from `stdin`

For other use cases see `--help` option.

---

## Use as library

`qrcat` can also be set as project dependency and used as regular library from your Python code as
well.

```bash
$ python
Python 3.13.7 (main, Mar  3 2026, 12:19:54) [GCC 15.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from qrcat import render_qr
>>> print(render_qr("https://MarcinOrlowski.com"))

█▀▀▀▀▀█  ██▀ █▄▄▀ █▀▀▀▀▀█
█ ███ █ █▄▄ █▄█▀▀ █ ███ █
█ ▀▀▀ █ █▄▀█▄▄█▄▀ █ ▀▀▀ █
▀▀▀▀▀▀▀ █▄█▄█ █ ▀ ▀▀▀▀▀▀▀
▀▄██▀▀▀▄▄▀█ █▀█▀█ ▀█▀▀▀▄
█▄▀█ █▀▀▀  █ ▀▄▀█▄██▄▀ ▀█
▄▄ ▀▄█▀▀█▄▀▀██▀▄▄█▀▄ ▄▀█▀
█  █ ▄▀  █▀  ▀▄▀▄ ▀██▀ ▀█
▀ ▀▀  ▀▀██ █▀█▀▄█▀▀▀█▄▀
█▀▀▀▀▀█ ▄▄▀▄  ▄ █ ▀ █▄▀▀▀
█ ███ █ ██▀█▀█ ▀▀██▀█▄█▄▄
█ ▀▀▀ █ ▀▄█▄▄▀▀██ ▄▄▄█▀ █
▀▀▀▀▀▀▀ ▀▀  ▀▀▀  ▀ ▀▀▀▀▀▀

>>> print(render_qr("Hello world!"))

█▀▀▀▀▀█ ▀ ▀ █ █ ▀
█ ███ █ █▀▄▀▀█▀
█ ▀▀▀ █   ▄▄█▄▀▄▄
▀▀▀▀▀▀▀ █▀▀  ▀  █
▀▄█▄██▀█ ▀█▀▀ █ █
▀█  ███▀█ █▀▀  ▀█
▀▀▄ █▄▄ ▄█▀▄▀▀█ ▀
▀ ▄ ▄▄▀█ ▀▄▀ ▄█ ▄
▀  ▀▀ ▀  ▀▀ ▀▀

>>>
```

## Renderers

- `HalfBlockRenderer` - packs 2 modules vertically per character using `▀ ▄ █` and space. Default.

More renderers (quadrant 2x2, etc.) can be added by subclassing `Renderer`.
