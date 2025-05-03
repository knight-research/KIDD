#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import platform
import re
import subprocess

def get_os_import_file():
    system = platform.system().lower()
    if 'linux' in system:
        return 'import_linux.py'
    elif 'windows' in system:
        return 'import_win.py'
    elif 'darwin' in system:
        return 'import_pi.py'  # Beispiel für macOS oder Pi
    else:
        raise RuntimeError(f"Unbekanntes Betriebssystem: {system}")

def extract_modules(filename):
    with open(filename, 'r') as f:
        content = f.read()
    imports = re.findall(r'^\s*(?:import|from)\s+([a-zA-Z0-9_\.]+)', content, re.MULTILINE)
    modules = set([i.split('.')[0] for i in imports if not i.startswith('kidd')])  # ggf. eigene Module filtern
    return sorted(modules)

def install_modules(modules):
    for module in modules:
        try:
            subprocess.check_call(['pip', 'install', module])
            print(f"✔ Installiert: {module}")
        except subprocess.CalledProcessError:
            print(f"✖ Fehler bei der Installation: {module}")

if __name__ == '__main__':
    import_file = get_os_import_file()
    print(f"Erkenne System – verwende: {import_file}")
    modules = extract_modules(import_file)
    print(f"Gefundene Module: {modules}")
    install_modules(modules)
