# Python MCP Server Template

> A **production-ready** starter template for building [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) servers in Python, designed to be a **role model** for clean, maintainable, and extensible codebases.

[![CI](https://github.com/your-username/mcp-server-template-python/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/mcp-server-template-python/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/mcp-server-template-python.svg)](https://badge.fury.io/py/mcp-server-template-python)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Available Tools](#available-tools)
- [CLI Reference](#cli-reference)
- [Running Tests](#running-tests)
- [Adding a New Tool](#adding-a-new-tool)
- [Publishing to PyPI](#publishing-to-pypi)
- [Contributing](#contributing)

---

## Features

- ✅ **`src` layout** – proper Python packaging with Hatchling build backend
- ✅ **FastMCP** – modern MCP server framework with full type support
- ✅ **Pydantic v2 configuration** – strongly typed, environment-driven config
- ✅ **Structured logging** – rotating file + console logging, level-controlled via env
- ✅ **Typer CLI** – `mcp-server start` / `mcp-server version` with rich help
- ✅ **Built-in tool library** – utility, math, text, and datetime tool modules
- ✅ **Full test suite** – pytest with coverage, ready for CI
- ✅ **GitHub Actions CI** – lint → test → build on every push/PR
- ✅ **GitHub Actions Publish** – automated TestPyPI → PyPI on version tag push
- ✅ **`scripts/publish.sh`** – local one-command publish helper

---

## Project Structure

```
mcp-server-template-python/
├── src/
│   └── mcp_server/
│       ├── __init__.py            # Package version & public API
│       ├── main.py                # Server entry point & tool registration
│       ├── cli.py                 # Typer CLI (start / version)
│       ├── config/
│       │   ├── __init__.py
│       │   └── config.py          # Pydantic config models + load_config()
│       ├── tools/
│       │   ├── __init__.py
│       │   ├── utility.py         # Echo, Ping, Server Info
│       │   ├── math_tools.py      # Add, Subtract, Multiply, Divide, Power, √, !
│       │   ├── text_tools.py      # Upper/Lower, Reverse, Word Count, Emails …
│       │   └── datetime_tools.py  # UTC time, timezone, date arithmetic …
│       └── utils/
│           ├── __init__.py
│           └── logging.py         # Rotating-file + console logging setup
├── tests/
│   ├── __init__.py
│   ├── test_config.py
│   ├── test_logging.py
│   ├── test_main.py
│   ├── test_tools_utility.py
│   ├── test_tools_math.py
│   ├── test_tools_text.py
│   └── test_tools_datetime.py
├── examples/
│   └── basic_usage.py             # Minimal runnable example
├── docs/
│   └── README.md                  # Extended documentation
├── scripts/
│   └── publish.sh                 # Local PyPI publish helper
├── .github/
│   └── workflows/
│       ├── ci.yml                 # Lint → Test → Build
│       └── publish.yml            # Publish to TestPyPI → PyPI on tag
├── .env.example                   # Environment variable reference
├── pyproject.toml                 # PEP 621 metadata + Hatchling build
├── CHANGELOG.md
├── CONTRIBUTING.md
└── LICENSE
```

---

## Quick Start

### 1 – Install

```bash
# Clone
git clone https://github.com/your-username/mcp-server-template-python.git
cd mcp-server-template-python

# Create & activate a virtual environment
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# Install in editable mode (dev extras include pytest, ruff, mypy, black…)
pip install -e ".[dev]"

# Copy and configure env
cp .env.example .env
```

### 2 – Run

```bash
# HTTP transport (default)
mcp-server start

# stdio transport (for Claude Desktop / Cursor integration)
mcp-server start --transport stdio

# Custom host / port
mcp-server start --host 127.0.0.1 --port 9000
```

### 3 – Verify

```bash
# Check version
mcp-server version

# Run as a Python module
python -m mcp_server.main
```

---

## Configuration

All settings are read from environment variables (`.env` is loaded automatically).

| Variable          | Default                                           | Description                          |
|-------------------|---------------------------------------------------|--------------------------------------|
| `APP_NAME`        | `mcp_server`                                      | Server name                          |
| `HOST`            | `0.0.0.0`                                         | Bind host                            |
| `PORT`            | `8000`                                            | Bind port                            |
| `DEBUG`           | `false`                                           | Enable debug mode                    |
| `TRANSPORT`       | `streamable-http`                                 | Transport (`stdio`, `streamable-http`, `sse`) |
| `LOG_LEVEL`       | `INFO`                                            | Log level                            |
| `LOG_FORMAT`      | `%(asctime)s - %(name)s - %(levelname)s - %(message)s` | Log format              |
| `LOG_FILE_ENABLED`| `true`                                            | Write logs to file                   |
| `LOG_FILE_DIR`    | `logs`                                            | Log file directory                   |
| `API_KEY_ENABLED` | `false`                                           | Enable API key auth                  |
| `API_KEY`         | *(unset)*                                         | API key value                        |
| `CORS_ORIGINS`    | `*`                                               | Comma-separated allowed origins      |

---

## Available Tools

### Utility
| Tool Name       | Description                         |
|-----------------|-------------------------------------|
| `hello-world`   | Returns a greeting for a given name |
| `Echo Message`  | Returns the message unchanged       |
| `Get Server Info` | Returns server name, version, description |
| `Ping`          | Health-check – returns `"pong"`     |

### Math
| Tool Name         | Description                     |
|-------------------|---------------------------------|
| `Add Numbers`     | a + b                           |
| `Subtract Numbers`| a − b                           |
| `Multiply Numbers`| a × b                           |
| `Divide Numbers`  | a ÷ b (raises on zero divisor)  |
| `Power`           | base ^ exponent                 |
| `Square Root`     | √value                          |
| `Factorial`       | n!                              |

### Text
| Tool Name         | Description                              |
|-------------------|------------------------------------------|
| `Uppercase Text`  | Convert to UPPER CASE                    |
| `Lowercase Text`  | Convert to lower case                    |
| `Reverse Text`    | Reverse a string                         |
| `Count Words`     | Count words in text                      |
| `Count Characters`| Count chars (optionally exclude spaces)  |
| `Title Case`      | Convert to Title Case                    |
| `Split Text`      | Split by delimiter                       |
| `Replace Text`    | Replace all occurrences                  |
| `Trim Text`       | Strip leading/trailing whitespace        |
| `Extract Emails`  | Find all email addresses in text         |

### Datetime
| Tool Name           | Description                                  |
|---------------------|----------------------------------------------|
| `Current UTC Time`  | Current UTC datetime in ISO 8601             |
| `Current Date`      | Today's date (UTC) in ISO 8601               |
| `Time In Timezone`  | Current time in a given IANA timezone        |
| `Add Days To Date`  | Add/subtract days from a date                |
| `Days Between Dates`| Count days between two dates                 |
| `Format Datetime`   | Re-format an ISO datetime with strftime      |

---

## CLI Reference

```
mcp-server --help

Commands:
  start    Start the MCP server
  version  Display the current version

mcp-server start --help

Options:
  -h, --host        Host to bind the server to  [default: 0.0.0.0]
  -p, --port        Port to bind the server to  [default: 8000]
  -t, --transport   Transport protocol           [default: streamable-http]
  -d, --debug       Enable debug mode
  -l, --log-level   Log level                   [default: INFO]
```

---

## Running Tests

```bash
# All tests
pytest

# With coverage
pytest --cov=src/mcp_server --cov-report=term-missing

# Single module
pytest tests/test_tools_math.py -v
```

---

## Adding a New Tool

1. Create `src/mcp_server/tools/<category>_tools.py`.
2. Implement `register_<category>_tools(mcp_instance: FastMCP) -> None`.
3. Add the register call in `src/mcp_server/main.py`.
4. Export from `src/mcp_server/tools/__init__.py`.
5. Write tests in `tests/test_tools_<category>.py`.

See [CONTRIBUTING.md](CONTRIBUTING.md) for a full skeleton and guidelines.

---

## Publishing to PyPI

### Automated (recommended)

Push a version tag to trigger the GitHub Actions publish workflow:

```bash
# Bump version in pyproject.toml and src/mcp_server/__init__.py first, then:
git commit -am "chore: release v0.2.0"
git tag v0.2.0
git push origin main --tags
```

The workflow publishes to **TestPyPI** first, then promotes to **PyPI**.  
You must configure **Trusted Publishing** (OIDC) on both registries – no API tokens needed.

> See [PyPI Trusted Publishing docs](https://docs.pypi.org/trusted-publishers/) for setup.

### Manual

```bash
# Build only (no upload)
./scripts/publish.sh --build-only

# Upload to TestPyPI
./scripts/publish.sh --test

# Upload to PyPI
./scripts/publish.sh
```

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR.

---

## License

[MIT](LICENSE) © Your Name


