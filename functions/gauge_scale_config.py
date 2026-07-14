import copy
import json
import os


DEFAULT_GAUGE_SCALE = {
    "DEV001": [
        {"key": "speed", "label": "SPEED", "min": 0, "max": 310, "step": 5},
        {"key": "signal", "label": "SIGNAL", "min": 0, "max": 100, "step": 5},
        {"key": "tuning", "label": "TUNING", "min": 0, "max": 200, "step": 5},
    ],
    "DEV002": [
        {"key": "rpm", "label": "RPM", "min": 0, "max": 990, "step": 10},
        {"key": "inlet", "label": "INLET", "min": 0, "max": 160, "step": 5},
        {"key": "oil_1", "label": "OIL 1", "min": 0, "max": 160, "step": 5},
        {"key": "egt", "label": "EGT", "min": 0, "max": 160, "step": 5},
        {"key": "oil_2", "label": "OIL 2", "min": 0, "max": 160, "step": 5},
        {"key": "fuel", "label": "FUEL", "min": 0, "max": 57, "step": 1},
        {"key": "tps", "label": "TPS", "min": 0, "max": 160, "step": 5},
        {"key": "vdc", "label": "VDC", "min": 0, "max": 600, "step": 5},
        {"key": "fuel_pump", "label": "FUEL PMP", "min": 0, "max": 150, "step": 5},
        {"key": "tps_v", "label": "TPS V", "min": 0, "max": 100, "step": 5},
    ],
}

_CACHE = {"path": None, "data": None}
_REVISION = 0


def _state_path(datadir):
    return os.path.join(datadir, "btn_states.json")


def _read_state(datadir):
    with open(_state_path(datadir), encoding="utf-8") as f:
        return json.load(f)


def _write_state(datadir, data):
    global _REVISION
    with open(_state_path(datadir), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    _CACHE.update({"path": None, "data": None})
    _REVISION += 1


def _merged_scale(data):
    scale = copy.deepcopy(DEFAULT_GAUGE_SCALE)
    saved = data.get("gauge_scale", {})
    for device, rows in saved.items():
        if device not in scale or not isinstance(rows, list):
            continue
        by_key = {row["key"]: row for row in scale[device]}
        for row in rows:
            if not isinstance(row, dict):
                continue
            key = row.get("key")
            if key in by_key:
                by_key[key].update({k: row[k] for k in ("min", "max", "step") if k in row})
    return scale


def load_gauge_scale(datadir):
    path = _state_path(datadir)
    if _CACHE["path"] == path and _CACHE["data"] is not None:
        return _CACHE["data"]
    data = _read_state(datadir)
    scale = _merged_scale(data)
    _CACHE.update({"path": path, "data": scale})
    return scale


def get_gauge_scale_revision():
    return _REVISION


def ensure_gauge_scale_config(datadir):
    data = _read_state(datadir)
    merged = _merged_scale(data)
    if data.get("gauge_scale") != merged:
        data["gauge_scale"] = merged
        _write_state(datadir, data)
    return merged


def get_gauge_scale_lists(datadir, device, default_min, default_max):
    rows = load_gauge_scale(datadir).get(device, [])
    mins = list(default_min)
    maxs = list(default_max)
    for index, row in enumerate(rows[: len(maxs)]):
        try:
            minimum = float(row.get("min", mins[index]))
            maximum = float(row.get("max", maxs[index]))
        except (TypeError, ValueError):
            continue
        if maximum > minimum:
            mins[index] = int(minimum) if minimum.is_integer() else minimum
            maxs[index] = int(maximum) if maximum.is_integer() else maximum
    return mins, maxs


def save_gauge_scale_value(datadir, device, key, field, value):
    data = _read_state(datadir)
    data["gauge_scale"] = _merged_scale(data)
    for row in data["gauge_scale"].get(device, []):
        if row.get("key") == key and field in ("min", "max"):
            row[field] = value
            _write_state(datadir, data)
            return row
    raise KeyError(f"Unknown gauge scale {device}.{key}.{field}")
