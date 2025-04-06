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


def get_latest_release_info():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def read_local_version(base_path):
    version_path = os.path.join(base_path, VERSION_FILE)
    if os.path.exists(version_path):
        with open(version_path, "r") as f:
            return f.read().strip()
    return None


def write_local_version(base_path, version):
    version_path = os.path.join(base_path, VERSION_FILE)
    with open(version_path, "w") as f:
        f.write(version)


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
            target_path = os.path.join(base_path, member_path)
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with z.open(member) as source, open(target_path, "wb") as target:
                shutil.copyfileobj(source, target)


def run_gui():
    base_path = os.path.dirname(os.path.abspath(__file__))

    root = tk.Tk()
    root.title("KIDD Updater")
    root.geometry("400x200")

    status_label = tk.Label(root, text="Initialisiere...", anchor="w")
    status_label.pack(fill="x", padx=10, pady=5)

    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=5)

    byte_label = tk.Label(root, text="", anchor="w")
    byte_label.pack(fill="x", padx=10)

    def update_progress(percent):
        progress["value"] = percent
        root.update_idletasks()

    def update_status(text):
        byte_label.config(text=text)
        root.update_idletasks()

    def do_update():
        try:
            status_label.config(text="Suche nach Updates...")
            release_info = get_latest_release_info()
            remote_version = release_info.get("tag_name")
            zip_url = release_info.get("zipball_url")
            local_version = read_local_version(base_path)

            status_label.config(text=f"Lokal: {local_version or 'keine'} | Neu: {remote_version}")

            if local_version == remote_version:
                messagebox.showinfo("Info", "Keine Aktualisierung notwendig.")
                return

            if not messagebox.askyesno("Update", f"Neue Version {remote_version} installieren?"):
                return

            status_label.config(text="Lade Release...")
            zip_data = download_with_progress(zip_url, update_progress, update_status)

            status_label.config(text="Backup erstellen...")
            backup_existing_files(base_path)

            status_label.config(text="Dateien entpacken...")
            extract_zip_to_base(zip_data, base_path)

            write_local_version(base_path, remote_version)
            status_label.config(text="Update abgeschlossen.")
            messagebox.showinfo("Fertig", "Update erfolgreich installiert.")
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    start_button = tk.Button(root, text="Update jetzt starten", command=lambda: threading.Thread(target=do_update).start())
    start_button.pack(pady=10)

    threading.Thread(target=do_update).start()

    root.mainloop()


if __name__ == "__main__":
    run_gui()
