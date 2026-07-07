from pages.page_context import sync_context, update_context
from image_loader import LazyImageList

sync_context(globals())

#------------------------------------------------------------------------------------------
# PAGE 00: BOOT
#------------------------------------------------------------------------------------------
class P00_BOOT(tk.Frame):
    _loaded_count = 0
    _total_count = 0  # wird dynamisch gezÃƒÆ’Ã‚Â¤hlt
    def __init__(self, master):
        sync_context(globals())
        P00_BOOT._loaded_count = 0
        P00_BOOT._total_count = sum([
            2,  # background (normal + dash)
            4,  # led (OF, LO, MI, FU)
            2,  # sled
            14, # voiceboxes
            14   # misc (segment, lcars, rpm)
        ])
        super().__init__(master)
        global device, style, theme, system
        global btn_states_PB, btn_states_PBFNKT, btn_states_FNKT, btn_states_HW, btn_states_SW, btn_states_qopt, btn_states_FAV
        global bgDEV001_img_list, bgDEV002_img_list, bgDEV004_img_list, bgDEV008_img_list
        global bgDEV001_DASH_img_list, bgDEV002_DASH_img_list, bgDEV004_DASH_img_list, bgDEV008_DASH_img_list
        global segmentKA_img_list, segmentKI_img_list
        global lcarsON_img_list, lcarsOF_img_list, lcarsON_R_img_list, lcarsOF_R_img_list
        global rpmON_img_list, rpmOF_img_list

        self.load_config()
        self.load_background_images()
        self.load_led_images()
        self.load_sled_images()
        self.load_voicebox_images()
        self.load_misc_images()
        update_context(globals(), [
            "device", "style", "theme", "system",
            "btn_states_PB", "btn_states_PBFNKT", "btn_states_FNKT", "btn_states_HW", "btn_states_SW", "btn_states_qopt", "btn_states_FAV",
            "states_txt_act",
            "bgDEV001_img_list", "bgDEV002_img_list", "bgDEV004_img_list", "bgDEV008_img_list",
            "bgDEV001_DASH_img_list", "bgDEV002_DASH_img_list", "bgDEV004_DASH_img_list", "bgDEV008_DASH_img_list",
            "ledOF_img_list", "ledLO_img_list", "ledMI_img_list", "ledFU_img_list",
            "sledOF_img_list", "sledON_img_list",
            "vbOF_MAX_img_list", "vbON_MAX_img_list", "vbOF_OTTO_img_list", "vbON_OTTO_img_list",
            "vbOF_PILOT_img_list", "vbON_PILOT_img_list", "vbOF_S01_img_list", "vbON_S01_img_list",
            "vbOF_S02_img_list", "vbON_S02_img_list", "vbOF_S03_img_list", "vbON_S03_img_list",
            "vbOF_S04_img_list", "vbON_S04_img_list",
            "segmentKA_img_list", "segmentKI_img_list",
            "lcarsOF_img_list", "lcarsON_img_list", "lcarsOF_R_img_list", "lcarsON_R_img_list",
            "rpmOF_img_list", "rpmON_img_list",
            "bttf_img_list", "infocenterOF_img_list", "infocenterON_img_list",
            "knight_img_list", "sysnew_img_list",
        ])

        self.create_canvas()
        master.after(100, lambda: master.switch_frame(P01_DASH))

    def load_config(self):
        global device, style, theme, system
        global btn_states_PB, btn_states_PBFNKT, btn_states_FNKT, btn_states_HW, btn_states_SW, btn_states_qopt, btn_states_FAV
        global states_txt_act

        with open(os.path.join(datadir, "btn_states.json"), encoding="utf-8") as f:
            data = json.load(f)
        device = data["main_config"]["device"]
        style = data["main_config"]["style"]
        theme = data["main_config"]["theme"]
        system = data["main_config"]["system"]

        btns = data["buttons"]
        if device in btns:
            btn_states = btns[device]
            btn_states_PB    = btn_states["PB"]
            btn_states_PBFNKT  = btn_states["PBFNKT"]
            btn_states_FNKT  = btn_states["FNKT"]
            btn_states_HW    = btn_states["HW"]
            btn_states_SW    = btn_states["SW"]
            btn_states_qopt  = btn_states["QOPT"]
            btn_states_FAV   = btn_states["FAV"]
        else:
            print(f"Unbekanntes GerÃƒÆ’Ã‚Â¤t: {device}")
        #LANGUAGE
        if btn_states_SW[4]:
            states_txt_act = states_txt_en
        else:
            states_txt_act = states_txt_de

    def load_images_from_folder(self, path, suffix=".jpg"):
        images = LazyImageList(path, suffix)
        P00_BOOT._loaded_count += 1
        percent = int((P00_BOOT._loaded_count / P00_BOOT._total_count) * 100)
        print(f"{percent}% vorbereitet... ({os.path.basename(path)})")
        return images

    def load_background_images(self):
        path_map = {
            "DEV001": (bgDEV001_img_dir, "bgDEV001_img_list"),
            "DEV002": (bgDEV002_img_dir, "bgDEV002_img_list"),
            "DEV004": (bgDEV004_img_dir, "bgDEV004_img_list"),
            "DEV008": (bgDEV008_img_dir, "bgDEV008_img_list")
        }
        dash_map = {
            "DEV001": (bgDEV001_DASH_img_dir, "bgDEV001_DASH_img_list"),
            "DEV002": (bgDEV002_DASH_img_dir, "bgDEV002_DASH_img_list"),
            "DEV004": (bgDEV004_DASH_img_dir, "bgDEV004_DASH_img_list"),
            "DEV008": (bgDEV008_DASH_img_dir, "bgDEV008_DASH_img_list")
        }
        if device in path_map:
            path, varname = path_map[device]
            globals()[varname] = self.load_images_from_folder(path)
        if device in dash_map:
            path, varname = dash_map[device]
            globals()[varname] = self.load_images_from_folder(path)

    def load_led_images(self):
        led_dirs = {
            "ledOF_img_list": ledOF_img_dir,
            "ledLO_img_list": ledLO_img_dir,
            "ledMI_img_list": ledMI_img_dir,
            "ledFU_img_list": ledFU_img_dir
        }
        for varname, path in led_dirs.items():
            globals()[varname] = self.load_images_from_folder(path, ".png")

    def load_sled_images(self):
        sled_dirs = {
            "sledOF_img_list": sledOF_img_dir,
            "sledON_img_list": sledON_img_dir
        }
        for varname, path in sled_dirs.items():
            globals()[varname] = self.load_images_from_folder(path, ".png")

    def load_voicebox_images(self):
        voicebox_dirs = {
            "vbOF_MAX_img_list": vbOF_MAX_img_dir,
            "vbON_MAX_img_list": vbON_MAX_img_dir,
            "vbOF_OTTO_img_list": vbOF_OTTO_img_dir,
            "vbON_OTTO_img_list": vbON_OTTO_img_dir,
            "vbOF_PILOT_img_list": vbOF_PILOT_img_dir,
            "vbON_PILOT_img_list": vbON_PILOT_img_dir,
            "vbOF_S01_img_list": vbOF_S01_img_dir,
            "vbON_S01_img_list": vbON_S01_img_dir,
            "vbOF_S02_img_list": vbOF_S02_img_dir,
            "vbON_S02_img_list": vbON_S02_img_dir,
            "vbOF_S03_img_list": vbOF_S03_img_dir,
            "vbON_S03_img_list": vbON_S03_img_dir,
            "vbOF_S04_img_list": vbOF_S04_img_dir,
            "vbON_S04_img_list": vbON_S04_img_dir
        }
        for varname, path in voicebox_dirs.items():
            globals()[varname] = self.load_images_from_folder(path, ".png")
                
    def load_misc_images(self):
        misc_dirs = {
            "segmentKA_img_list": segmentKA_img_dir,
            "segmentKI_img_list": segmentKI_img_dir,
            "lcarsOF_img_list": lcarsOF_img_dir,
            "lcarsON_img_list": lcarsON_img_dir,
            "lcarsOF_R_img_list": lcarsOF_R_img_dir,
            "lcarsON_R_img_list": lcarsON_R_img_dir,
            "rpmOF_img_list": rpmOF_img_dir,
            "rpmON_img_list": rpmON_img_dir,
            "bttf_img_list": bttf_img_dir,
            "infocenterOF_img_list": infocenterOF_img_dir,
            "infocenterON_img_list": infocenterON_img_dir,
            "knight_img_list": knight_img_dir,
            "sysnew_img_list": sysnew_img_dir
        }

        for varname, path in misc_dirs.items():
            globals()[varname] = self.load_images_from_folder(path, ".png")
        
    def create_canvas(self):
        self.canvas = tk.Canvas(self, bg='black', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

        bg_map = {
            "DEV001": bgDEV001_img_list,
            "DEV002": bgDEV002_img_list,
            "DEV004": bgDEV004_img_list,
            "DEV008": bgDEV008_img_list
        }
        background_image = bg_map.get(device, [None, None])[1]

        self.canvas.create_image(0, 0, image=background_image, anchor='nw')

        btn_menu_dash = tk.Button(self, bd=0, bg=sys_clr[8], fg=sty_clr[0], text="DASH",
                                   command=lambda: self.master.switch_frame(P01_DASH))
        btn_menu_dash.place(x=215, y=20)
