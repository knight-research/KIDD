#!/usr/bin/env bash
set -euo pipefail

APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PYTHON="$APP_DIR/.venv/bin/python"
MAIN_PATH="$APP_DIR/main.py"

if [[ ! -x "$VENV_PYTHON" ]]; then
  echo "KIDD virtual environment not found: $VENV_PYTHON" >&2
  echo "Run ./install.sh first." >&2
  exit 1
fi

exec "$VENV_PYTHON" "$MAIN_PATH" "$@"
