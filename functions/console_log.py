import os
import sys
import threading
import time
from collections import deque


_MAX_LINES = 300
_MAX_LOG_BYTES = 512 * 1024
_lines = deque(maxlen=_MAX_LINES)
_lock = threading.Lock()
_installed = False
_original_stdout = None
_original_stderr = None
_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_log_path = os.path.join(_project_root, "data", "console.log")


def get_console_log_path():
    return _log_path


def _trim_log_file_if_needed():
    try:
        if not os.path.exists(_log_path) or os.path.getsize(_log_path) <= _MAX_LOG_BYTES:
            return
        with open(_log_path, "rb") as f:
            f.seek(-_MAX_LOG_BYTES // 2, os.SEEK_END)
            data = f.read()
        with open(_log_path, "wb") as f:
            f.write(data)
    except OSError:
        pass


def _write_log_file(line):
    try:
        os.makedirs(os.path.dirname(_log_path), exist_ok=True)
        _trim_log_file_if_needed()
        with open(_log_path, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        pass


def _append_line(text):
    if not text:
        return
    timestamp = time.strftime("%H:%M:%S")
    line = f"{timestamp} {text}"
    with _lock:
        _lines.append(line)
        _write_log_file(line)


def log(message):
    _append_line(str(message))


def get_console_lines(limit=80):
    with _lock:
        return list(_lines)[-limit:]


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
