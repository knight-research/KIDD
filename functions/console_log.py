import os
import sys
import threading
import time
from collections import deque


_MAX_LINES = 300
_MAX_LOG_BYTES = 512 * 1024
_lines = deque(maxlen=_MAX_LINES)
_device_lines = {}
_lock = threading.Lock()
_sequence = 0
_installed = False
_original_stdout = None
_original_stderr = None
_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_log_path = os.path.join(_project_root, "data", "console.log")


def get_console_log_path():
    return _log_path


def get_device_console_log_path(device):
    safe_device = str(device).strip().lower()
    return os.path.join(_project_root, "data", f"console-{safe_device}.log")


def _trim_log_file_if_needed(path):
    try:
        if not os.path.exists(path) or os.path.getsize(path) <= _MAX_LOG_BYTES:
            return
        with open(path, "rb") as f:
            f.seek(-_MAX_LOG_BYTES // 2, os.SEEK_END)
            data = f.read()
        with open(path, "wb") as f:
            f.write(data)
    except OSError:
        pass


def _write_log_file(path, line):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        _trim_log_file_if_needed(path)
        with open(path, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        pass


def _next_sequence():
    global _sequence
    _sequence += 1
    return _sequence


def _append_line(text, device=None):
    if not text:
        return
    timestamp = time.strftime("%H:%M:%S")
    line = f"{timestamp} {text}"
    with _lock:
        sequence = _next_sequence()
        if device:
            device_key = str(device).strip().upper()
            _device_lines.setdefault(device_key, deque(maxlen=_MAX_LINES)).append((sequence, line))
            _write_log_file(get_device_console_log_path(device_key), line)
        else:
            _lines.append((sequence, line))
            _write_log_file(_log_path, line)


def log(message, device=None):
    _append_line(str(message), device=device)


def get_console_lines(limit=80, device=None):
    with _lock:
        lines = list(_lines)
        if device:
            device_key = str(device).strip().upper()
            lines += list(_device_lines.get(device_key, ()))
            lines.sort(key=lambda item: item[0])
        return [line for _, line in lines[-limit:]]


class _ConsoleTee:
    def __init__(self, target):
        self.target = target
        self._buffer = ""

    def write(self, text):
        if self.target is not None:
            self.target.write(text)
        if not text:
            return
        self._buffer += str(text)
        while "\n" in self._buffer:
            line, self._buffer = self._buffer.split("\n", 1)
            _append_line(line.rstrip("\r"))

    def flush(self):
        if self.target is not None:
            self.target.flush()

    def isatty(self):
        return bool(getattr(self.target, "isatty", lambda: False)())


def install_console_capture():
    global _installed, _original_stdout, _original_stderr
    if _installed:
        return
    _original_stdout = sys.stdout
    _original_stderr = sys.stderr
    sys.stdout = _ConsoleTee(_original_stdout)
    sys.stderr = _ConsoleTee(_original_stderr)
    _installed = True
    log("KIDD console capture active")
