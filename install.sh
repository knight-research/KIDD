#!/usr/bin/env bash
set -euo pipefail

APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
MAIN_PATH="$APP_DIR/main.py"
SERVICE_NAME="kidd"

INSTALL_RPI=0
INSTALL_AUDIO=1
CREATE_VENV=1
SYSTEM_INSTALL=0
INSTALL_AUTOSTART=1
VENV_DIR="$APP_DIR/.venv"

usage() {
  cat <<USAGE
KIDD dependency installer

Usage:
  ./install.sh [options]

Options:
  --rpi             Install Raspberry Pi hardware Python modules.
  --no-audio        Skip optional microphone/audio build dependencies and requirements-audio.txt.
  --venv            Create/use a local .venv before installing Python modules. This is the default.
  --system          Install Python modules into the active system Python.
  --no-autostart    Do not create the Raspberry Pi autostart service.
  --python PATH     Python executable to use. Default: python3
  -h, --help        Show this help.
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --rpi)
      INSTALL_RPI=1
      shift
      ;;
    --no-audio)
      INSTALL_AUDIO=0
      shift
      ;;
    --venv)
      CREATE_VENV=1
      shift
      ;;
    --system)
      CREATE_VENV=0
      SYSTEM_INSTALL=1
      shift
      ;;
    --no-autostart)
      INSTALL_AUTOSTART=0
      shift
      ;;
    --python)
      PYTHON_BIN="${2:-}"
      if [[ -z "$PYTHON_BIN" ]]; then
        echo "Missing value for --python" >&2
        exit 2
      fi
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage
      exit 2
      ;;
  esac
done

if [[ -f /proc/device-tree/model ]] && grep -qi "raspberry pi" /proc/device-tree/model 2>/dev/null; then
  INSTALL_RPI=1
fi

if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  echo "Python executable not found: $PYTHON_BIN" >&2
  exit 1
fi

if [[ ! -f "$MAIN_PATH" ]]; then
  echo "KIDD main.py not found: $MAIN_PATH" >&2
  exit 1
fi

run_sudo() {
  if [[ "${EUID:-$(id -u)}" -eq 0 ]]; then
    "$@"
  elif command -v sudo >/dev/null 2>&1; then
    sudo "$@"
  else
    echo "sudo is required for system packages, or run this script as root." >&2
    return 1
  fi
}

install_apt_packages() {
  if ! command -v apt-get >/dev/null 2>&1; then
    echo "apt-get not found, skipping system package installation."
    return
  fi

  local packages=(
    python3-pip
    python3-tk
    python3-venv
    git
    ffmpeg
    vlc
  )

  if [[ "$INSTALL_AUDIO" -eq 1 ]]; then
    packages+=(
      portaudio19-dev
      python3-pyaudio
      libasound2-dev
    )
  fi

  if [[ "$INSTALL_RPI" -eq 1 ]]; then
    packages+=(
      i2c-tools
      python3-smbus
    )
  fi

  echo "Installing system packages..."
  run_sudo apt-get update
  run_sudo apt-get install -y "${packages[@]}"
}

is_externally_managed_python() {
  local marker
  marker="$("$PYTHON_BIN" - <<'PY' || true
import pathlib
import sysconfig

paths = {
    pathlib.Path(sysconfig.get_path("stdlib", vars={"base": sysconfig.get_config_var("base") or ""})),
    pathlib.Path(sysconfig.get_path("stdlib")),
}

for path in paths:
    marker = path / "EXTERNALLY-MANAGED"
    if marker.exists():
        print(marker)
        raise SystemExit(0)

raise SystemExit(1)
PY
)"
  [[ -n "$marker" ]]
}

prepare_python() {
  if [[ "$CREATE_VENV" -eq 1 ]]; then
    if [[ ! -d "$VENV_DIR" ]]; then
      "$PYTHON_BIN" -m venv "$VENV_DIR"
    fi
    # shellcheck disable=SC1091
    source "$VENV_DIR/bin/activate"
    PYTHON_BIN="$VENV_DIR/bin/python"
  elif is_externally_managed_python; then
    echo "This Python environment is externally managed. Use the default .venv install or pass --venv." >&2
    echo "System installs are intentionally not forced with --break-system-packages." >&2
    exit 1
  fi

  "$PYTHON_BIN" -m pip install --upgrade pip setuptools wheel
}

install_requirements() {
  "$PYTHON_BIN" -m pip install -r "$APP_DIR/requirements.txt"

  if [[ "$INSTALL_RPI" -eq 1 ]]; then
    "$PYTHON_BIN" -m pip install -r "$APP_DIR/requirements-rpi.txt"
  fi

  if [[ "$INSTALL_AUDIO" -eq 1 ]]; then
    "$PYTHON_BIN" -m pip install -r "$APP_DIR/requirements-audio.txt"
  fi
}

install_pi_autostart() {
  if [[ "$INSTALL_RPI" -ne 1 || "$INSTALL_AUTOSTART" -ne 1 ]]; then
    return
  fi

  if ! command -v systemctl >/dev/null 2>&1; then
    echo "systemctl not found, skipping Raspberry Pi autostart service."
    return
  fi

  local service_path="/etc/systemd/system/${SERVICE_NAME}.service"
  local run_user="${SUDO_USER:-${USER}}"
  local run_home
  local run_uid
  run_home="$(getent passwd "$run_user" | cut -d: -f6)"
  if [[ -z "$run_home" ]]; then
    run_home="$HOME"
  fi
  run_uid="$(id -u "$run_user")"

  echo "Installing Raspberry Pi autostart service..."
  run_sudo tee "$service_path" >/dev/null <<EOF
[Unit]
Description=KIDD dashboard
After=graphical.target network-online.target sound.target
Wants=network-online.target

[Service]
Type=simple
User=${run_user}
WorkingDirectory=${APP_DIR}
Environment=PYTHONUNBUFFERED=1
Environment=DISPLAY=:0
Environment=XAUTHORITY=${run_home}/.Xauthority
Environment=XDG_RUNTIME_DIR=/run/user/${run_uid}
ExecStart=${PYTHON_BIN} ${MAIN_PATH}
Restart=always
RestartSec=10

[Install]
WantedBy=graphical.target
EOF

  run_sudo systemctl daemon-reload
  run_sudo systemctl enable "${SERVICE_NAME}.service"
  run_sudo systemctl restart "${SERVICE_NAME}.service" || true
  run_sudo systemctl --no-pager --full status "${SERVICE_NAME}.service" || true
}

echo "KIDD installer"
echo "App directory: $APP_DIR"
echo "Python: $PYTHON_BIN"
echo "Raspberry Pi modules: $INSTALL_RPI"
echo "Audio modules: $INSTALL_AUDIO"
echo "Virtualenv: $CREATE_VENV"
echo "System install: $SYSTEM_INSTALL"
echo "Pi autostart: $INSTALL_AUTOSTART"

install_apt_packages
prepare_python
install_requirements
install_pi_autostart

echo "KIDD dependencies installed."
if [[ "$CREATE_VENV" -eq 1 ]]; then
  echo "Start KIDD with: $VENV_DIR/bin/python $APP_DIR/main.py"
fi
if [[ "$INSTALL_RPI" -eq 1 && "$INSTALL_AUTOSTART" -eq 1 ]]; then
  echo "Autostart service: systemctl status ${SERVICE_NAME}"
  echo "Live logs: journalctl -u ${SERVICE_NAME} -f"
fi
