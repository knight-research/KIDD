import json
import tempfile
import unittest
from pathlib import Path

from functions.btn_state_manager import ButtonStateManager
from setup.config_state import load_config_state_symbols
from setup.platform_detection import detect_platform
from setup.style_config import load_style_symbols
from functions.text_lists import load_text_list_symbols
from functions.quicksound_config import (
    QUICKSOUND_COLORS,
    list_quicksound_files,
    list_quicksound_folders,
    normalize_quicksound_settings,
    normalize_quicksound_config,
)


class SmokeTests(unittest.TestCase):
    def test_platform_detection_shape(self):
        flags = detect_platform()

        self.assertEqual(len(flags), 3)
        self.assertTrue(all(isinstance(flag, bool) for flag in flags))

    def test_text_config_and_style_loaders(self):
        datadir = Path(__file__).resolve().parents[1] / "data"

        text_symbols = load_text_list_symbols(str(datadir))
        config_symbols = load_config_state_symbols(str(datadir))
        style_symbols = load_style_symbols(
            config_symbols["device"],
            config_symbols["style"],
            config_symbols["system"],
            text_symbols["DEVICE_B_txt"],
            text_symbols["STYLE_B_txt"],
            text_symbols["SYS_B_txt"],
        )

        self.assertIn("MENU_B_txt", text_symbols)
        self.assertIn("btn_states_HW", config_symbols)
        self.assertIn("kidd_width", style_symbols)

    def test_button_state_manager_writes_odo_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            data_dir = Path(tmp) / "data"
            data_dir.mkdir()
            state_path = data_dir / "btn_states.json"
            state_path.write_text(
                json.dumps(
                    {
                        "main_config": {
                            "device": "DEV001",
                            "style": "KITT",
                            "theme": "K2_S05",
                            "system": "GREEN",
                        },
                        "buttons": {"DEV001": {"HW": [], "SW": []}},
                        "gps": {"odo_metric_cnt_old": 0.0},
                        "odo_config": {"odo_trip_gps_metric": 1.0},
                        "config": {},
                    }
                ),
                encoding="utf-8",
            )

            manager = ButtonStateManager(tmp)
            manager.set_odo_value("odo_trip_gps_metric", 12.5)
            manager.save()

            saved = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual(saved["odo_config"]["odo_trip_gps_metric"], 12.5)
            self.assertNotIn("odo_trip_gps_metric", saved["config"])

    def test_quicksound_config_normalizes_invalid_values(self):
        config = normalize_quicksound_config([
            {"folder": "sfx", "file": "A.mp3", "mode": "bad", "color": "bad"},
            {"mode": "loop", "color": "aq"},
            {"mode": "autoplay"},
            {"mode": "autoplay"},
        ])

        self.assertEqual(config[0]["file"], "A.mp3")
        self.assertEqual(config[0]["mode"], "LOOP")
        self.assertEqual(config[0]["color"], "YE")
        self.assertEqual(config[1]["mode"], "LOOP")
        self.assertEqual(config[1]["color"], "AQ")
        self.assertEqual(config[2]["mode"], "AUTOPLAY")
        self.assertEqual(config[3]["mode"], "1X")

    def test_quicksound_colors_include_all_led_button_colors(self):
        self.assertEqual(QUICKSOUND_COLORS, ("AQ", "BU", "GN", "OR", "RD", "WH", "YE"))

    def test_quicksound_settings_normalize_label_visibility(self):
        self.assertEqual(normalize_quicksound_settings({})["labels_visible"], True)
        self.assertEqual(normalize_quicksound_settings({"labels_visible": False})["labels_visible"], False)

    def test_quicksound_lists_sound_folders_and_mp3_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "sfx").mkdir()
            (root / "sfx" / "B.mp3").write_text("", encoding="utf-8")
            (root / "sfx" / "A.MP3").write_text("", encoding="utf-8")
            (root / "sfx" / "ignore.txt").write_text("", encoding="utf-8")
            (root / "voice").mkdir()

            self.assertEqual(list_quicksound_folders(str(root)), ["sfx", "voice"])
            self.assertEqual(list_quicksound_files(str(root), "sfx"), ["A.MP3", "B.mp3"])


if __name__ == "__main__":
    unittest.main()
