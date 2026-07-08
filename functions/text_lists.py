import json
import os


def load_text_list_symbols(datadir):
    with open(os.path.join(datadir, "textlist.json"), encoding="utf-8") as f:
        textdata = json.load(f)

    all_devices = textdata["ALL_DEVICES"]
    config = all_devices["CONFIG"]
    devices = textdata["DEVICES"]

    dev001 = devices.get("DEV001", {})
    dev002 = devices.get("DEV002", {})
    gau001 = dev001.get("GAUGES", {})
    gau002 = dev002.get("GAUGES", {})
    inputs002 = dev002.get("INPUTS", {})

    return {
        "MENU_B_txt": all_devices["PAGES"],
        "DEVICE_B_txt": config["devices"],
        "STYLE_B_txt": config["styles"],
        "THEME_B_txt": config["themes"],
        "SYS_B_txt": config["systems"],
        "btn_SELECT_txt": all_devices["btn_SELECT_txt"],
        "FNKT_B_txt": all_devices["FNKT_B_NAMES"],
        "units_eu": all_devices["UNITS"]["eu"],
        "units_us": all_devices["UNITS"]["us"],
        "states_txt_de": all_devices["STATES"]["de"],
        "states_txt_en": all_devices["STATES"]["en"],
        "sysinfo01_txt": all_devices["SYSINFO_KEYS"]["group01"],
        "sysinfo02_txt": all_devices["SYSINFO_KEYS"]["group02"],
        "voicecmd_txt": all_devices["VOICECMDS"],
        "btnhw_DEV001_txt": dev001.get("BTN_HW", []),
        "lbl_btnsw_DEV001_txt": dev001.get("LBL_SW", []),
        "btnsw_DEV001_txt_0": dev001.get("BTN_SW_0", []),
        "btnsw_DEV001_txt_1": dev001.get("BTN_SW_1", []),
        "btnsw_DEV001_txt_3": dev001.get("BTN_SW_3", []),
        "msg_center_S01_txt": dev001.get("MSG_CENTER_S01", []),
        "gau_S01U01_txt": gau001.get("S01", []),
        "gau_S02U01_txt": gau001.get("S02", []),
        "gau_S03U01_txt": gau001.get("S03", []),
        "gau_S04U01_txt": gau001.get("S04", []),
        "gau_S05U01_txt": gau001.get("S05", []),
        "gau_S06U01_txt": gau001.get("S06", []),
        "gau_KR3KU01_txt": gau001.get("KR3K", []),
        "btnhw_DEV002_txt": dev002.get("BTN_HW", []),
        "lbl_btnsw_DEV002_txt": dev002.get("LBL_SW", []),
        "btnsw_DEV002_txt_0": dev002.get("BTN_SW_0", []),
        "btnsw_DEV002_txt_1": dev002.get("BTN_SW_1", []),
        "btnsw_DEV002_txt_3": dev002.get("BTN_SW_3", []),
        "gau_S01U02_txt": gau002.get("S01", []),
        "gau_S02U02_txt": gau002.get("S02", []),
        "gau_S03U02_txt": gau002.get("S03", []),
        "gau_S04U02_txt": gau002.get("S04", []),
        "gau_S05U02_txt": gau002.get("S05", []),
        "gau_S06U02_txt": gau002.get("S06", []),
        "ib01_DEV002_txt": inputs002.get("IB01", []),
        "ib02_DEV002_txt": inputs002.get("IB02", []),
        "ib03_DEV002_txt": inputs002.get("IB03", []),
        "rb01_DEV002_txt": inputs002.get("RB01", []),
        "rb02_DEV002_txt": inputs002.get("RB02", []),
        "rb03_DEV002_txt": inputs002.get("RB03", []),
        "vcmd_de": ["Habe dich gehoert", "2"],
        "vcmd_en": ["I heard you", "2"],
    }