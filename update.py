#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import datetime
import io
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import threading
import zipfile


def install_if_missing(module_name: str, package_name: str | None = None) -> None:
    try:
        __import__(module_name)
    except ImportError:
        print(f"Modul '{module_name}' nicht gefunden. Installiere...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name or module_name])


install_if_missing("requests")

import requests
import tkinter as tk
from tkinter import messagebox, ttk


GITHUB_REPO = "knight-research/KIDD"
BACKUP_PREFIX = "kidd.old"
VERSION_FILE = "version.txt"
INSTALL_DIR_NAME = "KIDD"
REQUEST_TIMEOUT = 30
CHUNK_SIZE = 1024 * 128

APP_ROOT = Path(__file__).resolve().parent
USER_AGENT = f"KIDD-Updater/{GITHUB_REPO}"


def get_latest_release_info() -> dict:
    url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.json()


def read_local_version(base_path: Path) -> tuple[str | None, str | None]:
    version_path = base_path / VERSION_FILE
    if not version_path.exists():
        return None, None

    lines = version_path.read_text(encoding="utf-8").splitlines()
    version = lines[0].strip() if len(lines) > 0 else None
    last_change = lines[1].strip() if len(lines) > 1 else None
    return version, last_change


def write_local_version(base_path: Path, version: str, last_change: str | None = None) -> None:
    version_path = base_path / VERSION_FILE
    lines = [version]
    if last_change:
        lines.append(last_change)
    version_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def default_install_path() -> Path:
    return Path.home() / INSTALL_DIR_NAME


def version_tuple(version: str | None) -> tuple[int, ...]:
    if not version:
        return ()
    return tuple(int(part) for part in re.findall(r"\d+", version))


def backup_existing_files(base_path: Path) -> Path:
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = base_path / f"{BACKUP_PREFIX}_{timestamp}"
    backup_path.mkdir()

    ignored_names = {
        Path(__file__).name,
        backup_path.name,
    }

    for item in base_path.iterdir():
        if item.name in ignored_names or item.name.startswith(BACKUP_PREFIX):
            continue
        shutil.move(str(item), str(backup_path / item.name))

    return backup_path


def backup_install_folder(install_path: Path) -> Path | None:
    if not install_path.exists():
        install_path.mkdir(parents=True, exist_ok=True)
        return None

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = install_path.parent / f"{BACKUP_PREFIX}_{timestamp}"
    shutil.move(str(install_path), str(backup_path))
    install_path.mkdir(parents=True, exist_ok=True)
    return backup_path


def download_with_progress(url: str, progress_callback=None, status_callback=None) -> bytes:
    response = requests.get(
        url,
        headers={"User-Agent": USER_AGENT},
        stream=True,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()

    total = int(response.headers.get("content-length", 0))
    downloaded = 0
    chunks: list[bytes] = []

    for data in response.iter_content(chunk_size=CHUNK_SIZE):
        if not data:
            continue
        chunks.append(data)
        downloaded += len(data)
        if total and progress_callback:
            progress_callback(int(downloaded * 100 / total))
        if status_callback:
            status_callback(f"{downloaded / 1024:.1f} KB heruntergeladen")

    return b"".join(chunks)


def is_safe_zip_member(target_path: Path, base_path: Path) -> bool:
    try:
        target_path.resolve().relative_to(base_path.resolve())
    except ValueError:
        return False
    return True


def extract_zip_to_base(zip_bytes: bytes, base_path: Path, include_sound: bool) -> None:
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as archive:
        top_level_folder = archive.namelist()[0].split("/")[0]
        for member in archive.infolist():
            if member.is_dir():
                continue

            member_path = Path(os.path.relpath(member.filename, top_level_folder))
            if member_path.parts and member_path.parts[0] == "..":
                continue
            if not include_sound and member_path.parts and member_path.parts[0] == "sound":
                continue

            target_path = base_path / member_path
            if not is_safe_zip_member(target_path, base_path):
                continue

            target_path.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(member) as source, target_path.open("wb") as target:
                shutil.copyfileobj(source, target)


def run_gui() -> None:
    base_path = APP_ROOT

    root = tk.Tk()
    include_sound = tk.BooleanVar(value=False)
    root.title("KIDD Updater")
    root.geometry("430x290")

    status_label = tk.Label(root, text="Initialisiere...", anchor="w")
    status_label.pack(fill="x", padx=10, pady=5)

    progress = ttk.Progressbar(root, orient="horizontal", length=320, mode="determinate")
    progress.pack(pady=5)

    byte_label = tk.Label(root, text="", anchor="w")
    byte_label.pack(fill="x", padx=10)

    sound_check = tk.Checkbutton(root, text="Sound-Ordner aktualisieren", variable=include_sound)
    sound_check.pack(pady=5)

    start_button = tk.Button(root, text="Update jetzt starten")
    force_button = tk.Button(root, text="Update erzwingen")
    install_button = tk.Button(root, text="KIDD komplett installieren")
    start_button.pack(pady=5)
    force_button.pack(pady=5)
    install_button.pack(pady=5)

    def on_ui(callback, *args, **kwargs) -> None:
        root.after(0, lambda: callback(*args, **kwargs))

    def set_status(text: str) -> None:
        on_ui(status_label.config, text=text)

    def set_download_status(text: str) -> None:
        on_ui(byte_label.config, text=text)

    def set_progress(percent: int) -> None:
        on_ui(progress.config, value=percent)

    def set_buttons_enabled(enabled: bool) -> None:
        state = "normal" if enabled else "disabled"
        on_ui(start_button.config, state=state)
        on_ui(force_button.config, state=state)
        on_ui(install_button.config, state=state)

    def show_info(title: str, text: str) -> None:
        on_ui(messagebox.showinfo, title, text)

    def show_error(title: str, text: str) -> None:
        on_ui(messagebox.showerror, title, text)

    def ask_yes_no(title: str, text: str) -> bool:
        answer = threading.Event()
        result = {"value": False}

        def ask() -> None:
            result["value"] = messagebox.askyesno(title, text)
            answer.set()

        root.after(0, ask)
        answer.wait()
        return result["value"]

    def do_update(force: bool = False) -> None:
        set_buttons_enabled(False)
        try:
            set_status("Suche nach Updates...")
            set_download_status("")
            set_progress(0)

            release_info = get_latest_release_info()
            remote_version = release_info.get("tag_name")
            zip_url = release_info.get("zipball_url")
            local_version, local_change = read_local_version(base_path)

            if not remote_version or not zip_url:
                raise RuntimeError("Release enthaelt keine Version oder keinen ZIP-Download.")

            set_status(f"Lokal: {local_version or 'keine'} ({local_change or '---'}) | Server: {remote_version}")

            if local_version and version_tuple(remote_version) <= version_tuple(local_version) and not force:
                show_info("Info", "Keine Aktualisierung notwendig.")
                return

            if not ask_yes_no("Update", f"Neue Version {remote_version} installieren?"):
                return

            set_status("Lade Release...")
            zip_data = download_with_progress(zip_url, set_progress, set_download_status)

            set_status("Backup erstellen...")
            backup_path = backup_existing_files(base_path)

            set_status("Dateien entpacken...")
            extract_zip_to_base(zip_data, base_path, include_sound.get())

            now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            write_local_version(base_path, remote_version, now_str)

            set_status(f"Update abgeschlossen. Backup: {backup_path.name}")
            show_info("Fertig", "Update erfolgreich installiert.")
        except Exception as exc:
            show_error("Fehler", str(exc))
        finally:
            set_buttons_enabled(True)

    def do_install() -> None:
        install_path = default_install_path()
        set_buttons_enabled(False)
        try:
            set_status("Suche GitHub Release...")
            set_download_status("")
            set_progress(0)

            release_info = get_latest_release_info()
            remote_version = release_info.get("tag_name")
            zip_url = release_info.get("zipball_url")

            if not remote_version or not zip_url:
                raise RuntimeError("Release enthaelt keine Version oder keinen ZIP-Download.")

            question = (
                f"KIDD {remote_version} komplett nach\n"
                f"{install_path}\n"
                "installieren? Ein vorhandener KIDD-Ordner wird vorher gesichert."
            )
            if not ask_yes_no("KIDD installieren", question):
                return

            set_status("Lade KIDD von GitHub...")
            zip_data = download_with_progress(zip_url, set_progress, set_download_status)

            set_status("Installationsordner vorbereiten...")
            if install_path.resolve() == base_path.resolve():
                backup_path = backup_existing_files(base_path)
            else:
                backup_path = backup_install_folder(install_path)

            set_status("KIDD installieren...")
            extract_zip_to_base(zip_data, install_path, include_sound.get())

            now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            write_local_version(install_path, remote_version, now_str)

            backup_text = f" Backup: {backup_path.name}" if backup_path else ""
            set_status(f"Installation abgeschlossen.{backup_text}")
            show_info("Fertig", f"KIDD wurde nach {install_path} installiert.")
        except Exception as exc:
            show_error("Fehler", str(exc))
        finally:
            set_buttons_enabled(True)

    def start_update(force: bool = False) -> None:
        thread = threading.Thread(target=lambda: do_update(force=force), daemon=True)
        thread.start()

    def start_install() -> None:
        thread = threading.Thread(target=do_install, daemon=True)
        thread.start()

    start_button.config(command=start_update)
    force_button.config(command=lambda: start_update(force=True))
    install_button.config(command=start_install)

    root.mainloop()


if __name__ == "__main__":
    run_gui()
