import os


def load_version():
    version_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "version.txt")
    try:
        with open(version_path, "r") as f:
            lines = f.readlines()
            version = lines[0].strip() if len(lines) > 0 else "unknown"
            last_change = lines[1].strip() if len(lines) > 1 else "unknown"
    except FileNotFoundError:
        version = "unknown"
        last_change = "unknown"
    return version, last_change