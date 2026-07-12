import copy
import json
import os


QUICKSOUND_MODES = ("LOOP", "1X", "AUTOPLAY")
QUICKSOUND_COLORS = ("AQ", "BU", "GN", "OR", "RD", "WH", "YE")
QUICKSOUND_COLOR_INDEX = {
    "AQ": 56,
    "BU": 57,
    "GN": 58,
    "OR": 59,
    "RD": 60,
    "WH": 61,
    "YE": 62,
}
DEFAULT_QUICKSOUND_CONFIG = [
    {"folder": "sfx", "file": "SCANNER_1x.mp3", "mode": "LOOP", "color": "YE"},
    {"folder": "sfx", "file": "STARTUP_001.mp3", "mode": "1X", "color": "YE"},
    {"folder": "notouch", "file": "NICHT_BERUEHREN_00.mp3", "mode": "1X", "color": "YE"},
    {"folder": "introduce", "file": "VORSTELLUNG_MITTEL.mp3", "mode": "1X", "color": "YE"},
]
DEFAULT_QUICKSOUND_SETTINGS = {
    "labels_visible": True,
}


def list_quicksound_folders(sound_root):
    if not sound_root or not os.path.isdir(sound_root):
        return []
    return [
        name
        for name in sorted(os.listdir(sound_root), key=str.lower)
        if os.path.isdir(os.path.join(sound_root, name))
    ]


def list_quicksound_files(sound_root, subfolder):
    folder_path = os.path.join(sound_root, subfolder)
    if not os.path.isdir(folder_path):
        return []
    return [
        name
        for name in sorted(os.listdir(folder_path), key=str.lower)
        if name.lower().endswith(".mp3")
    ]


def normalize_quicksound_config(config):
    normalized = copy.deepcopy(DEFAULT_QUICKSOUND_CONFIG)
    if not isinstance(config, list):
        return normalized

    for index, item in enumerate(config[:len(normalized)]):
        if not isinstance(item, dict):
            continue
        normalized[index]["folder"] = item.get("folder") or normalized[index]["folder"]
        normalized[index]["file"] = item.get("file") or normalized[index]["file"]
        mode = str(item.get("mode", normalized[index]["mode"])).upper()
        color = str(item.get("color", normalized[index]["color"])).upper()
        normalized[index]["mode"] = mode if mode in QUICKSOUND_MODES else normalized[index]["mode"]
        normalized[index]["color"] = color if color in QUICKSOUND_COLORS else normalized[index]["color"]

    autoplay_seen = False
    for item in normalized:
        if item["mode"] == "AUTOPLAY":
            if autoplay_seen:
                item["mode"] = "1X"
            autoplay_seen = True
    return normalized


def normalize_quicksound_settings(settings):
    normalized = copy.deepcopy(DEFAULT_QUICKSOUND_SETTINGS)
    if isinstance(settings, dict):
        normalized["labels_visible"] = bool(settings.get("labels_visible", normalized["labels_visible"]))
    return normalized


def load_quicksound_config(datadir):
    with open(os.path.join(datadir, "btn_states.json"), encoding="utf-8") as f:
        data = json.load(f)
    return normalize_quicksound_config(data.get("quicksound_config"))


def load_quicksound_settings(datadir):
    with open(os.path.join(datadir, "btn_states.json"), encoding="utf-8") as f:
        data = json.load(f)
    return normalize_quicksound_settings(data.get("quicksound_settings"))


def save_quicksound_config(datadir, config):
    path = os.path.join(datadir, "btn_states.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    data["quicksound_config"] = normalize_quicksound_config(config)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def save_quicksound_settings(datadir, settings):
    path = os.path.join(datadir, "btn_states.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    data["quicksound_settings"] = normalize_quicksound_settings(settings)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
