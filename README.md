# publish3d

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

A versatile tool for managing and synchronizing 3D printable designs across multiple platforms with a plugin-based architecture.

**WARNING**: This project is in early development and may not be fully functional. Use at your own risk.

## Features

- **Multi-platform support**: Publish to Thingiverse, Printables, GitHub, and more
- **Bidirectional sync**: Keep designs updated across platforms
- **Plugin architecture**: Easily add support for new platforms
- **Canonical data model**: Unified representation of 3D designs
- **CLI interface**: Simple command-line control
- **Extensible**: Create custom plugins for special workflows

## Supported Platforms

| Platform       | Read | Write |
|----------------|------|-------|
| Local Files    | 🚧   | 🚧    |

## Installation

```bash
pip install publish3d
```

Or install from source:

```bash
git clone https://github.com/nomike/publish3d
cd publish3d
pip install -e .
```
