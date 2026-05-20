from pages.page_context import sync_context

sync_context(globals())

#------------------------------------------------------------------------------------------
# PAGE 03: SETUP
#------------------------------------------------------------------------------------------
class P03_SETUP(tk.Frame):
    if debug == True:
        print (MENU_B_txt[3])
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
        coordinates = []
        for frame_bounds in frames:
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
        # CREATE MAIN CORNERS
        #--------------------------------------------------------------------------
        canvas.create_line(15, 90, 25, 90, fill=colors_corner[0], width=1)      #LT_X
        canvas.create_line(15, 90, 15, 100, fill=colors_corner[1], width=1)     #LT_Y
        canvas.create_line(1250, 90, 1260, 90, fill=colors_corner[0], width=1)  #RT_X
        canvas.create_line(1260, 90, 1260, 100, fill=colors_corner[1], width=1) #RT_Y
        canvas.create_line(15, 255, 25, 255, fill=colors_corner[0], width=1)    #LB_X
        canvas.create_line(15, 255, 15, 245, fill=colors_corner[1], width=1)    #LB_Y
        canvas.create_line(1250, 255, 1260, 255, fill=colors_corner[0], width=1)#RB_X
        canvas.create_line(1260, 255, 1260, 245, fill=colors_corner[1], width=1)#RB_Y
        #--------------------------------------------------------------------------
        # CREATE ADJUST CORNERS
        #--------------------------------------------------------------------------
        canvas.create_line(15, 285, 25, 285, fill=colors_corner[0], width=1)   #LT_X
        canvas.create_line(15, 285, 15, 295, fill=colors_corner[1], width=1)   #LT_Y
        canvas.create_line(290, 285, 300, 285, fill=colors_corner[0], width=1) #RT_X
        canvas.create_line(300, 285, 300, 295, fill=colors_corner[1], width=1) #RT_Y
        canvas.create_line(15, 615, 25, 615, fill=colors_corner[0], width=1)   #LB_X
        canvas.create_line(15, 605, 15, 615, fill=colors_corner[1], width=1)   #LB_Y
        canvas.create_line(290, 615, 300, 615, fill=colors_corner[0], width=1) #RB_X
        canvas.create_line(300, 605, 300, 615, fill=colors_corner[1], width=1) #RB_Y
        #--------------------------------------------------------------------------
        # CREATE KEYPAD CORNERS
        #--------------------------------------------------------------------------
        canvas.create_line(330, 285, 340, 285, fill=colors_corner[0], width=1) #LT_X
        canvas.create_line(330, 285, 330, 295, fill=colors_corner[1], width=1) #LT_Y
        canvas.create_line(650, 285, 660, 285, fill=colors_corner[0], width=1) #RT_X
        canvas.create_line(660, 285, 660, 295, fill=colors_corner[1], width=1) #RT_Y
        canvas.create_line(330, 615, 340, 615, fill=colors_corner[0], width=1) #LB_X
        canvas.create_line(330, 605, 330, 615, fill=colors_corner[1], width=1) #LB_Y
        canvas.create_line(650, 615, 660, 615, fill=colors_corner[0], width=1) #RB_X
        canvas.create_line(660, 605, 660, 615, fill=colors_corner[1], width=1) #RB_Y
        #--------------------------------------------------------------------------
        # CREATE SPARE CORNERS
        #--------------------------------------------------------------------------
        canvas.create_line(690, 285, 700, 285, fill=colors_corner[0], width=1) #LT_X
        canvas.create_line(690, 285, 690, 295, fill=colors_corner[1], width=1) #LT_Y
        canvas.create_line(1010, 285, 1020, 285, fill=colors_corner[0], width=1) #RT_X
        canvas.create_line(1020, 285, 1020, 295, fill=colors_corner[1], width=1) #RT_Y
        canvas.create_line(690, 615, 700, 615, fill=colors_corner[0], width=1) #LB_X
        canvas.create_line(690, 605, 690, 615, fill=colors_corner[1], width=1) #LB_Y
        canvas.create_line(1010, 615, 1020, 615, fill=colors_corner[0], width=1) #RB_X
        canvas.create_line(1020, 605, 1020, 615, fill=colors_corner[1], width=1) #RB_Y
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
            ip_address = subprocess.check_output(["ip", "address", "show", "wlan0"]).decode("utf-8")
            ip_line = [line.strip() for line in ip_address.split("\n") if "inet " in line][0]
            wlan0_ip = ip_line.split()[1]
        else:
            wlan0_ip = "127.0.0.1"
        canvas.create_text(20, 20, **txt_style_pagename, fill=sys_clr[9], text="SETUP")
        canvas.create_text(20, 50, **txt_style_pageinfo, fill=sys_clr[9], text=(version, last_change, sys.platform, carno, devno, wlan0_ip))
        canvas.create_text(20, (bggrid[4]-135), **txt_style_pagename, fill=sys_clr[9], text="MENU")
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
            lbls_btnhw = tk.Label(self, **lbl_style_setup_btns, bg=sys_clr[8], fg=sys_clr[9])
            if device == DEVICE_B_txt[1]:
                lbls_btnhw.config(text=btnhw_DEV001_txt[i])
            elif device == DEVICE_B_txt[2]:
                lbls_btnhw.config(text=btnhw_DEV002_txt[i])
            lbls_btnhw.place(x=x_pos, y=y_l1, width=lbl_w, height=lbl_f_h)
            x_pos += +px_to_next
        x_pos = x_start
        for i in range(quant_btns_HW):
            lbls_btnhw_info = tk.Label(self, **lbl_style_setup_btns_small, bg=sys_clr[8], fg=sys_clr[9])
            if device == DEVICE_B_txt[1]:
                lbls_btnhw_info.config(text=lbls_btnhw_info_txt_DEV001[i])
            elif device == DEVICE_B_txt[2]:
                lbls_btnhw_info.config(text=lbls_btnhw_info_txt_DEV002[i])
            lbls_btnhw_info.place(x=x_pos, y=y_l2, width=lbl_w, height=lbl_i_h)
            x_pos += +px_to_next
        x_pos = x_start
        for i in range(quant_btns_SW):
            lbls_btnsw = tk.Label(self, **lbl_style_setup_btns, bg=sys_clr[8], fg=sys_clr[9])
            if device == DEVICE_B_txt[1]:
                lbls_btnsw.config(text=lbl_btnsw_DEV001_txt[i])
            elif device == DEVICE_B_txt[2]:
                lbls_btnsw.config(text=lbl_btnsw_DEV002_txt[i])
            lbls_btnsw.place(x=x_pos, y=y_l4, width=lbl_w, height=lbl_f_h)
            x_pos += +px_to_next
        #----------------------------------------------------------------------------------
        # FUNCTION BUTTONS
        #----------------------------------------------------------------------------------
        global btns_HW
        global btns_SW
        global btn_HW
        global btn_SW
        #--------------------------------------------------------------------------
        # HW BUTTONS
        #--------------------------------------------------------------------------
        btns_HW = []
        x_pos = x_start
        for i in range(quant_btns_HW):
            btn_HW = tk.Button(canvas, bg=sys_clr[8], font=("Bebas Neue Bold", 28), command=lambda i=i: [read.toggle_btn_HW(i),self.master.switch_frame(P03_SETUP)])
            btn_HW.place(x=x_pos, y=y_l3, width=btn_w, height=btn_h)
            x_pos += +px_to_next
            btns_HW.append(btn_HW)
        #--------------------------------------------------------------------------
        # SW BUTTONS
        #--------------------------------------------------------------------------
        btns_SW = []
        x_pos = x_start
        for i in range(quant_btns_SW):
            btn_SW = tk.Button(canvas, bg=sys_clr[8], fg=sys_clr[9], font=("Bebas Neue Bold", 28),  command=lambda i=i: [read.toggle_btn_SW(i),self.master.switch_frame(P03_SETUP)])
            btn_SW.place(x=x_pos, y=y_l5, width=btn_w, height=btn_h)
            x_pos += +px_to_next
            btns_SW.append(btn_SW)
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
        opt_odo = tk.OptionMenu(self, self._odo_selected_key, *self._odo_keys, command=lambda *_: _on_select_odo())
        opt_odo.config(bg=sys_clr[8], fg=sys_clr[3], font=(fonts[6], 22))
        opt_odo.place(x=30, y=300, width=250, height=30)

        # Current/Edit (odo)
        lbl_curr_odo = tk.Label(self, **lbl_style_setup_btns, text="ACTUAL", bg=sys_clr[8], fg=sys_clr[3])
        lbl_curr_odo.place(x=30, y=345, width=120, height=30)
        val_curr_odo = tk.Label(self, **lbl_style_setup_btns, textvariable=self._odo_current_value_var, bg=sys_clr[8], fg=sys_clr[3])
        val_curr_odo.place(x=165, y=345, width=120, height=30)

        lbl_edit_odo = tk.Label(self, **lbl_style_setup_btns, text="NEW", bg=sys_clr[8], fg=sys_clr[3])
        lbl_edit_odo.place(x=30, y=390, width=120, height=30)
        val_edit_odo = tk.Label(self, **lbl_style_setup_btns, textvariable=self._odo_edit_value_var, bg=sys_clr[8], fg=sys_clr[3])
        val_edit_odo.place(x=165, y=390, width=120, height=30)

        # OTHER dropdown
        opt_other = tk.OptionMenu(self, self._other_selected_key, *self._other_keys, command=lambda *_: _on_select_other())
        opt_other.config(bg=sys_clr[8], fg=sys_clr[3], font=(fonts[6], 22))
        opt_other.place(x=30, y=435, width=250, height=30)

        # Current/Edit (other)
        lbl_curr_other = tk.Label(self, **lbl_style_setup_btns, text="ACTUAL", bg=sys_clr[8], fg=sys_clr[3])
        lbl_curr_other.place(x=30, y=480, width=120, height=30)
        val_curr_other = tk.Label(self, **lbl_style_setup_btns, textvariable=self._other_current_value_var, bg=sys_clr[8], fg=sys_clr[3])
        val_curr_other.place(x=165, y=480, width=120, height=30)

        lbl_edit_other = tk.Label(self, **lbl_style_setup_btns, text="NEW", bg=sys_clr[8], fg=sys_clr[3])
        lbl_edit_other.place(x=30, y=525, width=120, height=30)
        val_edit_other = tk.Label(self, **lbl_style_setup_btns, textvariable=self._other_edit_value_var, bg=sys_clr[8], fg=sys_clr[3])
        val_edit_other.place(x=165, y=525, width=120, height=30)

        # Active hint + status
        lbl_active = tk.Label(self, font=(fonts[6], 22), textvariable=self._active_section, bg=sys_clr[8], fg=sys_clr[3], anchor="c")
        lbl_active.place(x=30, y=570, width=60, height=30)

        lbl_status = tk.Label(self, font=(fonts[6], 22), textvariable=self._status_var, bg=sys_clr[8], fg=sys_clr[3], anchor="c")
        lbl_status.place(x=110, y=570, width=175, height=30)

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

        for r, row in enumerate(keypad_layout):
            for c, token in enumerate(row):
                if not token:
                    continue
                if token == "SAVE":
                    btn = tk.Button(self, **keypad_style, text=token, bg=sys_clr[8], fg=sys_clr[9], command=_save_active_value)
                else:
                    btn = tk.Button(self, **keypad_style, text=token, bg=sys_clr[8], fg=sys_clr[9], command=lambda t=token: _on_keypad_press(t))
                btn.place(x=x0 + c*dx, y=y0 + r*dy, width=w, height=h)

        # Initialize
        _refresh_value("ODO")
        _refresh_value("OTHER")
        self._active_section.set("ODO")
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
                    x_pos += +px_to_next
                else:
                    lbls_btnrb01.place(x=x_pos2, y=y_l12, width=lbl_w, height=lbl_f_h)
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
                    x_pos += +px_to_next
                else:
                    lbls_btnRB02.place(x=x_pos2, y=y_l16, width=lbl_w, height=lbl_f_h)
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
                    x_pos += +px_to_next
                else:
                    lbls_btnRB03.place(x=x_pos2, y=y_l20, width=lbl_w, height=lbl_f_h)
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
                    x_pos += +px_to_next
                else:
                    btn_RB01.place(x=x_pos2, y=y_l13, width=btn_w, height=btn_h)
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
                    x_pos += +px_to_next
                else:
                    btn_RB02.place(x=x_pos2, y=y_l17, width=btn_w, height=btn_h)
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
                    x_pos += +px_to_next
                else:
                    btn_RB03.place(x=x_pos2, y=y_l21, width=btn_w, height=btn_h)
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

        if device == DEVICE_B_txt[1]:
            quant_btns_FAV = quant_btns_HW + quant_btns_SW
        elif device == DEVICE_B_txt[2]:
            quant_btns_FAV = quant_btns_HW + quant_btns_SW + quant_btns_RB01 + quant_btns_RB02 + quant_btns_RB03
        elif device == DEVICE_B_txt[4]:
            quant_btns_FAV = quant_btns_HW + quant_btns_SW
        elif device == DEVICE_B_txt[8]:
            quant_btns_FAV = quant_btns_HW + quant_btns_SW
            
        for i in range(quant_btns_FAV):
            btn_FAV = tk.Button(canvas, bg=sys_clr[8], text="F", font=(fonts[1], 20), command=lambda i=i: read.toggle_btn_FAV(i))
                
            if i < 10:
                btn_FAV.place(x=x_pos, y=y_l3, width=btn_f_w, height=btn_h)
                x_pos += +px_to_next
            elif i < 20:
                btn_FAV.place(x=x_pos2, y=y_l5, width=btn_f_w, height=btn_h)
                x_pos2 += +px_to_next
            elif i < 28:
                btn_FAV.place(x=x_pos11, y=y_l11, width=btn_f_w, height=btn_h)
                x_pos11 += +px_to_next
            elif i < 36:
                btn_FAV.place(x=x_pos13, y=y_l13, width=btn_f_w, height=btn_h)
                x_pos13 += +px_to_next
            elif i < 44:
                btn_FAV.place(x=x_pos15, y=y_l15, width=btn_f_w, height=btn_h)
                x_pos15 += +px_to_next
            elif i < 52:
                btn_FAV.place(x=x_pos17, y=y_l17, width=btn_f_w, height=btn_h)
                x_pos17 += +px_to_next
            elif i < 60:
                btn_FAV.place(x=x_pos19, y=y_l19, width=btn_f_w, height=btn_h)
                x_pos19 += +px_to_next
            elif i < 68:
                btn_FAV.place(x=x_pos21, y=y_l21, width=btn_f_w, height=btn_h)
                x_pos21 += +px_to_next
            btns_FAV.append(btn_FAV)
        #----------------------------------------------------------------------------------
        # END INIT
        #----------------------------------------------------------------------------------
        self.update_page()
    def update_page(self):
        #----------------------------------------------------------------------------------
        # HW BUTTONS
        #----------------------------------------------------------------------------------
        for i in range(quant_btns_HW):              
            if btn_states_HW[i]:
                btns_HW[i].config(text=states_txt_act[1], fg=sys_clr[10])
            else:
                btns_HW[i].config(text=states_txt_act[0], fg=sys_clr[11])
        #----------------------------------------------------------------------------------
        # SW BUTTONS
        #----------------------------------------------------------------------------------
        for i in range(quant_btns_SW):
            if btn_states_SW[i]:
                btns_SW[i].config(text=btnsw_DEV001_txt_1[i])
            else:
                btns_SW[i].config(text=btnsw_DEV001_txt_0[i])
        #----------------------------------------------------------------------------------
        # FAV BUTTONS
        #----------------------------------------------------------------------------------
        for i in range(quant_btns_FAV):
            if btn_states_FAV[i]:
                btns_FAV[i].config(fg=sys_clr[10])
            else:
                btns_FAV[i].config(fg=sys_clr[11])
        #----------------------------------------------------------------------------------
        # RB BUTTONS
        #----------------------------------------------------------------------------------
        if device == DEVICE_B_txt[2]:
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