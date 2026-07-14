import time

from pages.page_context import sync_context
from functions.console_log import get_console_lines, log
from functions.gauge_scale_config import (
    DEFAULT_GAUGE_SCALE,
    ensure_gauge_scale_config,
    save_gauge_scale_value,
)
from functions.network_info import read_wlan0_ip
from functions.quicksound_config import (
    QUICKSOUND_COLORS,
    QUICKSOUND_MODES,
    list_quicksound_files,
    list_quicksound_folders,
    load_quicksound_config,
    load_quicksound_settings,
    save_quicksound_config,
    save_quicksound_settings,
)

sync_context(globals())

#------------------------------------------------------------------------------------------
# PAGE 03: SETUP
#------------------------------------------------------------------------------------------
class P03_SETUP(tk.Frame):
    dev001_setup_subpage = "HW/SW"

    if debug == True:
        print (MENU_B_txt[2])
    def __init__(self, master):
        sync_context(globals())
        tk.Frame.__init__(self, master)
        #----------------------------------------------------------------------------------
        # CREATE BACKGROUND
        #----------------------------------------------------------------------------------        
        canvas = tk.Canvas(self, bg=sys_clr[0], highlightthickness=0)
        canvas.pack(fill='both', expand=True)
        #------------------------------------------------------------------------------
        # CREATE BACKGROUND GRID
        #------------------------------------------------------------------------------ 
        for x in range(0, bggrid[1], grid_spacing):
            canvas.create_line(x, 0, x, bggrid[4], fill=sys_clr[1])
        for y in range(0, bggrid[4], grid_spacing):
            canvas.create_line(0, y, bggrid[1], y, fill=sys_clr[2])
        #------------------------------------------------------------------------------
        # CREATE BACKGROUND OVERLAYS
        #------------------------------------------------------------------------------
        #--------------------------------------------------------------------------
        # COORDINATES OF HORIZONTAL LINES
        #--------------------------------------------------------------------------            
        xlinborder = 40
        xcrnrborder = 15
        xcrnrborder_ri = xcrnrborder+5
        xy_width = 10
        frames = [
            [15, 75],   #0 TITLE FRAME
            [90, 255],  #1 MAIN FRAME
            [(bggrid[4]-138), (bggrid[4]-48)]  #2 MENU FRAME
        ]
        overlay_frames = [frames[0], frames[2]]
        coordinates = []
        for frame_bounds in overlay_frames:
            coordinates.append((bggrid[0] + xlinborder, bggrid[3] + frame_bounds[0], bggrid[1] - xlinborder, bggrid[3] + frame_bounds[0]))
            coordinates.append((bggrid[0] + xlinborder, bggrid[3] + frame_bounds[1], bggrid[1] - xlinborder, bggrid[3] + frame_bounds[1]))
        # Define colors
        colors_corner = [sys_clr[3], sys_clr[4]]
        gradient_colors = [sys_clr[5], sys_clr[6], sys_clr[7]]
        num_segments = 50               
        #----------------------------------------------------------------------
        # CREATE HORIZONTAL LINES
        #----------------------------------------------------------------------
        for i in range(num_segments):
            color_index = min(i // (num_segments // len(gradient_colors)), len(gradient_colors) - 1)
            color_start, color_end = gradient_colors[color_index], gradient_colors[min(color_index + 1, len(gradient_colors) - 1)]
            t = (i % (num_segments // len(gradient_colors))) / (num_segments // len(gradient_colors))
            r = int((1 - t) * int(color_start[1:3], 16) + t * int(color_end[1:3], 16))
            g = int((1 - t) * int(color_start[3:5], 16) + t * int(color_end[3:5], 16))
            b = int((1 - t) * int(color_start[5:7], 16) + t * int(color_end[5:7], 16))
            color = "#{:02x}{:02x}{:02x}".format(r, g, b)

            for x1, y1, x2, y2 in coordinates:
                x1_segment = x1 + (x2 - x1) * i / num_segments
                y1_segment = y1 + (y2 - y1) * i / num_segments
                x2_segment = x1 + (x2 - x1) * (i + 1) / num_segments
                y2_segment = y1 + (y2 - y1) * (i + 1) / num_segments
                canvas.create_line(x1_segment, y1_segment, x2_segment, y2_segment, fill=color)
        #--------------------------------------------------------------------------
        # CREATE FRAME 00 CORNERS LEFT/TOP DISPLAY
        #--------------------------------------------------------------------------
        coordinates = [
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][0]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[0][0]), 0, 1),        # LT_X
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][0]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][0]+xy_width), 1, 1),        # LT_Y
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][0]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[0][0]), 0, 0),  # RT_X
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][0]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][0]+xy_width), 1, 0),  # RT_Y
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][1]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[0][1]), 0, 1),        # LB_X
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][1]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[0][1]-xy_width), 1, 1),        # LB_Y
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][1]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[0][1]), 0, 0),  # RB_X
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][1]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[0][1]-xy_width), 1, 0),  # RB_Y
        ]
        for x1, y1, x2, y2, is_vertical, is_top in coordinates:
            line_color = colors_corner[is_vertical]
            line_width = 1
            canvas.create_line(x1, y1, x2, y2, fill=line_color, width=line_width) 
        #------------------------------------------------------------------------------
        # CREATE BACKGROUND GRID OVERLAYS
        #------------------------------------------------------------------------------
        #--------------------------------------------------------------------------
        # CREATE FRAME 02 (MENU) CORNERS LEFT/TOP DISPLAY
        #--------------------------------------------------------------------------
        coordinates = [
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][0]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[2][0]), 0, 1),        # LT_X
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][0]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][0]+xy_width), 1, 1),        # LT_Y
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][0]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[2][0]), 0, 0),  # RT_X
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][0]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][0]+xy_width), 1, 0),  # RT_Y
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][1]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[2][1]), 0, 1),        # LB_X
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][1]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[2][1]-xy_width), 1, 1),        # LB_Y
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][1]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[2][1]), 0, 0),  # RB_X
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][1]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[2][1]-xy_width), 1, 0),  # RB_Y
        ]
        for x1, y1, x2, y2, is_vertical, is_top in coordinates:
            line_color = colors_corner[is_vertical]
            line_width = 1
            canvas.create_line(x1, y1, x2, y2, fill=line_color, width=line_width)
        #--------------------------------------------------------------------------
        # RIGHT SCREEN CORNERS
        #--------------------------------------------------------------------------
        if device == DEVICE_B_txt[1]: 
            canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)  #PAGE RI
        elif device == DEVICE_B_txt[2]:
            canvas.create_line(1295, 15, 1305, 15, fill=colors_corner[0], width=1)   #LT_X
            canvas.create_line(1295, 15, 1295, 25, fill=colors_corner[1], width=1)   #LT_Y
            canvas.create_line(2345, 15, 2355, 15, fill=colors_corner[0], width=1)   #RT_X
            canvas.create_line(2355, 15, 2355, 25, fill=colors_corner[1], width=1)   #RT_Y
            canvas.create_line(1295, 720, 1305, 720, fill=colors_corner[0], width=1) #LB_X
            canvas.create_line(1295, 710, 1295, 720, fill=colors_corner[1], width=1) #LB_Y
            canvas.create_line(2345, 720, 2355, 720, fill=colors_corner[0], width=1) #RB_X
            canvas.create_line(2355, 710, 2355, 720, fill=colors_corner[1], width=1) #RB_Y
        #----------------------------------------------------------------------------------
        # INFO AND GRID CONFIG GLOBALS
        #----------------------------------------------------------------------------------
        global quant_btns_HW
        global quant_btns_SW
        global quant_btns_RB01
        global quant_btns_RB02
        global quant_btns_RB03       
        quant_btns_HW = 10
        quant_btns_SW = 10
        quant_btns_RB01 = 16
        quant_btns_RB02 = 16
        quant_btns_RB03 = 16
        px_to_next = 115
        btn_w = 80
        btn_f_w = 20
        btn_h = 40
        lbl_w = 105
        lbl_f_h = 20
        lbl_i_h = 15
        x_start = 68
        x_start_FAV = x_start + btn_w + 5
        x_start_RB = 1370
        x_start_RB_FAV = x_start_RB + btn_w + 5
        y_l1 = 95
        y_l2 = 117
        y_l3 = 135
        y_l4 = 185
        y_l5 = 208

        y_l10 = 30
        y_l11 = 53
        y_l12 = 100
        y_l13 = 123

        y_l14 = 230
        y_l15 = 253
        y_l16 = 300
        y_l17 = 323

        y_l18 = 430
        y_l19 = 453
        y_l20 = 500
        y_l21 = 523
        #----------------------------------------------------------------------------------
        # STATIC TEXT
        #----------------------------------------------------------------------------------
        if sys_linux and sys_pi:
            wlan0_ip = read_wlan0_ip()
        else:
            wlan0_ip = "127.0.0.1"
        canvas.create_text(20, 20, **txt_style_pagename, fill=sys_clr[9], text="SETUP")
        setup_info = f"VERSION {version} | CHANGE {last_change} | {sys.platform} | {carno} | {devno} | {wlan0_ip}"
        canvas.create_text(20, 50, **txt_style_pageinfo, fill=sys_clr[9], text=setup_info)
        canvas.create_text(20, (bggrid[4]-135), **txt_style_pagename, fill=sys_clr[9], text="MENU")
        if device == DEVICE_B_txt[1]:
            self._dev001_setup_area = (15, 90, 1245, 525)
            self._dev001_setup_frames = {
                "HW/SW": tk.Frame(self, bg=sys_clr[0], highlightthickness=0),
                "AUDIO": tk.Frame(self, bg=sys_clr[0], highlightthickness=0),
                "ODOMETER": tk.Frame(self, bg=sys_clr[0], highlightthickness=0),
                "SCALE": tk.Frame(self, bg=sys_clr[0], highlightthickness=0),
            }
            self._create_setup_console("DEV001", 1310, 25, 420, 30, 1310, 60, 425, 355, 21)
            self._create_dev001_device_status()
            self._create_dev001_submenu()
        elif device == DEVICE_B_txt[2]:
            self._dev002_scale_area = (620, 90, 700, 530)
            self._dev002_scale_frame = tk.Frame(self, bg=sys_clr[0], highlightthickness=0)
            self._create_dev002_submenu()
            self._create_setup_console("DEV002", 30, 265, 560, 28, 30, 295, 560, 315, 18)
            self._create_dev002_i2c_status()
        #----------------------------------------------------------------------------------
        # EXIT BUTTON
        #----------------------------------------------------------------------------------
        btn_EXIT = tk.Button(self, bd=0, bg=sys_clr[8], fg="#FF0000", font=(fonts[1], 28))
        btn_EXIT.config(text="X")
        btn_EXIT.configure(command=read.quitDASH)
        btn_EXIT.place(x=125, y=18, width=28, height=28)
        #----------------------------------------------------------------------------------
        # FUNCTION BUTTON LABELS
        #----------------------------------------------------------------------------------
        lbls_btnhw = []
        lbls_btnsw = []
        lbls_btnhw_info = []
        lbls_btnhw_info_txt_DEV001 = [gps_port, "---", "---", "---", "---", "---", "---", "---", "---", "---"]
        lbls_btnhw_info_txt_DEV002 = ["---", "---", "---", "---", "---", "---", "---", "---", "---", "---"]        
        x_pos = x_start
        for i in range(quant_btns_HW):
            lbls_btnhw = tk.Label(self._setup_parent("HW/SW"), **lbl_style_setup_btns, bg=sys_clr[8], fg=sys_clr[9])
            if device == DEVICE_B_txt[1]:
                lbls_btnhw.config(text=btnhw_DEV001_txt[i])
            elif device == DEVICE_B_txt[2]:
                lbls_btnhw.config(text=btnhw_DEV002_txt[i])
            self._setup_place(lbls_btnhw, "HW/SW", x_pos, y_l1, lbl_w, lbl_f_h)
            x_pos += +px_to_next
        x_pos = x_start
        for i in range(quant_btns_HW):
            lbls_btnhw_info = tk.Label(self._setup_parent("HW/SW"), **lbl_style_setup_btns_small, bg=sys_clr[8], fg=sys_clr[9])
            if device == DEVICE_B_txt[1]:
                lbls_btnhw_info.config(text=lbls_btnhw_info_txt_DEV001[i])
            elif device == DEVICE_B_txt[2]:
                lbls_btnhw_info.config(text=lbls_btnhw_info_txt_DEV002[i])
            self._setup_place(lbls_btnhw_info, "HW/SW", x_pos, y_l2, lbl_w, lbl_i_h)
            x_pos += +px_to_next
        x_pos = x_start
        for i in range(quant_btns_SW):
            lbls_btnsw = tk.Label(self._setup_parent("HW/SW"), **lbl_style_setup_btns, bg=sys_clr[8], fg=sys_clr[9])
            if device == DEVICE_B_txt[1]:
                lbls_btnsw.config(text=lbl_btnsw_DEV001_txt[i])
            elif device == DEVICE_B_txt[2]:
                lbls_btnsw.config(text=lbl_btnsw_DEV002_txt[i])
            self._setup_place(lbls_btnsw, "HW/SW", x_pos, y_l4, lbl_w, lbl_f_h)
            x_pos += +px_to_next
        #----------------------------------------------------------------------------------
        # FUNCTION BUTTONS
        #----------------------------------------------------------------------------------
        #--------------------------------------------------------------------------
        # HW BUTTONS
        #--------------------------------------------------------------------------
        self.btns_HW = []
        self.hw_button_render_state = {}
        x_pos = x_start
        for i in range(quant_btns_HW):
            btn_HW = tk.Button(self._setup_parent("HW/SW", canvas), bg=sys_clr[8], font=("Bebas Neue Bold", 28), command=lambda i=i: self._toggle_hw_button(i))
            self._setup_place(btn_HW, "HW/SW", x_pos, y_l3, btn_w, btn_h)
            x_pos += +px_to_next
            self.btns_HW.append(btn_HW)
        #--------------------------------------------------------------------------
        # SW BUTTONS
        #--------------------------------------------------------------------------
        self.btns_SW = []
        self.sw_button_render_state = {}
        x_pos = x_start
        for i in range(quant_btns_SW):
            btn_SW = tk.Button(self._setup_parent("HW/SW", canvas), bg=sys_clr[8], fg=sys_clr[9], font=("Bebas Neue Bold", 28), command=lambda i=i: self._toggle_sw_button(i))
            self._setup_place(btn_SW, "HW/SW", x_pos, y_l5, btn_w, btn_h)
            x_pos += +px_to_next
            self.btns_SW.append(btn_SW)
        #----------------------------------------------------------------------------------
        # KEYPAD BUTTONS
        #----------------------------------------------------------------------------------
        # CONFIG + OTHER_CONFIG: two dropdowns, one keypad (reads/writes btn_states.json)
        def _load_btn_states():
            with open(os.path.join(datadir, "btn_states.json"), encoding="utf-8") as f:
                return json.load(f)

        def _save_btn_states(data):
            with open(os.path.join(datadir, "btn_states.json"), "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

        # Local state
        self._cfg_data = _load_btn_states()

        self._odo_keys = list(self._cfg_data.get("odo_config", {}).keys()) or ["odo_trip_gps_imperial"]
        self._other_keys = list(self._cfg_data.get("other_config", {}).keys()) or ["timezone"]

        self._odo_selected_key    = tk.StringVar(value=self._odo_keys[0])
        self._other_selected_key  = tk.StringVar(value=self._other_keys[0])

        self._odo_current_value_var   = tk.StringVar()
        self._odo_edit_value_var      = tk.StringVar()
        self._other_current_value_var = tk.StringVar()
        self._other_edit_value_var    = tk.StringVar()

        self._status_var = tk.StringVar(value="")
        self._active_section = tk.StringVar(value="ODO")  # "ODO" or "OTHER"

        def _refresh_value(section):
            self._cfg_data = _load_btn_states()
            if section == "ODO":
                key = self._odo_selected_key.get()
                val = self._cfg_data.get("odo_config", {}).get(key, 0.0)
                s = str(val)
                self._odo_current_value_var.set(s)
                self._odo_edit_value_var.set(s)
            else:
                key = self._other_selected_key.get()
                val = self._cfg_data.get("other_config", {}).get(key, 0.0)
                s = str(val)
                self._other_current_value_var.set(s)
                self._other_edit_value_var.set(s)

        def _on_select_odo(*_):
            self._active_section.set("ODO")
            _refresh_value("ODO")

        def _on_select_other(*_):
            self._active_section.set("OTHER")
            _refresh_value("OTHER")

        def _keypad_target_vars():
            # return (edit_var, current_var, section, key)
            if self._active_section.get() == "ODO":
                return (self._odo_edit_value_var, self._odo_current_value_var, "ODO", self._odo_selected_key.get())
            else:
                return (self._other_edit_value_var, self._other_current_value_var, "OTHER", self._other_selected_key.get())

        def _on_keypad_press(token):
            edit_var, _, _, _ = _keypad_target_vars()
            buf = edit_var.get()

            if token == "C":
                edit_var.set("")
                return
            if token == "BS":
                edit_var.set(buf[:-1])
                return
            if token == "+/-":
                if buf.startswith("-"):
                    edit_var.set(buf[1:])
                else:
                    edit_var.set("-" + buf if buf else "-")
                return
            if token == ".":
                if "." not in buf:
                    edit_var.set(buf + ".")
                return
            if token.isdigit():
                edit_var.set(buf + token)
                return

        def _coerce_value(raw):
            txt = raw.strip().replace(",", ".")
            if txt in ("", "-", ".", "-."):
                raise ValueError("empty buffer")
            try:
                # store as int if it has no decimal point
                if "." not in txt:
                    return int(txt)
                else:
                    return float(txt)
            except ValueError:
                return raw  # allow non-numeric strings


        def _save_active_value():
            edit_var, curr_var, section, key = _keypad_target_vars()
            raw = edit_var.get()
            try:
                val = _coerce_value(raw)
            except Exception:
                self._status_var.set("Invalid value")
                self.after(1200, lambda: self._status_var.set(""))
                return

            data = _load_btn_states()
            if section == "ODO":
                data.setdefault("odo_config", {})[key] = val
            else:
                data.setdefault("other_config", {})[key] = val
            _save_btn_states(data)
    
            curr_var.set(str(val))
            self._status_var.set("CONFIG SAVED")
            self.after(1200, lambda: self._status_var.set(""))

        # ODO dropdown
        opt_odo = tk.OptionMenu(self._setup_parent("ODOMETER"), self._odo_selected_key, *self._odo_keys, command=lambda *_: _on_select_odo())
        opt_odo.config(bg=sys_clr[8], fg=sys_clr[3], font=(fonts[6], 22))
        self._setup_place(opt_odo, "ODOMETER", 30, 300, 250, 30)

        # Current/Edit (odo)
        lbl_curr_odo = tk.Label(self._setup_parent("ODOMETER"), **lbl_style_setup_btns, text="ACTUAL", bg=sys_clr[8], fg=sys_clr[3])
        self._setup_place(lbl_curr_odo, "ODOMETER", 30, 345, 120, 30)
        val_curr_odo = tk.Label(self._setup_parent("ODOMETER"), **lbl_style_setup_btns, textvariable=self._odo_current_value_var, bg=sys_clr[8], fg=sys_clr[3])
        self._setup_place(val_curr_odo, "ODOMETER", 165, 345, 120, 30)

        lbl_edit_odo = tk.Label(self._setup_parent("ODOMETER"), **lbl_style_setup_btns, text="NEW", bg=sys_clr[8], fg=sys_clr[3])
        self._setup_place(lbl_edit_odo, "ODOMETER", 30, 390, 120, 30)
        val_edit_odo = tk.Label(self._setup_parent("ODOMETER"), **lbl_style_setup_btns, textvariable=self._odo_edit_value_var, bg=sys_clr[8], fg=sys_clr[3])
        self._setup_place(val_edit_odo, "ODOMETER", 165, 390, 120, 30)

        # OTHER dropdown
        opt_other = tk.OptionMenu(self._setup_parent("ODOMETER"), self._other_selected_key, *self._other_keys, command=lambda *_: _on_select_other())
        opt_other.config(bg=sys_clr[8], fg=sys_clr[3], font=(fonts[6], 22))
        self._setup_place(opt_other, "ODOMETER", 30, 435, 250, 30)

        # Current/Edit (other)
        lbl_curr_other = tk.Label(self._setup_parent("ODOMETER"), **lbl_style_setup_btns, text="ACTUAL", bg=sys_clr[8], fg=sys_clr[3])
        self._setup_place(lbl_curr_other, "ODOMETER", 30, 480, 120, 30)
        val_curr_other = tk.Label(self._setup_parent("ODOMETER"), **lbl_style_setup_btns, textvariable=self._other_current_value_var, bg=sys_clr[8], fg=sys_clr[3])
        self._setup_place(val_curr_other, "ODOMETER", 165, 480, 120, 30)

        lbl_edit_other = tk.Label(self._setup_parent("ODOMETER"), **lbl_style_setup_btns, text="NEW", bg=sys_clr[8], fg=sys_clr[3])
        self._setup_place(lbl_edit_other, "ODOMETER", 30, 525, 120, 30)
        val_edit_other = tk.Label(self._setup_parent("ODOMETER"), **lbl_style_setup_btns, textvariable=self._other_edit_value_var, bg=sys_clr[8], fg=sys_clr[3])
        self._setup_place(val_edit_other, "ODOMETER", 165, 525, 120, 30)

        # Active hint + status
        lbl_active = tk.Label(self._setup_parent("ODOMETER"), font=(fonts[6], 22), textvariable=self._active_section, bg=sys_clr[8], fg=sys_clr[3], anchor="c")
        self._setup_place(lbl_active, "ODOMETER", 30, 570, 60, 30)

        lbl_status = tk.Label(self._setup_parent("ODOMETER"), font=(fonts[6], 22), textvariable=self._status_var, bg=sys_clr[8], fg=sys_clr[3], anchor="c")
        self._setup_place(lbl_status, "ODOMETER", 110, 570, 175, 30)

        # One keypad for both
        keypad_layout = [
            ("7","8","9","BS"),
            ("4","5","6","C"),
            ("1","2","3","+/-"),
            ("0",".","SAVE","")
        ]
        x0, y0 = 345, 300
        dx, dy = 77, 77
        w, h = 70, 70
        setup_keypad_style = dict(keypad_style)
        setup_keypad_style["font"] = (fonts[0], 16)

        for r, row in enumerate(keypad_layout):
            for c, token in enumerate(row):
                if not token:
                    continue
                if token == "SAVE":
                    btn = tk.Button(self._setup_parent("ODOMETER"), **setup_keypad_style, text=token, bg=sys_clr[8], fg=sys_clr[9], command=_save_active_value)
                else:
                    btn = tk.Button(self._setup_parent("ODOMETER"), **setup_keypad_style, text=token, bg=sys_clr[8], fg=sys_clr[9], command=lambda t=token: _on_keypad_press(t))
                self._setup_place(btn, "ODOMETER", x0 + c*dx, y0 + r*dy, w, h)

        # Initialize
        _refresh_value("ODO")
        _refresh_value("OTHER")
        self._active_section.set("ODO")

        #----------------------------------------------------------------------------------
        # QUICKSOUND SETUP
        #----------------------------------------------------------------------------------
        if "snd_fldr" not in globals() or not snd_fldr:
            read.load_soundfolder()
            sync_context(globals())
        self._quicksound_config = load_quicksound_config(datadir)
        self._quicksound_settings = load_quicksound_settings(datadir)
        quicksound_folders = list_quicksound_folders(snd_fldr)
        quicksound_color_fg = {
            "AQ": "#44FFFF",
            "BU": "#4488FF",
            "GN": "#44FF44",
            "OR": "#FF9900",
            "RD": "#FF4444",
            "WH": "#FFFFFF",
            "YE": "#FFF862",
        }

        def _cycle_quicksound_value(index, key, values):
            current = self._quicksound_config[index][key]
            next_index = (values.index(current) + 1) % len(values) if current in values else 0
            self._quicksound_config[index][key] = values[next_index]
            if key == "mode" and self._quicksound_config[index][key] == "AUTOPLAY":
                for other_index, quicksound in enumerate(self._quicksound_config):
                    if other_index != index and quicksound["mode"] == "AUTOPLAY":
                        quicksound["mode"] = "1X"
            save_quicksound_config(datadir, self._quicksound_config)
            self.master.switch_frame(P03_SETUP)

        def _set_quicksound_folder(index, selected_folder):
            files = list_quicksound_files(snd_fldr, selected_folder)
            self._quicksound_config[index]["folder"] = selected_folder
            if files and self._quicksound_config[index]["file"] not in files:
                self._quicksound_config[index]["file"] = files[0]
            save_quicksound_config(datadir, self._quicksound_config)
            self.master.switch_frame(P03_SETUP)

        def _set_quicksound_file(index, selected_file):
            self._quicksound_config[index]["file"] = selected_file
            save_quicksound_config(datadir, self._quicksound_config)
            self.master.switch_frame(P03_SETUP)

        def _sound_display_name(filename):
            return os.path.splitext(os.path.basename(filename))[0]

        def _toggle_quicksound_labels():
            self._quicksound_settings["labels_visible"] = not self._quicksound_settings["labels_visible"]
            save_quicksound_settings(datadir, self._quicksound_settings)
            self.master.switch_frame(P03_SETUP)

        qs_button_font = ("Bebas Neue Bold", 26)
        qs_button_font_small = ("Bebas Neue Bold", 22)
        qs_button_bg = sys_clr[8]
        qs_button_fg = sys_clr[9]
        qs_button_active_fg = sys_clr[9]
        qs_button_off_fg = sys_clr[11]

        def _make_qs_button(text, x, y, width, height, command, fg=None, font=None, anchor="c"):
            button = tk.Label(
                self._setup_parent("AUDIO"),
                bg=qs_button_bg,
                fg=fg or qs_button_fg,
                font=font or qs_button_font,
                text=text,
                anchor=anchor,
                bd=4,
                relief="raised",
            )
            button.bind("<ButtonPress-1>", lambda _event, b=button: b.config(relief="sunken"))
            button.bind("<ButtonRelease-1>", lambda _event, b=button, cmd=command: (b.config(relief="raised"), cmd()))
            self._setup_place(button, "AUDIO", x, y, width, height)
            return button

        lbl_qs_title = tk.Label(self._setup_parent("AUDIO"), text="QUICKSOUND", font=(fonts[6], 25), bg=sys_clr[0], fg=sys_clr[9], anchor="w")
        self._setup_place(lbl_qs_title, "AUDIO", 35, 112, 270, 34)
        lbl_qs_select_title = tk.Label(self._setup_parent("AUDIO"), text="SELECT", font=(fonts[6], 25), bg=sys_clr[0], fg=sys_clr[9], anchor="w")
        self._setup_place(lbl_qs_select_title, "AUDIO", 380, 112, 180, 34)
        qs_labels_text = "LBL ON" if self._quicksound_settings["labels_visible"] else "LBL OFF"
        qs_labels_fg = qs_button_active_fg if self._quicksound_settings["labels_visible"] else qs_button_off_fg
        _make_qs_button(qs_labels_text, 205, 108, 145, 44, _toggle_quicksound_labels, fg=qs_labels_fg, font=qs_button_font_small)

        self._qs_select_target = {"options": [], "command": None}
        qs_select_frame = tk.Frame(self._setup_parent("AUDIO"), bg=sys_clr[8], bd=4, relief="raised")
        self._setup_place(qs_select_frame, "AUDIO", 380, 165, 270, 445)
        qs_select_scroll = tk.Scale(
            qs_select_frame,
            from_=0,
            to=100,
            orient="vertical",
            showvalue=0,
            sliderlength=80,
            width=28,
            bg=qs_button_fg,
            activebackground=qs_button_fg,
            troughcolor=sys_clr[8],
            highlightbackground=sys_clr[8],
            highlightcolor=sys_clr[8],
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
        )
        def _sync_qs_scroll(first, _last=None):
            qs_select_scroll.set(float(first) * 100.0)

        qs_select_list = tk.Listbox(
            qs_select_frame,
            bg=sys_clr[8],
            fg=sys_clr[9],
            selectbackground=sys_clr[9],
            selectforeground=sys_clr[8],
            font=(fonts[6], 24),
            activestyle="none",
            yscrollcommand=_sync_qs_scroll,
            borderwidth=0,
            highlightthickness=0,
        )
        qs_select_scroll.config(command=lambda value: qs_select_list.yview_moveto(float(value) / 100.0))
        qs_select_scroll.pack(side="right", fill="y")
        qs_select_list.pack(side="left", fill="both", expand=True)

        def _show_quicksound_options(index, kind):
            if kind == "folder":
                options = quicksound_folders or [self._quicksound_config[index]["folder"]]
                command = lambda value, index=index: _set_quicksound_folder(index, value)
            else:
                folder_name = self._quicksound_config[index]["folder"]
                options = list_quicksound_files(snd_fldr, folder_name) or [self._quicksound_config[index]["file"]]
                command = lambda value, index=index: _set_quicksound_file(index, value)

            self._qs_select_target = {"options": options, "command": command}
            qs_select_list.delete(0, "end")
            for option in options:
                qs_select_list.insert("end", _sound_display_name(option) if kind == "file" else option)
            qs_select_scroll.set(0)

        def _select_quicksound_option(_event=None):
            selection = qs_select_list.curselection()
            if not selection:
                return
            value = self._qs_select_target["options"][selection[0]]
            self._qs_select_target["command"](value)

        qs_select_list.bind("<ButtonRelease-1>", _select_quicksound_option)
        qs_select_list.bind("<Return>", _select_quicksound_option)
        for i, quicksound in enumerate(self._quicksound_config):
            y_pos = 155 + i * 112
            lbl_qs_name = tk.Label(self._setup_parent("AUDIO"), font=(fonts[6], 22), text=f"Q{i + 1}", bg=sys_clr[8], fg=sys_clr[9], anchor="w")
            self._setup_place(lbl_qs_name, "AUDIO", 35, y_pos, 320, 28)

            _make_qs_button(
                quicksound["folder"],
                35,
                y_pos + 32,
                115,
                36,
                lambda i=i: _show_quicksound_options(i, "folder"),
                font=qs_button_font_small,
                anchor="w",
            )
            _make_qs_button(
                _sound_display_name(quicksound["file"]),
                158,
                y_pos + 32,
                200,
                36,
                lambda i=i: _show_quicksound_options(i, "file"),
                font=qs_button_font_small,
                anchor="w",
            )
            _make_qs_button(
                quicksound["mode"],
                35,
                y_pos + 76,
                150,
                36,
                lambda i=i: _cycle_quicksound_value(i, "mode", QUICKSOUND_MODES),
                font=qs_button_font,
            )
            _make_qs_button(
                quicksound["color"],
                195,
                y_pos + 76,
                90,
                36,
                lambda i=i: _cycle_quicksound_value(i, "color", QUICKSOUND_COLORS),
                fg=quicksound_color_fg.get(quicksound["color"], sys_clr[9]),
                font=qs_button_font,
            )
        _show_quicksound_options(0, "file")
        self._create_scale_setup()
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        read.buttons_menu()
        #----------------------------------------------------------------------------------
        # RB BUTTON LABELS
        #----------------------------------------------------------------------------------
        #--------------------------------------------------------------------------
        # RB01
        #--------------------------------------------------------------------------
        lbls_btnrb01 = []
        x_pos = x_start_RB
        x_pos2 = x_start_RB
        for i in range(quant_btns_RB01):
            lbls_btnrb01 = tk.Label(self, **lbl_style_setup_btns, bg=sys_clr[8], fg=sys_clr[9])
            if device == DEVICE_B_txt[2]:
                lbls_btnrb01.config(text=rb01_DEV002_txt[i])
                if i < (quant_btns_RB01/2):
                    lbls_btnrb01.place(x=x_pos, y=y_l10, width=lbl_w, height=lbl_f_h)
                    self._remember_visible_widget("dev002_hw_sw", lbls_btnrb01)
                    x_pos += +px_to_next
                else:
                    lbls_btnrb01.place(x=x_pos2, y=y_l12, width=lbl_w, height=lbl_f_h)
                    self._remember_visible_widget("dev002_hw_sw", lbls_btnrb01)
                    x_pos2 += +px_to_next
        #--------------------------------------------------------------------------
        # RB02
        #--------------------------------------------------------------------------
        lbls_btnRB02 = []
        x_pos = x_start_RB
        x_pos2 = x_start_RB
        for i in range(quant_btns_RB02):
            lbls_btnRB02 = tk.Label(self, **lbl_style_setup_btns, bg=sys_clr[8], fg=sys_clr[9])
            if device == DEVICE_B_txt[2]:
                lbls_btnRB02.config(text=rb02_DEV002_txt[i])
                if i < (quant_btns_RB02/2):
                    lbls_btnRB02.place(x=x_pos, y=y_l14, width=lbl_w, height=lbl_f_h)
                    self._remember_visible_widget("dev002_hw_sw", lbls_btnRB02)
                    x_pos += +px_to_next
                else:
                    lbls_btnRB02.place(x=x_pos2, y=y_l16, width=lbl_w, height=lbl_f_h)
                    self._remember_visible_widget("dev002_hw_sw", lbls_btnRB02)
                    x_pos2 += +px_to_next
        #--------------------------------------------------------------------------
        # RB03
        #--------------------------------------------------------------------------
        lbls_btnRB03 = []
        x_pos = x_start_RB
        x_pos2 = x_start_RB
        for i in range(quant_btns_RB03):
            lbls_btnRB03 = tk.Label(self, **lbl_style_setup_btns, bg=sys_clr[8], fg=sys_clr[9])
            if device == DEVICE_B_txt[2]:
                lbls_btnRB03.config(text=rb03_DEV002_txt[i])
                if i < (quant_btns_RB03/2):
                    lbls_btnRB03.place(x=x_pos, y=y_l18, width=lbl_w, height=lbl_f_h)
                    self._remember_visible_widget("dev002_hw_sw", lbls_btnRB03)
                    x_pos += +px_to_next
                else:
                    lbls_btnRB03.place(x=x_pos2, y=y_l20, width=lbl_w, height=lbl_f_h)
                    self._remember_visible_widget("dev002_hw_sw", lbls_btnRB03)
                    x_pos2 += +px_to_next
        #----------------------------------------------------------------------------------
        # RB BUTTONS
        #----------------------------------------------------------------------------------
        if device == DEVICE_B_txt[2]:
            global btns_RB01
            global btn_RB01
            global btns_RB02
            global btn_RB02
            global btns_RB03
            global btn_RB03
            #--------------------------------------------------------------------------
            # RB01
            #--------------------------------------------------------------------------
            btns_RB01 = []
            x_pos = x_start_RB
            x_pos2 = x_start_RB
            for i in range(quant_btns_RB01):
                btn_RB01 = tk.Button(canvas, bg=sys_clr[8], font=(fonts[1], 28), command=lambda i=i: read.toggle_relay(i))
                if i < (quant_btns_RB01/2):
                    btn_RB01.place(x=x_pos, y=y_l11, width=btn_w, height=btn_h)
                    self._remember_visible_widget("dev002_hw_sw", btn_RB01)
                    x_pos += +px_to_next
                else:
                    btn_RB01.place(x=x_pos2, y=y_l13, width=btn_w, height=btn_h)
                    self._remember_visible_widget("dev002_hw_sw", btn_RB01)
                    x_pos2 += +px_to_next
                btns_RB01.append(btn_RB01)
            #--------------------------------------------------------------------------
            # RB02
            #--------------------------------------------------------------------------
            btns_RB02 = []
            x_pos = x_start_RB
            x_pos2 = x_start_RB
            for i in range(quant_btns_RB02):
                btn_RB02 = tk.Button(canvas, bg=sys_clr[8], font=(fonts[1], 28), command=lambda i=i: read.toggle_relay(i+16))
                if i < (quant_btns_RB02/2):
                    btn_RB02.place(x=x_pos, y=y_l15, width=btn_w, height=btn_h)
                    self._remember_visible_widget("dev002_hw_sw", btn_RB02)
                    x_pos += +px_to_next
                else:
                    btn_RB02.place(x=x_pos2, y=y_l17, width=btn_w, height=btn_h)
                    self._remember_visible_widget("dev002_hw_sw", btn_RB02)
                    x_pos2 += +px_to_next
                btns_RB02.append(btn_RB02)
            #--------------------------------------------------------------------------
            # RB03
            #--------------------------------------------------------------------------
            btns_RB03 = []
            x_pos = x_start_RB
            x_pos2 = x_start_RB
            for i in range(quant_btns_RB03):
                btn_RB03 = tk.Button(canvas, bg=sys_clr[8], font=(fonts[1], 28), command=lambda i=i: read.toggle_relay(i+32))
                if i < (quant_btns_RB03/2):
                    btn_RB03.place(x=x_pos, y=y_l19, width=btn_w, height=btn_h)
                    self._remember_visible_widget("dev002_hw_sw", btn_RB03)
                    x_pos += +px_to_next
                else:
                    btn_RB03.place(x=x_pos2, y=y_l21, width=btn_w, height=btn_h)
                    self._remember_visible_widget("dev002_hw_sw", btn_RB03)
                    x_pos2 += +px_to_next
                btns_RB03.append(btn_RB03)
        #----------------------------------------------------------------------------------
        # FAVORITES BUTTONS
        #----------------------------------------------------------------------------------
        global quant_btns_FAV
        global btn_FAV
        global btns_FAV
        btns_FAV = []
        x_pos = x_start_FAV
        x_pos2 = x_start_FAV
        x_pos11 = x_start_RB_FAV
        x_pos13 = x_start_RB_FAV
        x_pos15 = x_start_RB_FAV
        x_pos17 = x_start_RB_FAV
        x_pos19 = x_start_RB_FAV
        x_pos21 = x_start_RB_FAV
        self.fav_button_render_state = {}

        if device == DEVICE_B_txt[1]:
            quant_btns_FAV = quant_btns_HW + quant_btns_SW
        elif device == DEVICE_B_txt[2]:
            quant_btns_FAV = quant_btns_HW + quant_btns_SW + quant_btns_RB01 + quant_btns_RB02 + quant_btns_RB03
        elif device == DEVICE_B_txt[4]:
            quant_btns_FAV = quant_btns_HW + quant_btns_SW
        elif device == DEVICE_B_txt[8]:
            quant_btns_FAV = quant_btns_HW + quant_btns_SW

        def _toggle_fav_button(index, button):
            is_active = read.toggle_btn_FAV(index)
            btn_states_FAV[index] = is_active
            if is_active:
                button.config(bg=sys_clr[10], fg=sys_clr[8])
            else:
                button.config(bg=sys_clr[8], fg=sys_clr[11])
            
        for i in range(quant_btns_FAV):
            btn_FAV = tk.Button(self._setup_parent("HW/SW", canvas), bg=sys_clr[8], text="F", font=(fonts[1], 20))
            btn_FAV.config(command=lambda i=i, button=btn_FAV: _toggle_fav_button(i, button))
                
            if i < 10:
                self._setup_place(btn_FAV, "HW/SW", x_pos, y_l3, btn_f_w, btn_h)
                x_pos += +px_to_next
            elif i < 20:
                self._setup_place(btn_FAV, "HW/SW", x_pos2, y_l5, btn_f_w, btn_h)
                x_pos2 += +px_to_next
            elif i < 28:
                self._setup_place(btn_FAV, "HW/SW", x_pos11, y_l11, btn_f_w, btn_h)
                x_pos11 += +px_to_next
            elif i < 36:
                self._setup_place(btn_FAV, "HW/SW", x_pos13, y_l13, btn_f_w, btn_h)
                x_pos13 += +px_to_next
            elif i < 44:
                self._setup_place(btn_FAV, "HW/SW", x_pos15, y_l15, btn_f_w, btn_h)
                x_pos15 += +px_to_next
            elif i < 52:
                self._setup_place(btn_FAV, "HW/SW", x_pos17, y_l17, btn_f_w, btn_h)
                x_pos17 += +px_to_next
            elif i < 60:
                self._setup_place(btn_FAV, "HW/SW", x_pos19, y_l19, btn_f_w, btn_h)
                x_pos19 += +px_to_next
            elif i < 68:
                self._setup_place(btn_FAV, "HW/SW", x_pos21, y_l21, btn_f_w, btn_h)
                x_pos21 += +px_to_next
            btns_FAV.append(btn_FAV)
        #----------------------------------------------------------------------------------
        # END INIT
        #----------------------------------------------------------------------------------
        if device == DEVICE_B_txt[1]:
            self._show_dev001_setup_subpage(P03_SETUP.dev001_setup_subpage)
        elif device == DEVICE_B_txt[2]:
            self._show_dev002_setup_subpage(getattr(P03_SETUP, "dev002_setup_subpage", "HW/SW"))
        self.update_page()

    def _setup_parent(self, section, fallback_parent=None):
        if device == DEVICE_B_txt[1] and hasattr(self, "_dev001_setup_frames"):
            return self._dev001_setup_frames[section]
        if device == DEVICE_B_txt[2] and section == "SCALE" and hasattr(self, "_dev002_scale_frame"):
            return self._dev002_scale_frame
        if section in ("AUDIO", "ODOMETER", "SCALE"):
            if not hasattr(self, "_hidden_setup_frames"):
                self._hidden_setup_frames = {}
            if section not in self._hidden_setup_frames:
                self._hidden_setup_frames[section] = tk.Frame(self, bg=sys_clr[0], highlightthickness=0)
            return self._hidden_setup_frames[section]
        return fallback_parent if fallback_parent is not None else self

    def _setup_place(self, widget, section, x, y, width, height):
        if device == DEVICE_B_txt[1] and hasattr(self, "_dev001_setup_area"):
            area_x, area_y, _, _ = self._dev001_setup_area
            widget.place(x=x - area_x, y=y - area_y, width=width, height=height)
        elif device == DEVICE_B_txt[2] and section == "SCALE" and hasattr(self, "_dev002_scale_area"):
            area_x, area_y, _, _ = self._dev002_scale_area
            widget.place(x=x - area_x, y=y - area_y, width=width, height=height)
        elif section in ("AUDIO", "ODOMETER", "SCALE"):
            return
        else:
            widget.place(x=x, y=y, width=width, height=height)
            if device == DEVICE_B_txt[2] and section == "HW/SW":
                self._remember_visible_widget("dev002_hw_sw", widget)

    def _remember_visible_widget(self, group, widget):
        if not hasattr(self, "_visible_widget_groups"):
            self._visible_widget_groups = {}
        widgets = self._visible_widget_groups.setdefault(group, [])
        if widget not in widgets:
            widgets.append(widget)
        widget._kidd_place_info = widget.place_info()

    def _set_visible_group(self, group, visible):
        for widget in getattr(self, "_visible_widget_groups", {}).get(group, []):
            if visible:
                place_info = getattr(widget, "_kidd_place_info", None)
                if place_info:
                    widget.place(**place_info)
            else:
                widget.place_forget()

    def _create_dev001_submenu(self):
        self.dev001_submenu_buttons = {}
        items = [("HW/SW", 230), ("AUDIO", 360), ("ODOMETER", 490), ("SCALE", 620)]
        for name, x_pos in items:
            btn = tk.Button(
                self,
                bg=sys_clr[8],
                fg=sys_clr[9],
                activebackground=sys_clr[8],
                activeforeground=sys_clr[9],
                bd=4,
                highlightthickness=0,
                font=(fonts[0], 16),
                text=name,
                command=lambda name=name: self._show_dev001_setup_subpage(name),
            )
            btn.place(x=x_pos, y=18, width=115, height=32)
            self.dev001_submenu_buttons[name] = btn

    def _create_dev002_submenu(self):
        self.dev002_submenu_buttons = {}
        items = [("HW/SW", 230), ("SCALE", 620)]
        for name, x_pos in items:
            btn = tk.Button(
                self,
                bg=sys_clr[8],
                fg=sys_clr[9],
                activebackground=sys_clr[8],
                activeforeground=sys_clr[9],
                bd=4,
                highlightthickness=0,
                font=(fonts[0], 16),
                text=name,
                command=lambda name=name: self._show_dev002_setup_subpage(name),
            )
            btn.place(x=x_pos, y=18, width=115, height=32)
            self.dev002_submenu_buttons[name] = btn

    def _show_dev001_setup_subpage(self, name):
        if not hasattr(self, "_dev001_setup_frames"):
            return
        P03_SETUP.dev001_setup_subpage = name
        area_x, area_y, area_w, area_h = self._dev001_setup_area
        for frame_name, frame in self._dev001_setup_frames.items():
            if frame_name == name:
                frame.place(x=area_x, y=area_y, width=area_w, height=area_h)
            else:
                frame.place_forget()
        self._set_visible_group("dev001_device_status", name == "HW/SW")
        for frame_name, button in getattr(self, "dev001_submenu_buttons", {}).items():
            if frame_name == name:
                button.config(bg=sys_clr[8], fg=sys_clr[9], relief="sunken")
            else:
                button.config(bg=sys_clr[8], fg=sys_clr[11], relief="raised")

    def _show_dev002_setup_subpage(self, name):
        if not hasattr(self, "_dev002_scale_frame"):
            return
        P03_SETUP.dev002_setup_subpage = name
        if name == "SCALE":
            self._set_visible_group("dev002_hw_sw", False)
            area_x, area_y, area_w, area_h = self._dev002_scale_area
            self._dev002_scale_frame.place(x=area_x, y=area_y, width=area_w, height=area_h)
        else:
            self._dev002_scale_frame.place_forget()
            self._set_visible_group("dev002_hw_sw", True)
        for frame_name, button in getattr(self, "dev002_submenu_buttons", {}).items():
            if frame_name == name:
                button.config(bg=sys_clr[8], fg=sys_clr[9], relief="sunken")
            else:
                button.config(bg=sys_clr[8], fg=sys_clr[11], relief="raised")

    def _create_scale_setup(self):
        if device not in (DEVICE_B_txt[1], DEVICE_B_txt[2]):
            return
        device_key = device
        scale_data = ensure_gauge_scale_config(datadir)
        rows = scale_data.get(device_key, DEFAULT_GAUGE_SCALE.get(device_key, []))
        if not rows:
            return

        parent = self._setup_parent("SCALE")
        for child in parent.winfo_children():
            child.destroy()

        y_offset = 0
        title = tk.Label(parent, text="SCALE", font=(fonts[6], 26), bg=sys_clr[0], fg=sys_clr[9], anchor="w")
        title.place(x=20, y=20 + y_offset, width=180, height=34)
        headers = [("GAUGE", 20, 65 + y_offset, 145), ("MIN", 175, 65 + y_offset, 120), ("MAX", 365, 65 + y_offset, 120)]
        for text, x_pos, y_pos, width in headers:
            tk.Label(parent, text=text, font=(fonts[6], 18), bg=sys_clr[8], fg=sys_clr[9], anchor="c").place(
                x=x_pos, y=y_pos, width=width, height=24
            )

        def _fmt(value):
            try:
                number = float(value)
            except (TypeError, ValueError):
                return str(value)
            return str(int(number)) if number.is_integer() else f"{number:.1f}"

        def _change(row, field, direction, value_var):
            step = float(row.get("step", 1))
            value = float(row.get(field, 0)) + (step * direction)
            other = float(row.get("max" if field == "min" else "min", 0))
            if field == "min":
                value = min(value, other - step)
            else:
                value = max(value, other + step)
            value = int(value) if float(value).is_integer() else round(value, 2)
            row[field] = value
            save_gauge_scale_value(datadir, device_key, row["key"], field, value)
            value_var.set(_fmt(value))

        max_visible_rows = 10 if device_key == DEVICE_B_txt[2] else 6
        row_height = 42 if device_key == DEVICE_B_txt[2] else 54
        button_w = 42 if device_key == DEVICE_B_txt[2] else 54
        value_w = 76
        font_size = 19 if device_key == DEVICE_B_txt[2] else 22
        for row_index, row in enumerate(rows[:max_visible_rows]):
            y_pos = 95 + y_offset + row_index * row_height
            label = tk.Label(parent, text=row["label"], font=(fonts[6], font_size), bg=sys_clr[8], fg=sys_clr[9], anchor="w")
            label.place(x=20, y=y_pos, width=145, height=row_height - 6)

            min_var = tk.StringVar(value=_fmt(row["min"]))
            max_var = tk.StringVar(value=_fmt(row["max"]))
            for field, x_pos, var in (("min", 175, min_var), ("max", 365, max_var)):
                tk.Button(
                    parent,
                    text="-",
                    bg=sys_clr[8],
                    fg=sys_clr[9],
                    activebackground=sys_clr[8],
                    activeforeground=sys_clr[9],
                    font=(fonts[0], 16),
                    command=lambda r=row, f=field, v=var: _change(r, f, -1, v),
                ).place(x=x_pos, y=y_pos, width=button_w, height=row_height - 6)
                tk.Label(parent, textvariable=var, font=(fonts[6], font_size), bg=sys_clr[8], fg=sys_clr[9], anchor="c").place(
                    x=x_pos + button_w + 4, y=y_pos, width=value_w, height=row_height - 6
                )
                tk.Button(
                    parent,
                    text="+",
                    bg=sys_clr[8],
                    fg=sys_clr[9],
                    activebackground=sys_clr[8],
                    activeforeground=sys_clr[9],
                    font=(fonts[0], 16),
                    command=lambda r=row, f=field, v=var: _change(r, f, 1, v),
                ).place(x=x_pos + button_w + value_w + 8, y=y_pos, width=button_w, height=row_height - 6)

    def _create_setup_console(self, device_key, title_x, title_y, title_w, title_h, text_x, text_y, text_w, text_h, font_size):
        self.setup_console_device = device_key
        log(f"[SETUP] {device_key} console ready", device=device_key)
        title = tk.Label(self, text="CONSOLE", font=(fonts[6], 22), bg=sys_clr[8], fg=sys_clr[9], anchor="w")
        title.place(x=title_x, y=title_y, width=title_w, height=title_h)
        if device_key == "DEV002":
            self._remember_visible_widget("dev002_hw_sw", title)

        self.console_text = tk.Text(
            self,
            bg=sys_clr[8],
            fg=sys_clr[9],
            insertbackground=sys_clr[9],
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            font=(fonts[6], font_size),
            wrap="word",
            state="disabled",
        )
        self.console_text.place(x=text_x, y=text_y, width=text_w, height=text_h)
        if device_key == "DEV002":
            self._remember_visible_widget("dev002_hw_sw", self.console_text)
        self.console_text_state = None
        self.setup_gps_log_times = {}
        self._update_setup_console()
        if device_key == "DEV001":
            self._poll_dev001_gps_console()

    def _create_dev001_device_status(self):
        self.dev001_device_probe_at = 0.0
        self.dev001_device_reachable_state = {}
        self.dev001_device_status_labels = {}
        title = tk.Label(self, text="DEVICE STATUS", font=(fonts[6], 22), bg=sys_clr[8], fg=sys_clr[9], anchor="w")
        title.place(x=620, y=265, width=520, height=28)
        self._remember_visible_widget("dev001_device_status", title)

        headers = [("DEVICE", 620, 295, 150), ("ON", 780, 295, 70), ("OK", 860, 295, 70), ("ADDR", 940, 295, 120)]
        for text, x_pos, y_pos, width in headers:
            header = tk.Label(self, text=text, font=(fonts[6], 18), bg=sys_clr[8], fg=sys_clr[9], anchor="c")
            header.place(x=x_pos, y=y_pos, width=width, height=24)
            self._remember_visible_widget("dev001_device_status", header)

        for row_index, row in enumerate(self._dev001_device_rows()):
            y_pos = 325 + row_index * 34
            name_label = tk.Label(self, text=row["name"], font=(fonts[6], 20), bg=sys_clr[8], fg=sys_clr[9], anchor="w")
            name_label.place(x=620, y=y_pos, width=150, height=28)
            on_label = tk.Label(self, font=(fonts[6], 20), bg=sys_clr[8], fg=sys_clr[11], anchor="c")
            ok_label = tk.Label(self, font=(fonts[6], 20), bg=sys_clr[8], fg=sys_clr[11], anchor="c")
            addr_label = tk.Label(self, text=row["addr"], font=(fonts[6], 18), bg=sys_clr[8], fg=sys_clr[9], anchor="c")
            on_label.place(x=780, y=y_pos, width=70, height=28)
            ok_label.place(x=860, y=y_pos, width=70, height=28)
            addr_label.place(x=940, y=y_pos, width=120, height=28)
            for widget in (name_label, on_label, ok_label, addr_label):
                self._remember_visible_widget("dev001_device_status", widget)
            self.dev001_device_status_labels[row["name"]] = {"on": on_label, "ok": ok_label, "addr": addr_label}

    def _dev001_device_rows(self):
        return [
            {"name": "GPS", "hw": 0, "kind": "gps", "addr": gps_port or "---"},
            {"name": "MICRO", "hw": 1, "kind": "mic", "addr": "AUDIO"},
            {"name": "TANK", "hw": 6, "kind": "obj", "obj": "ads", "addr": f"0x{i2cAI01:02X}"},
        ]

    def _probe_dev001_devices(self):
        now = time.time()
        if now < getattr(self, "dev001_device_probe_at", 0.0):
            return
        self.dev001_device_probe_at = now + 2.0
        reachable = {}
        for row in self._dev001_device_rows():
            active = bool(btn_states_HW[row["hw"]]) if row["hw"] < len(btn_states_HW) else False
            if not active:
                reachable[row["name"]] = None
            elif row["kind"] == "gps":
                reachable[row["name"]] = gps_serial is not None
            elif row["kind"] == "mic":
                reachable[row["name"]] = None
            else:
                reachable[row["name"]] = globals().get(row["obj"]) is not None
        self.dev001_device_reachable_state = reachable

    def _update_dev001_device_status(self):
        if not hasattr(self, "dev001_device_status_labels"):
            return
        self._probe_dev001_devices()
        for row in self._dev001_device_rows():
            labels = self.dev001_device_status_labels[row["name"]]
            active = bool(btn_states_HW[row["hw"]]) if row["hw"] < len(btn_states_HW) else False
            reachable = self.dev001_device_reachable_state.get(row["name"])
            labels["on"].config(text="ON" if active else "OFF", fg=sys_clr[10] if active else sys_clr[11])
            labels["addr"].config(text=row["addr"])
            if reachable is None:
                labels["ok"].config(text="N/A" if active else "--", fg=sys_clr[9] if active else sys_clr[11])
            else:
                labels["ok"].config(text="YES" if reachable else "NO", fg=sys_clr[10] if reachable else sys_clr[11])

    def _create_dev002_i2c_status(self):
        self.dev002_i2c_probe_at = 0.0
        self.dev002_i2c_reachable_state = {}
        self.dev002_i2c_status_labels = {}
        title = tk.Label(self, text="I2C STATUS", font=(fonts[6], 22), bg=sys_clr[8], fg=sys_clr[9], anchor="w")
        title.place(x=620, y=265, width=520, height=28)
        self._remember_visible_widget("dev002_hw_sw", title)

        headers = [("DEVICE", 620, 295, 150), ("ON", 780, 295, 70), ("OK", 860, 295, 70), ("ADDR", 940, 295, 90)]
        for text, x_pos, y_pos, width in headers:
            header = tk.Label(self, text=text, font=(fonts[6], 18), bg=sys_clr[8], fg=sys_clr[9], anchor="c")
            header.place(x=x_pos, y=y_pos, width=width, height=24)
            self._remember_visible_widget("dev002_hw_sw", header)

        rows = self._dev002_i2c_rows()
        for row_index, row in enumerate(rows):
            y_pos = 325 + row_index * 34
            name_label = tk.Label(self, text=row["name"], font=(fonts[6], 20), bg=sys_clr[8], fg=sys_clr[9], anchor="w")
            name_label.place(x=620, y=y_pos, width=150, height=28)
            on_label = tk.Label(self, font=(fonts[6], 20), bg=sys_clr[8], fg=sys_clr[11], anchor="c")
            ok_label = tk.Label(self, font=(fonts[6], 20), bg=sys_clr[8], fg=sys_clr[11], anchor="c")
            addr_label = tk.Label(self, text=row["addr"], font=(fonts[6], 18), bg=sys_clr[8], fg=sys_clr[9], anchor="c")
            on_label.place(x=780, y=y_pos, width=70, height=28)
            ok_label.place(x=860, y=y_pos, width=70, height=28)
            addr_label.place(x=940, y=y_pos, width=90, height=28)
            for widget in (name_label, on_label, ok_label, addr_label):
                self._remember_visible_widget("dev002_hw_sw", widget)
            self.dev002_i2c_status_labels[row["name"]] = {"on": on_label, "ok": ok_label}

    def _dev002_i2c_rows(self):
        return [
            {"name": "RB01", "hw": 0, "kind": "rb", "rb": 0, "addr": f"0x{i2c_addr_dev02rb[0]:02X}"},
            {"name": "RB02", "hw": 1, "kind": "rb", "rb": 1, "addr": f"0x{i2c_addr_dev02rb[1]:02X}"},
            {"name": "RB03", "hw": 2, "kind": "rb", "rb": 2, "addr": f"0x{i2c_addr_dev02rb[2]:02X}"},
            {"name": "AI01", "hw": 6, "kind": "obj", "obj": "ads", "addr": f"0x{i2cAI01:02X}"},
            {"name": "DI01", "hw": 7, "kind": "obj", "obj": "aw001", "addr": f"0x{i2cDI01:02X}"},
            {"name": "DI02", "hw": 8, "kind": "obj", "obj": "aw002", "addr": f"0x{i2cDI02:02X}"},
        ]

    def _probe_dev002_i2c(self):
        now = time.time()
        if now < getattr(self, "dev002_i2c_probe_at", 0.0):
            return
        self.dev002_i2c_probe_at = now + 2.0
        reachable = {}
        for row in self._dev002_i2c_rows():
            active = bool(btn_states_HW[row["hw"]]) if row["hw"] < len(btn_states_HW) else False
            if not active:
                reachable[row["name"]] = None
            elif row["kind"] == "rb":
                reachable[row["name"]] = self._probe_dev002_relay_board(row["rb"])
            else:
                reachable[row["name"]] = globals().get(row["obj"]) is not None
        self.dev002_i2c_reachable_state = reachable

    def _probe_dev002_relay_board(self, board_index):
        if not (sys_linux and sys_pi):
            return None
        try:
            bus = buses[board_index]
            address = i2c_addr_dev02rb[board_index]
            bus.read_byte(address)
            return True
        except Exception:
            return False

    def _update_dev002_i2c_status(self):
        if not hasattr(self, "dev002_i2c_status_labels"):
            return
        self._probe_dev002_i2c()
        for row in self._dev002_i2c_rows():
            labels = self.dev002_i2c_status_labels[row["name"]]
            active = bool(btn_states_HW[row["hw"]]) if row["hw"] < len(btn_states_HW) else False
            reachable = self.dev002_i2c_reachable_state.get(row["name"])
            labels["on"].config(text="ON" if active else "OFF", fg=sys_clr[10] if active else sys_clr[11])
            if reachable is None:
                labels["ok"].config(text="N/A" if active else "--", fg=sys_clr[9] if active else sys_clr[11])
            else:
                labels["ok"].config(text="YES" if reachable else "NO", fg=sys_clr[10] if reachable else sys_clr[11])

    def _update_setup_console(self):
        if not hasattr(self, "console_text"):
            return
        self._render_setup_console()
        self.after(500, self._update_setup_console)

    def _refresh_console_now(self):
        if hasattr(self, "console_text"):
            self.console_text_state = None
            self._render_setup_console()

    def _render_setup_console(self):
        device_key = getattr(self, "setup_console_device", None)
        line_limit = 25 if device_key == "DEV001" else 30
        lines = "\n".join(get_console_lines(line_limit, device=device_key))
        if self.console_text_state != lines:
            self.console_text.configure(state="normal")
            self.console_text.delete("1.0", "end")
            self.console_text.insert("1.0", lines)
            self.console_text.see("end")
            self.console_text.configure(state="disabled")
            self.console_text_state = lines

    def _log_setup_gps(self, message, interval=5.0):
        now = time.time()
        if now - self.setup_gps_log_times.get(message, 0.0) >= interval:
            log(message, device="DEV001")
            self.setup_gps_log_times[message] = now

    def _poll_dev001_gps_console(self):
        if not hasattr(self, "console_text"):
            return
        try:
            sync_context(globals())
            gps_enabled = bool(btn_states_HW[0]) if btn_states_HW else False
            if gps_enabled:
                if gps_port is None:
                    self._log_setup_gps("[GPS] HW aktiv, aber kein GPS-Port erkannt")
                elif gps_serial is None:
                    self._log_setup_gps(f"[GPS] HW aktiv, Port {gps_port}, aber Serial nicht offen")
                else:
                    read.gps_data()
                    sync_context(globals())
                self._refresh_console_now()
        except Exception as e:
            log(f"[GPS] Setup Diagnose Fehler: {e}", device="DEV001")
            self._refresh_console_now()
        self.after(1000, self._poll_dev001_gps_console)

    def _update_hw_button(self, index):
        if btn_states_HW[index]:
            state = (states_txt_act[1], sys_clr[10])
        else:
            state = (states_txt_act[0], sys_clr[11])
        if self.hw_button_render_state.get(index) != state:
            self.btns_HW[index].config(text=state[0], fg=state[1])
            self.hw_button_render_state[index] = state

    def _update_sw_button(self, index):
        on_texts = btnsw_DEV002_txt_1 if device == DEVICE_B_txt[2] else btnsw_DEV001_txt_1
        off_texts = btnsw_DEV002_txt_0 if device == DEVICE_B_txt[2] else btnsw_DEV001_txt_0
        if btn_states_SW[index]:
            state = on_texts[index]
        else:
            state = off_texts[index]
        if self.sw_button_render_state.get(index) != state:
            self.btns_SW[index].config(text=state)
            self.sw_button_render_state[index] = state

    def _toggle_hw_button(self, index):
        read.toggle_btn_HW(index)
        sync_context(globals())
        self._update_hw_button(index)
        self._refresh_console_now()

    def _toggle_sw_button(self, index):
        read.toggle_btn_SW(index)
        sync_context(globals())
        self._update_sw_button(index)
        self._refresh_console_now()

    def update_page(self):
        #----------------------------------------------------------------------------------
        # HW BUTTONS
        #----------------------------------------------------------------------------------
        for i in range(quant_btns_HW):              
            self._update_hw_button(i)
        #----------------------------------------------------------------------------------
        # SW BUTTONS
        #----------------------------------------------------------------------------------
        for i in range(quant_btns_SW):
            self._update_sw_button(i)
        #----------------------------------------------------------------------------------
        # FAV BUTTONS
        #----------------------------------------------------------------------------------
        for i in range(quant_btns_FAV):
            if btn_states_FAV[i]:
                state = (sys_clr[10], sys_clr[8])
            else:
                state = (sys_clr[8], sys_clr[11])
            if self.fav_button_render_state.get(i) != state:
                btns_FAV[i].config(bg=state[0], fg=state[1])
                self.fav_button_render_state[i] = state
        if device == DEVICE_B_txt[1]:
            self._update_dev001_device_status()
        #----------------------------------------------------------------------------------
        # RB BUTTONS
        #----------------------------------------------------------------------------------
        if device == DEVICE_B_txt[2]:
            self._update_dev002_i2c_status()
            #------------------------------------------------------------------------------
            # DEV002 BTNRB01
            #------------------------------------------------------------------------------
            for i in range(quant_btns_RB01):
                board = i // 16
                bit = i % 16
                if bit < 8:
                    state = not (relay_states_1to8[board] & (1 << bit))
                else:
                    state = not (relay_states_9to16[board] & (1 << (bit - 8)))

                if state:
                    btns_RB01[i].config(text=states_txt_act[1], fg=sys_clr[10])
                else:
                    btns_RB01[i].config(text=states_txt_act[0], fg=sys_clr[11])
            #------------------------------------------------------------------------------
            # DEV002 BTNRB02
            #------------------------------------------------------------------------------
            for i in range(quant_btns_RB02):
                if btn_states_DEV002RB02[i]:
                    btns_RB02[i].config(text=states_txt_act[1], fg=sys_clr[10])
                else:
                    btns_RB02[i].config(text=states_txt_act[0], fg=sys_clr[11])
            #------------------------------------------------------------------------------
            # DEV002 BTNRB03
            #------------------------------------------------------------------------------
            for i in range(quant_btns_RB03):
                if btn_states_DEV002RB03[i]:
                    btns_RB03[i].config(text=states_txt_act[1], fg=sys_clr[10])
                else:
                    btns_RB03[i].config(text=states_txt_act[0], fg=sys_clr[11])
        self.after(time_conf, self.update_page)
