import os

from functions.image_loader import LazyImageList


IMAGE_PATHS = {
    "bgDEV001": ("000_bg", "DEV001"),
    "bgDEV001_DASH": ("000_bg", "DEV001", "DASH"),
    "bgDEV002": ("000_bg", "DEV002"),
    "bgDEV002_DASH": ("000_bg", "DEV002", "DASH"),
    "bgDEV004": ("000_bg", "DEV004"),
    "bgDEV004_DASH": ("000_bg", "DEV004", "DASH"),
    "bgDEV008": ("000_bg", "DEV008"),
    "bgDEV008_DASH": ("000_bg", "DEV008", "DASH"),
    "ledOF": ("001_led", "000_OFF"),
    "ledLO": ("001_led", "001_LOW"),
    "ledMI": ("001_led", "002_MID"),
    "ledFU": ("001_led", "003_FUL"),
    "sledOF": ("002_sled", "OFF"),
    "sledON": ("002_sled", "ON"),
    "vbOF_MAX": ("003_vb", "MAX", "OFF"),
    "vbON_MAX": ("003_vb", "MAX", "ON"),
    "vbOF_OTTO": ("003_vb", "OTTO", "OFF"),
    "vbON_OTTO": ("003_vb", "OTTO", "ON"),
    "vbOF_PILOT": ("003_vb", "PILOT", "OFF"),
    "vbON_PILOT": ("003_vb", "PILOT", "ON"),
    "vbOF_S01": ("003_vb", "S01", "OFF"),
    "vbON_S01": ("003_vb", "S01", "ON"),
    "vbOF_S02": ("003_vb", "S02", "OFF"),
    "vbON_S02": ("003_vb", "S02", "ON"),
    "vbOF_S03": ("003_vb", "S03", "OFF"),
    "vbON_S03": ("003_vb", "S03", "ON"),
    "vbOF_S04": ("003_vb", "S04", "OFF"),
    "vbON_S04": ("003_vb", "S04", "ON"),
    "bttf": ("bttf",),
    "infocenterOF": ("infocenter", "OFF"),
    "infocenterON": ("infocenter", "ON"),
    "knight": ("knight",),
    "lcarsOF": ("lcars", "OFF"),
    "lcarsON": ("lcars", "ON"),
    "lcarsOF_R": ("lcars", "OFF_R"),
    "lcarsON_R": ("lcars", "ON_R"),
    "rpmOF": ("rpm", "OFF"),
    "rpmON": ("rpm", "ON"),
    "segmentKA": ("segment", "KA"),
    "segmentKI": ("segment", "KI"),
    "sysnew": ("sys_new",),
}


def load_image_path_symbols(folder):
    symbols = {}
    image_root = os.path.join(folder, "images")

    for name, parts in IMAGE_PATHS.items():
        image_dir = os.path.join(image_root, *parts)
        suffix = ".jpg" if name.startswith("bgDEV") else ".png"
        symbols[f"{name}_img_dir"] = image_dir
        symbols[f"{name}_img_dir_srt"] = sorted(os.listdir(image_dir), key=str.lower)
        symbols[f"{name}_img_list"] = LazyImageList(image_dir, suffix)

    return symbols
