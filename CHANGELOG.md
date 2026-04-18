# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- Initial template structure

---

## [0.1.0] – 2024-01-01

### Added
- `src` layout with `mcp_server` package
- `FastMCP`-based server with `hello-world` tool
- Centralized configuration via Pydantic models (`AppConfig`, `ServerConfig`, `LoggingConfig`, `SecurityConfig`)
- Rotating-file logging utility (`utils/logging.py`)
- Utility tools: Echo Message, Get Server Info, Ping
- Math tools: Add, Subtract, Multiply, Divide, Power, Square Root, Factorial
- Text tools: Uppercase, Lowercase, Reverse, Count Words/Characters, Title Case, Split, Replace, Trim, Extract Emails
- Datetime tools: Current UTC Time, Current Date, Time In Timezone, Add Days, Days Between Dates, Format Datetime
- Typer-based CLI with `start` and `version` commands supporting `--host`, `--port`, `--transport`, `--debug`, `--log-level`
- Comprehensive test suite with pytest
- GitHub Actions CI workflow (lint, test, build)
- GitHub Actions Publish workflow (TestPyPI → PyPI on version tag push)
- `scripts/publish.sh` helper for local publishing
- `pyproject.toml` with Hatchling build backend, classifiers, and project URLs
- `LICENSE` (MIT), `CONTRIBUTING.md`, `CHANGELOG.md`

[Unreleased]: https://github.com/your-username/mcp-server-template-python/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/your-username/mcp-server-template-python/releases/tag/v0.1.0
