import sys
import threading
import time
from collections import deque


_MAX_LINES = 300
_lines = deque(maxlen=_MAX_LINES)
_lock = threading.Lock()
_installed = False
_original_stdout = None
_original_stderr = None


def _append_line(text):
    if not text:
        return
    timestamp = time.strftime("%H:%M:%S")
    with _lock:
        _lines.append(f"{timestamp} {text}")


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
