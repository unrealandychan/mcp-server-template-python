# Contributing

Thank you for your interest in contributing to **mcp-server-template-python**! 🎉  
This document outlines the process for contributing code, bug reports, and documentation improvements.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Workflow](#development-workflow)
4. [Coding Standards](#coding-standards)
5. [Running Tests](#running-tests)
6. [Adding a New Tool](#adding-a-new-tool)
7. [Submitting a Pull Request](#submitting-a-pull-request)
8. [Publishing a Release](#publishing-a-release)

---

## Code of Conduct

Be respectful and constructive. We follow the [Contributor Covenant](https://www.contributor-covenant.org/).

---

## Getting Started

```bash
# 1. Fork and clone the repo
git clone https://github.com/your-username/mcp-server-template-python.git
cd mcp-server-template-python

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install the package in editable mode with dev extras
pip install -e ".[dev]"

# 4. Copy the example env file
cp .env.example .env
```

---

## Development Workflow

```
main          ← stable releases only
develop       ← integration branch
feature/xyz   ← your feature branch (branch off develop)
fix/xyz       ← bug fixes (branch off develop)
```

1. Branch off `develop`: `git checkout -b feature/my-feature develop`
2. Make your changes with tests.
3. Run lint and tests locally (see below).
4. Open a PR targeting `develop`.

---

## Coding Standards

| Tool     | Purpose                   | Command                       |
|----------|---------------------------|-------------------------------|
| `ruff`   | Linting + import sorting  | `ruff check src/ tests/`      |
| `black`  | Code formatting           | `black src/ tests/`           |
| `mypy`   | Static type checking      | `mypy src/`                   |

All public functions and methods **must** have type annotations and docstrings.

---

## Running Tests

```bash
# Run the full test suite
pytest

# With coverage report
pytest --cov=src/mcp_server --cov-report=term-missing

# Run a specific test file
pytest tests/test_tools_math.py -v
```

---

## Adding a New Tool

1. Create `src/mcp_server/tools/<category>_tools.py`.
2. Define a `register_<category>_tools(mcp_instance: FastMCP) -> None` function.
3. Decorate each tool with `@mcp_instance.tool("Tool Name")`.
4. Add the register call in `src/mcp_server/main.py`.
5. Export from `src/mcp_server/tools/__init__.py`.
6. Write tests in `tests/test_tools_<category>.py`.

**Example skeleton:**

```python
# src/mcp_server/tools/my_tools.py
from fastmcp import FastMCP


def register_my_tools(mcp_instance: FastMCP) -> None:
    @mcp_instance.tool("My Tool")
    def my_tool(param: str) -> str:
        """Short description of what the tool does."""
        return param.upper()
```

---

## Submitting a Pull Request

- Keep PRs focused – one logical change per PR.
- Include tests for new functionality.
- Update `CHANGELOG.md` under `[Unreleased]`.
- Make sure CI passes before requesting review.

---

## Publishing a Release

Releases are automated via GitHub Actions when a version tag is pushed:

```bash
# 1. Bump the version in pyproject.toml and src/mcp_server/__init__.py
# 2. Update CHANGELOG.md (move Unreleased → new version)
# 3. Commit and tag
git commit -am "chore: release v0.2.0"
git tag v0.2.0
git push origin main --tags
```

The CI/CD pipeline will:
1. Build the wheel and sdist.
2. Publish to **TestPyPI** first.
3. Promote to **PyPI** after the TestPyPI environment is approved.

For a local manual release, use the helper script:

```bash
# Dry-run (build only, no upload)
./scripts/publish.sh --build-only

# Publish to TestPyPI
./scripts/publish.sh --test

# Publish to PyPI
./scripts/publish.sh
```
