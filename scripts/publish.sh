#!/usr/bin/env bash
# =============================================================================
# publish.sh – Build and publish the package to PyPI (or TestPyPI).
#
# Usage:
#   ./scripts/publish.sh               # publish to PyPI
#   ./scripts/publish.sh --test        # publish to TestPyPI
#   ./scripts/publish.sh --build-only  # build without uploading
#
# Pre-requisites:
#   pip install build twine
#
# For TestPyPI / PyPI you need either:
#   - A ~/.pypirc file with credentials, OR
#   - TWINE_USERNAME / TWINE_PASSWORD environment variables, OR
#   - Trusted Publishing configured on PyPI (recommended for CI).
# =============================================================================

set -euo pipefail

# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────
info()  { echo "[INFO]  $*"; }
error() { echo "[ERROR] $*" >&2; }

# ──────────────────────────────────────────────────────────────────────────────
# Parse arguments
# ──────────────────────────────────────────────────────────────────────────────
REPOSITORY="pypi"
BUILD_ONLY=false

for arg in "$@"; do
  case "$arg" in
    --test)       REPOSITORY="testpypi" ;;
    --build-only) BUILD_ONLY=true ;;
    *)
      error "Unknown argument: $arg"
      echo "Usage: $0 [--test] [--build-only]"
      exit 1
      ;;
  esac
done

# ──────────────────────────────────────────────────────────────────────────────
# Verify required tools
# ──────────────────────────────────────────────────────────────────────────────
for tool in python twine; do
  if ! command -v "$tool" &>/dev/null; then
    error "'$tool' is not installed. Run: pip install build twine"
    exit 1
  fi
done

# ──────────────────────────────────────────────────────────────────────────────
# Read version from pyproject.toml
# ──────────────────────────────────────────────────────────────────────────────
VERSION=$(python -c "
import re, pathlib
text = pathlib.Path('pyproject.toml').read_text()
m = re.search(r'^version\s*=\s*\"([^\"]+)\"', text, re.MULTILINE)
print(m.group(1) if m else 'unknown')
")
info "Package version: $VERSION"

# ──────────────────────────────────────────────────────────────────────────────
# Confirm before proceeding (skip in CI)
# ──────────────────────────────────────────────────────────────────────────────
if [[ -z "${CI:-}" && "$BUILD_ONLY" == false ]]; then
  read -r -p "Publish v${VERSION} to ${REPOSITORY}? [y/N] " confirm
  if [[ "${confirm,,}" != "y" ]]; then
    info "Aborted."
    exit 0
  fi
fi

# ──────────────────────────────────────────────────────────────────────────────
# Clean previous builds
# ──────────────────────────────────────────────────────────────────────────────
info "Cleaning previous dist/ and build/ directories..."
rm -rf dist/ build/ src/*.egg-info

# ──────────────────────────────────────────────────────────────────────────────
# Build
# ──────────────────────────────────────────────────────────────────────────────
info "Building source distribution and wheel..."
python -m build

info "Verifying distribution with twine..."
twine check dist/*

if [[ "$BUILD_ONLY" == true ]]; then
  info "Build complete (--build-only mode, skipping upload)."
  exit 0
fi

# ──────────────────────────────────────────────────────────────────────────────
# Upload
# ──────────────────────────────────────────────────────────────────────────────
if [[ "$REPOSITORY" == "testpypi" ]]; then
  info "Uploading to TestPyPI..."
  twine upload --repository testpypi dist/*
  info "Done! Install test release with:"
  echo "  pip install --index-url https://test.pypi.org/simple/ mcp-server-template-python==${VERSION}"
else
  info "Uploading to PyPI..."
  twine upload dist/*
  info "Done! Install with:"
  echo "  pip install mcp-server-template-python==${VERSION}"
fi
