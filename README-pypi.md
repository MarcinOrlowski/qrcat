![qrcat logo](https://raw.githubusercontent.com/MarcinOrlowski/qrcat/refs/heads/master/docs/logo.webp)


![PyPI - Version](https://img.shields.io/pypi/v/qrcat?style=flat)
[![PyPI Downloads](https://static.pepy.tech/badge/qrcat)](https://pepy.tech/projects/qrcat)
![MIT License](https://img.shields.io/github/license/MarcinOrlowski/qrcat)

# qrcat

`qrcat` (pronounced `Purr Cat`) is a command line utility that prints QR codes directly to your
terminal using nothing but block characters.

```bash
pipx install qrcat
```

Aside from being a standalone application, you can also use `qrcat` in your Python project.
See [dev docs](docs/README.md) for more information.

## Features

- Pure-Python, single runtime dep (`segno`) — no Pillow, no browser, no PNG.
- Pluggable renderer architecture — half-block today, quadrant / ANSI-color drop-in tomorrow.
- Works in any unicode-capable terminal.
- Library for your Python project *and* CLI tool from the same package.

## Example

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

## Easy installation

Use [pipx](https://pypi.org/project/pipx/) package manager to install `qrcat` as standalone
application.

```bash
pipx install qrcat
```

Once installed `qrcat` binary should be instantly available in your terminal.

## License

* Written and copyrighted &copy;2026 by Marcin Orlowski <mail (#) marcinorlowski (.) com>
* `qrcat` is open-source software licensed under
  the [MIT license](http://opensource.org/licenses/MIT)
