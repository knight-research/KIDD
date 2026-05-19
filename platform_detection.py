import sys


def detect_platform():
    sys_win = sys.platform == "win32" or sys.platform == "win64"
    sys_linux = sys.platform == "linux"
    sys_pi = False

    if sys_linux:
        try:
            with open("/sys/firmware/devicetree/base/model", "r") as f:
                model = f.read().strip()
            sys_pi = "Raspberry Pi" in model
        except FileNotFoundError:
            pass

    return sys_win, sys_linux, sys_pi