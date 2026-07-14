import json
import os


def load_config_state_symbols(datadir):
    with open(os.path.join(datadir, "btn_states.json"), encoding="utf-8") as f:
        data = json.load(f)
    with open(os.path.join(datadir, "textlist.json"), encoding="utf-8") as f:
        textdata = json.load(f)

    device = data["main_config"]["device"]
    states = textdata["ALL_DEVICES"]["STATES"]
    symbols = {
        "data": data,
        "device": device,
        "style": data["main_config"]["style"],
        "theme": data["main_config"]["theme"],
        "system": data["main_config"]["system"],
        "odo_trip_gps_imperial_old": data["odo_config"]["odo_trip_gps_imperial"],
        "odo_trip_gps_metric_old": data["odo_config"]["odo_trip_gps_metric"],
        "odo_total_gps_imperial_old": data["odo_config"]["odo_total_gps_imperial"],
        "odo_total_gps_metric_old": data["odo_config"]["odo_total_gps_metric"],
        "odo_trip_aldl_imperial_old": data["odo_config"]["odo_trip_aldl_imperial"],
        "odo_trip_aldl_metric_old": data["odo_config"]["odo_trip_aldl_metric"],
        "odo_total_aldl_imperial_old": data["odo_config"]["odo_total_aldl_imperial"],
        "odo_total_aldl_metric_old": data["odo_config"]["odo_total_aldl_metric"],
        "btns": data["buttons"],
        "btn_states_DEV002RB01": [False] * 16,
        "btn_states_DEV002RB02": [False] * 16,
        "btn_states_DEV002RB03": [False] * 16,
    }

    if device in symbols["btns"]:
        btn_states = symbols["btns"][device]
        btn_states_SW = btn_states["SW"]
        symbols.update({
            "btn_states_PB": btn_states["PB"],
            "btn_states_PBFNKT": btn_states["PBFNKT"],
            "btn_states_FNKT": btn_states["FNKT"],
            "btn_states_HW": btn_states["HW"],
            "btn_states_SW": btn_states_SW,
            "btn_states_qopt": btn_states["QOPT"],
            "btn_states_FAV": btn_states["FAV"],
            "states_txt_act": states["en"] if btn_states_SW[4] else states["de"],
        })
    else:
        print(f" Unbekanntes Gerät: {device}")

    return symbols
