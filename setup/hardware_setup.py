def _init_pcf8575(bus, address, board_index, relay_states_1to8, relay_states_9to16):
    relay_states_1to8[board_index] = 0xFF
    relay_states_9to16[board_index] = 0xFF
    hi = relay_states_9to16[board_index]
    lo = relay_states_1to8[board_index]
    bus.write_word_data(address, lo, hi)


def setup_hardware(sys_linux, sys_pi, btn_states_HW, device, device_names, dependencies):
    hardware = {
        "gps_serial": None,
        "gps_port": None,
        "i2cRB01": 0x20,  # DO POSIBBLE I2C: 20-27
        "i2cRB02": 0x21,  # DO POSIBBLE I2C: 20-27
        "i2cRB03": 0x22,  # DO POSIBBLE I2C: 20-27
        "i2cDI01": 0x64,  # DI POSIBBLE I2C: 64-78
        "i2cDI02": 0x65,  # DI POSIBBLE I2C: 64-78
        "i2cDI03": 0x66,  # DI POSIBBLE I2C: 64-78
        "i2cAI01": 0x00,  # AI POSIBBLE I2C: ?
        "buses": [],
        "i2c_dev02ai01": None,
        "ads": None,
        "i2c_dev02di01": None,
        "aw001": None,
        "i2c_dev02di02": None,
        "aw002": None,
    }
    hardware["i2c_addr_dev02rb"] = [
        hardware["i2cRB01"],
        hardware["i2cRB02"],
        hardware["i2cRB03"],
    ]
    hardware["relay_states_1to8"] = [0xFF for _ in hardware["i2c_addr_dev02rb"]]
    hardware["relay_states_9to16"] = [0xFF for _ in hardware["i2c_addr_dev02rb"]]

    serial = dependencies.get("serial")
    if btn_states_HW[0] == True and serial is not None:
        for port in serial.tools.list_ports.comports():
            if "ACM" in port.device or "COM" in port.device:
                try:
                    hardware["gps_serial"] = serial.Serial(port.device, 9600, timeout=1)
                    hardware["gps_port"] = port.device
                    hardware["gps_serial"].write(b'ATI\r\n')
                    response = hardware["gps_serial"].readline().decode("utf-8")
                    print(response)
                    if "u-blox" in response:
                        hardware["gps_serial"].timeout = 0
                        break
                except serial.SerialException:
                    print("no GPS")
                    break

    SMBus = dependencies.get("SMBus")
    if sys_pi and SMBus is not None:
        hardware["buses"] = [SMBus(1) for _ in hardware["i2c_addr_dev02rb"]]

    if sys_pi and sys_linux and btn_states_HW[0] == True and device == device_names[2]:
        for i, addr in enumerate(hardware["i2c_addr_dev02rb"]):
            if btn_states_HW[i]:
                _init_pcf8575(
                    hardware["buses"][i],
                    addr,
                    i,
                    hardware["relay_states_1to8"],
                    hardware["relay_states_9to16"],
                )

    board = dependencies.get("board")
    busio = dependencies.get("busio")
    ADS = dependencies.get("ADS")
    adafruit_aw9523 = dependencies.get("adafruit_aw9523")

    if sys_linux and btn_states_HW[6] == True and board is not None and busio is not None and ADS is not None:
        try:
            hardware["i2c_dev02ai01"] = busio.I2C(board.SCL, board.SDA)
            hardware["ads"] = ADS.ADS1115(hardware["i2c_dev02ai01"], address=hardware["i2cAI01"])
        except Exception:
            print("DEVICE AI01 NOT FOUND")

    if sys_linux and btn_states_HW[7] == True and board is not None and adafruit_aw9523 is not None:
        try:
            hardware["i2c_dev02di01"] = board.I2C()
            hardware["aw001"] = adafruit_aw9523.AW9523(hardware["i2c_dev02di01"], address=hardware["i2cDI01"])
        except Exception:
            print("DEVICE DI01 NOT FOUND")

    if sys_linux and btn_states_HW[8] == True and board is not None and adafruit_aw9523 is not None:
        try:
            hardware["i2c_dev02di02"] = board.I2C()
            hardware["aw002"] = adafruit_aw9523.AW9523(hardware["i2c_dev02di02"], address=hardware["i2cDI02"])
        except Exception:
            print("DEVICE DI02 NOT FOUND")

    return hardware
