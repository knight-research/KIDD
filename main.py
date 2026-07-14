#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------
# SERVICE
#------------------------------------------------------------------------------------------
debug = True # PRINT INFORMATIONS TO CONSOLE

#------------------------------------------------------------------------------------------
# region BEFORE MAINAPP
#------------------------------------------------------------------------------------------
#--------------------
# region VERSION
#--------------------
from functions.app_version import load_version
version, last_change = load_version()
from functions.gauge_scale_config import get_gauge_scale_lists, get_gauge_scale_revision
from functions.quicksound_config import QUICKSOUND_COLOR_INDEX, load_quicksound_config, load_quicksound_settings
# endregion

#--------------------
# region IMPORTS
#--------------------
from setup.import_all import *
from setup.platform_detection import detect_platform
from setup.platform_imports import load_platform_symbols
from functions.console_log import install_console_capture

sys_win, sys_linux, sys_pi = detect_platform()
globals().update(load_platform_symbols(sys_win, sys_linux, sys_pi))
install_console_capture()
#--------------------
# DATA FOLDERS
#--------------------
folder = os.path.dirname(os.path.abspath(__file__))
datadir = os.path.join(folder,'data')
#--------------------
# BUTTONSTATEMANEAGER
#--------------------
bsm = ButtonStateManager(folder)
#--------------------
# INIT SOUND
#--------------------
pygame.mixer.init()
# endregion

#--------------------
# region GLOBAL VARIABLES
#--------------------
from setup.runtime_defaults import load_runtime_default_symbols
globals().update(load_runtime_default_symbols(sys_linux, socket))

#----------------------------------------------------------------------------------
# TEXT LISTS
#----------------------------------------------------------------------------------
from functions.text_lists import load_text_list_symbols
globals().update(load_text_list_symbols(datadir))

#----------------------------------------------------------------------------------
# IMAGES
#----------------------------------------------------------------------------------
from functions.image_paths import load_image_path_symbols
globals().update(load_image_path_symbols(folder))

#--------------------------------------------------------------------------------------
#region UPDATE LAST CONFIGURATIONS
#--------------------------------------------------------------------------------------
from setup.config_state import load_config_state_symbols
globals().update(load_config_state_symbols(datadir))

#------------------------------------------------------------------------------
# region STYLES
#------------------------------------------------------------------------------
from setup.style_config import load_style_symbols
globals().update(load_style_symbols(device, style, system, DEVICE_B_txt, STYLE_B_txt, SYS_B_txt))

#--------------------------------------------------------------------------------------
# SETUP HARDWARE
#--------------------------------------------------------------------------------------
from setup.hardware_setup import setup_hardware
globals().update(setup_hardware(sys_linux, sys_pi, btn_states_HW, device, DEVICE_B_txt, globals()))
from pages.voicebox import create_voicebox_controls, create_voicebox_leds, update_voicebox_animation, update_voicebox_status

#------------------------------------------------------------------------------------------
# MAIN APP
#------------------------------------------------------------------------------------------
class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        global read
        read = KIDDController(self, globals())
        set_context(globals())
        self.title(version)
        self.geometry(kidd_width+"x"+kidd_height+"+"+kidd_left+"+"+kidd_top)

        if sys_win:
            self.resizable(0, 0)
            self.current_frame = None
            self.switch_frame(P00_BOOT)
        elif sys_linux:
            self.overrideredirect(True)
            self.configure(relief="flat")
            self.configure(highlightthickness=0)
            self.wm_attributes("-alpha", 0.5)
            self.current_frame = None
            self.switch_frame(P00_BOOT)

    def switch_frame(self, frame_class):
        frame_mapping = {
            0: P00_BOOT,
            1: P01_DASH,
            2: P02_QOPT,
            3: P03_SETUP,
            4: P04_THEMES,
            5: P05_CARFUNCTIONS,
            6: P06_KNIGHTFUNCTIONS,
            7: P07_AUDIO,
            8: P08_VIDEO
        }
        newframe = frame_mapping.get(frame_class, frame_class)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = newframe(self)
        self.current_frame.place(x=kidd_left, y=kidd_top, width=kidd_width, height=kidd_height)

#------------------------------------------------------------------------------------------
# PAGE 01: DASHBOARD
#------------------------------------------------------------------------------------------
class P01_DASH(tk.Frame):
    #--------------------------------------------------------------------------------------
    # CREATE THE PAGE
    #--------------------------------------------------------------------------------------
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.update_job = None
        self._destroyed = False
        self.lbls_sysinfo = []
        self.lbls_voicecmd = []
        self.gps_reception_label = None
        self.gps_reception_state = None
        self.label_7SEG001 = None
        self.label_7SEG002 = None
        self.label_7SEG003 = None
        self.background_image = None
        self.vinfo = None
        self.vtext = None
        self.activation_word_info = None
        self.val_cnt_sim = [0] * 12
        self.val_cnt_sim_updn = [True] * 12
        self.update_duration = 0.0
        self.theme_assets = None
        self.theme_assets_key = None
        self.widget_image_states = {}
        self.gauge_scale_revision = get_gauge_scale_revision()
        self.sysinfo_text_states = {}
        self.voice_text_states = {}
        self.last_system_data_update = 0.0
        self.system_data_refresh_interval = 10.0
        self.btn_setup = None
        self.btn_units = None
        self.btn_SELECT = []
        self.audio_buttons = []
        self.audio_labels = []
        self.audio_definitions = []
        self.audio_label_states = []
        self.last_audio_label_update = 0.0
        self.btn_FNKT = []
        self.led_DEV002IC = []
        self.led_DEV002 = []
        self.quantity_DEV002 = []
        self.led_DEV001G000 = []
        self.led_DEV001G001 = []
        self.led_DEV001G002 = []
        self.ammount_DEV001G000 = 0
        self.ammount_DEV001G001 = 0
        self.ammount_DEV001G002 = 0
        self.btns_DEV001VBBTN = []
        self.btns_DEV001VBSTBTN = []
        self.led_DEV001VBS34L01 = []
        self.led_DEV001VBS34L02 = []
        self.led_DEV001VBS34L03 = []
        self.ammount_VB = 0
        self.middle_index = 0
        self.led_DEV002G000 = []
        self.ammount_DEV002G000 = 0
        self.btns_PBFNKT = []
        self.ammount_PBFNKT = 0
        self.led_DEV002G007 = []
        self.led_DEV002G008 = []
        self.led_DEV002G009 = []
        self.ammount_DEV002G007 = 0
        self.ammount_DEV002G008 = 0
        self.ammount_DEV002G009 = 0
        self.dev002_update_phase = 0
        self.dev002_pb_value_labels = []
        self.dev002_pb_value_label_states = {}
        self.canvas = tk.Canvas(self, bg='black', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        self.create_widgets()

    def destroy(self):
        self._destroyed = True
        if self.update_job is not None:
            try:
                self.after_cancel(self.update_job)
            except tk.TclError:
                pass
            self.update_job = None
        super().destroy()

    def _is_alive(self):
        try:
            return not self._destroyed and self.winfo_exists()
        except tk.TclError:
            return False

    def _schedule_update(self):
        if self._is_alive():
            self.update_job = self.after(time_digital, self.update_page)

    def _set_widget_image(self, key, widget, image):
        if self.widget_image_states.get(key) is image:
            return
        widget.config(image=image)
        self.widget_image_states[key] = image

    def _consume_gauge_scale_refresh(self):
        revision = get_gauge_scale_revision()
        if revision == self.gauge_scale_revision:
            return False
        self.gauge_scale_revision = revision
        self.widget_image_states.clear()
        for cache_name in ("old_bar_leds", "old_signal_leds", "old_tuning_leds"):
            if hasattr(self, cache_name):
                getattr(self, cache_name).clear()
        return True

    def _scaled_led_count(self, value, minimum, maximum, amount):
        if amount <= 0 or maximum <= minimum:
            return 0
        try:
            value = float(value)
            minimum = float(minimum)
            maximum = float(maximum)
        except (TypeError, ValueError):
            return 0
        if value <= minimum:
            return 0
        step = (maximum - minimum) / amount
        if step <= 0:
            return 0
        return max(0, min(amount, int((value - minimum) / step) + 1))

    def _set_sysinfo_text(self, index, value):
        if self.sysinfo_text_states.get(index) == value:
            return
        self.lbls_sysinfo[index].config(text=value)
        self.sysinfo_text_states[index] = value

    def _set_gps_reception_text(self, value):
        if self.gps_reception_label is None:
            return
        if self.gps_reception_state == value:
            return
        self.gps_reception_label.config(text=value)
        self.gps_reception_state = value

    def _hide_gps_reception_label(self):
        if self.gps_reception_label is not None:
            self.gps_reception_label.place_forget()
        self.gps_reception_state = None

    def _set_voice_text(self, index, value):
        if self.voice_text_states.get(index) == value:
            return
        self.lbls_voicecmd[index].config(text=value)
        self.voice_text_states[index] = value

    def _refresh_system_data(self):
        now = time.monotonic()
        if now - self.last_system_data_update < self.system_data_refresh_interval:
            return
        read.get_system_data()
        self.last_system_data_update = now

    def _trace_step(self, timings, name):
        timings.append((name, time.perf_counter()))

    def _log_slow_update(self, timings):
        if len(timings) < 2:
            return
        total = timings[-1][1] - timings[0][1]
        if total < 0.05:
            return
        sections = []
        for index in range(1, len(timings)):
            elapsed = timings[index][1] - timings[index - 1][1]
            if elapsed >= 0.02:
                sections.append(f"{timings[index - 1][0]}->{timings[index][0]}={elapsed:.4f}s")
        detail = ", ".join(sections) if sections else "no single section >=0.02s"
        print(f"[PERF] dash update {total:.4f}s: {detail}")

    def _place_label_7SEG002(self):
        if self.label_7SEG002 is None:
            self.label_7SEG002 = tk.Label(self, **lbl_style_7SEG01_S34, bg=sty_clr[3], fg=sty_clr[2])
        else:
            self.label_7SEG002.config(**lbl_style_7SEG01_S34, bg=sty_clr[3], fg=sty_clr[2])

        if theme in THEME_B_txt[0:3]:
            self.label_7SEG002.place(x=2175, y=515, width=245, height=100)
        elif theme in THEME_B_txt[3:11]:
            self.label_7SEG002.place(x=1810, y=34, width=320, height=100)

    def _hide_label_7SEG002(self):
        if self.label_7SEG002 is not None:
            self.label_7SEG002.place_forget()

    def update_pb_buttons(self, active_image, inactive_image):
        for button, text in zip(self.btn_SELECT, btn_SELECT_txt):
            if btn_states_PB == text:
                button.config(image=active_image)
            else:
                button.config(image=inactive_image)

    #--------------------------------------------------------------------------------------
    # CREATE THE WIDGETS
    #--------------------------------------------------------------------------------------
    def create_widgets(self):
        read.load_soundfolder()
        #----------------------------------------------------------------------------------
        # UPDATE TEXT POSITIONS
        #----------------------------------------------------------------------------------
        with open(os.path.join(datadir, "positions.json"), encoding="utf-8") as f:
            self.positions = json.load(f)
        #----------------------------------------------------------------------------------
        # UPDATE SYSINFO TEXTS
        #----------------------------------------------------------------------------------
        with open(os.path.join(datadir, "sysinfo_texts.json"), encoding="utf-8") as f:
            self.pb_texts = json.load(f)
        #----------------------------------------------------------------------------------
        # THEME DEVICE001 AND DEVICE002
        #----------------------------------------------------------------------------------
        assets = self._get_theme_assets()
        widget_images = assets["widgets"]
        l_img01 = widget_images["l_img01"]
        l_img02 = widget_images["l_img02"]
        l_img03 = widget_images["l_img03"]
        l_img04 = widget_images["l_img04"]
        l_img05 = widget_images["l_img05"]
        l_img06 = widget_images["l_img06"]
        l_img07 = widget_images["l_img07"]
        l_img08 = widget_images["l_img08"]
        l_img09 = widget_images["l_img09"]
        l_img15 = widget_images["l_img15"]
        l_img16 = widget_images["l_img16"]
        l_img17 = widget_images["l_img17"]
        l_img18 = widget_images["l_img18"]
        l_img19 = widget_images["l_img19"]
        l_img20 = widget_images["l_img20"]
        l_img61 = widget_images["l_img61"]
        l_img64 = widget_images["l_img64"]
        l_img65 = widget_images["l_img65"]
        l_img66 = widget_images["l_img66"]
        l_img71 = widget_images["l_img71"]
        l_img74 = widget_images["l_img74"]
        l_img75 = widget_images["l_img75"]
        l_img76 = widget_images["l_img76"]
        l_img80 = widget_images["l_img80"]
        l_img81 = widget_images["l_img81"]
        localimagelist01 = widget_images["localimagelist01"]
        localimagelist02 = widget_images["localimagelist02"]
        #----------------------------------------------------------------------------------
        # UPDATE BACKGROUNDIMAGE
        #----------------------------------------------------------------------------------
        if device == DEVICE_B_txt[1]:
            #--------------------------------------------------------------------------
            # GET BACKGROUNDIMAGE
            #--------------------------------------------------------------------------
            theme_bg_image = bgDEV001_DASH_img_list
            self.background_image = theme_bg_image[THEME_B_txt.index(theme)]
            self.canvas.create_image(0, 0, image=self.background_image, anchor='nw')
            #--------------------------------------------------------------------------
            # BACKGROUNDIMAGE OVERLAYS
            #--------------------------------------------------------------------------
            if THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                self.canvas.create_rectangle(4, 195, 355, 332, fill=sty_clr[3])      #MTR
                self.canvas.create_rectangle(498, 571, 1270, 699, fill=sty_clr[3])   #TOTAL
        elif device == DEVICE_B_txt[2]:
            #--------------------------------------------------------------------------
            # GET BACKGROUNDIMAGE
            #--------------------------------------------------------------------------
            theme_bg_image = bgDEV002_DASH_img_list
            self.background_image = theme_bg_image[THEME_B_txt.index(theme)]
            self.canvas.create_image(0, 0, image=self.background_image, anchor='nw')
            #--------------------------------------------------------------------------
            # BACKGROUNDIMAGE OVERLAYS
            #--------------------------------------------------------------------------
            if THEME_B_txt[3:11].count(theme) > 0: # THEME 3 to 8
                self.canvas.create_rectangle(1808, 30, 2130, 134, fill=sty_clr[3])   #PROGNO
        #----------------------------------------------------------------------------------
        # STATIC TEXT
        #----------------------------------------------------------------------------------
        if device == DEVICE_B_txt[1]:
            if theme == THEME_B_txt[0] or THEME_B_txt[1] or theme == THEME_B_txt[2]:
                pass
            if theme == THEME_B_txt[3]:
                #OVERLAY TEXTE SPEEDOMETER
                self.canvas.create_text( 100,  65, **txt_style_S34c, text=gau_S03U01_txt[1])
                self.canvas.create_text( 700,  65, **txt_style_S34c, text=gau_S03U01_txt[2])
                self.canvas.create_text( 950,  65, **txt_style_S34c, text=gau_S03U01_txt[3])
                self.canvas.create_text(1235,  65, **txt_style_S34c, text=gau_S03U01_txt[4])
                self.canvas.create_text( 385, 318, **txt_style_S34c, text=gau_S03U01_txt[5])
                self.canvas.create_text( 385, 440, **txt_style_S34c, text=gau_S03U01_txt[6])
                self.canvas.create_text( 385, 615, **txt_style_S34c, text=gau_S03U01_txt[7])
                self.canvas.create_text( 548, 475, **txt_style_S34c, text=gau_S03U01_txt[8])
                self.canvas.create_text( 660, 475, **txt_style_S34c, text=gau_S03U01_txt[9])
                self.canvas.create_text( 770, 475, **txt_style_S34c, text=gau_S03U01_txt[10])
                self.canvas.create_text( 880, 475, **txt_style_S34c, text=gau_S03U01_txt[11])
                self.canvas.create_text( 995, 475, **txt_style_S34c, text=gau_S03U01_txt[12])
                self.canvas.create_text(1110, 475, **txt_style_S34c, text=gau_S03U01_txt[13])
                self.canvas.create_text(1225, 475, **txt_style_S34c, text=gau_S03U01_txt[14])
                self.canvas.create_text( 525, 545, **txt_style_S34c, text=gau_S03U01_txt[15])
                self.canvas.create_text( 140,  95, **txt_style_S34c, text=gau_S03U01_txt[16])
                self.canvas.create_text( 220,  95, **txt_style_S34c, text=gau_S03U01_txt[17])
                self.canvas.create_text( 300,  95, **txt_style_S34c, text=gau_S03U01_txt[18])
            elif theme == THEME_B_txt[4]:
                #OVERLAY TEXTE SPEEDOMETER
                self.canvas.create_text( 100,  65, **txt_style_S34c, text=gau_S04U01_txt[1])
                self.canvas.create_text( 700,  65, **txt_style_S34c, text=gau_S04U01_txt[2])
                self.canvas.create_text( 950,  65, **txt_style_S34c, text=gau_S04U01_txt[3])
                self.canvas.create_text(1235,  65, **txt_style_S34c, text=gau_S04U01_txt[4])
                self.canvas.create_text( 385, 318, **txt_style_S34c, text=gau_S04U01_txt[5])
                self.canvas.create_text( 385, 440, **txt_style_S34c, text=gau_S04U01_txt[6])
                self.canvas.create_text( 385, 615, **txt_style_S34c, text=gau_S04U01_txt[7])
                self.canvas.create_text( 548, 475, **txt_style_S34c, text=gau_S04U01_txt[8])
                self.canvas.create_text( 660, 475, **txt_style_S34c, text=gau_S04U01_txt[9])
                self.canvas.create_text( 770, 475, **txt_style_S34c, text=gau_S04U01_txt[10])
                self.canvas.create_text( 880, 475, **txt_style_S34c, text=gau_S04U01_txt[11])
                self.canvas.create_text( 995, 475, **txt_style_S34c, text=gau_S04U01_txt[12])
                self.canvas.create_text(1110, 475, **txt_style_S34c, text=gau_S04U01_txt[13])
                self.canvas.create_text(1225, 475, **txt_style_S34c, text=gau_S04U01_txt[14])
                self.canvas.create_text( 525, 545, **txt_style_S34c, text=gau_S04U01_txt[15])
                self.canvas.create_text( 140,  95, **txt_style_S34c, text=gau_S04U01_txt[16])
                self.canvas.create_text( 220,  95, **txt_style_S34c, text=gau_S04U01_txt[17])
                self.canvas.create_text( 300,  95, **txt_style_S34c, text=gau_S04U01_txt[18])
            elif theme == THEME_B_txt[5]:
                #OVERLAY TEXTE SPEEDOMETER
                self.canvas.create_text( 100,  65, **txt_style_S34c, text=gau_S05U01_txt[1])
                self.canvas.create_text( 700,  65, **txt_style_S34c, text=gau_S05U01_txt[2])
                self.canvas.create_text( 950,  65, **txt_style_S34c, text=gau_S05U01_txt[3])
                self.canvas.create_text(1235,  65, **txt_style_S34c, text=gau_S05U01_txt[4])
                self.canvas.create_text( 385, 318, **txt_style_S34c, text=gau_S05U01_txt[5])
                self.canvas.create_text( 385, 440, **txt_style_S34c, text=gau_S05U01_txt[6])
                self.canvas.create_text( 385, 615, **txt_style_S34c, text=gau_S05U01_txt[7])
                self.canvas.create_text( 548, 475, **txt_style_S34c, text=gau_S05U01_txt[8])
                self.canvas.create_text( 660, 475, **txt_style_S34c, text=gau_S05U01_txt[9])
                self.canvas.create_text( 770, 475, **txt_style_S34c, text=gau_S05U01_txt[10])
                self.canvas.create_text( 880, 475, **txt_style_S34c, text=gau_S05U01_txt[11])
                self.canvas.create_text( 995, 475, **txt_style_S34c, text=gau_S05U01_txt[12])
                self.canvas.create_text(1110, 475, **txt_style_S34c, text=gau_S05U01_txt[13])
                self.canvas.create_text(1225, 475, **txt_style_S34c, text=gau_S05U01_txt[14])
                self.canvas.create_text( 525, 545, **txt_style_S34c, text=gau_S05U01_txt[15])
                self.canvas.create_text( 140,  95, **txt_style_S34c, text=gau_S05U01_txt[16])
                self.canvas.create_text( 220,  95, **txt_style_S34c, text=gau_S05U01_txt[17])
                self.canvas.create_text( 300,  95, **txt_style_S34c, text=gau_S05U01_txt[18])
            elif theme == THEME_B_txt[6]:
                #OVERLAY TEXTE SPEEDOMETER
                self.canvas.create_text( 100,  65, **txt_style_S34c, text=gau_S06U01_txt[1])
                self.canvas.create_text( 700,  65, **txt_style_S34c, text=gau_S06U01_txt[2])
                self.canvas.create_text( 950,  65, **txt_style_S34c, text=gau_S06U01_txt[3])
                self.canvas.create_text(1235,  65, **txt_style_S34c, text=gau_S06U01_txt[4])
                self.canvas.create_text( 385, 318, **txt_style_S34c, text=gau_S06U01_txt[5])
                self.canvas.create_text( 385, 440, **txt_style_S34c, text=gau_S06U01_txt[6])
                self.canvas.create_text( 385, 615, **txt_style_S34c, text=gau_S06U01_txt[7])
                self.canvas.create_text( 548, 475, **txt_style_S34c, text=gau_S06U01_txt[8])
                self.canvas.create_text( 660, 475, **txt_style_S34c, text=gau_S06U01_txt[9])
                self.canvas.create_text( 770, 475, **txt_style_S34c, text=gau_S06U01_txt[10])
                self.canvas.create_text( 880, 475, **txt_style_S34c, text=gau_S06U01_txt[11])
                self.canvas.create_text( 995, 475, **txt_style_S34c, text=gau_S06U01_txt[12])
                self.canvas.create_text(1110, 475, **txt_style_S34c, text=gau_S06U01_txt[13])
                self.canvas.create_text(1225, 475, **txt_style_S34c, text=gau_S06U01_txt[14])
                self.canvas.create_text( 525, 545, **txt_style_S34c, text=gau_S06U01_txt[15])
                self.canvas.create_text( 140,  95, **txt_style_S34c, text=gau_S06U01_txt[16])
                self.canvas.create_text( 220,  95, **txt_style_S34c, text=gau_S06U01_txt[17])
                self.canvas.create_text( 300,  95, **txt_style_S34c, text=gau_S06U01_txt[18])
            elif theme == THEME_B_txt[7]:
                #OVERLAY TEXTE SPEEDOMETER
                self.canvas.create_text( 100,  65, **txt_style_S34c, text=gau_S06U01_txt[1])
                self.canvas.create_text( 700,  65, **txt_style_S34c, text=gau_S06U01_txt[2])
                self.canvas.create_text( 950,  65, **txt_style_S34c, text=gau_S06U01_txt[3])
                self.canvas.create_text(1235,  65, **txt_style_S34c, text=gau_S06U01_txt[4])
                self.canvas.create_text( 385, 318, **txt_style_S34c, text=gau_S06U01_txt[5])
                self.canvas.create_text( 385, 440, **txt_style_S34c, text=gau_S06U01_txt[6])
                self.canvas.create_text( 385, 615, **txt_style_S34c, text=gau_S06U01_txt[7])
                self.canvas.create_text( 548, 475, **txt_style_S34c, text=gau_S06U01_txt[8])
                self.canvas.create_text( 660, 475, **txt_style_S34c, text=gau_S06U01_txt[9])
                self.canvas.create_text( 770, 475, **txt_style_S34c, text=gau_S06U01_txt[10])
                self.canvas.create_text( 880, 475, **txt_style_S34c, text=gau_S06U01_txt[11])
                self.canvas.create_text( 995, 475, **txt_style_S34c, text=gau_S06U01_txt[12])
                self.canvas.create_text(1110, 475, **txt_style_S34c, text=gau_S06U01_txt[13])
                self.canvas.create_text(1225, 475, **txt_style_S34c, text=gau_S06U01_txt[14])
                self.canvas.create_text( 525, 545, **txt_style_S34c, text=gau_S06U01_txt[15])
                self.canvas.create_text( 140,  95, **txt_style_S34c, text=gau_S06U01_txt[16])
                self.canvas.create_text( 220,  95, **txt_style_S34c, text=gau_S06U01_txt[17])
                self.canvas.create_text( 300,  95, **txt_style_S34c, text=gau_S06U01_txt[18])
            elif theme == THEME_B_txt[9]:
                #OVERLAY TEXTE SPEEDOMETER
                self.canvas.create_text( 100,  65, **txt_style_S34c, text=gau_KR3KU01_txt[1])
                self.canvas.create_text( 700,  65, **txt_style_S34c, text=gau_KR3KU01_txt[2])
                self.canvas.create_text( 950,  65, **txt_style_S34c, text=gau_KR3KU01_txt[3])
                self.canvas.create_text(1235,  65, **txt_style_S34c, text=gau_KR3KU01_txt[4])
                self.canvas.create_text( 548, 475, **txt_style_S34c, text=gau_KR3KU01_txt[8])
                self.canvas.create_text( 660, 475, **txt_style_S34c, text=gau_KR3KU01_txt[9])
                self.canvas.create_text( 770, 475, **txt_style_S34c, text=gau_KR3KU01_txt[10])
                self.canvas.create_text( 880, 475, **txt_style_S34c, text=gau_KR3KU01_txt[11])
                self.canvas.create_text( 995, 475, **txt_style_S34c, text=gau_KR3KU01_txt[12])
                self.canvas.create_text(1110, 475, **txt_style_S34c, text=gau_KR3KU01_txt[13])
                self.canvas.create_text(1225, 475, **txt_style_S34c, text=gau_KR3KU01_txt[14])
                self.canvas.create_text( 140,  95, **txt_style_S34c, text=gau_KR3KU01_txt[16])
                self.canvas.create_text( 220,  95, **txt_style_S34c, text=gau_KR3KU01_txt[17])
                self.canvas.create_text( 300,  95, **txt_style_S34c, text=gau_KR3KU01_txt[18])
        elif device == DEVICE_B_txt[2]:
            if theme == THEME_B_txt[3]:
                #----------------------------------------------------------------------
                # TACHOBOARD
                #----------------------------------------------------------------------
                self.canvas.create_text(35, 370, **txt_style_S34e, text=gau_S03U02_txt[0])      # 0 RPM
                self.canvas.create_text(350, 220, **txt_style_S34e, text=gau_S03U02_txt[1])     # 2000 RPM
                self.canvas.create_text(650, 110, **txt_style_S34e, text=gau_S03U02_txt[2])     # 4000 RPM
                self.canvas.create_text(1265, 160, **txt_style_S34e, text=gau_S03U02_txt[3])    # 9000 RPM
                self.canvas.create_text(550, 444, **txt_style_S34e, text=gau_S03U02_txt[4])     #G000
                self.canvas.create_text(590, 444, **txt_style_S34e, text=units_us[3])           #G000 UNIT
                self.canvas.create_text(1235, 444, **txt_style_S34e, text=gau_S03U02_txt[5])    #G001
                self.canvas.create_text(1275, 444, **txt_style_S34e, text=units_us[3])          #G001 UNIT
                self.canvas.create_text(550, 552, **txt_style_S34e, text=gau_S03U02_txt[6])     #G002
                self.canvas.create_text(590, 552, **txt_style_S34e, text=units_us[3])           #G002 UNIT
                self.canvas.create_text(1220, 552, **txt_style_S34e, text=gau_S03U02_txt[7])    #G03
                self.canvas.create_text(1275, 552, **txt_style_S34e, text=units_us[4])          #G003 UNIT
                self.canvas.create_text(500, 660, **txt_style_S34e, text=gau_S03U02_txt[8])     #G004
                self.canvas.create_text(590, 660, **txt_style_S34e, text=units_us[5])           #G004 UNIT
                self.canvas.create_text(1200, 660, **txt_style_S34e, text=gau_S03U02_txt[9])    #G005
                self.canvas.create_text(1275, 660, **txt_style_S34e, text=units_us[6])          #G005 UNIT
                #----------------------------------------------------------------------
                # POWERBOARD
                #----------------------------------------------------------------------
                self.canvas.create_text(1700, 50, **txt_style_S34e, text=gau_S03U02_txt[10])
                self.canvas.create_text(1700, 162, **txt_style_S34e, text=gau_S03U02_txt[11])
                self.canvas.create_text(1700, 274, **txt_style_S34e, text=gau_S03U02_txt[12])
                self.canvas.create_text(1323, 490, **txt_style_S34c, text=gau_S03U02_txt[13])
                self.canvas.create_text(1593, 490, **txt_style_S34c, text=gau_S03U02_txt[14])
                self.canvas.create_text(1855, 490, **txt_style_S34c, text=gau_S03U02_txt[15])
                self.canvas.create_text(2120, 490, **txt_style_S34c, text=gau_S03U02_txt[16])
                self.canvas.create_text(1805, 225, **txt_style_S34c, text=gau_S03U02_txt[17])
                self.canvas.create_text(1910, 225, **txt_style_S34c, text=gau_S03U02_txt[18])
                self.canvas.create_text(2020, 225, **txt_style_S34c, text=gau_S03U02_txt[19])
                self.canvas.create_text(2120, 225, **txt_style_S34c, text=gau_S03U02_txt[20])
                self.canvas.create_text(1970, 170, **txt_style_S34c, text=gau_S03U02_txt[21])
            elif theme == THEME_B_txt[4]:
                #----------------------------------------------------------------------
                # TACHOBOARD
                #----------------------------------------------------------------------
                self.canvas.create_text(35, 370, **txt_style_S34e, text=gau_S04U02_txt[0])      # 0 RPM
                self.canvas.create_text(350, 220, **txt_style_S34e, text=gau_S04U02_txt[1])     # 2000 RPM
                self.canvas.create_text(650, 110, **txt_style_S34e, text=gau_S04U02_txt[2])     # 4000 RPM
                self.canvas.create_text(1265, 160, **txt_style_S34e, text=gau_S04U02_txt[3])    # 9000 RPM
                self.canvas.create_text(550, 444, **txt_style_S34e, text=gau_S04U02_txt[4])     #G000
                self.canvas.create_text(590, 444, **txt_style_S34e, text=units_us[3])           #G000 UNIT
                self.canvas.create_text(1235, 444, **txt_style_S34e, text=gau_S04U02_txt[5])    #G001
                self.canvas.create_text(1275, 444, **txt_style_S34e, text=units_us[3])          #G001 UNIT
                self.canvas.create_text(550, 552, **txt_style_S34e, text=gau_S04U02_txt[6])     #G002
                self.canvas.create_text(590, 552, **txt_style_S34e, text=units_us[3])           #G002 UNIT
                self.canvas.create_text(1220, 552, **txt_style_S34e, text=gau_S04U02_txt[7])    #G03
                self.canvas.create_text(1275, 552, **txt_style_S34e, text=units_us[4])          #G003 UNIT
                self.canvas.create_text(500, 660, **txt_style_S34e, text=gau_S04U02_txt[8])     #G004
                self.canvas.create_text(590, 660, **txt_style_S34e, text=units_us[5])           #G004 UNIT
                self.canvas.create_text(1200, 660, **txt_style_S34e, text=gau_S04U02_txt[9])    #G005
                self.canvas.create_text(1275, 660, **txt_style_S34e, text=units_us[6])          #G005 UNIT
                #----------------------------------------------------------------------
                # POWERBOARD
                #----------------------------------------------------------------------
                self.canvas.create_text(1700, 50, **txt_style_S34e, text=gau_S04U02_txt[10])
                self.canvas.create_text(1700, 162, **txt_style_S34e, text=gau_S04U02_txt[11])
                self.canvas.create_text(1700, 274, **txt_style_S34e, text=gau_S04U02_txt[12])
                self.canvas.create_text(1323, 490, **txt_style_S34c, text=gau_S04U02_txt[13])
                self.canvas.create_text(1593, 490, **txt_style_S34c, text=gau_S04U02_txt[14])
                self.canvas.create_text(1855, 490, **txt_style_S34c, text=gau_S04U02_txt[15])
                self.canvas.create_text(2120, 490, **txt_style_S34c, text=gau_S04U02_txt[16])
                self.canvas.create_text(1805, 225, **txt_style_S34c, text=gau_S04U02_txt[17])
                self.canvas.create_text(1910, 225, **txt_style_S34c, text=gau_S04U02_txt[18])
                self.canvas.create_text(2020, 225, **txt_style_S34c, text=gau_S04U02_txt[19])
                self.canvas.create_text(2120, 225, **txt_style_S34c, text=gau_S04U02_txt[20])
                self.canvas.create_text(1970, 170, **txt_style_S34c, text=gau_S04U02_txt[21])
            elif theme == THEME_B_txt[5]:
                #----------------------------------------------------------------------
                # TACHOBOARD
                #----------------------------------------------------------------------
                self.canvas.create_text(35, 370, **txt_style_S34e, text=gau_S05U02_txt[0])      # 0 RPM
                self.canvas.create_text(350, 220, **txt_style_S34e, text=gau_S05U02_txt[1])     # 2000 RPM
                self.canvas.create_text(650, 110, **txt_style_S34e, text=gau_S05U02_txt[2])     # 4000 RPM
                self.canvas.create_text(1265, 160, **txt_style_S34e, text=gau_S05U02_txt[3])    # 9000 RPM
                self.canvas.create_text(550, 444, **txt_style_S34e, text=gau_S05U02_txt[4])     #G000
                self.canvas.create_text(590, 444, **txt_style_S34e, text=units_us[3])           #G000 UNIT
                self.canvas.create_text(1235, 444, **txt_style_S34e, text=gau_S05U02_txt[5])    #G001
                self.canvas.create_text(1275, 444, **txt_style_S34e, text=units_us[3])          #G001 UNIT
                self.canvas.create_text(550, 552, **txt_style_S34e, text=gau_S05U02_txt[6])     #G002
                self.canvas.create_text(590, 552, **txt_style_S34e, text=units_us[3])           #G002 UNIT
                self.canvas.create_text(1220, 552, **txt_style_S34e, text=gau_S05U02_txt[7])    #G03
                self.canvas.create_text(1275, 552, **txt_style_S34e, text=units_us[4])          #G003 UNIT
                self.canvas.create_text(500, 660, **txt_style_S34e, text=gau_S05U02_txt[8])     #G004
                self.canvas.create_text(590, 660, **txt_style_S34e, text=units_us[5])           #G004 UNIT
                self.canvas.create_text(1200, 660, **txt_style_S34e, text=gau_S05U02_txt[9])    #G005
                self.canvas.create_text(1275, 660, **txt_style_S34e, text=units_us[6])          #G005 UNIT
                #----------------------------------------------------------------------
                # POWERBOARD
                #----------------------------------------------------------------------
                self.canvas.create_text(1700, 50, **txt_style_S34e, text=gau_S05U02_txt[10])
                self.canvas.create_text(1700, 162, **txt_style_S34e, text=gau_S05U02_txt[11])
                self.canvas.create_text(1700, 274, **txt_style_S34e, text=gau_S05U02_txt[12])
                self.canvas.create_text(1323, 490, **txt_style_S34c, text=gau_S05U02_txt[13])
                self.canvas.create_text(1593, 490, **txt_style_S34c, text=gau_S05U02_txt[14])
                self.canvas.create_text(1855, 490, **txt_style_S34c, text=gau_S05U02_txt[15])
                self.canvas.create_text(2120, 490, **txt_style_S34c, text=gau_S05U02_txt[16])
                self.canvas.create_text(1805, 225, **txt_style_S34c, text=gau_S05U02_txt[17])
                self.canvas.create_text(1910, 225, **txt_style_S34c, text=gau_S05U02_txt[18])
                self.canvas.create_text(2020, 225, **txt_style_S34c, text=gau_S05U02_txt[19])
                self.canvas.create_text(2120, 225, **txt_style_S34c, text=gau_S05U02_txt[20])
                self.canvas.create_text(1970, 170, **txt_style_S34c, text=gau_S05U02_txt[21])
            elif theme == THEME_B_txt[6]:
                #----------------------------------------------------------------------
                # TACHOBOARD
                #----------------------------------------------------------------------
                self.canvas.create_text(35, 370, **txt_style_S34e, text=gau_S06U02_txt[0])      # 0 RPM
                self.canvas.create_text(350, 220, **txt_style_S34e, text=gau_S06U02_txt[1])     # 2000 RPM
                self.canvas.create_text(650, 110, **txt_style_S34e, text=gau_S06U02_txt[2])     # 4000 RPM
                self.canvas.create_text(1265, 160, **txt_style_S34e, text=gau_S06U02_txt[3])    # 9000 RPM
                self.canvas.create_text(550, 444, **txt_style_S34e, text=gau_S06U02_txt[4])     #G000
                self.canvas.create_text(590, 444, **txt_style_S34e, text=units_us[3])           #G000 UNIT
                self.canvas.create_text(1235, 444, **txt_style_S34e, text=gau_S06U02_txt[5])    #G001
                self.canvas.create_text(1275, 444, **txt_style_S34e, text=units_us[3])          #G001 UNIT
                self.canvas.create_text(550, 552, **txt_style_S34e, text=gau_S06U02_txt[6])     #G002
                self.canvas.create_text(590, 552, **txt_style_S34e, text=units_us[3])           #G002 UNIT
                self.canvas.create_text(1220, 552, **txt_style_S34e, text=gau_S06U02_txt[7])    #G03
                self.canvas.create_text(1275, 552, **txt_style_S34e, text=units_us[4])          #G003 UNIT
                self.canvas.create_text(500, 660, **txt_style_S34e, text=gau_S06U02_txt[8])     #G004
                self.canvas.create_text(590, 660, **txt_style_S34e, text=units_us[5])           #G004 UNIT
                self.canvas.create_text(1200, 660, **txt_style_S34e, text=gau_S06U02_txt[9])    #G005
                self.canvas.create_text(1275, 660, **txt_style_S34e, text=units_us[6])          #G005 UNIT
                #----------------------------------------------------------------------
                # POWERBOARD
                #----------------------------------------------------------------------
                self.canvas.create_text(1700, 50, **txt_style_S34e, text=gau_S06U02_txt[10])
                self.canvas.create_text(1700, 162, **txt_style_S34e, text=gau_S06U02_txt[11])
                self.canvas.create_text(1700, 274, **txt_style_S34e, text=gau_S06U02_txt[12])
                self.canvas.create_text(1323, 490, **txt_style_S34c, text=gau_S06U02_txt[13])
                self.canvas.create_text(1593, 490, **txt_style_S34c, text=gau_S06U02_txt[14])
                self.canvas.create_text(1855, 490, **txt_style_S34c, text=gau_S06U02_txt[15])
                self.canvas.create_text(2120, 490, **txt_style_S34c, text=gau_S06U02_txt[16])
                self.canvas.create_text(1805, 225, **txt_style_S34c, text=gau_S06U02_txt[17])
                self.canvas.create_text(1910, 225, **txt_style_S34c, text=gau_S06U02_txt[18])
                self.canvas.create_text(2020, 225, **txt_style_S34c, text=gau_S06U02_txt[19])
                self.canvas.create_text(2120, 225, **txt_style_S34c, text=gau_S06U02_txt[20])
                self.canvas.create_text(1970, 170, **txt_style_S34c, text=gau_S06U02_txt[21])
            elif theme == THEME_B_txt[7]:
                #----------------------------------------------------------------------
                # TACHOBOARD
                #----------------------------------------------------------------------
                self.canvas.create_text(35, 370, **txt_style_S34e, text=gau_S06U02_txt[0])      # 0 RPM
                self.canvas.create_text(350, 220, **txt_style_S34e, text=gau_S06U02_txt[1])     # 2000 RPM
                self.canvas.create_text(650, 110, **txt_style_S34e, text=gau_S06U02_txt[2])     # 4000 RPM
                self.canvas.create_text(1265, 160, **txt_style_S34e, text=gau_S06U02_txt[3])    # 9000 RPM
                self.canvas.create_text(550, 444, **txt_style_S34e, text=gau_S06U02_txt[4])     #G000
                self.canvas.create_text(590, 444, **txt_style_S34e, text=units_us[3])           #G000 UNIT
                self.canvas.create_text(1235, 444, **txt_style_S34e, text=gau_S06U02_txt[5])    #G001
                self.canvas.create_text(1275, 444, **txt_style_S34e, text=units_us[3])          #G001 UNIT
                self.canvas.create_text(550, 552, **txt_style_S34e, text=gau_S06U02_txt[6])     #G002
                self.canvas.create_text(590, 552, **txt_style_S34e, text=units_us[3])           #G002 UNIT
                self.canvas.create_text(1220, 552, **txt_style_S34e, text=gau_S06U02_txt[7])    #G03
                self.canvas.create_text(1275, 552, **txt_style_S34e, text=units_us[4])          #G003 UNIT
                self.canvas.create_text(500, 660, **txt_style_S34e, text=gau_S06U02_txt[8])     #G004
                self.canvas.create_text(590, 660, **txt_style_S34e, text=units_us[5])           #G004 UNIT
                self.canvas.create_text(1200, 660, **txt_style_S34e, text=gau_S06U02_txt[9])    #G005
                self.canvas.create_text(1275, 660, **txt_style_S34e, text=units_us[6])          #G005 UNIT
                #----------------------------------------------------------------------
                # POWERBOARD
                #----------------------------------------------------------------------
                self.canvas.create_text(1700, 50, **txt_style_S34e, text=gau_S06U02_txt[10])
                self.canvas.create_text(1700, 162, **txt_style_S34e, text=gau_S06U02_txt[11])
                self.canvas.create_text(1700, 274, **txt_style_S34e, text=gau_S06U02_txt[12])
                self.canvas.create_text(1323, 490, **txt_style_S34c, text=gau_S06U02_txt[13])
                self.canvas.create_text(1593, 490, **txt_style_S34c, text=gau_S06U02_txt[14])
                self.canvas.create_text(1855, 490, **txt_style_S34c, text=gau_S06U02_txt[15])
                self.canvas.create_text(2120, 490, **txt_style_S34c, text=gau_S06U02_txt[16])
                self.canvas.create_text(1805, 225, **txt_style_S34c, text=gau_S06U02_txt[17])
                self.canvas.create_text(1910, 225, **txt_style_S34c, text=gau_S06U02_txt[18])
                self.canvas.create_text(2020, 225, **txt_style_S34c, text=gau_S06U02_txt[19])
                self.canvas.create_text(2120, 225, **txt_style_S34c, text=gau_S06U02_txt[20])
                self.canvas.create_text(1970, 170, **txt_style_S34c, text=gau_S06U02_txt[21])
        #----------------------------------------------------------------------------------
        # SETUP BUTTON
        #----------------------------------------------------------------------------------
        try:
            theme_index = THEME_B_txt.index(theme)
            theme_key = f"THEME{theme_index}"

            setup_pos = self.positions["BUTTON_POSITIONS"][device][theme_key]
            x_setup = setup_pos.get("x_btn_SETUP", 10)
            y_setup = setup_pos.get("y_btn_SETUP", 10)

            self.btn_setup = tk.Button(
                self,
                **btn_style_imgbtn,
                image=l_img80,
                command=lambda: self.master.switch_frame(P03_SETUP),
            )
            self.btn_setup.place(x=x_setup, y=y_setup)
        except Exception as e:
            print(f"[WARN] Failed to place SETUP button for {device} / {theme_key}: {e}")
        #----------------------------------------------------------------------------------
        # SELECT BUTTONS
        #----------------------------------------------------------------------------------
        #--------------------------------------------------------------------------
        # BUTTONS
        #--------------------------------------------------------------------------
        self.btn_SELECT = []
        for pb_text in btn_SELECT_txt:
            btns_SELECT = tk.Button(self, **btn_style_imgbtn, command=lambda text=pb_text: [
                read.toggle_PB(text),
                self.update_pb_buttons(l_img80, l_img81),
            self.refresh_background_image(),
            self.update_positions(),
            self.update_pb_ui_elements(),
            self.update_labels()
            ])
            self.btn_SELECT.append(btns_SELECT)
        try:
            theme_index = THEME_B_txt.index(theme)
            theme_key = f"THEME{theme_index}"

            setup_pos = self.positions["BUTTON_POSITIONS"][device][theme_key]
            x_btn = setup_pos.get("x_btn_SELECT", [])
            y_btn = setup_pos.get("y_btn_SELECT", [])
            quant_btn = min(len(x_btn), len(y_btn), len(self.btn_SELECT))

            for i in range(quant_btn):
                self.btn_SELECT[i].place(x=x_btn[i], y=y_btn[i])
            self._create_dev002_pb_value_labels(x_btn, y_btn)
        except (KeyError, ValueError) as e:
            print(f"⚠️ Keine PB-Button-Positionen für {device} / {theme_key}: {e}")
        #--------------------------------------------------------------------------
        # STATE
        #--------------------------------------------------------------------------
        for i, text in enumerate(btn_SELECT_txt):
            if btn_states_PB == text:
                if THEME_B_txt[0:11].count(theme) > 0: # THEME 0 to 9
                    self.btn_SELECT[i].config(image=l_img80)
                elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                    self.btn_SELECT[i].config(image=lcarsON_img_list[3])
            else:
                if THEME_B_txt[0:11].count(theme) > 0: # THEME 0 to 9
                    self.btn_SELECT[i].config(image=l_img81)
                elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                    self.btn_SELECT[i].config(image=lcarsOF_img_list[3])
        #----------------------------------------------------------------------------------
        # QUICKSOUND BUTTONS (YELLOW)
        #----------------------------------------------------------------------------------
        self.audio_on_img = l_img80
        self.audio_off_img = l_img81

        self.audio_buttons = []
        self.audio_labels = []
        self.audio_label_states = []
        self.audio_definitions = load_quicksound_config(datadir)
        self.audio_settings = load_quicksound_settings(datadir)

        try:
            theme_index = THEME_B_txt.index(theme)
            theme_key = f"THEME{theme_index}"

            special_pos = self.positions["BUTTON_POSITIONS"][device][theme_key]
            x_btns = special_pos.get("x_btn_QUICKSOUND", [])
            y_btns = special_pos.get("y_btn_QUICKSOUND", [])
            audio_btn_width = self.audio_off_img.width()
            audio_btn_height = self.audio_off_img.height()
            has_quicksound_positions = len(x_btns) >= len(self.audio_definitions) and len(y_btns) >= len(self.audio_definitions)

            for i, definition in enumerate(self.audio_definitions if has_quicksound_positions else []):
                subfolder = definition["folder"]
                filename = definition["file"]
                quicksound_mode = definition["mode"]
                loop_mode = quicksound_mode == "LOOP"
                color_index = QUICKSOUND_COLOR_INDEX.get(definition["color"], QUICKSOUND_COLOR_INDEX["YE"])
                audio_on_img = ledFU_img_list[color_index]
                audio_off_img = ledOF_img_list[color_index]
                filepath = os.path.join(snd_fldr, subfolder, filename)
                label_text = "AUTOPLAY" if quicksound_mode == "AUTOPLAY" else os.path.splitext(filename)[0]
                lbl = tk.Label(
                    self,
                    **lbl_style_setup_btns_small,
                    bg=sys_clr[8],
                    fg=sys_clr[9],
                )
                btn = tk.Button(
                    self,
                    **btn_style_imgbtn,
                    image=audio_off_img,
                    command=lambda path=filepath, idx=i, loop=loop_mode, mode=quicksound_mode: self.toggle_audio(idx, path, loop, mode),
                )
                btn.audio_on_img = audio_on_img
                btn.audio_off_img = audio_off_img
                if i < len(x_btns) and i < len(y_btns):
                    btn.place(x=x_btns[i], y=y_btns[i])
                    if self.audio_settings["labels_visible"]:
                        lbl.place(
                            x=x_btns[i],
                            y=y_btns[i] + audio_btn_height + 1,
                            width=audio_btn_width,
                            height=22,
                        )
                else:
                    print(f"[WARN] Missing QUICKSOUND button position for index {i}")
                self.audio_labels.append(lbl)
                self.audio_label_states.append({"text": label_text, "offset": 0, "display": None})
                self.audio_buttons.append(btn)
        except Exception as e:
            print(f"[ERROR] Failed to place QUICKSOUND buttons for {device}/{theme_key}: {e}")
        #----------------------------------------------------------------------------------
        # FUNCTION BUTTONS (LO HI VHF UHF AM FM CB) / (ATTACK SUST DELAY DEL)
        #----------------------------------------------------------------------------------
        self.btn_FNKT = []  # ← sicherstellen, dass Attribut immer existiert
        try:
            theme_index = THEME_B_txt.index(theme)
            theme_key = f"THEME{theme_index}"

            fnkt_pos = self.positions["BUTTON_POSITIONS"][device][theme_key]
            x_btn = fnkt_pos.get("x_btn_FUNCTION", [])
            y_btn = fnkt_pos.get("y_btn_FUNCTION", [])

            quant_btn = min(len(x_btn), len(y_btn))

            #IMAGES FOR OHC THATS WHY WE NEED MAPPING
            map_img_on = [
                l_img64, l_img64, l_img64, l_img64, l_img64, l_img64,
                l_img66, l_img66,
                l_img66, l_img61,
                l_img61, l_img61, l_img61, l_img61,
                l_img66, l_img61,
                l_img66, l_img66,
                l_img65, l_img65, l_img65, l_img65, l_img65, l_img65
            ]

            map_img_off = [
                l_img74, l_img74, l_img74, l_img74, l_img74, l_img74,
                l_img76, l_img76,
                l_img76, l_img71,
                l_img71, l_img71, l_img71, l_img71,
                l_img76, l_img71,
                l_img76, l_img76,
                l_img75, l_img75, l_img75, l_img75, l_img75, l_img75
            ]

            for i in range(quant_btn):
                btn = tk.Button(self, **btn_style_imgbtn,
                                command=lambda i=i: [read.toggle_button_states_FNKT(i),self.master.switch_frame(P01_DASH)])
                btn.place(x=x_btn[i], y=y_btn[i])
                self.btn_FNKT.append(btn)

                if i < len(btn_states_FNKT) and btn_states_FNKT[i]:
                    if device == DEVICE_B_txt[8] and i < len(map_img_on):
                        btn.config(image=map_img_on[i])
                    else:
                        btn.config(image=l_img06)
                else:
                    if device == DEVICE_B_txt[8] and i < len(map_img_off):
                        btn.config(image=map_img_off[i])
                    else:
                        btn.config(image=l_img07)

        except Exception as e:
            print(f"[ERROR] Failed to load FNKT button positions or images for {device}/{theme_key}: {e}")
        #----------------------------------------------------------------------------------
        # SWITCH UNITS BUTTON (IMPERIAL/METRIC)
        #----------------------------------------------------------------------------------
        if device == DEVICE_B_txt[1]:
            self.btn_units = tk.Button(self, **btn_style_imgbtn, command=lambda:[read.toggle_btn_SW(0),self.master.switch_frame(P01_DASH)])
            if THEME_B_txt[0:3].count(theme) > 0: # THEME 3 to 8
                self.btn_units.place(x=1040, y=218, width=166, height=81)
            elif THEME_B_txt[3:11].count(theme) > 0: # THEME 3 to 8
                self.btn_units.place(x=1105, y=248, width=166, height=81)
            elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                self.btn_units.place(x=770, y=110, width=202, height=68)
            if btn_states_SW[0] == True:
                self.btn_units.config(image=l_img01)
            else:
                self.btn_units.config(image=l_img02)
        elif device == DEVICE_B_txt[2]:
            self.btn_units = tk.Button(self, **btn_style_imgbtn, command=lambda:[read.toggle_btn_SW(0),self.master.switch_frame(P01_DASH)])
            if THEME_B_txt[0:3].count(theme) > 0: # THEME 0 to 2
                self.btn_units.place(x=970, y=245, width=166, height=81)
            elif THEME_B_txt[3:11].count(theme) > 0: # THEME 3 to 8
                self.btn_units.place(x=1064, y=296, width=166, height=81)
            elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                self.btn_units.place(x=1064, y=296, width=166, height=81)
            if btn_states_SW[0] == True:
                self.btn_units.config(image=l_img08)
            else:
                self.btn_units.config(image=l_img09)
        #----------------------------------------------------------------------------------
        # VOICECOMMAND LABELS AND ICONS
        #----------------------------------------------------------------------------------
        if device == DEVICE_B_txt[1]:
            self.lbls_voicecmd = []
            for voicecmdtext in voicecmd_txt:
                label_voicecmd = tk.Label(self.canvas, **lbl_style_voicecmd, bg=sty_clr[3], fg=sty_clr[1])
                self.lbls_voicecmd.append(label_voicecmd)

            if THEME_B_txt[3:8].count(theme) > 0: # THEME 3 to 8
                self.lbls_voicecmd[0].place(x=500, y=590, height="30", width="280")
                self.lbls_voicecmd[1].place(x=500, y=620, height="30", width="280")
                self.lbls_voicecmd[2].place(x=500, y=650, height="30", width="280")

            self.btn_FNKT[1].config(command=lambda: [self.toggle_function(),read.toggle_button_states_FNKT(1),self.master.switch_frame(P01_DASH)])
            self.function_running = False
        else:
            pass
        #----------------------------------------------------------------------------------
        # CREATE GAUGES FUNCTION
        #----------------------------------------------------------------------------------
        def create_gauges(self, x_pos, y_pos, x_pos_next, width, height, quantity):
            led = []
            for i in range(quantity):
                val = tk.Label(self, **btn_style_imgbtn)
                val.place(x=x_pos, y=y_pos, width=width, height=height)
                x_pos += x_pos_next
                led.append(val)
            return led
        #----------------------------------------------------------------------------------
        # CREATE GAUGES
        #----------------------------------------------------------------------------------
        #------------------------------------------------------------------------------
        # DEV001 GAUGES
        #------------------------------------------------------------------------------
        if device == DEVICE_B_txt[1]:
            quant = [0,0,0,0,0,0,0,0,0,0]
            #--------------------------------------------------------------------------
            # DEV001G000 (SPEED)
            #--------------------------------------------------------------------------
            self.led_DEV001G000 = []
            if theme in THEME_B_txt[:3]:  # THEME 0 1 2
                x_pos = 585
                y_pos = 103
                x_pos_nxt = 31
                width = 30
                height = 30
                self.ammount_DEV001G000 = 21
            elif theme in THEME_B_txt[3:11]:  # THEME 3 to 10
                x_pos = 95
                y_pos = 8
                x_pos_nxt = 84
                width = 80
                height = 40
                self.ammount_DEV001G000 = 14
            self.led_DEV001G000 = create_gauges(self, x_pos, y_pos, x_pos_nxt, width, height, self.ammount_DEV001G000)
            #--------------------------------------------------------------------------
            # DEV001G001 (SIGNAL)
            #--------------------------------------------------------------------------
            if theme in THEME_B_txt[:3]:  # THEME 0 1 2
                x_pos = 10
                y_pos = 442
                x_pos_nxt = 31
                width = 30
                height = 30
                self.ammount_DEV001G001 = 16
            elif theme in THEME_B_txt[3:11]:  # THEME 3 to 9
                x_pos = 5
                y_pos = 465
                x_pos_nxt = 20
                width = 20
                height = 77
                self.ammount_DEV001G001 = 20
            self.led_DEV001G001 = create_gauges(self, x_pos, y_pos, x_pos_nxt, width, height, self.ammount_DEV001G001)
            #--------------------------------------------------------------------------
            # DEV001G002 (TUNING)
            #--------------------------------------------------------------------------
            if theme in THEME_B_txt[:3]:  # THEME 0 1 2
                x_pos = 5
                y_pos = 640
                x_pos_nxt = 31
                width = 30
                height = 30
                self.ammount_DEV001G002 = 16
            elif theme in THEME_B_txt[3:11]:  # THEME 3 to 9
                x_pos = 5
                y_pos = 640
                x_pos_nxt = 20
                width = 20
                height = 77
                self.ammount_DEV001G002 = 20
            self.led_DEV001G002 = create_gauges(self, x_pos, y_pos, x_pos_nxt, width, height, self.ammount_DEV001G002)
            #--------------------------------------------------------------------------
            # VOICEBOX BUTTONS (PILOT S01 S02 OTTO = 8/3) / (S03 S04 S05 S06 MAX =10/6)
            #--------------------------------------------------------------------------
            create_voicebox_controls(self, theme, THEME_B_txt, btn_style_imgbtn, localimagelist01)
            #--------------------------------------------------------------------------
            # DEV001VBS34 (VOICEBOX)
            #--------------------------------------------------------------------------
            create_voicebox_leds(self, theme, THEME_B_txt, btn_style_imgbtn, ledOF_img_list[74] if theme == THEME_B_txt[0] else None)
        #------------------------------------------------------------------------------
        # DEV002 GAUGES
        #------------------------------------------------------------------------------
        if device == DEVICE_B_txt[2]:
            #--------------------------------------------------------------------------
            # POSITIONS AND QUANTITY
            #--------------------------------------------------------------------------
            #          #0   #1   #2   #3   #4   #5   #6
            x_pos01  = [5, 108, 815, 108, 815, 108, 815]
            y_pos01  = [5, 440, 440, 540, 540, 640, 640]
            x_posn01 = [5,  29,  29,  29,  29,  29,  29]
            width01  = [5,  29,  29,  29,  29,  29,  29]
            height01 = [5,  22,  22,  22,  22,  22,  22]
            quant01  = [5,  12,  12,  12,  12,  12,  12]
            x_pos02  = [5,   3, 696,   3, 696,   3, 696]
            y_pos02  = [5, 459, 459, 568, 568, 676, 676]
            x_posn02 = [5,  84,  84,  84,  84,  84,  84]
            width02  = [5,  80,  80,  80,  80,  80,  80]
            height02 = [5,  40,  40,  40,  40,  40,  40]
            quant02  = [5,   7,   7,   7,   7,   7,   7]
            self.quantity_DEV002 = [1,   2,   3,   4,   5,   6,   7]
            #--------------------------------------------------------------------------
            # DEV002GMASTER (RPM)   #todo
            #--------------------------------------------------------------------------
            self.led_DEV002G000 = []
            if THEME_B_txt[:3].count(theme) > 0: # THEME 0 to 2
                x_pos_RPM = 100
                y_pos_RPM = [295, 270, 247, 226, 205, 186, 168, 152, 136, 122, 109, 97, 86, 76, 67, 58, 52, 47, 42, 39, 36, 35, 35, 36, 40, 43, 48, 53, 60, 69, 79, 90, 103, 115, 130]
                x_pos_RPM_next = +30
                self.ammount_DEV002G000 = len(y_pos_RPM)
            elif THEME_B_txt[3:11].count(theme) > 0: # THEME 3 to 8
                x_pos_RPM = 5
                y_pos_RPM = [290, 257, 230, 205, 185, 162, 147, 130, 113, 100, 90, 78, 68, 58, 53, 46, 40, 35, 32, 30, 30, 30, 28, 30, 35, 40, 47, 55, 65, 75, 88, 100]
                x_pos_RPM_next = +40
                self.ammount_DEV002G000 = len(y_pos_RPM)
            elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                x_pos_RPM = 203
                y_pos_RPM = [15] * self.ammount_DEV002G000
                x_pos_RPM_next = +28
            for i in range(0, self.ammount_DEV002G000):
                led_gauge_U02MASTER = tk.Label(self, **btn_style_imgbtn)
                led_gauge_U02MASTER.place(x=x_pos_RPM, y=y_pos_RPM[i])
                x_pos_RPM += x_pos_RPM_next
                self.led_DEV002G000.append(led_gauge_U02MASTER)
            #--------------------------------------------------------------------------
            # DEV002G001-G006
            #--------------------------------------------------------------------------
            self.led_DEV002 = [None] * len(self.quantity_DEV002)
            for i in range(len(self.quantity_DEV002)):
                if theme in THEME_B_txt[:3]:  # THEME 0 1 2
                    x_pos = x_pos01[i]
                    y_pos = y_pos01[i]
                    x_pos_nxt = x_posn01[i]
                    width = width01[i]
                    height = height01[i]
                    quant = quant01[i]
                elif theme in THEME_B_txt[3:11]:  # THEME 3 to 9
                    x_pos = x_pos02[i]
                    y_pos = y_pos02[i]
                    x_pos_nxt = x_posn02[i]
                    width = width02[i]
                    height = height02[i]
                    quant = quant02[i]
                self.quantity_DEV002[i] = quant
                self.led_DEV002[i] = create_gauges(self, x_pos, y_pos, x_pos_nxt, width, height, quant)
            #--------------------------------------------------------------------------
            # DEV002G007 (VDC)
            #--------------------------------------------------------------------------
            self.led_DEV002G007 = []
            if theme in THEME_B_txt[:3]: # THEME 0 1 2
                x_pos_DEV002G007 = 1365
                x_pos_DEV002G007_after12 = 1785
                y_pos_DEV002G007 = 93
                x_pos_DEV002G007_next = +29
                width_DEV002G007 = 29
                height_DEV002G007 = 22
                self.ammount_DEV002G007 = 24
            elif theme in THEME_B_txt[3:11]: # THEME 3 to 9
                x_pos_DEV002G007 = 1285
                y_pos_DEV002G007 = 71
                x_pos_DEV002G007_next = +84
                width_DEV002G007 = 80
                height_DEV002G007 = 40
                self.ammount_DEV002G007 = 5
            for i in range(0, self.ammount_DEV002G007):
                val_DEV002G007 = tk.Label(self, **btn_style_imgbtn)
                if i < 12:
                    val_DEV002G007.place(x=x_pos_DEV002G007, y=y_pos_DEV002G007, width=width_DEV002G007, height=height_DEV002G007)
                    x_pos_DEV002G007 += x_pos_DEV002G007_next
                elif i > 11:
                    val_DEV002G007.place(x=x_pos_DEV002G007_after12, y=y_pos_DEV002G007, width=width_DEV002G007, height=height_DEV002G007)
                    x_pos_DEV002G007_after12 += x_pos_DEV002G007_next
                self.led_DEV002G007.append(val_DEV002G007)
            #--------------------------------------------------------------------------
            # DEV002G008 (AMP)
            #--------------------------------------------------------------------------
            self.led_DEV002G008 = []
            if theme in THEME_B_txt[:3]: # THEME 0 1 2
                x_pos_DEV002G008 = 1365
                x_pos_DEV002G008_after12 = 1785
                y_pos_DEV002G008 = 203
                x_pos_DEV002G008_next = +29
                width_DEV002G008 = 29
                height_DEV002G008 = 22
                self.ammount_DEV002G008 = 24
            elif theme in THEME_B_txt[3:11]: # THEME 3 to 9
                x_pos_DEV002G008 = 1285
                y_pos_DEV002G008 = 184
                x_pos_DEV002G008_next = +84
                width_DEV002G008 = 80
                height_DEV002G008 = 40
                self.ammount_DEV002G008 = 5
            for i in range(0, self.ammount_DEV002G008):
                val_DEV002G008 = tk.Label(self, **btn_style_imgbtn)
                if i < 12:
                    val_DEV002G008.place(x=x_pos_DEV002G008, y=y_pos_DEV002G008, width=width_DEV002G008, height=height_DEV002G008)
                    x_pos_DEV002G008 += x_pos_DEV002G008_next
                elif i > 11:
                    val_DEV002G008.place(x=x_pos_DEV002G008_after12, y=y_pos_DEV002G008, width=width_DEV002G008, height=height_DEV002G008)
                    x_pos_DEV002G008_after12 += x_pos_DEV002G008_next
                self.led_DEV002G008.append(val_DEV002G008)
            #--------------------------------------------------------------------------
            # DEV002G009 (AUX)
            #--------------------------------------------------------------------------
            self.led_DEV002G009 = []
            if theme in THEME_B_txt[:3]: # THEME 0 1 2
                x_pos_DEV002G009 = 1365
                x_pos_DEV002G009_after12 = 1785
                y_pos_DEV002G009 = 313
                x_pos_DEV002G009_next = +29
                width_DEV002G009 = 29
                height_DEV002G009 = 22
                self.ammount_DEV002G009 = 24
            elif theme in THEME_B_txt[3:11]: # THEME 3 to 9
                x_pos_DEV002G009 = 1285
                y_pos_DEV002G009 = 297
                x_pos_DEV002G009_next = +84
                width_DEV002G009 = 80
                height_DEV002G009 = 40
                self.ammount_DEV002G009 = 5
            for i in range(0, self.ammount_DEV002G009):
                val_DEV002G009 = tk.Label(self, **btn_style_imgbtn)
                if i < 12:
                    val_DEV002G009.place(x=x_pos_DEV002G009, y=y_pos_DEV002G009, width=width_DEV002G009, height=height_DEV002G009)
                    x_pos_DEV002G009 += x_pos_DEV002G009_next
                elif i > 11:
                    val_DEV002G009.place(x=x_pos_DEV002G009_after12, y=y_pos_DEV002G009, width=width_DEV002G009, height=height_DEV002G009)
                    x_pos_DEV002G009_after12 += x_pos_DEV002G009_next
                self.led_DEV002G009.append(val_DEV002G009)
            #--------------------------------------------------------------------------
            # FUNCTION POWER BUTTONS DEVICE02 (POWER AUTO NORMAL PURSUIT)
            #--------------------------------------------------------------------------
            self.btns_PBFNKT = []
            if theme in THEME_B_txt[:3]: # THEME 0 1 2
                x_pos_PBFNKT = 2175
                y_pos_PBFNKT = 655
                width_PBFNKT = 55
                height_PBFNKT = 55
                x_pos_PBFNKT_mext = +width_PBFNKT +8
                self.ammount_PBFNKT = 4
            elif theme in THEME_B_txt[3:11]: # THEME 3 to 9
                x_pos_PBFNKT = 1285
                y_pos_PBFNKT = 546
                width_PBFNKT = 82
                height_PBFNKT = 154
                x_pos_PBFNKT_mext = +265
                self.ammount_PBFNKT = 4
            for i in range(self.ammount_PBFNKT):
                btn_PBFNKT = tk.Button(self, **btn_style_imgbtn, command=lambda i=i: [read.toggle_button_states_PBFNKT(i),self.master.switch_frame(P01_DASH)])
                btn_PBFNKT.place(x=x_pos_PBFNKT, y=y_pos_PBFNKT, width=width_PBFNKT, height=height_PBFNKT)
                x_pos_PBFNKT += x_pos_PBFNKT_mext
                self.btns_PBFNKT.append(btn_PBFNKT)

            btn_PBFNKT_FU = [l_img16, l_img15, l_img17, l_img16]
            btn_PBFNKT_OF = [l_img19, l_img18, l_img20, l_img19]
            for i in range(4):
                if btn_states_PBFNKT[i]:
                    self.btns_PBFNKT[i].config(image=btn_PBFNKT_FU[i])
                else:
                    self.btns_PBFNKT[i].config(image=btn_PBFNKT_OF[i])
            #--------------------------------------------------------------------------
            # DEV002 INFORMATION CENTER
            #--------------------------------------------------------------------------
            self.led_DEV002IC = []
            for i in range(0, 16):
                led_gauge_DEV002IC = tk.Label(self, **btn_style_imgbtn)
                self.led_DEV002IC.append(led_gauge_DEV002IC)
            self.led_DEV002IC[0].place(x=2174, y=17, width=80, height=80)
            self.led_DEV002IC[1].place(x=2257, y=17, width=80, height=80)
            self.led_DEV002IC[2].place(x=2340, y=17, width=80, height=80)
            self.led_DEV002IC[3].place(x=2174, y=100, width=80, height=80)
            self.led_DEV002IC[4].place(x=2257, y=100, width=80, height=80)
            self.led_DEV002IC[5].place(x=2340, y=100, width=80, height=80)
            self.led_DEV002IC[6].place(x=2174, y=183, width=80, height=80)
            self.led_DEV002IC[7].place(x=2257, y=183, width=80, height=80)
            self.led_DEV002IC[8].place(x=2340, y=183, width=80, height=80)
            self.led_DEV002IC[9].place(x=2174, y=266, width=80, height=80)
            self.led_DEV002IC[10].place(x=2257, y=266, width=80, height=80)
            self.led_DEV002IC[11].place(x=2340, y=266, width=80, height=80)
            self.led_DEV002IC[12].place(x=2174, y=349, width=80, height=80)
            self.led_DEV002IC[13].place(x=2257, y=349, width=80, height=80)
            self.led_DEV002IC[14].place(x=2340, y=349, width=80, height=80)
            self.led_DEV002IC[15].place(x=2174, y=432, width=80, height=80)
        #----------------------------------------------------------------------------------
        # SYSINFO LABELS
        #----------------------------------------------------------------------------------
        self.update_positions()
        self.update_pb_ui_elements()
        self.update_labels()
        #------------------------------------------------------------------------------
        # PLACE LABEL
        #------------------------------------------------------------------------------
        for i, label in enumerate(self.lbls_sysinfo):
            if i < len(self.x_lbl_sysinfo) and i < len(self.y_lbl_sysinfo):
                if i < 5:
                    label.place(
                        x=self.x_lbl_sysinfo[i],
                        y=self.y_lbl_sysinfo[i],
                        width=self.wh_lbl_sysinfo[0],
                        height=self.wh_lbl_sysinfo[1]
                    )
                else:
                    label.place(
                        x=self.x_lbl_sysinfo[i],
                        y=self.y_lbl_sysinfo[i],
                        width=self.wh_lbl_sysinfo[2],
                        height=self.wh_lbl_sysinfo[3]
                    )
        #----------------------------------------------------------------------------------
        # GAUGE 7-SEGMENT DISPLAYS
        #----------------------------------------------------------------------------------
        self.label_7SEG001 = tk.Label(self, bg=sty_clr[3], fg=sty_clr[2])
        self.label_7SEG003 = tk.Label(self)

        if device == DEVICE_B_txt[1]:
            #--------------------------------------------------------------------------
            # 7-SEGMENT DISPLAY 001: SPEED / RPM
            #--------------------------------------------------------------------------
            if THEME_B_txt[0:3].count(theme) > 0: # THEME 0 to 2
                self.label_7SEG001.config(font=(fonts[2], 125), anchor="nw")
                self.label_7SEG001.place(x=582, y=160, width=370, height=147)
            elif THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                if btn_states_SW[3] == False:
                    if btn_states_SW[1] == True:
                        self.label_7SEG001.config(image=l_img03, compound="center")
                    else:
                        self.label_7SEG001.config(image=l_img04, compound="center")
                else:
                    self.label_7SEG001.config(image=l_img05, compound="center")
                self.label_7SEG001.config(font=(fonts[2], 165), anchor="nw")
                self.label_7SEG001.place(x=609, y=116, width=496, height=212)
            elif theme in [THEME_B_txt[9], THEME_B_txt[10]]:
                self.label_7SEG001.config(font=(fonts[9], 150), bg=sty_clr[6], fg=sty_clr[0], anchor="c")
                self.label_7SEG001.place(x=609, y=116, width=496, height=212)
            elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                self.label_7SEG001.place(x=985, y=100, width=220, height=200)
            #--------------------------------------------------------------------------
            # 7-SEGMENT DISPLAY 003: TOTAL / ---
            #--------------------------------------------------------------------------
            if THEME_B_txt[0:3].count(theme) > 0: # THEME 0 to 3
                self.label_7SEG003.config(**lbl_style_7SEG01_S12, bg=sty_clr[4], fg=sty_clr[5])
                self.label_7SEG003.place(x=940, y=470, width=285, height=84)
            elif THEME_B_txt[3:9].count(theme) > 0: # THEME 3 to 8
                self.label_7SEG003.config(**lbl_style_7SEG01_S34, bg=sty_clr[3], fg=sty_clr[2])
                self.label_7SEG003.place(x=800, y=590, width=460, height=90)
            elif theme in [THEME_B_txt[9], THEME_B_txt[10]]:
                self.label_7SEG003.config(**lbl_style_7SEG01_S34, bg=sty_clr[6], fg=sty_clr[0])
                self.label_7SEG003.place(x=800, y=590, width=460, height=90)
        elif device == DEVICE_B_txt[2]:
            #--------------------------------------------------------------------------
            # 7-SEGMENT DISPLAY 001: SPEED / RPM
            #--------------------------------------------------------------------------
            if THEME_B_txt[0:3].count(theme) > 0: # THEME 0 to 2
                self.label_7SEG001.config(font=(fonts[2], 125), anchor="c")
                self.label_7SEG001.place(x=625, y=150, width=220, height=185)
            elif THEME_B_txt[3:11].count(theme) > 0: # THEME 3 to 8
                self.label_7SEG001.config(font=(fonts[2], 165), anchor="nw")
                self.label_7SEG001.config(image=l_img04, compound="center")
                self.label_7SEG001.place(x=567, y=164, width=496, height=212)
            elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
                self.label_7SEG001.place(x=985, y=100, width=220, height=200)
        #----------------------------------------------------------------------------------
        # END INIT PAGE
        #----------------------------------------------------------------------------------
        self.update_page()

    def update_pb_ui_elements(self):
        self.canvas.delete("pb_overlay")

        lang = "eng" if btn_states_SW[4] else "deu"
        pb = btn_states_PB

        if pb not in self.pb_texts or lang not in self.pb_texts[pb]:
            return

        if not hasattr(self, "x_txt_sysinfo") or not hasattr(self, "y_txt_sysinfo"):
            return

        entries = self.pb_texts[pb][lang]
        for entry, x, y in zip(entries, self.x_txt_sysinfo, self.y_txt_sysinfo):
            style = dict(txt_style_sysinfo)
            if "font" in entry:
                style["font"] = tuple(entry["font"])
            if "anchor" in entry:
                style["anchor"] = entry["anchor"]

            fill_color = entry.get("fill", sty_clr[2])
            self.canvas.create_text(
                x, y,
                text=entry["text"],
                fill=fill_color,
                tags="pb_overlay",
                **style
            )

    def update_positions(self):
        pb = btn_states_PB
        try:
            theme_index = THEME_B_txt.index(theme)
            theme_key = f"THEME{theme_index}"
        except ValueError:
            print(f"Theme {theme} nicht in THEME_B_txt")
            return

        try:
            pos_data = self.positions[pb][device][theme_key]
            self.x_txt_sysinfo = pos_data.get("x_txt_sysinfo", [])
            self.y_txt_sysinfo = pos_data.get("y_txt_sysinfo", [])
            self.x_lbl_sysinfo = pos_data.get("x_lbl_sysinfo", [])
            self.y_lbl_sysinfo = pos_data.get("y_lbl_sysinfo", [])
            self.wh_lbl_sysinfo = pos_data.get("wh_lbl_sysinfo", [])
        except KeyError:
            self.x_txt_sysinfo = []
            self.y_txt_sysinfo = []
            self.x_lbl_sysinfo = []
            self.y_lbl_sysinfo = []
            self.wh_lbl_sysinfo = []

    def refresh_background_image(self):
        try:
            theme_index = THEME_B_txt.index(theme)
        except ValueError:
            print(f"⚠️ Theme '{theme}' nicht in THEME_B_txt gefunden")
            return

        # Hintergrundbild je Device auswählen
        if device == DEVICE_B_txt[1]:
            self.background_image = bgDEV001_DASH_img_list[theme_index]
        elif device == DEVICE_B_txt[2]:
            self.background_image = bgDEV002_DASH_img_list[theme_index]
        else:
            print(f"⚠️ Kein Hintergrundbild für Device {device}")
            return

            # Canvas leeren und neu zeichnen
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, image=self.background_image, anchor="nw", tags="bg")

    def update_labels(self):
        current_pb = btn_states_PB
        # Prüfen, ob sich PB geändert hat
        if hasattr(self, "last_pb_state") and self.last_pb_state == current_pb:
            return False  # Kein Update noetig
        self.last_pb_state = current_pb
        self.sysinfo_text_states.clear()

        # Alte Labels entfernen
        for lbl in self.lbls_sysinfo:
            lbl.destroy()
        self.lbls_sysinfo.clear()
        if self.gps_reception_label is not None:
            self.gps_reception_label.destroy()
            self.gps_reception_label = None
            self.gps_reception_state = None

        # Prüfen, ob Positionen vorhanden sind
        if not hasattr(self, "x_lbl_sysinfo") or not hasattr(self, "y_lbl_sysinfo") or not hasattr(self, "wh_lbl_sysinfo"):
            print("⚠️ Positionen für Labels nicht gesetzt.")
            return True

        # Anzahl = kleinste gültige Länge der Listen
        anzahl = min(len(self.x_lbl_sysinfo), len(self.y_lbl_sysinfo))

        for i in range(anzahl):
            x = self.x_lbl_sysinfo[i]
            y = self.y_lbl_sysinfo[i]

            # Nur echte Koordinaten > 0 verwenden
            if x > 0 and y > 0:
                lbl = tk.Label(self.canvas, **lbl_style_sysinfo, bg=sty_clr[3], fg=sty_clr[1])

                # Größe je nach Index wählen
                if i < 5:
                    w, h = self.wh_lbl_sysinfo[0], self.wh_lbl_sysinfo[1]
                else:
                    w = self.wh_lbl_sysinfo[2] if len(self.wh_lbl_sysinfo) > 2 else self.wh_lbl_sysinfo[0]
                    h = self.wh_lbl_sysinfo[3] if len(self.wh_lbl_sysinfo) > 3 else self.wh_lbl_sysinfo[1]

                lbl.place(x=x, y=y, width=w, height=h)
                self.lbls_sysinfo.append(lbl)
        while len(self.lbls_sysinfo) < 8:
            lbl = tk.Label(self.canvas, **lbl_style_sysinfo, bg=sty_clr[3], fg=sty_clr[1])
            lbl.place_forget()
            self.lbls_sysinfo.append(lbl)
        self._place_gps_reception_label()
        return True

    def _place_gps_reception_label(self):
        if device != DEVICE_B_txt[1] or btn_states_PB != "pb01":
            return
        if not hasattr(self, "x_lbl_sysinfo") or not self.x_lbl_sysinfo:
            return
        if not hasattr(self, "y_lbl_sysinfo") or not self.y_lbl_sysinfo:
            return

        base_width = self.wh_lbl_sysinfo[0] if hasattr(self, "wh_lbl_sysinfo") and self.wh_lbl_sysinfo else 180
        base_height = self.wh_lbl_sysinfo[1] if hasattr(self, "wh_lbl_sysinfo") and len(self.wh_lbl_sysinfo) > 1 else 42
        x_pos = self.x_lbl_sysinfo[0] + base_width - 42
        y_pos = self.y_lbl_sysinfo[0]
        label_width = 120

        self.gps_reception_label = tk.Label(self.canvas, **lbl_style_sysinfo, bg=sty_clr[3], fg=sty_clr[1])
        self.gps_reception_label.place(x=x_pos, y=y_pos, width=label_width, height=base_height)

    def _update_audio_labels(self):
        if not self.audio_settings.get("labels_visible", True):
            return

        now = time.monotonic()
        if now - self.last_audio_label_update < 0.25:
            return
        self.last_audio_label_update = now

        visible_chars = 11
        for label, state in zip(self.audio_labels, self.audio_label_states):
            text = state["text"]
            if len(text) <= visible_chars:
                if state.get("display") != text:
                    label.config(text=text)
                    state["display"] = text
                continue

            scroll_text = f"{text}   "
            offset = state["offset"] % len(scroll_text)
            doubled = scroll_text + scroll_text
            display_text = doubled[offset:offset + visible_chars]
            if state.get("display") != display_text:
                label.config(text=display_text)
                state["display"] = display_text
            state["offset"] = offset + 1

    def _update_audio_button_states(self):
        for idx, definition in enumerate(self.audio_definitions):
            if definition["mode"] == "AUTOPLAY" and idx < len(self.audio_buttons):
                image = self.audio_buttons[idx].audio_on_img if read.autoplay_active else self.audio_buttons[idx].audio_off_img
                self._set_widget_image(("quicksound_autoplay", idx), self.audio_buttons[idx], image)

    def _create_dev002_pb_value_labels(self, x_btn, y_btn):
        if device != DEVICE_B_txt[2] or theme != "K2_S05":
            return

        label_style = {"font": (fonts[6], 24), "anchor": "c", "borderwidth": 0, "highlightthickness": 0}
        self.dev002_pb_value_labels = []
        self.dev002_pb_value_label_states = {}
        for i in range(min(9, len(x_btn), len(y_btn))):
            lbl = tk.Label(self, **label_style, bg=sty_clr[3], fg=sty_clr[1])
            lbl.place(x=x_btn[i] + 100, y=y_btn[i] + 3, width=110, height=34)
            self.dev002_pb_value_labels.append(lbl)

    def _update_dev002_pb_value_labels(self, dev002_values):
        if not self.dev002_pb_value_labels:
            return

        for index, pb_key in enumerate(btn_SELECT_txt[:len(self.dev002_pb_value_labels)]):
            text = str(dev002_values.get(pb_key, "---"))
            if self.dev002_pb_value_label_states.get(index) != text:
                self.dev002_pb_value_labels[index].config(text=text)
                self.dev002_pb_value_label_states[index] = text

    def toggle_audio(self, idx, filepath, loop, mode="1X"):
        if mode == "AUTOPLAY":
            read.toggle_random_autoplay()
            if read.autoplay_active:
                self.audio_buttons[idx].config(image=self.audio_buttons[idx].audio_on_img)
            else:
                self.audio_buttons[idx].config(image=self.audio_buttons[idx].audio_off_img)
            return

        result = read.toggle_audio_loop(filepath, loop)
        if loop:
            # Bei Loop: ON/OFF je nach Zustand
            if result is True:
                self.audio_buttons[idx].config(image=self.audio_buttons[idx].audio_on_img)
            elif result is False:
                self.audio_buttons[idx].config(image=self.audio_buttons[idx].audio_off_img)
        else:
            # Bei einmaliger Wiedergabe: Bild kurz auf ON, dann zurück
            self.audio_buttons[idx].config(image=self.audio_buttons[idx].audio_on_img)
            self.after(500, lambda: self.audio_buttons[idx].config(image=self.audio_buttons[idx].audio_off_img))

    #--------------------------------------------------------------------------------------
    # THREAD LISTEN_FOR_ACTIVATION_WORD #todo move to myfunctions
    #--------------------------------------------------------------------------------------
    def toggle_function(self):
        if btn_states_FNKT[1] == False and not self.function_running:
            # Start the function in a separate thread
            self.function_running = True
            self.thread = Thread(target=self.listen_for_activation_word)
            self.thread.start()
        else:
            # Stop the function by setting the flag to False
            self.function_running = False
            try:
                self.thread.Event()
                self.thread.join()
            except:
                pass
    #--------------------------------------------------------------------------------------
    # LISTEN TO VOICE #todo move to myfunctions
    #--------------------------------------------------------------------------------------
    def listen_for_activation_word(self):
        while self.function_running:
            r = sr.Recognizer() # Create a speech recognizer object
            # Use the microphone as the audio source
            try:
                with sr.Microphone() as source:
                    self.vinfo = "Waiting for activation Word..."
                    r.adjust_for_ambient_noise(source) # Adjust for ambient noise
                    audio = r.listen(source) # Listen for audio input
                    #--------------------------------------------------------------------------
                    # MP3 FOLDERS
                    #--------------------------------------------------------------------------
                    main_mp3_fldr = os.path.join(folder,'sound', snd_fldr)
                    yes_mp3_fldr = os.path.join(main_mp3_fldr,'yes')
                    what_mp3_fldr = os.path.join(main_mp3_fldr,'what')
                    states_car_mp3_fldr = os.path.join(main_mp3_fldr,'states_car')
                    time_mp3_fldr = os.path.join(main_mp3_fldr,'time')
                    try:
                        #----------------------------------------------------------------------
                        # RECOGNIZE SPEECH IN DIFFERENT LANGUAGES
                        #----------------------------------------------------------------------
                        text = r.recognize_google(audio, language='de-DE')
                        #text = r.recognize_google(audio, language='en-EN')
                        self.vtext = text
                        #----------------------------------------------------------------------
                        # CHECK FOR CORRECT ACTIVATION WORD #TODO NOT USED IN NEXT FUNCTION
                        #----------------------------------------------------------------------
                        if style == STYLE_B_txt[0]:
                            activation_words = ["kid", "kit", "hey kid", "fake it", "Hacked", "Hackett", "Hey Kid", "shake it"]
                            self.activation_word_info = "Say: Hey KARR"
                        elif style == STYLE_B_txt[1]:
                            activation_words = ["hey.car", "hey car", "heycar", "hey karr", "helga"]
                            self.activation_word_info = "Say: Hey KITT"
                        self.vinfo = self.activation_word_info
                        #----------------------------------------------------------------------
                        # WAIT FOR ACTIVATION WORD IS SPOKEN
                        #----------------------------------------------------------------------
                        if "hey kid" or "fake it" or "Hacked" or"hey car" or "hey.car" or "heycar" or "hey karr" or "helga" in text.lower():
                        #if any(phrase in text.lower() for phrase in activation_words):
                            self.vinfo = "I heard you"
                            #------------------------------------------------------------------
                            # PLAY RANDOM RECOGNIZED ACTIVATION WORD SOUND
                            #------------------------------------------------------------------
                            yes_mp3_files = [f for f in os.listdir(yes_mp3_fldr) if f.endswith(".mp3")]
                            if yes_mp3_files:
                                yes_random_mp3 = random.choice(yes_mp3_files)
                                yes_mp3_path = os.path.join(yes_mp3_fldr, yes_random_mp3)
                                sound = AudioSegment.from_file(yes_mp3_path, format="mp3")
                                play(sound)
                                self.vinfo = yes_random_mp3
                            #------------------------------------------------------------------
                            # LISTEN TO ACTUAL COMMAND WORDS
                            #------------------------------------------------------------------
                            self.vinfo = "Please speak command..."
                            audio = r.listen(source)
                            text = r.recognize_google(audio, language='de-DE')
                            self.vtext = text

                            #------------------------------------------------------------------
                            # LISTEN FOR "STATUS" WORD
                            #------------------------------------------------------------------
                            if "status" or "wie ist dein status" in text.lower():
                                states_car_mp3_files = [f for f in os.listdir(states_car_mp3_fldr) if f.endswith(".mp3")]
                                self.vtext = "Status"
                                states_car_random_mp3 = random.choice(states_car_mp3_files)
                                states_car_mp3_path = os.path.join(states_car_mp3_fldr, states_car_random_mp3)
                                sound = AudioSegment.from_file(states_car_mp3_path, format="mp3")
                                play(sound)
                            #------------------------------------------------------------------
                            # LISTEN FOR "TIME" WORD
                            #------------------------------------------------------------------
                            elif "wie spät ist es" or "wie spät is es" or "uhrzeit" or "sag mir wie spät es ist" in text.lower():
                                mp3_files = [f for f in os.listdir(time_mp3_fldr) if f.endswith(".mp3")]
                                self.vtext = "Time:"
                                random_mp3 = random.choice(mp3_files)
                                mp3_path = os.path.join(time_mp3_fldr, random_mp3)
                                sound = AudioSegment.from_file(mp3_path, format="mp3")
                                play(sound)
                            #------------------------------------------------------------------
                            # WHEN NOTHING OF THE ABOVE IS RECOGNIZED
                            #------------------------------------------------------------------
                            else:
                                self.vinfo = "what?"
                                what_mp3_files = [f for f in os.listdir(what_mp3_fldr) if f.endswith(".mp3")]
                                if what_mp3_files:
                                    what_random_mp3 = random.choice(what_mp3_files)
                                    what_mp3_path = os.path.join(what_mp3_fldr, what_random_mp3)
                                    sound = AudioSegment.from_file(what_mp3_path, format="mp3")
                                    play(sound)
                                    self.vinfo = what_random_mp3
                        else:
                            self.vinfo = "cancel"
                    except sr.UnknownValueError:
                        # Handle unknown value error
                        print("UnknownValueError")
                        self.vinfo = "UnknownValueError"
            except:
                pass

    def _update_dev001(
        self,
        l_img10,
        l_img11,
        l_img12,
        l_img13,
        l_img14,
        l_img15,
        l_img18,
        l_img19,
        l_img20,
        l_img23,
        l_img80,
        l_img81,
        localimagelist01,
        localimagelist02,
    ):
        #------------------------------------------------------------------------------
        # SIMULATION
        #------------------------------------------------------------------------------
        #               #00  #01  #02
        val_min      = [  0,   0,   0]
        val_max      = [310, 100, 200]
        val_sim      = [ 5,  10,  14] #HIGHER NUMBER FASTER SIMULATION
        val_min, val_max, val_sim = get_gauge_scale_lists(datadir, DEVICE_B_txt[1], val_min, val_max, val_sim)
        self._consume_gauge_scale_refresh()
        val_conf_min = [  0,   0,   0]
        if btn_states_SW[3] == True:
            for i in range(3):
                self.val_cnt_sim[i] += val_sim[i] if self.val_cnt_sim_updn[i] else -val_sim[i]
                if self.val_cnt_sim[i] > val_max[i]:
                    self.val_cnt_sim_updn[i], self.val_cnt_sim[i] = False, self.val_cnt_sim[i] - val_sim[i]
                elif self.val_cnt_sim[i] < val_min[i]:
                    self.val_cnt_sim_updn[i], self.val_cnt_sim[i] = True, self.val_cnt_sim[i] + val_sim[i]
        #------------------------------------------------------------------------------
        # UPDATE GPS DATA AND WRITE SPEED DATA
        #------------------------------------------------------------------------------
        #--------------------------------------------------------------------------
        # GET NEW GPS DATA
        #--------------------------------------------------------------------------
        if btn_states_HW[0] == True and not btn_states_SW[3]:  #HW0 = GPS MODUL
            if gps_port is not None:
                read.gps_data()
        #--------------------------------------------------------------------------
        # WRITE SPEED VARIABLE TO 7SEG VARIABLE
        #--------------------------------------------------------------------------
        if btn_states_SW[3]:
            seven_seg_speed = self.val_cnt_sim[0]
        elif btn_states_SW[0] and not btn_states_SW[1]:
            seven_seg_speed = aldl_vehicle_speed_mph
        elif not btn_states_SW[0] and not btn_states_SW[1]:
            seven_seg_speed = aldl_vehicle_speed_kph
        elif btn_states_HW[0] and btn_states_SW[1]:
            if btn_states_SW[0]:
                seven_seg_speed = gps_mph_0
            else:
                seven_seg_speed = gps_kph_0
        else:
            if btn_states_SW[0]:
                seven_seg_speed = aldl_vehicle_speed_mph
            else:
                seven_seg_speed = aldl_vehicle_speed_kph
        #------------------------------------------------------------------------------
        # UPDATE VOICECOMMAND TEXT IN TOTAL DISPLAY
        #------------------------------------------------------------------------------
        if btn_states_FNKT[1] == True:
            self._set_voice_text(0, self.vinfo)
            self._set_voice_text(1, self.vtext)
            self._set_voice_text(2, self.activation_word_info)
        else:
            self._set_voice_text(0, "---")
            self._set_voice_text(1, "---")
            self._set_voice_text(2, "SpeechRecognition is off")
        #------------------------------------------------------------------------------
        # UPDATE DEV001G000 (SPEED)
        #------------------------------------------------------------------------------
        if not hasattr(self, "old_bar_leds"):
            self.old_bar_leds = {}

        speed_int = int(seven_seg_speed)

        val_DEV001G000 = self._scaled_led_count(speed_int, val_min[0], val_max[0], self.ammount_DEV001G000)

        def get_led_image(i, on):
            if i < 7:
                return l_img15 if on else l_img12
            elif i == 7:
                return l_img81 if on else l_img11
            return l_img80 if on else l_img10

        for i in range(val_conf_min[0], self.ammount_DEV001G000):
            is_on = btn_states_FNKT[3] and val_DEV001G000 >= i + 1
            img = get_led_image(i, is_on)
            if self.old_bar_leds.get(i) != img:
                self.led_DEV001G000[i].config(image=img)
                self.old_bar_leds[i] = img
        #------------------------------------------------------------------------------
        # UPDATE DEV001G001 (SIGNAL)
        #------------------------------------------------------------------------------
        if not hasattr(self, "old_signal_leds"):
            self.old_signal_leds = {}

        if btn_states_SW[3] == False:
            seven_seg_DEV001G001 = speed_int / 10
        else:
            seven_seg_DEV001G001 = self.val_cnt_sim[1]

        perc_DEV001G001 = self._scaled_led_count(seven_seg_DEV001G001, val_min[1], val_max[1], self.ammount_DEV001G001)

        for i in range(val_conf_min[1], self.ammount_DEV001G001):
            is_on = btn_states_FNKT[3] and (perc_DEV001G001 >= i + 1)
            img = l_img13 if is_on else l_img14
            if self.old_signal_leds.get(i) != img:
                self.led_DEV001G001[i].config(image=img)
                self.old_signal_leds[i] = img
        #------------------------------------------------------------------------------
        # UPDATE DEV001G002 (TUNING)
        #------------------------------------------------------------------------------
        if not hasattr(self, "old_tuning_leds"):
            self.old_tuning_leds = {}

        if btn_states_SW[3] == False:
            seven_seg_DEV001G002 = speed_int / 15
        else:
            seven_seg_DEV001G002 = self.val_cnt_sim[2]

        perc_DEV001G002 = self._scaled_led_count(seven_seg_DEV001G002, val_min[2], val_max[2], self.ammount_DEV001G002)

        for i in range(val_conf_min[2], self.ammount_DEV001G002):
            is_on = btn_states_FNKT[3] and (perc_DEV001G002 >= i + 1)
            img = l_img13 if is_on else l_img14
            if self.old_tuning_leds.get(i) != img:
                self.led_DEV001G002[i].config(image=img)
                self.old_tuning_leds[i] = img
        #------------------------------------------------------------------------------
        # DEV001 VOICEBOX
        #------------------------------------------------------------------------------
        update_voicebox_animation(
            self,
            theme,
            THEME_B_txt,
            style,
            STYLE_B_txt,
            btn_states_FNKT[3],
            l_img18,
            l_img19,
            l_img20,
            l_img23,
        )
        update_voicebox_status(
            self,
            theme,
            THEME_B_txt,
            btn_states_FNKT,
            speed_int,
            localimagelist01,
            localimagelist02,
        )

        return seven_seg_speed

    def _update_dev002(self, images):
        l_img16 = images["rpm_on"]
        l_img17 = images["rpm_off"]
        l_img30 = images["gauge_1_off_low"]
        l_img31 = images["gauge_1_off_high"]
        l_img32 = images["gauge_1_on_low"]
        l_img33 = images["gauge_1_on_high"]
        l_img34 = images["gauge_warning_off"]
        l_img40 = images["gauge_2_off_low"]
        l_img41 = images["gauge_2_off_high"]
        l_img42 = images["gauge_2_on_low"]
        l_img43 = images["gauge_2_on_high"]
        l_img44 = images["gauge_warning_on"]

        #               #00  #01  #02  #03  #04  #05  #06  #07  #08  #09
        val_min      = [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0]
        val_max      = [990, 160, 160, 160, 160,  57, 160, 600, 150, 100]
        val_sim      = [ 20,  10,  14,   8,   2,   6,  10,   7,   8,   9] #HIGHER NUMBER FASTER SIMULATION
        val_min, val_max, val_sim = get_gauge_scale_lists(datadir, DEVICE_B_txt[2], val_min, val_max, val_sim)
        force_gauge_refresh = self._consume_gauge_scale_refresh()
        val_conf_min = [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0]

        if btn_states_SW[3] == True:
            for i in range(len(val_sim)):
                self.val_cnt_sim[i] += val_sim[i] if self.val_cnt_sim_updn[i] else -val_sim[i]
                if self.val_cnt_sim[i] > val_max[i]:
                    self.val_cnt_sim_updn[i], self.val_cnt_sim[i] = False, self.val_cnt_sim[i] - val_sim[i]
                elif self.val_cnt_sim[i] < val_min[i]:
                    self.val_cnt_sim_updn[i], self.val_cnt_sim[i] = True, self.val_cnt_sim[i] + val_sim[i]

        # ADS MODULE 0to100 = [30, 35, 40, 45, 50, 55, 57] # if LG06V >= val 43=50%
        if btn_states_HW[6] == True:
            try:
                a_chan0 = AnalogIn(ads, ADS.P0) #DATA FROM ANALOG INPUT 0
                aldl_fuel_capacity = '%.0f'% (float(a_chan0.value)*val_max[5]/32768.0) #TANKINHALT 0-57 LITER
            except:
                aldl_fuel_capacity = val_min[5]
        else:
            aldl_fuel_capacity = val_min[5]

        seg_DEV002 = [0,1,2,3,4,5,6]
        if btn_states_SW[3] == False:  # LIVE
            seg_DEV002[0] = int(aldl_engine_speed)
            seg_DEV002[1] = int(aldl_mainfold_air_temp)
            seg_DEV002[2] = int(aldl_coolant_temp)
            seg_DEV002[3] = int(aldl_coolant_temp)
            seg_DEV002[4] = int(aldl_barometric_pressure)
            seg_DEV002[5] = int(aldl_fuel_capacity)
            seg_DEV002[6] = int(aldl_throttle_pos)
        else:
            seg_DEV002[0] = self.val_cnt_sim[0]
            seg_DEV002[1] = self.val_cnt_sim[1]
            seg_DEV002[2] = self.val_cnt_sim[2]
            seg_DEV002[3] = self.val_cnt_sim[3]
            seg_DEV002[4] = self.val_cnt_sim[4]
            seg_DEV002[5] = self.val_cnt_sim[5]
            seg_DEV002[6] = self.val_cnt_sim[6]

        perc_DEV002 = [0] * 7
        perc_DEV002[0] = self._scaled_led_count(seg_DEV002[0], val_min[0], val_max[0], self.ammount_DEV002G000)
        for i in range(1, len(perc_DEV002)):
            perc_DEV002[i] = self._scaled_led_count(seg_DEV002[i], val_min[i], val_max[i], self.quantity_DEV002[i])

        phase = self.dev002_update_phase
        self.dev002_update_phase = 1 if force_gauge_refresh else (self.dev002_update_phase + 1) % 4

        # DEV002G000 (RPM)
        if force_gauge_refresh or phase == 0:
            if theme in [THEME_B_txt[0], THEME_B_txt[1], THEME_B_txt[2]]:
                for i in range(val_conf_min[0], self.ammount_DEV002G000):
                    is_on = btn_states_FNKT[3] and perc_DEV002[0] >= i + 1
                    image = l_img16 if is_on else l_img17
                    self._set_widget_image(("dev002_g000", i), self.led_DEV002G000[i], image)
            else:
                for i in range(val_conf_min[0], self.ammount_DEV002G000):
                    is_on = btn_states_FNKT[3] and perc_DEV002[0] >= i + 1
                    image = l_img16[i] if is_on else l_img17[i]
                    self._set_widget_image(("dev002_g000", i), self.led_DEV002G000[i], image)

        # DEV002 GAUGES 1-6
        parameters = [
            (1, l_img33, l_img32, l_img31, l_img30),
            (2, l_img43, l_img42, l_img41, l_img40),
            (3, l_img43, l_img42, l_img41, l_img40),
            (4, l_img33, l_img32, l_img31, l_img30),
            (5, l_img33, l_img32, l_img31, l_img30),
            (6, l_img43, l_img42, l_img41, l_img40),
        ]

        active_parameters = parameters
        if force_gauge_refresh:
            active_parameters = parameters
        elif phase == 1:
            active_parameters = parameters[:3]
        elif phase == 2:
            active_parameters = parameters[3:]
        else:
            active_parameters = []

        if btn_states_FNKT[3]:
            for param_index, img1_low, img2_low, img1_high, img2_high in active_parameters:
                for i in range(val_conf_min[param_index], self.quantity_DEV002[param_index]):
                    if perc_DEV002[param_index] >= i + 1:
                        image = img1_low if i < 8 else img2_low
                    else:
                        image = img1_high if i < 8 else img2_high
                    self._set_widget_image(
                        ("dev002_gauge", param_index, i),
                        self.led_DEV002[param_index][i],
                        image,
                    )
        else:
            for param_index, img1_low, img2_low, img1_high, img2_high in active_parameters:
                for i in range(val_conf_min[param_index], self.quantity_DEV002[param_index]):
                    image = img1_high if i < 8 else img2_high
                    self._set_widget_image(
                        ("dev002_gauge", param_index, i),
                        self.led_DEV002[param_index][i],
                        image,
                    )

        if btn_states_SW[3] == False:
            seven_seg_DEV002G007 = int(aldl_battery_voltage)
            seven_seg_DEV002G008 = int(aldl_fuel_pump_voltage)
            seven_seg_DEV002G009 = int(aldl_throttle_pos_v)
        else:
            seven_seg_DEV002G007 = self.val_cnt_sim[7]
            seven_seg_DEV002G008 = self.val_cnt_sim[8]
            seven_seg_DEV002G009 = self.val_cnt_sim[9]

        if force_gauge_refresh or phase == 3:
            aux_gauges = [
                (seven_seg_DEV002G007, self.ammount_DEV002G007, self.led_DEV002G007, 7),
                (seven_seg_DEV002G008, self.ammount_DEV002G008, self.led_DEV002G008, 8),
                (seven_seg_DEV002G009, self.ammount_DEV002G009, self.led_DEV002G009, 9),
            ]
            for value, amount, leds, value_index in aux_gauges:
                percentage = self._scaled_led_count(value, val_min[value_index], val_max[value_index], amount)
                for i in range(val_conf_min[value_index], amount):
                    is_on = btn_states_FNKT[3] and percentage >= i + 1
                    if i == 0:
                        image = l_img32 if is_on else l_img30
                    elif i == 1:
                        image = l_img44 if is_on else l_img34
                    else:
                        image = l_img42 if is_on else l_img40
                    self._set_widget_image(("dev002_aux", value_index, i), leds[i], image)

            # DEV002 INFORMATION CENTER
            infocenter_states = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
            for i, is_on in enumerate(infocenter_states):
                image = infocenterON_img_list[i] if is_on else infocenterOF_img_list[i]
                self._set_widget_image(("dev002_infocenter", i), self.led_DEV002IC[i], image)

        # UPDATE DEV002 DIGITAL I/O todo
        #button_pin = aw001.get_pin(0)  # Button on AW io 1
        #button_pin.direction = digitalio.Direction.INPUT
        #val_io001_01 = button_pin.value

        return (
            seg_DEV002,
            seven_seg_DEV002G007,
            seven_seg_DEV002G008,
            seven_seg_DEV002G009,
        )

    def _gps_reception_bars(self):
        try:
            sats = int(gps_num_sats)
        except (TypeError, ValueError):
            sats = 0
        try:
            fix_quality = int(gps_fix_quality)
        except (TypeError, ValueError):
            fix_quality = 0

        if fix_quality <= 0 or sats <= 0:
            level = 0
        elif sats >= 8:
            level = 4
        elif sats >= 6:
            level = 3
        elif sats >= 4:
            level = 2
        else:
            level = 1

        bars = "|" * level + " " * (4 - level)
        return f"[{bars}] {sats:02d}"

    def _update_sysinfo(self, dev002_values=None):
        # Initialisiere 8 Labels für sysinfo global und leer
        labels_changed = self.update_labels()
        if theme not in THEME_B_txt[0:3] + THEME_B_txt[3:11] + THEME_B_txt[15:17]:
            return

        if device == DEVICE_B_txt[1]:
            if btn_states_PB != "pb01":
                self._hide_gps_reception_label()
            if btn_states_PB == "pb00":
                if sys_linux:
                    self._refresh_system_data()
                    values = [
                        sys_diskused,
                        sys_diskmax,
                        sys_memused,
                        sys_memmax,
                        sys_cpuload,
                        sys_cputemp,
                        self.update_duration,
                    ]
                else:
                    values = ["--.--", "--.--", "--.--", "--.--", "--.--", "--.--", self.update_duration]
            elif btn_states_PB == "pb01":
                values = [
                    gps_time,
                    gps_date,
                    gps_altitude,
                    gps_lat_str,
                    gps_long_str,
                    gps_altitude_units,
                    gps_lon_dir,
                    gps_lat_dir,
                ]
            elif btn_states_PB == "pb02":
                values = [
                    gps_mph_0,
                    gps_kph_0,
                    gps_odo_imperial_0str,
                    gps_odo_metric_0str,
                    self.update_duration,
                ]
            elif btn_states_PB == "pb03":
                values = [
                    odo_trip_gps_imperial_old,
                    odo_trip_gps_metric_old,
                    odo_total_gps_imperial_old,
                    odo_total_gps_metric_old,
                    self.update_duration,
                ]
            elif btn_states_PB == "pb04":
                values = [
                    odo_trip_aldl_imperial_old,
                    odo_trip_aldl_metric_old,
                    odo_total_aldl_imperial_old,
                    odo_total_aldl_metric_old,
                    self.update_duration,
                ]
            else:
                return

            for index, value in enumerate(values):
                self._set_sysinfo_text(index, value)
            if btn_states_PB == "pb01":
                self._set_gps_reception_text(self._gps_reception_bars())
            return

        if device != DEVICE_B_txt[2] or dev002_values is None:
            return

        self._update_dev002_pb_value_labels(dev002_values)

        if btn_states_PB != "pb09" and labels_changed:
            self._place_label_7SEG002()
            for label in self.lbls_sysinfo:
                label.place_forget()

        if btn_states_PB == "pb09": # POWER BUTTON
            if labels_changed:
                self._hide_label_7SEG002()
            if sys_linux and btn_states_FNKT[2]:
                self._refresh_system_data()
                sys_info = [
                    sys_diskused,
                    sys_diskmax,
                    sys_memused,
                    sys_memmax,
                    sys_cputemp,
                    sys_cpuload,
                    self.update_duration,
                ]
            else:
                sys_info = ["- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -"]

            for i in range(7):
                self._set_sysinfo_text(i, sys_info[i])
            self._set_sysinfo_text(7, self.update_duration)
        elif btn_states_PB in dev002_values:
            if self.label_7SEG002 is None:
                self._place_label_7SEG002()
            new_value = str(dev002_values[btn_states_PB]).zfill(4)
            if self.old_values.get("dev002_pb_value") != new_value:
                self.label_7SEG002.config(text=new_value, anchor="c")
                self.old_values["dev002_pb_value"] = new_value

    def _update_digital_displays(self, seven_seg_speed=None, seg_DEV002=None):
        if device == DEVICE_B_txt[1] and seven_seg_speed is not None:
            if self.old_values.get("speed_label") != seven_seg_speed:
                self.label_7SEG001.config(text=str(seven_seg_speed).zfill(3))
                self.label_7SEG003.config(text=str(seven_seg_speed).zfill(6))
                self.old_values["speed_label"] = seven_seg_speed

        if device == DEVICE_B_txt[2] and seg_DEV002 is not None:
            new_rpm = seg_DEV002[0]
            if self.old_values.get("rpm_label") != new_rpm:
                self.label_7SEG001.config(text=str(new_rpm).zfill(3), anchor="nw")
                self.old_values["rpm_label"] = new_rpm

    def _get_theme_assets(self):
        theme_assets_key = (device, theme, style)
        if self.theme_assets_key != theme_assets_key:
            self.theme_assets = {
                "widgets": self._get_widget_images(),
                "updates": self._get_update_images(),
            }
            self.theme_assets_key = theme_assets_key
        return self.theme_assets

    def _get_widget_images(self):
        l_img01 = None
        l_img02 = None
        l_img03 = None
        l_img04 = None
        l_img05 = None
        l_img06 = None
        l_img07 = None
        l_img08 = None
        l_img09 = None
        l_img15 = None
        l_img16 = None
        l_img17 = None
        l_img18 = None
        l_img19 = None
        l_img20 = None
        l_img61 = None
        l_img64 = None
        l_img65 = None
        l_img66 = None
        l_img71 = None
        l_img74 = None
        l_img75 = None
        l_img76 = None
        l_img80 = None
        l_img81 = None
        localimagelist01 = []
        localimagelist02 = []

        if style == STYLE_B_txt[0]:
            if theme in [THEME_B_txt[0]]:
                localimagelist01 = list(vbON_PILOT_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_PILOT_img_list)
                l_img01 = sledON_img_list[30] #MPH
                l_img02 = sledON_img_list[29] #KPH
                l_img06 = ledFU_img_list[9] #HI LO VHF
                l_img07 = ledFU_img_list[11] #HI LO VHF
                l_img08 = sledON_img_list[33] #RPMi
                l_img09 = sledON_img_list[34] #RPMm
                l_img80 = ledFU_img_list[6] #SELECT BUTTONS
                l_img81 = ledOF_img_list[6] #SELECT BUTTONS
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
            elif theme in [THEME_B_txt[1]]:
                localimagelist01 = list(vbON_S01_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S01_img_list)
                l_img01 = sledON_img_list[32] #MPH
                l_img02 = sledON_img_list[31] #KPH
                l_img06 = ledFU_img_list[9] #HI LO VHF
                l_img07 = ledFU_img_list[11] #HI LO VHF
                l_img08 = sledON_img_list[35] #RPMi
                l_img09 = sledON_img_list[36] #RPMm
                l_img80 = ledFU_img_list[6] #SELECT BUTTONS
                l_img81 = ledOF_img_list[6] #SELECT BUTTONS
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
            elif theme in [THEME_B_txt[2]]:
                localimagelist01 = list(vbON_S02_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S02_img_list)
                l_img01 = sledON_img_list[32] #MPH
                l_img02 = sledON_img_list[31] #KPH
                l_img06 = ledFU_img_list[9] #HI LO VHF
                l_img07 = ledFU_img_list[11] #HI LO VHF
                l_img08 = sledON_img_list[35] #RPMi
                l_img09 = sledON_img_list[36] #RPMm
                l_img80 = ledFU_img_list[6] #SELECT BUTTONS
                l_img81 = ledOF_img_list[6] #SELECT BUTTONS
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
            elif theme in [THEME_B_txt[3]]:
                l_img01 = sledON_img_list[10] #MPH
                l_img02 = sledON_img_list[9] #KPH
                l_img03 = segmentKA_img_list[5] #GPS SPEED GAUGE
                l_img04 = segmentKA_img_list[4] #ALDL SPEED GAUGE
                l_img05 = segmentKA_img_list[6] #SIM SPEED GAUGE
                l_img06 = sledON_img_list[7] #HI LO VHF
                l_img07 = sledOF_img_list[7] #HI LO VHF
                l_img08 = sledON_img_list[17] #RPMi
                l_img09 = sledON_img_list[18] #RPMm
                l_img80 = ledFU_img_list[62] #YE
                l_img81 = ledOF_img_list[61] #GY
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
                localimagelist01 = list(vbON_S03_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S03_img_list)
            elif theme in [THEME_B_txt[4]]:
                l_img01 = sledON_img_list[10] #MPH
                l_img02 = sledON_img_list[9] #KPH
                l_img03 = segmentKA_img_list[5] #GPS SPEED GAUGE
                l_img04 = segmentKA_img_list[4] #ALDL SPEED GAUGE
                l_img05 = segmentKA_img_list[6] #SIM SPEED GAUGE
                l_img06 = sledON_img_list[8] #HI LO VHF
                l_img07 = sledOF_img_list[8] #HI LO VHF
                l_img08 = sledON_img_list[17] #RPMi
                l_img09 = sledON_img_list[18] #RPMm
                l_img80 = ledFU_img_list[62] #YE
                l_img81 = ledOF_img_list[62] #YEDK
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
                localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S04_img_list)
            elif theme in [THEME_B_txt[5]]:
                l_img01 = sledON_img_list[10] #MPH
                l_img02 = sledON_img_list[9] #KPH
                l_img03 = segmentKA_img_list[5] #GPS SPEED GAUGE
                l_img04 = segmentKA_img_list[4] #ALDL SPEED GAUGE
                l_img05 = segmentKA_img_list[6] #SIM SPEED GAUGE
                l_img06 = sledON_img_list[8] #HI LO VHF
                l_img07 = sledOF_img_list[8] #HI LO VHF
                l_img08 = sledON_img_list[17] #RPMi
                l_img09 = sledON_img_list[18] #RPMm
                l_img80 = ledFU_img_list[62] #YE
                l_img81 = ledOF_img_list[62] #YEDK
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
                localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S04_img_list)
            elif theme in [THEME_B_txt[6]]:
                l_img01 = sledON_img_list[10] #MPH
                l_img02 = sledON_img_list[9] #KPH
                l_img03 = segmentKA_img_list[5] #GPS SPEED GAUGE
                l_img04 = segmentKA_img_list[4] #ALDL SPEED GAUGE
                l_img05 = segmentKA_img_list[6] #SIM SPEED GAUGE
                l_img06 = sledON_img_list[8] #HI LO VHF
                l_img07 = sledOF_img_list[8] #HI LO VHF
                l_img08 = sledON_img_list[17] #RPMi
                l_img09 = sledON_img_list[18] #RPMm
                l_img80 = ledFU_img_list[62] #YE
                l_img81 = ledOF_img_list[62] #YEDK
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
                localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S04_img_list)
            elif theme in [THEME_B_txt[7]]:
                l_img01 = sledON_img_list[10] #MPH
                l_img02 = sledON_img_list[9] #KPH
                l_img03 = segmentKA_img_list[5] #GPS SPEED GAUGE
                l_img04 = segmentKA_img_list[4] #ALDL SPEED GAUGE
                l_img05 = segmentKA_img_list[6] #SIM SPEED GAUGE
                l_img06 = sledON_img_list[8] #HI LO VHF
                l_img07 = sledOF_img_list[8] #HI LO VHF
                l_img08 = sledON_img_list[25] #RPMi
                l_img09 = sledON_img_list[26] #RPMm
                l_img80 = ledFU_img_list[62] #YE
                l_img81 = ledOF_img_list[62] #YEDK
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
                localimagelist01 = list(vbON_OTTO_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_OTTO_img_list)
            elif theme in [THEME_B_txt[8]]:
                l_img01 = sledON_img_list[12] #MPH
                l_img02 = sledON_img_list[11] #KPH
                l_img03 = segmentKA_img_list[7] #GPS SPEED GAUGE
                l_img04 = segmentKA_img_list[7] #ALDL SPEED GAUGE
                l_img05 = segmentKA_img_list[7] #SIM SPEED GAUGE
                l_img06 = sledON_img_list[8] #HI LO VHF
                l_img07 = sledOF_img_list[8] #HI LO VHF
                l_img08 = sledON_img_list[19] #RPMi
                l_img09 = sledON_img_list[20] #RPMm
                l_img80 = ledFU_img_list[62] #YE
                l_img81 = ledOF_img_list[62] #YEDK
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
                localimagelist01 = list(vbON_MAX_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_MAX_img_list)
            elif theme in [THEME_B_txt[9]]:
                l_img01 = sledON_img_list[10] #MPH
                l_img02 = sledON_img_list[9] #KPH
                l_img03 = segmentKA_img_list[5] #GPS SPEED GAUGE
                l_img04 = segmentKA_img_list[4] #ALDL SPEED GAUGE
                l_img05 = segmentKA_img_list[6] #SIM SPEED GAUGE
                l_img06 = sledON_img_list[8] #HI LO VHF
                l_img07 = sledOF_img_list[8] #HI LO VHF
                l_img08 = sledON_img_list[17] #RPMi
                l_img09 = sledON_img_list[18] #RPMm
                l_img80 = ledFU_img_list[62] #YE
                l_img81 = ledOF_img_list[62] #YEDK
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
            elif theme in [THEME_B_txt[10]]:
                l_img01 = sledON_img_list[10] #MPH
                l_img02 = sledON_img_list[9] #KPH
                l_img03 = segmentKA_img_list[5] #GPS SPEED GAUGE
                l_img04 = segmentKA_img_list[4] #ALDL SPEED GAUGE
                l_img05 = segmentKA_img_list[6] #SIM SPEED GAUGE
                l_img06 = sledON_img_list[8] #HI LO VHF
                l_img07 = sledOF_img_list[8] #HI LO VHF
                l_img08 = sledON_img_list[17] #RPMi
                l_img09 = sledON_img_list[18] #RPMm
                l_img80 = ledFU_img_list[62] #YE
                l_img81 = ledOF_img_list[62] #YEDK
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
            elif theme in [THEME_B_txt[11]]:
                pass
            elif theme in [THEME_B_txt[12]]:
                pass
            elif theme in [THEME_B_txt[13]]:
                pass
            elif theme in [THEME_B_txt[14]]:
                pass
            elif theme in [THEME_B_txt[15]]:
                l_img01 = lcarsON_img_list[0]
                l_img02 = lcarsOF_img_list[0]
                l_img03 = segmentKA_img_list[11]
            elif theme in [THEME_B_txt[16]]:
                l_img01 = lcarsON_img_list[0]
                l_img02 = lcarsOF_img_list[0]
                l_img03 = segmentKA_img_list[11]
        elif style == STYLE_B_txt[1]:
            if theme in [THEME_B_txt[0]]:
                localimagelist01 = list(vbON_PILOT_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_PILOT_img_list)
                l_img01 = sledON_img_list[30] #MPH
                l_img02 = sledON_img_list[29] #KPH
                l_img06 = ledFU_img_list[9] #HI LO VHF
                l_img07 = ledFU_img_list[11] #HI LO VHF
                l_img08 = sledON_img_list[33] #RPMi
                l_img09 = sledON_img_list[34] #RPMm
                l_img80 = ledFU_img_list[6] #SELECT BUTTONS
                l_img81 = ledOF_img_list[6] #SELECT BUTTONS
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
            elif theme in [THEME_B_txt[1]]:
                localimagelist01 = list(vbON_S01_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S01_img_list)
                l_img01 = sledON_img_list[32] #MPH
                l_img02 = sledON_img_list[31] #KPH
                l_img06 = ledFU_img_list[9] #HI LO VHF
                l_img07 = ledFU_img_list[11] #HI LO VHF
                l_img08 = sledON_img_list[35] #RPMi
                l_img09 = sledON_img_list[36] #RPMm
                l_img80 = ledFU_img_list[6] #SELECT BUTTONS
                l_img81 = ledOF_img_list[6] #SELECT BUTTONS
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
            elif theme in [THEME_B_txt[2]]:
                localimagelist01 = list(vbON_S02_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S02_img_list)
                l_img01 = sledON_img_list[32] #MPH
                l_img02 = sledON_img_list[31] #KPH
                l_img06 = ledFU_img_list[9] #HI LO VHF
                l_img07 = ledFU_img_list[11] #HI LO VHF
                l_img08 = sledON_img_list[35] #RPMi
                l_img09 = sledON_img_list[36] #RPMm
                l_img80 = ledFU_img_list[6] #SELECT BUTTONS
                l_img81 = ledOF_img_list[6] #SELECT BUTTONS
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
            elif theme in [THEME_B_txt[3]]:
                l_img01 = sledON_img_list[14] #MPH
                l_img02 = sledON_img_list[13] #KPH
                l_img03 = segmentKI_img_list[5] #GPS SPEED GAUGE
                l_img04 = segmentKI_img_list[4] #ALDL SPEED GAUGE
                l_img05 = segmentKI_img_list[6] #SIM SPEED GAUGE
                l_img06 = sledON_img_list[7] #HI LO VHF
                l_img07 = sledOF_img_list[7] #HI LO VHF
                l_img08 = sledON_img_list[21] #RPMi
                l_img09 = sledON_img_list[22] #RPMm
                l_img80 = ledFU_img_list[62] #YE
                l_img81 = ledOF_img_list[61] #GY
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
                localimagelist01 = list(vbON_S03_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S03_img_list)
            elif theme in [THEME_B_txt[4]]:
                l_img01 = sledON_img_list[14] #MPH
                l_img02 = sledON_img_list[13] #KPH
                l_img03 = segmentKI_img_list[5] #GPS SPEED GAUGE
                l_img04 = segmentKI_img_list[4] #ALDL SPEED GAUGE
                l_img05 = segmentKI_img_list[6] #SIM SPEED GAUGE
                l_img06 = sledON_img_list[8] #HI LO VHF
                l_img07 = sledOF_img_list[8] #HI LO VHF
                l_img08 = sledON_img_list[21] #RPMi
                l_img09 = sledON_img_list[22] #RPMm
                l_img80 = ledFU_img_list[62] #YE
                l_img81 = ledOF_img_list[62] #YEDK
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
                localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S04_img_list)
            elif theme in [THEME_B_txt[5]]:
                l_img01 = sledON_img_list[14] #MPH
                l_img02 = sledON_img_list[13] #KPH
                l_img03 = segmentKI_img_list[5] #GPS SPEED GAUGE
                l_img04 = segmentKI_img_list[4] #ALDL SPEED GAUGE
                l_img05 = segmentKI_img_list[6] #SIM SPEED GAUGE
                l_img06 = sledON_img_list[8] #HI LO VHF
                l_img07 = sledOF_img_list[8] #HI LO VHF
                l_img08 = sledON_img_list[21] #RPMi
                l_img09 = sledON_img_list[22] #RPMm
                l_img80 = ledFU_img_list[62] #YE
                l_img81 = ledOF_img_list[62] #YEDK
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
                localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S04_img_list)
            elif theme in [THEME_B_txt[6]]:
                l_img01 = sledON_img_list[14] #MPH
                l_img02 = sledON_img_list[13] #KPH
                l_img03 = segmentKI_img_list[5] #GPS SPEED GAUGE
                l_img04 = segmentKI_img_list[4] #ALDL SPEED GAUGE
                l_img05 = segmentKI_img_list[6] #SIM SPEED GAUGE
                l_img06 = sledON_img_list[8] #HI LO VHF
                l_img07 = sledOF_img_list[8] #HI LO VHF
                l_img08 = sledON_img_list[21] #RPMi
                l_img09 = sledON_img_list[22] #RPMm
                l_img80 = ledFU_img_list[62] #YE
                l_img81 = ledOF_img_list[62] #YEDK
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
                localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S04_img_list)
            elif theme in [THEME_B_txt[7]]:
                l_img01 = sledON_img_list[14] #MPH
                l_img02 = sledON_img_list[13] #KPH
                l_img03 = segmentKI_img_list[5] #GPS SPEED GAUGE
                l_img04 = segmentKI_img_list[4] #ALDL SPEED GAUGE
                l_img05 = segmentKI_img_list[6] #SIM SPEED GAUGE
                l_img06 = sledON_img_list[8] #HI LO VHF
                l_img07 = sledOF_img_list[8] #HI LO VHF
                l_img08 = sledON_img_list[27] #RPMi
                l_img09 = sledON_img_list[28] #RPMm
                l_img80 = ledFU_img_list[62] #YE
                l_img81 = ledOF_img_list[62] #YEDK
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
                localimagelist01 = list(vbON_OTTO_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_OTTO_img_list)
            elif theme in [THEME_B_txt[8]]:
                l_img01 = sledON_img_list[16] #MPH
                l_img02 = sledON_img_list[15] #KPH
                l_img03 = segmentKI_img_list[7] #GPS SPEED GAUGE
                l_img04 = segmentKI_img_list[7] #ALDL SPEED GAUGE
                l_img05 = segmentKI_img_list[7] #SIM SPEED GAUGE
                l_img06 = sledON_img_list[8] #HI LO VHF
                l_img07 = sledOF_img_list[8] #HI LO VHF
                l_img08 = sledON_img_list[23] #RPMi
                l_img09 = sledON_img_list[24] #RPMm
                l_img80 = ledFU_img_list[62] #YE
                l_img81 = ledOF_img_list[62] #YEDK
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
                localimagelist01 = list(vbON_MAX_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_MAX_img_list)
            elif theme in [THEME_B_txt[9]]:
                l_img01 = sledON_img_list[14] #MPH
                l_img02 = sledON_img_list[13] #KPH
                l_img03 = segmentKI_img_list[5] #GPS SPEED GAUGE
                l_img04 = segmentKI_img_list[4] #ALDL SPEED GAUGE
                l_img05 = segmentKI_img_list[6] #SIM SPEED GAUGE
                l_img06 = sledON_img_list[46] #HI LO VHF
                l_img07 = sledOF_img_list[46] #HI LO VHF
                l_img08 = sledON_img_list[21] #RPMi
                l_img09 = sledON_img_list[22] #RPMm
                l_img80 = ledFU_img_list[62] #YE
                l_img81 = ledOF_img_list[62] #YEDK
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
                localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S04_img_list)
            elif theme in [THEME_B_txt[10]]:
                l_img01 = sledON_img_list[14] #MPH
                l_img02 = sledON_img_list[13] #KPH
                l_img03 = segmentKI_img_list[5] #GPS SPEED GAUGE
                l_img04 = segmentKI_img_list[4] #ALDL SPEED GAUGE
                l_img05 = segmentKI_img_list[6] #SIM SPEED GAUGE
                l_img06 = sledON_img_list[8] #HI LO VHF
                l_img07 = sledOF_img_list[8] #HI LO VHF
                l_img08 = sledON_img_list[21] #RPMi
                l_img09 = sledON_img_list[22] #RPMm
                l_img80 = ledFU_img_list[62] #YE
                l_img81 = ledOF_img_list[62] #YEDK
                l_img15 = ledFU_img_list[65] #POWER BTNS GN
                l_img16 = ledFU_img_list[67] #POWER BTNS RD
                l_img17 = ledFU_img_list[69] #POWER BTNS YE
                l_img18 = ledOF_img_list[65] #POWER BTNS GN
                l_img19 = ledOF_img_list[67] #POWER BTNS RD
                l_img20 = ledOF_img_list[69] #POWER BTNS YE
                l_img61 = ledFU_img_list[78] #OHC BU
                l_img64 = ledFU_img_list[81] #OHC RD
                l_img65 = ledFU_img_list[82] #OHC WH
                l_img66 = ledFU_img_list[83] #OHC YE
                l_img71 = ledOF_img_list[78] #OHC BU
                l_img74 = ledOF_img_list[81] #OHC RD
                l_img75 = ledOF_img_list[82] #OHC WH
                l_img76 = ledOF_img_list[83] #OHC YE
                localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S04_img_list)
            elif theme in [THEME_B_txt[11]]:
                pass
            elif theme in [THEME_B_txt[12]]:
                pass
            elif theme in [THEME_B_txt[13]]:
                pass
            elif theme in [THEME_B_txt[14]]:
                pass
            elif theme in [THEME_B_txt[15]]:
                l_img01 = lcarsON_img_list[0]
                l_img02 = lcarsOF_img_list[0]
                l_img03 = segmentKI_img_list[11]
                l_img06 = lcarsON_img_list[7] #HI LO VHF
                l_img07 = lcarsOF_img_list[7] #HI LO VHF
            elif theme in [THEME_B_txt[16]]:
                l_img01 = lcarsON_img_list[0]
                l_img02 = lcarsOF_img_list[0]
                l_img03 = segmentKI_img_list[11]
                l_img06 = lcarsON_img_list[7] #HI LO VHF
                l_img07 = lcarsOF_img_list[7]

        return {
            "l_img01": l_img01,
            "l_img02": l_img02,
            "l_img03": l_img03,
            "l_img04": l_img04,
            "l_img05": l_img05,
            "l_img06": l_img06,
            "l_img07": l_img07,
            "l_img08": l_img08,
            "l_img09": l_img09,
            "l_img15": l_img15,
            "l_img16": l_img16,
            "l_img17": l_img17,
            "l_img18": l_img18,
            "l_img19": l_img19,
            "l_img20": l_img20,
            "l_img61": l_img61,
            "l_img64": l_img64,
            "l_img65": l_img65,
            "l_img66": l_img66,
            "l_img71": l_img71,
            "l_img74": l_img74,
            "l_img75": l_img75,
            "l_img76": l_img76,
            "l_img80": l_img80,
            "l_img81": l_img81,
            "localimagelist01": localimagelist01,
            "localimagelist02": localimagelist02,
        }

    def _get_update_images(self):
        l_img18 = None
        l_img19 = None
        l_img20 = None
        l_img23 = None
        l_img30 = None
        l_img31 = None
        l_img32 = None
        l_img33 = None
        l_img34 = None
        l_img40 = None
        l_img41 = None
        l_img42 = None
        l_img43 = None
        l_img44 = None
        localimagelist01 = []
        localimagelist02 = []

        if theme in [THEME_B_txt[0], THEME_B_txt[1], THEME_B_txt[2]]:
            l_img10 = ledOF_img_list[11] #SPEED OFRD
            l_img11 = ledOF_img_list[11] #SPEED OFRD
            l_img12 = ledOF_img_list[11] #SPEED OFRD
            l_img13 = ledFU_img_list[11] #SIGNAL FURD
            l_img14 = ledOF_img_list[11] #SIGNAL OFRD
            l_img80 = ledFU_img_list[11] #SPEED FURD
            l_img81 = ledFU_img_list[11] #SPEED FURD
            l_img15 = ledFU_img_list[11] #SPEED FURD
            l_img16 = ledFU_img_list[11]
            l_img17 = ledOF_img_list[11]
            if theme == THEME_B_txt[0]:
                localimagelist01 = list(vbON_PILOT_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_PILOT_img_list)
                if style == STYLE_B_txt[0]:
                    l_img30 = ledOF_img_list[19] #DEV002GAUGES 1GN
                    l_img31 = ledOF_img_list[19] #DEV002GAUGES 1RD
                    l_img32 = ledFU_img_list[16] #DEV002GAUGES 1GN
                    l_img33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                    l_img34 = ledFU_img_list[18] #DEV002GAUGES 1RD
                    l_img40 = ledOF_img_list[19] #DEV002GAUGES 2GN
                    l_img41 = ledOF_img_list[19] #DEV002GAUGES 2RD
                    l_img42 = ledFU_img_list[16] #DEV002GAUGES 2GN
                    l_img43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                    l_img44 = ledFU_img_list[18] #DEV002GAUGES 2RD
                    l_img18 = ledFU_img_list[74] #VOICEBOX34 BULB_RD ONMAX
                    l_img19 = ledMI_img_list[74] #VOICEBOX34 BULB_RD ONNORM
                    l_img20 = ledLO_img_list[74] #VOICEBOX34 BULB_RD ONMIN
                    l_img23 = ledOF_img_list[74] #VOICEBOX34 BULB_RD OF
                elif style == STYLE_B_txt[1]:
                    l_img30 = ledOF_img_list[19] #DEV002GAUGES 1GN
                    l_img31 = ledOF_img_list[19] #DEV002GAUGES 1RD
                    l_img32 = ledFU_img_list[16] #DEV002GAUGES 1GN
                    l_img33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                    l_img34 = ledFU_img_list[18] #DEV002GAUGES 1RD
                    l_img40 = ledOF_img_list[19] #DEV002GAUGES 2GN
                    l_img41 = ledOF_img_list[19] #DEV002GAUGES 2RD
                    l_img42 = ledFU_img_list[16] #DEV002GAUGES 2GN
                    l_img43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                    l_img44 = ledFU_img_list[18] #DEV002GAUGES 2RD
                    l_img18 = ledFU_img_list[74] #VOICEBOX34 BULB_RD ONMAX
                    l_img19 = ledMI_img_list[74] #VOICEBOX34 BULB_RD ONNORM
                    l_img20 = ledLO_img_list[74] #VOICEBOX34 BULB_RD ONMIN
                    l_img23 = ledOF_img_list[74] #VOICEBOX34 BULB_RD OF
            elif theme == THEME_B_txt[1]:
                localimagelist01 = list(vbON_S01_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S01_img_list)
                if style == STYLE_B_txt[0]:
                    l_img30 = ledOF_img_list[20] #DEV002GAUGES 1GN
                    l_img31 = ledOF_img_list[18] #DEV002GAUGES 1RD
                    l_img32 = ledFU_img_list[20] #DEV002GAUGES 1GN
                    l_img33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                    l_img34 = ledFU_img_list[18] #DEV002GAUGES 1RD
                    l_img40 = ledOF_img_list[20] #DEV002GAUGES 2GN
                    l_img41 = ledOF_img_list[18] #DEV002GAUGES 2RD
                    l_img42 = ledFU_img_list[20] #DEV002GAUGES 2GN
                    l_img43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                    l_img44 = ledFU_img_list[18] #DEV002GAUGES 2RD
                    l_img18 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                    l_img19 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                    l_img20 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                    l_img23 = ledOF_img_list[48]
                elif style == STYLE_B_txt[1]:
                    l_img30 = ledOF_img_list[16] #DEV002GAUGES 1GN
                    l_img31 = ledOF_img_list[18] #DEV002GAUGES 1RD
                    l_img32 = ledFU_img_list[16] #DEV002GAUGES 1GN
                    l_img33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                    l_img34 = ledFU_img_list[18] #DEV002GAUGES 1RD
                    l_img40 = ledOF_img_list[16] #DEV002GAUGES 2GN
                    l_img41 = ledOF_img_list[18] #DEV002GAUGES 2RD
                    l_img42 = ledFU_img_list[16] #DEV002GAUGES 2GN
                    l_img43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                    l_img44 = ledFU_img_list[18] #DEV002GAUGES 2RD
                    l_img18 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                    l_img19 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                    l_img20 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                    l_img23 = ledOF_img_list[46]
            elif theme == THEME_B_txt[2]:
                localimagelist01 = list(vbON_S02_img_list) #VOICEBOX
                localimagelist02 = list(vbOF_S02_img_list) #VOICEBOX
                if style == STYLE_B_txt[0]:
                    l_img30 = ledOF_img_list[14] #DEV002GAUGES 1GN
                    l_img31 = ledOF_img_list[18] #DEV002GAUGES 1RD
                    l_img32 = ledFU_img_list[14] #DEV002GAUGES 1GN
                    l_img33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                    l_img34 = ledFU_img_list[18] #DEV002GAUGES 1RD
                    l_img40 = ledOF_img_list[14] #DEV002GAUGES 2GN
                    l_img41 = ledOF_img_list[18] #DEV002GAUGES 2RD
                    l_img42 = ledFU_img_list[14] #DEV002GAUGES 2GN
                    l_img43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                    l_img44 = ledFU_img_list[18] #DEV002GAUGES 2RD
                    l_img18 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                    l_img19 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                    l_img20 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                    l_img23 = ledOF_img_list[48]
                elif style == STYLE_B_txt[1]:
                    l_img30 = ledOF_img_list[16] #DEV002GAUGES 1GN
                    l_img31 = ledOF_img_list[18] #DEV002GAUGES 1RD
                    l_img32 = ledFU_img_list[16] #DEV002GAUGES 1GN
                    l_img33 = ledFU_img_list[18] #DEV002GAUGES 1RD
                    l_img34 = ledOF_img_list[16] #DEV002GAUGES 1RD
                    l_img40 = ledOF_img_list[16] #DEV002GAUGES 2GN
                    l_img41 = ledOF_img_list[18] #DEV002GAUGES 2RD
                    l_img42 = ledFU_img_list[16] #DEV002GAUGES 2GN
                    l_img43 = ledFU_img_list[18] #DEV002GAUGES 2RD
                    l_img44 = ledFU_img_list[16] #DEV002GAUGES 2RD
                    l_img18 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                    l_img19 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                    l_img20 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                    l_img23 = ledOF_img_list[46]
        elif theme == THEME_B_txt[3]:
            l_img30 = ledOF_img_list[61] #DEV002GAUGES 1GY
            l_img31 = ledOF_img_list[61] #DEV002GAUGES 1GY
            l_img32 = ledFU_img_list[60] #DEV002GAUGES 1RD
            l_img33 = ledFU_img_list[60] #DEV002GAUGES 1RD
            l_img34 = ledOF_img_list[62] #DEV002GAUGES 1YE
            l_img40 = ledOF_img_list[61] #DEV002GAUGES 2GN
            l_img41 = ledOF_img_list[61] #DEV002GAUGES 2RD
            l_img42 = ledFU_img_list[58] #DEV002GAUGES 2GN
            l_img43 = ledFU_img_list[58] #DEV002GAUGES 2GN
            l_img44 = ledFU_img_list[62] #DEV002GAUGES 2YE
            l_img10 = ledOF_img_list[61] #RPM OF GY
            l_img11 = ledOF_img_list[61] #RPM OF GY
            l_img12 = ledOF_img_list[61] #RPM OF GY
            l_img13 = ledFU_img_list[25] #SIGNAL ONRD
            l_img14 = ledOF_img_list[25] #SIGNAL OFRD
            l_img80 = ledFU_img_list[60] #RD
            l_img81 = ledFU_img_list[62] #YE
            l_img15 = ledFU_img_list[58] #RD
            l_img16 = rpmON_img_list
            l_img17 = rpmOF_img_list
            localimagelist01 = list(vbON_S03_img_list) #VOICEBOX
            localimagelist02 = list(vbOF_S03_img_list) #VOICEBOX
            if style == STYLE_B_txt[0]:
                l_img18 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                l_img19 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                l_img20 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                l_img23 = ledOF_img_list[48] #VOICEBOX34 OF
            elif style == STYLE_B_txt[1]:
                l_img18 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                l_img19 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                l_img20 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                l_img23 = ledOF_img_list[46]
        elif theme == THEME_B_txt[4]:
            l_img30 = ledOF_img_list[60] #DEV002GAUGES 1DK
            l_img31 = ledOF_img_list[60] #DEV002GAUGES 1DK
            l_img32 = ledFU_img_list[60] #DEV002GAUGES 1RD
            l_img33 = ledFU_img_list[60] #DEV002GAUGES 1RD
            l_img34 = ledOF_img_list[62] #DEV002GAUGES 1YE
            l_img40 = ledOF_img_list[58] #DEV002GAUGES 2DK
            l_img41 = ledOF_img_list[58] #DEV002GAUGES 2DK
            l_img42 = ledFU_img_list[58] #DEV002GAUGES 2GN
            l_img43 = ledFU_img_list[58] #DEV002GAUGES 2GN
            l_img44 = ledFU_img_list[62] #DEV002GAUGES 2YE
            l_img10 = ledOF_img_list[60] #RPM RD
            l_img11 = ledOF_img_list[62] #YE
            l_img12 = ledOF_img_list[58] #RPM GN
            l_img13 = ledFU_img_list[32] #SIGNAL ONRD
            l_img14 = ledOF_img_list[32] #SIGNAL OFRD
            l_img80 = ledFU_img_list[60] #RD
            l_img81 = ledFU_img_list[62] #YE
            l_img15 = ledFU_img_list[58] #RD
            l_img16 = rpmON_img_list
            l_img17 = rpmOF_img_list
            localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
            localimagelist02 = list(vbOF_S04_img_list) #VOICEBOX
            if style == STYLE_B_txt[0]:
                l_img18 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                l_img19 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                l_img20 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                l_img23 = ledOF_img_list[48] #VOICEBOX34 OF
            elif style == STYLE_B_txt[1]:
                l_img18 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                l_img19 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                l_img20 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                l_img23 = ledOF_img_list[46]
        elif theme == THEME_B_txt[5]:
            l_img30 = ledOF_img_list[60] #DEV002GAUGES 1DK
            l_img31 = ledOF_img_list[60] #DEV002GAUGES 1DK
            l_img32 = ledFU_img_list[60] #DEV002GAUGES 1RD
            l_img33 = ledFU_img_list[60] #DEV002GAUGES 1RD
            l_img34 = ledOF_img_list[62] #DEV002GAUGES 1YE
            l_img40 = ledOF_img_list[58] #DEV002GAUGES 2DK
            l_img41 = ledOF_img_list[58] #DEV002GAUGES 2DK
            l_img42 = ledFU_img_list[58] #DEV002GAUGES 2GN
            l_img43 = ledFU_img_list[58] #DEV002GAUGES 2GN
            l_img44 = ledFU_img_list[62] #DEV002GAUGES 2YE
            l_img10 = ledOF_img_list[60] #RD
            l_img11 = ledOF_img_list[62] #YE
            l_img12 = ledOF_img_list[58] #RD
            l_img13 = ledFU_img_list[30] #SIGNAL ONRD
            l_img14 = ledOF_img_list[30] #SIGNAL OFRD
            l_img80 = ledFU_img_list[60] #RD
            l_img81 = ledFU_img_list[62] #YE
            l_img15 = ledFU_img_list[58] #RD
            l_img16 = rpmON_img_list
            l_img17 = rpmOF_img_list
            localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
            localimagelist02 = list(vbOF_S04_img_list) #VOICEBOX
            if style == STYLE_B_txt[0]:
                l_img18 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                l_img19 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                l_img20 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                l_img23 = ledOF_img_list[48] #VOICEBOX34 OF
            elif style == STYLE_B_txt[1]:
                l_img18 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                l_img19 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                l_img20 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                l_img23 = ledOF_img_list[46]
        elif theme == THEME_B_txt[6]:
            l_img30 = ledOF_img_list[60] #DEV002GAUGES 1DK
            l_img31 = ledOF_img_list[60] #DEV002GAUGES 1DK
            l_img32 = ledFU_img_list[60] #DEV002GAUGES 1RD
            l_img33 = ledFU_img_list[60] #DEV002GAUGES 1RD
            l_img34 = ledOF_img_list[62] #DEV002GAUGES 1YE
            l_img40 = ledOF_img_list[58] #DEV002GAUGES 2DK
            l_img41 = ledOF_img_list[58] #DEV002GAUGES 2DK
            l_img42 = ledFU_img_list[58] #DEV002GAUGES 2GN
            l_img43 = ledFU_img_list[58] #DEV002GAUGES 2GN
            l_img44 = ledFU_img_list[62] #DEV002GAUGES 2YE
            l_img10 = ledOF_img_list[60] #RD
            l_img11 = ledOF_img_list[62] #YE
            l_img12 = ledOF_img_list[58] #RD
            l_img13 = ledFU_img_list[32] #SIGNAL ONRD
            l_img14 = ledOF_img_list[32] #SIGNAL OFRD
            l_img80 = ledFU_img_list[60] #RD
            l_img81 = ledFU_img_list[62] #YE
            l_img15 = ledFU_img_list[58] #RD
            l_img16 = rpmON_img_list
            l_img17 = rpmOF_img_list
            localimagelist01 = list(vbON_S04_img_list) #VOICEBOX
            localimagelist02 = list(vbOF_S04_img_list) #VOICEBOX
            if style == STYLE_B_txt[0]:
                l_img18 = ledFU_img_list[48] #VOICEBOX34 ONMAX
                l_img19 = ledMI_img_list[48] #VOICEBOX34 ONNORM
                l_img20 = ledLO_img_list[48] #VOICEBOX34 ONMIN
                l_img23 = ledOF_img_list[48] #VOICEBOX34 OF
            elif style == STYLE_B_txt[1]:
                l_img18 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                l_img19 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                l_img20 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                l_img23 = ledOF_img_list[46]
        elif theme == THEME_B_txt[7]:
            l_img30 = ledOF_img_list[60] #DEV002GAUGES 1DK
            l_img31 = ledOF_img_list[60] #DEV002GAUGES 1DK
            l_img32 = ledFU_img_list[60] #DEV002GAUGES 1RD
            l_img33 = ledFU_img_list[60] #DEV002GAUGES 1RD
            l_img34 = ledOF_img_list[62] #DEV002GAUGES 1YE
            l_img40 = ledOF_img_list[58] #DEV002GAUGES 2DK
            l_img41 = ledOF_img_list[58] #DEV002GAUGES 2DK
            l_img42 = ledFU_img_list[58] #DEV002GAUGES 2GN
            l_img43 = ledFU_img_list[58] #DEV002GAUGES 2GN
            l_img44 = ledFU_img_list[62] #DEV002GAUGES 2YE
            l_img10 = ledOF_img_list[60] #RD
            l_img11 = ledOF_img_list[62] #YE
            l_img12 = ledOF_img_list[58] #RD
            l_img13 = ledFU_img_list[32] #SIGNAL ONRD
            l_img14 = ledOF_img_list[32] #SIGNAL OFRD
            l_img80 = ledFU_img_list[60] #RD
            l_img81 = ledFU_img_list[62] #YE
            l_img15 = ledFU_img_list[58] #RD
            l_img16 = rpmON_img_list
            l_img17 = rpmOF_img_list
            if style == STYLE_B_txt[0]:
                l_img18 = sledON_img_list[0] #VOICEBOXOTTO ONMAX LE
                l_img19 = sledON_img_list[1] #VOICEBOXOTTO ONMAX RI
                l_img20 = sledOF_img_list[0]  #VOICEBOXOTTO OF RI
                l_img23 = sledOF_img_list[1]  #VOICEBOXOTTO OF LE
            elif style == STYLE_B_txt[1]:
                l_img18 = sledON_img_list[2] #VOICEBOXOTTO ONMAX LE
                l_img19 = sledON_img_list[3] #VOICEBOXOTTO ONMAX RI
                l_img20 = sledOF_img_list[2]  #VOICEBOXOTTO OF RI
                l_img23 = sledOF_img_list[3]  #VOICEBOXOTTO OF LE
            localimagelist01 = list(vbON_OTTO_img_list) #VOICEBOX
            localimagelist02 = list(vbOF_OTTO_img_list)
        elif theme == THEME_B_txt[8]:
            l_img30 = ledOF_img_list[60] #DEV002GAUGES 1DK
            l_img31 = ledOF_img_list[60] #DEV002GAUGES 1DK
            l_img32 = ledFU_img_list[60] #DEV002GAUGES 1RD
            l_img33 = ledFU_img_list[60] #DEV002GAUGES 1RD
            l_img34 = ledOF_img_list[62] #DEV002GAUGES 1YE
            l_img40 = ledOF_img_list[58] #DEV002GAUGES 2DK
            l_img41 = ledOF_img_list[58] #DEV002GAUGES 2DK
            l_img42 = ledFU_img_list[58] #DEV002GAUGES 2GN
            l_img43 = ledFU_img_list[58] #DEV002GAUGES 2GN
            l_img44 = ledFU_img_list[62] #DEV002GAUGES 2YE
            l_img10 = ledOF_img_list[60] #RD
            l_img11 = ledOF_img_list[62] #YE
            l_img12 = ledOF_img_list[58] #RD
            l_img13 = ledFU_img_list[32] #SIGNAL ONRD
            l_img14 = ledOF_img_list[32] #SIGNAL OFRD
            l_img80 = ledFU_img_list[60] #RD
            l_img81 = ledFU_img_list[62] #YE
            l_img15 = ledFU_img_list[58] #RD
            l_img16 = rpmON_img_list
            l_img17 = rpmOF_img_list
            localimagelist01 = list(vbON_MAX_img_list) #VOICEBOX
            localimagelist02 = list(vbOF_MAX_img_list) #VOICEBOX
            if style == STYLE_B_txt[0]:
                l_img18 = ledFU_img_list[41] #VOICEBOX34 ONMAX
                l_img19 = ledMI_img_list[41] #VOICEBOX34 ONNORM
                l_img20 = ledLO_img_list[41] #VOICEBOX34 ONMIN
                l_img23 = ledOF_img_list[41] #VOICEBOX34 OF
            elif style == STYLE_B_txt[1]:
                l_img18 = ledFU_img_list[46] #VOICEBOX34 ONMAX
                l_img19 = ledMI_img_list[46] #VOICEBOX34 ONNORM
                l_img20 = ledLO_img_list[46] #VOICEBOX34 ONMIN
                l_img23 = ledOF_img_list[46]
        elif theme == THEME_B_txt[9]:
            l_img30 = ledOF_img_list[60] #DEV002GAUGES 1DK
            l_img31 = ledOF_img_list[60] #DEV002GAUGES 1DK
            l_img32 = ledFU_img_list[60] #DEV002GAUGES 1RD
            l_img33 = ledFU_img_list[60] #DEV002GAUGES 1RD
            l_img34 = ledOF_img_list[62] #DEV002GAUGES 1YE
            l_img40 = ledOF_img_list[58] #DEV002GAUGES 2DK
            l_img41 = ledOF_img_list[58] #DEV002GAUGES 2DK
            l_img42 = ledFU_img_list[58] #DEV002GAUGES 2GN
            l_img43 = ledFU_img_list[58] #DEV002GAUGES 2GN
            l_img44 = ledFU_img_list[62] #DEV002GAUGES 2YE
            l_img10 = ledOF_img_list[60] #RD
            l_img11 = ledOF_img_list[62] #YE
            l_img12 = ledOF_img_list[58] #RD
            l_img13 = ledFU_img_list[28] #SIGNAL ONRD
            l_img14 = ledOF_img_list[28] #SIGNAL OFRD
            l_img80 = ledFU_img_list[60] #RD
            l_img81 = ledFU_img_list[62] #YE
            l_img15 = ledFU_img_list[58] #RD
            l_img16 = rpmON_img_list
            l_img17 = rpmOF_img_list
        elif theme == THEME_B_txt[10]:
            l_img30 = ledOF_img_list[60] #DEV002GAUGES 1DK
            l_img31 = ledOF_img_list[60] #DEV002GAUGES 1DK
            l_img32 = ledFU_img_list[60] #DEV002GAUGES 1RD
            l_img33 = ledFU_img_list[60] #DEV002GAUGES 1RD
            l_img34 = ledOF_img_list[62] #DEV002GAUGES 1YE
            l_img40 = ledOF_img_list[58] #DEV002GAUGES 2DK
            l_img41 = ledOF_img_list[58] #DEV002GAUGES 2DK
            l_img42 = ledFU_img_list[58] #DEV002GAUGES 2GN
            l_img43 = ledFU_img_list[58] #DEV002GAUGES 2GN
            l_img44 = ledFU_img_list[62] #DEV002GAUGES 2YE
            l_img10 = ledOF_img_list[60] #RD
            l_img11 = ledOF_img_list[62] #YE
            l_img12 = ledOF_img_list[58] #RD
            l_img13 = ledFU_img_list[30] #SIGNAL ONRD
            l_img14 = ledOF_img_list[30] #SIGNAL OFRD
            l_img80 = ledFU_img_list[60] #RD
            l_img81 = ledFU_img_list[62] #YE
            l_img15 = ledFU_img_list[58] #RD
            l_img16 = rpmON_img_list
            l_img17 = rpmOF_img_list
        elif theme in [THEME_B_txt[15], THEME_B_txt[16]]:
            l_img10 = lcarsOF_img_list[5]
            l_img11 = lcarsOF_img_list[5]
            l_img12 = lcarsOF_img_list[5]
            l_img13 = ledFU_img_list[32] #SIGNAL ONRD
            l_img14 = ledOF_img_list[32] #SIGNAL OFRD
            l_img80 = lcarsON_img_list[5]
            l_img81 = lcarsON_img_list[5]
            l_img15 = lcarsON_img_list[6]
            l_img16 = lcarsON_R_img_list
            l_img17 = lcarsOF_R_img_list

        return {
            "l_img10": l_img10,
            "l_img11": l_img11,
            "l_img12": l_img12,
            "l_img13": l_img13,
            "l_img14": l_img14,
            "l_img15": l_img15,
            "l_img16": l_img16,
            "l_img17": l_img17,
            "l_img18": l_img18,
            "l_img19": l_img19,
            "l_img20": l_img20,
            "l_img23": l_img23,
            "l_img30": l_img30,
            "l_img31": l_img31,
            "l_img32": l_img32,
            "l_img33": l_img33,
            "l_img34": l_img34,
            "l_img40": l_img40,
            "l_img41": l_img41,
            "l_img42": l_img42,
            "l_img43": l_img43,
            "l_img44": l_img44,
            "l_img80": l_img80,
            "l_img81": l_img81,
            "localimagelist01": localimagelist01,
            "localimagelist02": localimagelist02,
        }

    #--------------------------------------------------------------------------------------
    # MAINLOOP DASH
    #--------------------------------------------------------------------------------------
    def update_page(self):
        if not self._is_alive():
            return
        self.update_job = None
        start_time = time.time()
        timings = [("start", time.perf_counter())]
        self._update_audio_labels()
        self._trace_step(timings, "audio_labels")
        self._update_audio_button_states()
        self._trace_step(timings, "audio_buttons")
        #----------------------------------------------------------------------------------
        # Dictionary chechen if not, create
        #----------------------------------------------------------------------------------
        if not hasattr(self, "old_values"):
            self.old_values = {}
        #----------------------------------------------------------------------------------
        # UPDATE STYLES
        #----------------------------------------------------------------------------------
        images = self._get_theme_assets()["updates"]
        self._trace_step(timings, "theme_assets")
        l_img10 = images["l_img10"]
        l_img11 = images["l_img11"]
        l_img12 = images["l_img12"]
        l_img13 = images["l_img13"]
        l_img14 = images["l_img14"]
        l_img15 = images["l_img15"]
        l_img16 = images["l_img16"]
        l_img17 = images["l_img17"]
        l_img18 = images["l_img18"]
        l_img19 = images["l_img19"]
        l_img20 = images["l_img20"]
        l_img23 = images["l_img23"]
        l_img30 = images["l_img30"]
        l_img31 = images["l_img31"]
        l_img32 = images["l_img32"]
        l_img33 = images["l_img33"]
        l_img34 = images["l_img34"]
        l_img40 = images["l_img40"]
        l_img41 = images["l_img41"]
        l_img42 = images["l_img42"]
        l_img43 = images["l_img43"]
        l_img44 = images["l_img44"]
        l_img80 = images["l_img80"]
        l_img81 = images["l_img81"]
        localimagelist01 = images["localimagelist01"]
        localimagelist02 = images["localimagelist02"]
        #----------------------------------------------------------------------------------
        # DEV001 GAUGES
        #----------------------------------------------------------------------------------
        if device == DEVICE_B_txt[1]:
            seven_seg_speed = self._update_dev001(
                l_img10,
                l_img11,
                l_img12,
                l_img13,
                l_img14,
                l_img15,
                l_img18,
                l_img19,
                l_img20,
                l_img23,
                l_img80,
                l_img81,
                localimagelist01,
                localimagelist02,
            )
            self._trace_step(timings, "dev001")
        #----------------------------------------------------------------------------------
        # DEV002 GAUGES
        #----------------------------------------------------------------------------------
        if device == DEVICE_B_txt[2]:
            dev002_images = {
                "rpm_on": l_img16,
                "rpm_off": l_img17,
                "gauge_1_off_low": l_img30,
                "gauge_1_off_high": l_img31,
                "gauge_1_on_low": l_img32,
                "gauge_1_on_high": l_img33,
                "gauge_warning_off": l_img34,
                "gauge_2_off_low": l_img40,
                "gauge_2_off_high": l_img41,
                "gauge_2_on_low": l_img42,
                "gauge_2_on_high": l_img43,
                "gauge_warning_on": l_img44,
            }
            (
                seg_DEV002,
                seven_seg_DEV002G007,
                seven_seg_DEV002G008,
                seven_seg_DEV002G009,
            ) = self._update_dev002(dev002_images)
            self._trace_step(timings, "dev002")
        #----------------------------------------------------------------------------------
        # UPDATE SYSINFO MTR DISPLAY
        #----------------------------------------------------------------------------------
        if device == DEVICE_B_txt[2]:
            dev002_values = {
                "pb00": seg_DEV002[1],
                "pb01": seg_DEV002[2],
                "pb02": seg_DEV002[3],
                "pb03": seg_DEV002[4],
                "pb04": seg_DEV002[5],
                "pb05": seg_DEV002[6],
                "pb06": seven_seg_DEV002G007,
                "pb07": seven_seg_DEV002G008,
                "pb08": seven_seg_DEV002G009,
            }
            self._update_sysinfo(dev002_values)
        else:
            self._update_sysinfo()
        self._trace_step(timings, "sysinfo")
        #----------------------------------------------------------------------------------
        # UPDATE ONLY IF SOMETHING CHANGED // 7 SEGMENT SPEED AND TOTAL RPM PROGNO DISPLAY
        #----------------------------------------------------------------------------------
        if device == DEVICE_B_txt[1]:
            self._update_digital_displays(seven_seg_speed=seven_seg_speed)
        elif device == DEVICE_B_txt[2]:
            self._update_digital_displays(seg_DEV002=seg_DEV002)
        self._trace_step(timings, "digital")
        #----------------------------------------------------------------------------------
        # END UPDATE LABEL
        #----------------------------------------------------------------------------------
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.update_duration = f"{elapsed_time:.4f}"
        self._trace_step(timings, "end")
        self._log_slow_update(timings)
        self._schedule_update()

#------------------------------------------------------------------------------------------
# LOAD PAGES
#------------------------------------------------------------------------------------------
from pages.page_context import set_context
set_context(globals())

from pages.P00_BOOT import P00_BOOT
from pages.P02_QOPT import P02_QOPT
from pages.P03_SETUP import P03_SETUP
from pages.P04_THEMES import P04_THEMES
from pages.P05_CARFUNCTIONS import P05_CARFUNCTIONS
from pages.P06_KNIGHTFUNCTIONS import P06_KNIGHTFUNCTIONS
from pages.P07_AUDIO import P07_AUDIO
from pages.P08_VIDEO import P08_VIDEO
set_context(globals())
#------------------------------------------------------------------------------------------
# LOAD CONTROLLER
#------------------------------------------------------------------------------------------
from functions.app_controller import KIDDController

#------------------------------------------------------------------------------------------
# END PROGRAM
#------------------------------------------------------------------------------------------
if __name__ == "__main__":
    kidd = MainApplication()
    kidd.mainloop()
