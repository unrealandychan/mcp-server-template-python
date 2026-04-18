# MCP Server Template – Extended Documentation

Refer to the [main README](../README.md) for a quick-start guide and feature overview.

## Architecture

The template follows the **`src` layout**:

```
src/mcp_server/   ← installable Python package
tests/            ← pytest test suite (never bundled in the wheel)
```

This keeps the package root clean and ensures that installed code is always
tested – not the raw source tree.

## Configuration System

`AppConfig` (Pydantic v2) is composed of three sub-models:

| Sub-model       | Env prefix | Key settings                     |
|-----------------|-----------|----------------------------------|
| `ServerConfig`  | –         | `HOST`, `PORT`, `DEBUG`, `TRANSPORT` |
| `LoggingConfig` | `LOG_`    | `LOG_LEVEL`, `LOG_FORMAT`, `LOG_FILE_ENABLED`, `LOG_FILE_DIR` |
| `SecurityConfig`| –         | `API_KEY_ENABLED`, `API_KEY`, `CORS_ORIGINS` |

Call `load_config()` anywhere, or import the module-level `config` singleton:

```python
from mcp_server.config import load_config

cfg = load_config()
print(cfg.server.port)   # 8000
```

## Transport Modes

| Transport          | Use Case                             |
|--------------------|--------------------------------------|
| `streamable-http`  | Remote HTTP clients, Cursor, REST    |
| `stdio`            | Claude Desktop, local LLM pipelines  |
| `sse`              | Server-Sent Events clients           |

## Logging

Logs are written to both `stdout` and `logs/<app_name>.log` (10 MB rotating,
5 backups). Set `LOG_FILE_ENABLED=false` to disable the file sink.

## CI/CD Pipeline

```
push / PR
   │
   ├── lint   (ruff, black --check, mypy)
   ├── test   (pytest + coverage)
   └── build  (python -m build + twine check)

push tag vX.Y.Z
   │
   ├── build → dist artifacts
   ├── publish → TestPyPI  (environment: testpypi)
   └── publish → PyPI      (environment: pypi, after testpypi approval)
```

## Security Notes

- Never commit `.env` – it is in `.gitignore`.
- Rotate `API_KEY` regularly if `API_KEY_ENABLED=true`.
- Review `CORS_ORIGINS` before deploying to production; restrict from `*`.
- Use [Trusted Publishing (OIDC)](https://docs.pypi.org/trusted-publishers/) instead of long-lived PyPI tokens.

