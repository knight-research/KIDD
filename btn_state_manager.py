import os
import json

class ButtonStateManager:
    def __init__(self, datadir):
        self.datadir = datadir
        self.filepath = os.path.join(datadir, "data", "btn_states.json")
        self._load()

    def _load(self):
        with open(self.filepath) as f:
            self.data = json.load(f)

    def save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.data, f, indent=4)

    def get_device(self):
        return self.data["main_config"].get("device", None)

    def get_style(self):
        return self.data["main_config"].get("style", None)

    def get_theme(self):
        return self.data["main_config"].get("theme", None)

    def get_system(self):
        return self.data["main_config"].get("system", None)

    def get_install_done(self):
        return self.data["main_config"].get("installdone", False)

    def set_install_done(self, value):
        self.data["main_config"]["installdone"] = value

    def get_button_states(self, dev, key):
        return self.data["buttons"].get(dev, {}).get(key, [])

    def set_button_states(self, dev, key, value):
        if dev in self.data["buttons"]:
            self.data["buttons"][dev][key] = value

    def get_odometer(self):
        return self.data["gps"].get("odo_metric_cnt_old", 0.0)

    def set_odometer(self, value):
        self.data["gps"]["odo_metric_cnt_old"] = value

    def get_current_button_states(self, key):
        dev = self.get_device()
        return self.get_button_states(dev, key)

    def set_current_button_states(self, key, value):
        dev = self.get_device()
        self.set_button_states(dev, key, value)

    def save_btn_states_HW(self, value):
        self.set_current_button_states("HW", value)
        self.save()

    def save_btn_states_SW(self, value):
        self.set_current_button_states("SW", value)
        self.save()

    def odometer_data(self, value):
        self.set_odometer(value)
        self.save()
        
    def get_config_value(self, key, fallback=None):
        return self.data.get("config", {}).get(key, fallback)

    def set_config_value(self, key, value):
        if "config" not in self.data:
            self.data["config"] = {}
        self.data["config"][key] = value
