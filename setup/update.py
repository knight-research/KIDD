#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import threading

def install_if_missing(module_name, package_name=None):
    try:
        __import__(module_name)
    except ImportError:
        print(f"Modul '{module_name}' nicht gefunden. Installiere...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name or module_name])

install_if_missing("requests")
install_if_missing("tkinter", "tk")

import shutil
import requests
import zipfile
import io
import datetime
import json
import tkinter as tk
from tkinter import messagebox, ttk

GITHUB_REPO = "knight-research/KIDD"
BACKUP_PREFIX = "kidd.old"
VERSION_FILE = "version.txt"

# Checkbox-Zustand global
include_sound = None  # wird in run_gui() gesetzt

def get_latest_release_info():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def read_local_version(base_path):
    version_path = os.path.join(base_path, VERSION_FILE)
    if os.path.exists(version_path):
        with open(version_path, "r") as f:
            lines = f.readlines()
            version = lines[0].strip() if len(lines) > 0 else None
            last_change = lines[1].strip() if len(lines) > 1 else None
            return version, last_change
    return None, None

def write_local_version(base_path, version, last_change=None):
    version_path = os.path.join(base_path, VERSION_FILE)
    with open(version_path, "w") as f:
        f.write(version + "\n")
        if last_change:
            f.write(last_change + "\n")

def backup_existing_files(base_path):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder = f"{BACKUP_PREFIX}_{timestamp}"
    backup_path = os.path.join(base_path, backup_folder)
    os.makedirs(backup_path)

    for item in os.listdir(base_path):
        if item.startswith(BACKUP_PREFIX) or item == os.path.basename(__file__):
            continue
        src = os.path.join(base_path, item)
        dst = os.path.join(backup_path, item)
        shutil.move(src, dst)

def download_with_progress(url, progress_callback=None, status_callback=None):
    response = requests.get(url, stream=True)
    total = int(response.headers.get('content-length', 0))
    downloaded = 0
    chunks = []

    for data in response.iter_content(chunk_size=8192):
        chunks.append(data)
        downloaded += len(data)
        if total and progress_callback:
            percent = int(downloaded * 100 / total)
            progress_callback(percent)
        if status_callback:
            status_callback(f"{downloaded / 1024:.1f} KB heruntergeladen")

    return b"".join(chunks)

def extract_zip_to_base(zip_bytes, base_path):
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
        top_level_folder = z.namelist()[0].split("/")[0]
        for member in z.infolist():
            if member.is_dir():
                continue
            member_path = os.path.relpath(member.filename, top_level_folder)
            if member_path.startswith(".."):  # Sicherheitscheck
                continue
            if not include_sound.get() and member_path.startswith("sound/"):
                continue
            target_path = os.path.join(base_path, member_path)
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with z.open(member) as source, open(target_path, "wb") as target:
                shutil.copyfileobj(source, target)

def run_gui():
    global include_sound
    base_path = os.path.dirname(os.path.abspath(__file__))

    root = tk.Tk()
    include_sound = tk.BooleanVar(value=False)
    root.title("KIDD Updater")
    root.geometry("400x240")

    status_label = tk.Label(root, text="Initialisiere...", anchor="w")
    status_label.pack(fill="x", padx=10, pady=5)

    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=5)

    byte_label = tk.Label(root, text="", anchor="w")
    byte_label.pack(fill="x", padx=10)

    sound_check = tk.Checkbutton(root, text="Sound-Ordner aktualisieren", variable=include_sound)
    sound_check.pack(pady=5)

    def update_progress(percent):
        progress["value"] = percent
        root.update_idletasks()

    def update_status(text):
        byte_label.config(text=text)
        root.update_idletasks()

    def do_update(force=False):
        try:
            status_label.config(text="Suche nach Updates...")
            release_info = get_latest_release_info()
            remote_version = release_info.get("tag_name")
            zip_url = release_info.get("zipball_url")
            local_version, local_change = read_local_version(base_path)

            status_label.config(text=f"Lokal: {local_version or 'keine'} ({local_change or '---'}) | Server: {remote_version}")

            def version_tuple(v):
                return tuple(map(int, v.lstrip("v").split(".")))

            if local_version:
                try:
                    if version_tuple(remote_version) <= version_tuple(local_version) and not force:
                        messagebox.showinfo("Info", "Keine Aktualisierung notwendig.")
                        start_button.config(state="disabled")
                        return
                except Exception as e:
                    messagebox.showerror("Versionsvergleich fehlgeschlagen", f"Fehler beim Vergleich der Versionen:\n{e}")
                    start_button.config(state="disabled")
                    return

            if not messagebox.askyesno("Update", f"Neue Version {remote_version} installieren?"):
                return

            status_label.config(text="Lade Release...")
            zip_data = download_with_progress(zip_url, update_progress, update_status)

            status_label.config(text="Backup erstellen...")
            backup_existing_files(base_path)

            status_label.config(text="Dateien entpacken...")
            extract_zip_to_base(zip_data, base_path)

            now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            write_local_version(base_path, remote_version, now_str)

            status_label.config(text="Update abgeschlossen.")
            messagebox.showinfo("Fertig", "Update erfolgreich installiert.")
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    start_button = tk.Button(root, text="Update jetzt starten", command=lambda: threading.Thread(target=do_update).start())
    force_button = tk.Button(root, text="Update erzwingen", command=lambda: threading.Thread(target=lambda: do_update(force=True)).start())
    start_button.pack(pady=5)
    force_button.pack(pady=5)

    threading.Thread(target=do_update).start()

    root.mainloop()

if __name__ == "__main__":
    run_gui()