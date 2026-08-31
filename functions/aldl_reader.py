import argparse
import re
import time
from dataclasses import dataclass
from pathlib import Path


def aldl_checksum(data):
    return (-sum(data)) & 0xFF


def with_checksum(data):
    payload = bytes(data)
    return payload + bytes([aldl_checksum(payload)])


@dataclass
class ALDLValueDefinition:
    key: str
    title: str
    unit: str
    byte_number: int
    size_bits: int
    operation: int
    factor: float
    offset: float
    lookup_index: int


class ALDLDefinition:
    def __init__(self, baud, command, payload_size, bytes_before_payload, values, lookups):
        self.baud = baud
        self.command = command
        self.payload_size = payload_size
        self.bytes_before_payload = bytes_before_payload
        self.values = values
        self.lookups = lookups

    @classmethod
    def from_ads(cls, path):
        text = Path(path).read_text(encoding="utf-8", errors="replace")
        blocks = re.findall(r"\{(.*?)\}", text, re.S)
        header = next((block for block in blocks if "iBaud" in block and "rgbtCommand" in block), "")

        def get(block, name, default=""):
            match = re.search(rf"{name}\s*=([^;]*);", block)
            return match.group(1).strip() if match else default

        baud = int(get(header, "iBaud", "8192"))
        command = bytes(int(part.strip(), 16) for part in get(header, "rgbtCommand").split(",") if part.strip())
        payload_size = int(get(header, "iNumBytesInPayload", "0"))
        bytes_before_payload = int(get(header, "iNumBytesBeforePayload", "0"))

        values = []
        for block in blocks:
            if "dwItemType               =1;" not in block:
                continue
            title = get(block, "strItemTitle")
            values.append(
                ALDLValueDefinition(
                    key=_key_from_title(title),
                    title=title,
                    unit=get(block, "strUnitLabel"),
                    byte_number=int(get(block, "btByteNumber", "0")),
                    size_bits=int(get(block, "dwItemSizeBits", "8")),
                    operation=int(get(block, "dwOperation", "0")),
                    factor=float(get(block, "dFactor", "1")),
                    offset=float(get(block, "dOffset", "0")),
                    lookup_index=int(get(block, "iLookupTableIndex", "-1")),
                )
            )

        lookups = {}
        for block in blocks:
            if "dwItemType               =5;" not in block:
                continue
            lookup_id = int(get(block, "dwUniqueID", "-1"))
            points = [(int(raw), float(value)) for raw, value in re.findall(r"(\d+)\s*,\s*(-?\d+(?:\.\d+)?)", block)]
            if lookup_id >= 0 and points:
                lookups[lookup_id] = sorted(points)

        return cls(baud, command, payload_size, bytes_before_payload, values, lookups)

    @property
    def request(self):
        return with_checksum(self.command)

    @property
    def expected_frame_size(self):
        return self.bytes_before_payload + self.payload_size

    def decode_frame(self, frame):
        frame = bytes(frame)
        if len(frame) >= self.expected_frame_size:
            payload = frame[self.bytes_before_payload:self.bytes_before_payload + self.payload_size]
        else:
            payload = frame
        return self.decode_payload(payload)

    def decode_payload(self, payload):
        payload = bytes(payload)
        decoded = {}
        for item in self.values:
            value = self._decode_item(payload, item)
            if value is not None:
                decoded[item.key] = value
                decoded[f"{item.key}_unit"] = item.unit
        return decoded

    def _decode_item(self, payload, item):
        index = item.byte_number - 1
        if index < 0 or index >= len(payload):
            return None
        if item.size_bits == 16:
            if index + 1 >= len(payload):
                return None
            raw = (payload[index] << 8) | payload[index + 1]
        else:
            raw = payload[index]

        if item.operation == 6 and item.lookup_index in self.lookups:
            return _lookup_value(self.lookups[item.lookup_index], raw)
        if item.operation in (0, 1, 2):
            return raw * item.factor + item.offset
        return raw


class ALDLReader:
    def __init__(self, definition, port=None, timeout=0.15):
        self.definition = definition
        self.port = port
        self.timeout = timeout
        self.serial = None

    def open(self):
        import serial

        port = self.port or find_aldl_port()
        if not port:
            raise RuntimeError("No ALDL serial port found. Pass --port COMx or /dev/rfcomm0.")
        self.serial = serial.Serial(port, self.definition.baud, timeout=0, write_timeout=1)
        self.port = port
        return port

    def close(self):
        if self.serial is not None:
            self.serial.close()
            self.serial = None

    def request_frame(self):
        if self.serial is None:
            self.open()
        self.serial.reset_input_buffer()
        self.serial.write(self.definition.request)
        return self._read_frame()

    def read_values(self):
        frame = self.request_frame()
        return frame, self.definition.decode_frame(frame)

    def _read_frame(self):
        expected = self.definition.expected_frame_size
        deadline = time.monotonic() + self.timeout
        buffer = bytearray()
        while time.monotonic() < deadline:
            chunk = self.serial.read(max(1, expected - len(buffer)))
            if chunk:
                buffer.extend(chunk)
                if len(buffer) >= expected:
                    return bytes(buffer[-expected:])
            else:
                time.sleep(0.002)
        return bytes(buffer)


def find_aldl_port():
    import serial.tools.list_ports

    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        vid = getattr(port, "vid", None)
        pid = getattr(port, "pid", None)
        if vid == 0x04D8 and pid == 0x00DD:
            return port.device
    for port in ports:
        text = " ".join(str(part or "") for part in (port.device, port.description, port.manufacturer, port.hwid)).lower()
        if any(token in text for token in ("aldl", "microchip", "hc-05", "bluetooth")):
            return port.device
    return None


def list_serial_ports():
    import serial.tools.list_ports

    return list(serial.tools.list_ports.comports())


def _lookup_value(points, raw):
    if raw <= points[0][0]:
        return points[0][1]
    if raw >= points[-1][0]:
        return points[-1][1]
    for (raw_a, value_a), (raw_b, value_b) in zip(points, points[1:]):
        if raw_a <= raw <= raw_b:
            if raw_a == raw_b:
                return value_b
            ratio = (raw - raw_a) / (raw_b - raw_a)
            return value_a + ((value_b - value_a) * ratio)
    return float(raw)


def _key_from_title(title):
    key = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
    aliases = {
        "engine_speed": "aldl_engine_speed",
        "vehicle_speed": "aldl_vehicle_speed",
        "coolant_temp_c": "aldl_coolant_temp",
        "tps_volts": "aldl_throttle_pos_v",
        "tps": "aldl_throttle_pos",
        "map_kpa": "aldl_map",
        "mat_c": "aldl_mainfold_air_temp",
        "fuel_pump_voltage": "aldl_fuel_pump_voltage",
        "battery_voltage": "aldl_battery_voltage",
        "spark_advance": "aldl_spark_advance_rel_to_ref_pulse",
        "bpw": "aldl_injector_base_pulse_width",
        "egr_duty_cycle": "aldl_duty_cycle",
        "knock_retard": "aldl_knock_retard",
        "engine_runtime": "aldl_engine_run_time",
        "knock_counter": "aldl_knock_counter",
        "o2_sensor": "aldl_oxygen_sensor",
        "rich_lean_transitions": "aldl_o2_cross_counts",
        "blm": "aldl_block_learn_BLM",
        "blm_cell": "aldl_bl_cell",
        "int": "aldl_integrator_int",
        "iac_position": "aldl_iac_motor_pos",
        "desired_idle_speed": "aldl_desired_idle_speed",
        "barometric_kpa": "aldl_barometric_pressure",
    }
    return aliases.get(key, f"aldl_{key}" if not key.startswith("aldl_") else key)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Read GM ALDL data with a TunerPro ADS definition.")
    parser.add_argument("--ads", default=str(Path("documents") / "aldl" / "A057.ads"))
    parser.add_argument("--port", default=None, help="Serial port, for example COM5, /dev/ttyACM0 or /dev/rfcomm0.")
    parser.add_argument("--list-ports", action="store_true")
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--interval", type=float, default=0.25)
    parser.add_argument("--timeout", type=float, default=0.15)
    parser.add_argument("--raw", action="store_true")
    args = parser.parse_args(argv)

    if args.list_ports:
        for port in list_serial_ports():
            print(f"{port.device}\t{port.description}\t{port.hwid}")
        return 0

    definition = ALDLDefinition.from_ads(args.ads)
    reader = ALDLReader(definition, args.port, args.timeout)
    port = reader.open()
    print(f"[ALDL] port={port} baud={definition.baud} request={definition.request.hex(' ').upper()} expected={definition.expected_frame_size}")
    try:
        while True:
            frame, values = reader.read_values()
            if args.raw:
                print(f"[ALDL] raw({len(frame)}): {frame.hex(' ').upper()}")
            print(
                "[ALDL] "
                f"rpm={values.get('aldl_engine_speed', 0):.0f} "
                f"mph={values.get('aldl_vehicle_speed', 0):.0f} "
                f"kph={values.get('aldl_vehicle_speed', 0) * 1.609344:.0f} "
                f"coolant={values.get('aldl_coolant_temp', 0):.1f}C "
                f"tps={values.get('aldl_throttle_pos', 0):.1f}% "
                f"map={values.get('aldl_map', 0):.1f}kPa "
                f"mat={values.get('aldl_mainfold_air_temp', 0):.1f}C "
                f"bat={values.get('aldl_battery_voltage', 0):.1f}V"
            )
            if args.once:
                break
            time.sleep(args.interval)
    finally:
        reader.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
