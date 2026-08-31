import unittest
from pathlib import Path

from functions.aldl_reader import ALDLDefinition, aldl_checksum, with_checksum


class ALDLReaderTests(unittest.TestCase):
    def test_a057_header_and_request(self):
        definition = ALDLDefinition.from_ads(Path(__file__).resolve().parents[1] / "documents" / "aldl" / "A057.ads")

        self.assertEqual(definition.baud, 8192)
        self.assertEqual(definition.command, bytes([0xF0, 0x56, 0x01]))
        self.assertEqual(definition.request, bytes([0xF0, 0x56, 0x01, 0xB9]))
        self.assertEqual(definition.payload_size, 63)
        self.assertEqual(definition.bytes_before_payload, 3)

    def test_checksum_makes_sum_zero(self):
        request = with_checksum([0xF0, 0x56, 0x01])

        self.assertEqual(aldl_checksum([0xF0, 0x56, 0x01]), 0xB9)
        self.assertEqual(sum(request) & 0xFF, 0)

    def test_decodes_common_a057_values(self):
        definition = ALDLDefinition.from_ads(Path(__file__).resolve().parents[1] / "documents" / "aldl" / "A057.ads")
        payload = bytearray(63)
        payload[6] = 100
        payload[8] = 128
        payload[9] = 128
        payload[10] = 40
        payload[16] = 55
        payload[28] = 100
        payload[29] = 56
        payload[33] = 135

        values = definition.decode_payload(payload)

        self.assertAlmostEqual(values["aldl_coolant_temp"], 35.0)
        self.assertAlmostEqual(values["aldl_throttle_pos_v"], 2.509824, places=5)
        self.assertAlmostEqual(values["aldl_throttle_pos"], 50.196096, places=5)
        self.assertAlmostEqual(values["aldl_engine_speed"], 1000.0)
        self.assertEqual(values["aldl_vehicle_speed"], 55)
        self.assertAlmostEqual(values["aldl_map"], 47.254)
        self.assertAlmostEqual(values["aldl_mainfold_air_temp"], 20.0)
        self.assertAlmostEqual(values["aldl_battery_voltage"], 13.5)


if __name__ == "__main__":
    unittest.main()
