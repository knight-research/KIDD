# ALDL notes

Vehicle:
- 1991 Pontiac Firebird 3.1 V6
- Known working TunerPro/ALDL ScanTool definition: `A057.ads`

Adapter:
- 1320 Electronics LLC ALDL Bluetooth Adapter USB MK2
- Bluetooth name: `HC05`
- Bluetooth PIN: `1234`
- USB ID: `04d8:00dd` Microchip Technology

Protocol from `A057.ads`:
- Baud: `8192`
- Transmit Stream command: `F0 56 01`
- Command with checksum: `F0 56 01 B9`
- Payload bytes: `63`
- Bytes before payload: `3`

Test commands:

```bash
python tools/read_aldl.py --list-ports
python tools/read_aldl.py --port COM5 --once --raw
python tools/read_aldl.py --port /dev/ttyACM0 --once --raw
python tools/read_aldl.py --port /dev/rfcomm0 --once --raw
python tools/read_aldl.py --port /dev/ttyACM0
```

Bluetooth on Raspberry Pi normally has to be paired first. If it exposes a serial RFCOMM device, pass that device with `--port`, for example `/dev/rfcomm0`.
