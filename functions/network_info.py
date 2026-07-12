import subprocess


def read_wlan0_ip():
    try:
        ip_address = subprocess.check_output(
            ["ip", "address", "show", "wlan0"],
            stderr=subprocess.DEVNULL,
        ).decode("utf-8")
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "127.0.0.1"

    ip_lines = [line.strip() for line in ip_address.splitlines() if "inet " in line]
    if not ip_lines:
        return "127.0.0.1"

    return ip_lines[0].split()[1]
