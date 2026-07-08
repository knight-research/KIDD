import unittest

from functions.favorite_manager import (
    build_qopt_favorites,
    favorite_label,
    favorite_limit,
    favorite_status,
    favorite_target,
)


DEVICE_NAMES = ["ALL", "DEV001", "DEV002", "DEV003"]
STATE_TEXTS = ["OFF", "ON"]


class FavoriteManagerTests(unittest.TestCase):
    def test_dev001_favorites_are_limited_to_hw_and_sw(self):
        fav_states = [False] * 30
        fav_states[1] = True
        fav_states[20] = True
        limit = favorite_limit("DEV001", DEVICE_NAMES, [False] * 10, [False] * 10)

        favorites = build_qopt_favorites(
            fav_states,
            limit,
            lambda index: favorite_label(index, "DEV001", DEVICE_NAMES, [f"HW{n}" for n in range(10)], [f"SW{n}" for n in range(10)]),
        )

        self.assertEqual(favorites, [{"fav_index": 1, "label": "HW1"}])

    def test_dev002_favorites_include_relay_labels(self):
        fav_states = [False] * 40
        fav_states[20] = True
        limit = favorite_limit("DEV002", DEVICE_NAMES, [False] * 10, [False] * 10, ["RB01-0"], ["RB02-0"], ["RB03-0"])

        favorites = build_qopt_favorites(
            fav_states,
            limit,
            lambda index: favorite_label(
                index,
                "DEV002",
                DEVICE_NAMES,
                [f"HW{n}" for n in range(10)],
                [f"SW{n}" for n in range(10)],
                ["RB01-0"],
                ["RB02-0"],
                ["RB03-0"],
            ),
        )

        self.assertEqual(favorites, [{"fav_index": 20, "label": "RB01-0"}])

    def test_favorite_target_maps_to_original_function(self):
        self.assertEqual(favorite_target(2, "DEV001", DEVICE_NAMES, [False] * 10, [False] * 10), ("HW", 2))
        self.assertEqual(favorite_target(12, "DEV001", DEVICE_NAMES, [False] * 10, [False] * 10), ("SW", 2))
        self.assertEqual(favorite_target(20, "DEV002", DEVICE_NAMES, [False] * 10, [False] * 10), ("RELAY", 0))
        self.assertEqual(favorite_target(20, "DEV001", DEVICE_NAMES, [False] * 10, [False] * 10), ("UNKNOWN", 20))

    def test_favorite_status_uses_source_state(self):
        self.assertEqual(
            favorite_status(0, "DEV001", DEVICE_NAMES, STATE_TEXTS, [True], [False], ["SW ON"], ["SW OFF"]),
            "ON",
        )
        self.assertEqual(
            favorite_status(1, "DEV001", DEVICE_NAMES, STATE_TEXTS, [False], [False], ["SW ON"], ["SW OFF"]),
            "SW OFF",
        )
        self.assertEqual(
            favorite_status(20, "DEV002", DEVICE_NAMES, STATE_TEXTS, [False] * 10, [False] * 10, [], [], [0xFE], [0xFF]),
            "ON",
        )


if __name__ == "__main__":
    unittest.main()
