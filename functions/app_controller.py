from pages.page_context import set_context, sync_context
from functions.favorite_manager import (
    build_qopt_favorites,
    favorite_label,
    favorite_limit,
    favorite_status,
    favorite_target,
)

sync_context(globals())

#------------------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------------------
class KIDDController:
    def __init__(self, app, main_globals):
        sync_context(globals())
        self.app = app
        self.main_globals = main_globals
        self.audio_channels = {}  # filename -> Channel
        self.audio_sounds = {}    # filename -> Sound
        self.btns_device = []
        self.btns_style = []
        self.btns_theme = []
        self.btns_sys = []
        self.btns_menu = []
        self.btn_device_place = 0
        self.btn_style_place = 0
        self.btn_theme_place = 0
        self.btn_sys_place = 0
        self.btn_menu_place = 0
    #--------------------------------------------------------------------------------------
    # MAIN APP FUNCTIONS
    #--------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------
    # QUIT THE PROGRAM
    #----------------------------------------------------------------------------------
    def quitDASH(self):
        if sys_linux and sys_pi:
            GPIO.cleanup()
        self.app.destroy()
    #----------------------------------------------------------------------------------
    # NAV AND INPUT BUTTONS
    #----------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    # DEVICE BUTTONS
    #------------------------------------------------------------------------------
    def buttons_device(self):
        self.btn_device_place = len(DEVICE_B_txt)
        self.btns_device = []
        x_pos_r1 = 20
        btn_w = 130
        btn_h = 40
        for i in range(self.btn_device_place):
            btn_device = tk.Button(text=DEVICE_B_txt[i], bd=4, bg=sys_clr[8], fg=sys_clr[9], font=("Bebas Neue Bold", 28), command=lambda i=i: [self.toggle_button_device(DEVICE_B_txt[i]),self.app.switch_frame(P00_BOOT)])
            self.btns_device.append(btn_device)
            self.btns_device[i].place(x=x_pos_r1, y=frm01_YPOS+45, width=btn_w, height=btn_h)
            x_pos_r1 += +(btn_w+15)
        for i, text in enumerate(DEVICE_B_txt):
            if device == text:
                self.btns_device[i].config(fg=sys_clr[10])
            else:
                self.btns_device[i].config(fg=sys_clr[11])
        # ENABLE DISABLE BUTTONS
        self.btns_device[0].config(state=tk.DISABLED)
        #self.btns_device[1].config(state=tk.DISABLED)
        #self.btns_device[2].config(state=tk.DISABLED)
        self.btns_device[3].config(state=tk.DISABLED)
        #self.btns_device[4].config(state=tk.DISABLED)
        self.btns_device[5].config(state=tk.DISABLED)
        self.btns_device[6].config(state=tk.DISABLED)
        self.btns_device[7].config(state=tk.DISABLED)
        #self.btns_device[8].config(state=tk.DISABLED)
        self.btns_device[9].config(state=tk.DISABLED)
        self.btns_device[10].config(state=tk.DISABLED)
        self.btns_device[11].config(state=tk.DISABLED)
        self.btns_device[12].config(state=tk.DISABLED)
        self.btns_device[13].config(state=tk.DISABLED)
        self.btns_device[14].config(state=tk.DISABLED)
        self.btns_device[15].config(state=tk.DISABLED)
        self.btns_device[16].config(state=tk.DISABLED)
        self.btns_device[17].config(state=tk.DISABLED)
        self.btns_device[18].config(state=tk.DISABLED)
        self.btns_device[19].config(state=tk.DISABLED)
        self.btns_device[20].config(state=tk.DISABLED)
        self.btns_device[21].config(state=tk.DISABLED)
        self.btns_device[22].config(state=tk.DISABLED)
        self.btns_device[23].config(state=tk.DISABLED)
        self.btns_device[24].config(state=tk.DISABLED)
        self.btns_device[25].config(state=tk.DISABLED)
        self.btns_device[26].config(state=tk.DISABLED)
        self.btns_device[27].config(state=tk.DISABLED)
        self.btns_device[28].config(state=tk.DISABLED)
        self.btns_device[29].config(state=tk.DISABLED)
        self.btns_device[30].config(state=tk.DISABLED)
        self.btns_device[31].config(state=tk.DISABLED)
        self.btns_device[32].config(state=tk.DISABLED)
        self.btns_device[33].config(state=tk.DISABLED)
        self.btns_device[34].config(state=tk.DISABLED)
        self.btns_device[35].config(state=tk.DISABLED)
        self.btns_device[36].config(state=tk.DISABLED)
        self.btns_device[37].config(state=tk.DISABLED)
        self.btns_device[38].config(state=tk.DISABLED)
        self.btns_device[39].config(state=tk.DISABLED)
        self.btns_device[40].config(state=tk.DISABLED)
        self.btns_device_slider = tk.Scale(from_=0, to=self.btn_device_place, command=self.buttons_device_show, showvalue=0, length=(bggrid[1]-175), orient='horizontal', width=22, sliderlength=40, troughcolor="#000000", highlightbackground=sys_clr[8], bg=sys_clr[4])
        self.btns_device_slider.set(1)
        self.btns_device_slider.place(x=145, y=frm01_YPOS+2)
    #------------------------------------------------------------------------------
    # SHOW DEVICE BUTTONS IN SLIDER
    #------------------------------------------------------------------------------
    def buttons_device_show(self, value):
        start_index = int(float(value))  # Convert float value to integer
        x_pos_r1 = 20
        btn_w = 130
        btn_h = 40
        for i in range(self.btn_device_place):
            if i < start_index or i >= start_index + 8:
                self.btns_device[i].place_forget()  # Hide the self.btns_device outside the range
            else:
                self.btns_device[i].place(x=x_pos_r1, y=frm01_YPOS+45, width=btn_w, height=btn_h)  # Show the self.btns_device within the range
                x_pos_r1 += +(btn_w+15)
    #------------------------------------------------------------------------------
    # STYLE BUTTONS
    #------------------------------------------------------------------------------
    def buttons_style(self):
        self.btn_style_place = len(STYLE_B_txt)
        self.btns_style = []
        x_pos_r1 = 20
        btn_w = 130
        btn_h = 40
        for i in range(self.btn_style_place):
            btn_style = tk.Button(text=STYLE_B_txt[i], bd=4, bg=sys_clr[8], fg=sys_clr[9], font=("Bebas Neue Bold", 28), command=lambda i=i: [self.toggle_button_style(STYLE_B_txt[i]),self.app.switch_frame(P01_DASH)])
            self.btns_style.append(btn_style)
            self.btns_style[i].place(x=x_pos_r1, y=frm02_YPOS+45, width=btn_w, height=btn_h)
            x_pos_r1 += +(btn_w+15)
        for i, text in enumerate(STYLE_B_txt):
            if style == text:
                self.btns_style[i].config(fg=sys_clr[10])
            else:
                self.btns_style[i].config(fg=sys_clr[11])
        # ENABLE DISABLE BUTTONS
        #self.btns_style[0].config(state=tk.DISABLED)
        #self.btns_style[1].config(state=tk.DISABLED)
        self.btns_style[2].config(state=tk.DISABLED)
        self.btns_style[3].config(state=tk.DISABLED)
        self.btns_style[4].config(state=tk.DISABLED)
        self.btns_style_slider = tk.Scale(from_=0, to=self.btn_style_place, command=self.buttons_style_show, showvalue=0, length=(bggrid[1]-175), orient='horizontal', width=22, sliderlength=40, troughcolor="#000000", highlightbackground=sys_clr[8], bg=sys_clr[4])
        self.btns_style_slider.set(0)
        self.btns_style_slider.place(x=145, y=frm02_YPOS+2)
    #------------------------------------------------------------------------------
    # SHOW STYLE BUTTONS IN SLIDER
    #------------------------------------------------------------------------------
    def buttons_style_show(self, value):
        start_index = int(float(value))  # Convert float value to integer
        x_pos_r1 = 20
        btn_w = 130
        btn_h = 40
        for i in range(self.btn_style_place):
            if i < start_index or i >= start_index + 8:
                self.btns_style[i].place_forget()  # Hide the self.btns_style outside the range
            else:
                self.btns_style[i].place(x=x_pos_r1, y=frm02_YPOS+45, width=btn_w, height=btn_h)  # Show the self.btns_style within the range
                x_pos_r1 += +(btn_w+15)
    #------------------------------------------------------------------------------
    # THEME BUTTONS
    #------------------------------------------------------------------------------
    def buttons_theme(self):
        self.btn_theme_place = len(THEME_B_txt)
        self.btns_theme = []
        x_pos_r1 = 20
        btn_w = 130
        btn_h = 40
        for i in range(self.btn_theme_place):
            btn_theme = tk.Button(text=THEME_B_txt[i], bd=4, bg=sys_clr[8], fg=sys_clr[9], font=("Bebas Neue Bold", 28), command=lambda i=i: [self.toggle_button_theme(THEME_B_txt[i]),self.app.switch_frame(P01_DASH)])
            self.btns_theme.append(btn_theme)
            self.btns_theme[i].place(x=x_pos_r1, y=frm03_YPOS+45, width=btn_w, height=btn_h)
            x_pos_r1 += +(btn_w+15)
        for i, text in enumerate(THEME_B_txt):
            if theme == text:
                self.btns_theme[i].config(fg=sys_clr[10])
            else:
                self.btns_theme[i].config(fg=sys_clr[11])
        # ENABLE DISABLE BUTTONS
        #self.btns_theme[0].config(state=tk.DISABLED)
        #self.btns_theme[1].config(state=tk.DISABLED)
        #self.btns_theme[2].config(state=tk.DISABLED)
        #self.btns_theme[3].config(state=tk.DISABLED)
        #self.btns_theme[4].config(state=tk.DISABLED)
        #self.btns_theme[5].config(state=tk.DISABLED)
        #self.btns_theme[6].config(state=tk.DISABLED)
        #self.btns_theme[7].config(state=tk.DISABLED)
        #self.btns_theme[8].config(state=tk.DISABLED)
        #self.btns_theme[9].config(state=tk.DISABLED)
        #self.btns_theme[10].config(state=tk.DISABLED)
        self.btns_theme[11].config(state=tk.DISABLED)
        self.btns_theme[12].config(state=tk.DISABLED)
        self.btns_theme[13].config(state=tk.DISABLED)
        self.btns_theme[14].config(state=tk.DISABLED)
        self.btns_theme[15].config(state=tk.DISABLED)
        self.btns_theme[16].config(state=tk.DISABLED)
        self.btns_theme_slider = tk.Scale(from_=0, to=self.btn_theme_place, command=self.buttons_theme_show, showvalue=0, length=(bggrid[1]-160), orient='horizontal', width=22, sliderlength=40, troughcolor="#000000", highlightbackground=sys_clr[8], bg=sys_clr[4])
        self.btns_theme_slider.set(1)
        self.btns_theme_slider.place(x=127, y=frm03_YPOS+2)
    #------------------------------------------------------------------------------
    # SHOW THEME BUTTONS IN SLIDER
    #------------------------------------------------------------------------------
    def buttons_theme_show(self, value):
        start_index = int(float(value))  # Convert float value to integer
        x_pos_r1 = 20
        btn_w = 130
        btn_h = 40
        for i in range(self.btn_theme_place):
            if i < start_index or i >= start_index + 8:
                self.btns_theme[i].place_forget()  # Hide the self.btns_theme outside the range
            else:
                self.btns_theme[i].place(x=x_pos_r1, y=frm03_YPOS+45, width=btn_w, height=btn_h)  # Show the self.btns_theme within the range
                x_pos_r1 += +(btn_w+15)
    #------------------------------------------------------------------------------
    # SYS BUTTONS
    #------------------------------------------------------------------------------
    def buttons_sys(self):
        self.btn_sys_place = len(SYS_B_txt)
        self.btns_sys = []
        x_pos_r1 = 20
        btn_w = 130
        btn_h = 40
        for i in range(self.btn_sys_place):
            btn_sys = tk.Button(text=SYS_B_txt[i], bd=4, bg=sys_clr[8], fg=sys_clr[9], font=("Bebas Neue Bold", 28), command=lambda i=i: [self.toggle_button_system(SYS_B_txt[i]),self.app.switch_frame(P04_THEMES)])
            self.btns_sys.append(btn_sys)
            self.btns_sys[i].place(x=x_pos_r1, y=frm04_YPOS+45, width=btn_w, height=btn_h)
            x_pos_r1 += +(btn_w+15)
        for i, text in enumerate(SYS_B_txt):
            if system == text:
                self.btns_sys[i].config(fg=sys_clr[10])
            else:
                self.btns_sys[i].config(fg=sys_clr[11])
        self.btns_sys_slider = tk.Scale(from_=0, to=self.btn_sys_place, command=self.buttons_sys_show, showvalue=0, length=(bggrid[1]-140), orient='horizontal', width=22, sliderlength=40, troughcolor="#000000", highlightbackground=sys_clr[8], bg=sys_clr[4])
        self.btns_sys_slider.set(0)
        self.btns_sys_slider.place(x=107, y=frm04_YPOS+2)
    #------------------------------------------------------------------------------
    # SHOW SYS BUTTONS IN SLIDER
    #------------------------------------------------------------------------------
    def buttons_sys_show(self, value):
        start_index = int(float(value))  # Convert float value to integer
        x_pos_r1 = 20
        btn_w = 130
        btn_h = 40
        for i in range(self.btn_sys_place):
            if i < start_index or i >= start_index + 8:
                self.btns_sys[i].place_forget()  # Hide the self.btns_sys outside the range
            else:
                self.btns_sys[i].place(x=x_pos_r1, y=frm04_YPOS+45, width=btn_w, height=btn_h)  # Show the self.btns_sys within the range
                x_pos_r1 += +(btn_w+15)
    #------------------------------------------------------------------------------
    # MENU BUTTONS
    #------------------------------------------------------------------------------
    def buttons_menu(self):
        self.btn_menu_place = len(MENU_B_txt)
        self.btns_menu = []
        x_pos_r1 = 20
        btn_w = 130
        btn_h = 40
        for i in range(self.btn_menu_place):
            btn_menu = tk.Button(text=MENU_B_txt[i], bd=4, bg=sys_clr[8], fg=sys_clr[9], font=("Bebas Neue Bold", 28))
            btn_menu.config(command=lambda i=i: self.app.switch_frame(i))
            self.btns_menu.append(btn_menu)
            self.btns_menu[i].place(x=x_pos_r1, y=frm05_YPOS+45, width=btn_w, height=btn_h)
            x_pos_r1 += +(btn_w+15)
        #for i, text in enumerate(MENU_B_txt):
        #    if menu == text:
        #        self.btns_menu[i].config(fg=sys_clr[10])
        #    else:
        #        self.btns_menu[i].config(fg=sys_clr[11])
        self.btns_menu_slider = tk.Scale(from_=0, to=self.btn_menu_place-5, command=self.buttons_menu_show, showvalue=0, length=(bggrid[1]-140), orient='horizontal', width=22, sliderlength=40, troughcolor="#000000", highlightbackground=sys_clr[8], bg=sys_clr[4])
        self.btns_menu_slider.set(1)
        self.btns_menu_slider.place(x=107, y=frm05_YPOS+2)
    #------------------------------------------------------------------------------
    # SHOW MENU BUTTONS IN SLIDER
    #------------------------------------------------------------------------------
    def buttons_menu_show(self, value):
        start_index = int(float(value))  # Convert float value to integer
        x_pos_r1 = 20
        btn_w = 130
        btn_h = 40
        for i in range(self.btn_menu_place):
            if i < start_index or i >= start_index + 8:
                self.btns_menu[i].place_forget()  # Hide the self.btns_menu outside the range
            else:
                self.btns_menu[i].place(x=x_pos_r1, y=frm05_YPOS+45, width=btn_w, height=btn_h)  # Show the self.btns_menu within the range
                x_pos_r1 += +(btn_w+15)
    #------------------------------------------------------------------------------
    # QOPT PAGE: SHOW FAV BUTTONS (MAX 20)
    #------------------------------------------------------------------------------
    def _hw_count(self):
        return len(btn_states_HW)

    def _sw_count(self):
        return len(btn_states_SW)

    def _rb_counts(self):
        return (len(rb01_DEV002_txt), len(rb02_DEV002_txt), len(rb03_DEV002_txt))

    def _favorite_limit(self):
        return favorite_limit(
            device,
            DEVICE_B_txt,
            btn_states_HW,
            btn_states_SW,
            rb01_DEV002_txt,
            rb02_DEV002_txt,
            rb03_DEV002_txt,
        )

    def _state_texts(self):
        if "states_txt_act" in globals():
            return states_txt_act
        return states_txt_en if btn_states_SW[4] else states_txt_de

    def _favorite_label(self, fav_index):
        hw_labels = btnhw_DEV002_txt if device == DEVICE_B_txt[2] else btnhw_DEV001_txt
        sw_labels = lbl_btnsw_DEV002_txt if device == DEVICE_B_txt[2] else lbl_btnsw_DEV001_txt
        return favorite_label(
            fav_index,
            device,
            DEVICE_B_txt,
            hw_labels,
            sw_labels,
            rb01_DEV002_txt,
            rb02_DEV002_txt,
            rb03_DEV002_txt,
        )

    def _favorite_status(self, fav_index):
        state_texts = self._state_texts()
        if device == DEVICE_B_txt[2]:
            on_texts = btnsw_DEV002_txt_1
            off_texts = btnsw_DEV002_txt_0
        else:
            on_texts = btnsw_DEV001_txt_1
            off_texts = btnsw_DEV001_txt_0
        return favorite_status(
            fav_index,
            device,
            DEVICE_B_txt,
            state_texts,
            btn_states_HW,
            btn_states_SW,
            on_texts,
            off_texts,
            relay_states_1to8,
            relay_states_9to16,
        )

    def _toggle_favorite(self, fav_index):
        target_type, target_index = favorite_target(fav_index, device, DEVICE_B_txt, btn_states_HW, btn_states_SW)
        if target_type == "HW":
            self.toggle_btn_HW(target_index)
        elif target_type == "SW":
            self.toggle_btn_SW(target_index)
        elif target_type == "RELAY":
            self.toggle_relay(target_index)

    def _build_qopt_favorites(self):
        sync_context(globals())
        return build_qopt_favorites(btn_states_FAV, self._favorite_limit(), self._favorite_label)

    def qopt(self):
        global btns_qopt
        global lbls_qopt
        global btn_qopt
        global btn_qopt_place
        global qopt_favorites
        px_to_next = 115
        btn_w = 80
        btn_h = 40
        lbl_h = 32
        qopt_favorites = self._build_qopt_favorites()
        btn_qopt_place = len(qopt_favorites)
        btns_qopt = []
        lbls_qopt = []
        x_pos = 20
        x_pos2 = 20
        for i in range(btn_qopt_place):
            favorite = qopt_favorites[i]
            lbl_qopt = tk.Label(
                bg=sys_clr[8],
                fg=sys_clr[9],
                font=("Bebas Neue Bold", 18),
                text=favorite["label"],
            )
            btn_qopt = tk.Button(bg=sys_clr[8], font=("Bebas Neue Bold", 28))
            btn_qopt.config(command=lambda fav_index=favorite["fav_index"]: self._toggle_favorite(fav_index))
            lbls_qopt.append(lbl_qopt)
            btns_qopt.append(btn_qopt)
            if i < 10:
                lbl_qopt.place(x=x_pos, y=165, width=btn_w, height=lbl_h)
                btn_qopt.place(x=x_pos, y=200, width=btn_w, height=btn_h)
                x_pos += +px_to_next
            else:
                lbl_qopt.place(x=x_pos2, y=365, width=btn_w, height=lbl_h)
                btn_qopt.place(x=x_pos2, y=400, width=btn_w, height=btn_h)
                x_pos2 += +px_to_next
        self._publish_state(
            btns_qopt=btns_qopt,
            lbls_qopt=lbls_qopt,
            btn_qopt_place=btn_qopt_place,
            qopt_favorites=qopt_favorites,
        )
    #------------------------------------------------------------------------------
    # SETUP PAGE: NUMPAD KEYS
    #------------------------------------------------------------------------------
    def btn_key_click(self, number):
        current_value.set(current_value.get() + str(number))
    #------------------------------------------------------------------------------
    # SETUP PAGE: DOT KEY
    #------------------------------------------------------------------------------
    def btn_dot_click(self):
        if '.' not in current_value.get():
            current_value.set(current_value.get() + '.')
    #------------------------------------------------------------------------------
    # SETUP PAGE: APPLY KEY
    #------------------------------------------------------------------------------
    def btn_apply_click(self):
        try:
            new_value = float(current_value.get())
            selected_variable = variable_dropdown.get()
            if selected_variable in variables:
                variables[selected_variable].set(new_value)
            current_value.set('')
            self.btn_apply_update_label()
        except ValueError:
            pass
    #------------------------------------------------------------------------------
    # SETUP PAGE: APPLY KEY UPDATE THE LABEL
    #------------------------------------------------------------------------------
    def btn_apply_update_label(self):
        variable_text = "\n".join([f"{var}: {variables[var].get()}" for var in variables])
        lbl_target_val.config(text=variable_text)
    #----------------------------------------------------------------------------------
    # TOGGLE AND SAVE BUTTON STATES 2025 OK
    #----------------------------------------------------------------------------------
    def toggle_PB(self, pb_text):
        global btn_states_PB
        btn_states_PB = pb_text
        bsm.set_current_button_states("PB", pb_text)
        bsm.save()
        self._publish_state(btn_states_PB=btn_states_PB)

    def toggle_button_states_FNKT(self, i):
        if btn_states_FNKT[i] == True:
            btn_states_FNKT[i] = False
        else:
            btn_states_FNKT[i] = True
        bsm.set_current_button_states("FNKT", btn_states_FNKT)
        bsm.save()
        self._publish_state(btn_states_FNKT=btn_states_FNKT)

    def toggle_button_states_PBFNKT(self, i):
        if btn_states_PBFNKT[i] == True:
            btn_states_PBFNKT[i] = False
        else:
            btn_states_PBFNKT[i] = True
        bsm.set_current_button_states("PBFNKT", btn_states_PBFNKT)
        bsm.save()
        self._publish_state(btn_states_PBFNKT=btn_states_PBFNKT)

    def toggle_btn_HW(self, i):
        if btn_states_HW[i] == True:
            btn_states_HW[i] = False
        else:
            btn_states_HW[i] = True
        bsm.set_current_button_states("HW", btn_states_HW)
        bsm.save()
        self._publish_state(btn_states_HW=btn_states_HW)

    def toggle_btn_SW(self, i):
        global btn_states_SW
        if btn_states_SW[i] == True:
            btn_states_SW[i] = False
        else:
            btn_states_SW[i] = True
        bsm.set_current_button_states("SW", btn_states_SW)
        bsm.save()
        self._publish_state(btn_states_SW=btn_states_SW)

    def toggle_btn_qopt(self, i):
        if btn_states_qopt[i] == True:
            btn_states_qopt[i] = False
        else:
            btn_states_qopt[i] = True
        bsm.set_current_button_states("QOPT", btn_states_qopt)
        bsm.save()
        self._publish_state(btn_states_qopt=btn_states_qopt)

    def toggle_btn_FAV(self, i):
        if btn_states_FAV[i] == True:
            btn_states_FAV[i] = False
        else:
            btn_states_FAV[i] = True
        bsm.set_current_button_states("FAV", btn_states_FAV)
        bsm.save()
        self._publish_state(btn_states_FAV=btn_states_FAV)
        return btn_states_FAV[i]
    #----------------------------------------------------------------------------------
    # LOAD SYSTEMDATA IF THE SYSTEM IS A RASPBERRY PI
    #----------------------------------------------------------------------------------
    def get_system_data(self):
        global sys_diskused
        global sys_diskmax
        global sys_memused
        global sys_memmax
        global sys_cpuload
        global sys_cputemp
        global power_info

        disk_usage = psutil.disk_usage('/')
        memory = psutil.virtual_memory()
        sys_diskused = str(round(disk_usage.used / (1024.0 ** 3), 2))
        sys_diskmax = str(round(disk_usage.total / (1024.0 ** 3), 2))
        sys_memused = str(memory.percent)
        sys_memmax = str(round(memory.total / (1024.0 ** 3), 2))
        sys_cpuload = str(psutil.cpu_percent())
        res01 = os.popen('vcgencmd measure_temp').readline()
        sys_cputemp = res01.replace("temp=","").replace("'C\n","")
    #--------------------------------------------------------------------------------------
    # STYLING FUNCTIONS
    #--------------------------------------------------------------------------------------
    def toggle_button_device(self, device_text):
        global device, btn_states_PB, btn_states_PBFNKT, btn_states_FNKT
        global btn_states_HW, btn_states_SW, btn_states_qopt, btn_states_FAV
        global states_txt_act
        device = device_text
        bsm.data["main_config"]["device"] = device
        device_buttons = bsm.data.get("buttons", {}).get(device, {})
        btn_states_PB = device_buttons.get("PB", btn_states_PB)
        btn_states_PBFNKT = device_buttons.get("PBFNKT", btn_states_PBFNKT)
        btn_states_FNKT = device_buttons.get("FNKT", btn_states_FNKT)
        btn_states_HW = device_buttons.get("HW", btn_states_HW)
        btn_states_SW = device_buttons.get("SW", btn_states_SW)
        btn_states_qopt = device_buttons.get("QOPT", btn_states_qopt)
        btn_states_FAV = device_buttons.get("FAV", btn_states_FAV)
        states_txt_act = states_txt_en if btn_states_SW[4] else states_txt_de
        bsm.save()
        self._publish_state(
            device=device,
            btn_states_PB=btn_states_PB,
            btn_states_PBFNKT=btn_states_PBFNKT,
            btn_states_FNKT=btn_states_FNKT,
            btn_states_HW=btn_states_HW,
            btn_states_SW=btn_states_SW,
            btn_states_qopt=btn_states_qopt,
            btn_states_FAV=btn_states_FAV,
            states_txt_act=states_txt_act,
        )
    def toggle_button_style(self, style_text):
        global style
        global sty_clr
        style = style_text
        if style == STYLE_B_txt[0]:
            sty_clr = sty_clr_ka
        elif style == STYLE_B_txt[1]:
            sty_clr = sty_clr_ki
        bsm.data["main_config"]["style"] = style
        bsm.save()
        self._publish_state(style=style, sty_clr=sty_clr)
    def toggle_button_theme(self, theme_text):
        global theme
        theme = theme_text
        bsm.data["main_config"]["theme"] = theme
        bsm.save()
        self._publish_state(theme=theme)
    def toggle_button_system(self, system_text):
        global system
        global sys_clr
        system = system_text
        if system == SYS_B_txt[0]:
            sys_clr = sys_clr_OR
        elif system == SYS_B_txt[1]:
            sys_clr = sys_clr_GN
        elif system == SYS_B_txt[2]:
            sys_clr = sys_clr_BU
        elif system == SYS_B_txt[3]:
            sys_clr = sys_clr_WH
        elif system == SYS_B_txt[4]:
            sys_clr = sys_clr_CP
        bsm.data["main_config"]["system"] = system
        bsm.save()
        self._publish_state(system=system, sys_clr=sys_clr)
    #--------------------------------------------------------------------------------------
    # SOUND FUNCTIONS
    #--------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------
    # GET THE TEXT OF A SOUND BUTTON
    #----------------------------------------------------------------------------------
    def get_snd_menu_btn_txt(self, var):
        global snd_btn_txt
        snd_btn_txt = var.cget("text")
    #----------------------------------------------------------------------------------
    # GET AMOUNT OF SOUND SUBFOLDERS AND THEIR NAMES
    #----------------------------------------------------------------------------------
    def get_subfolders_count_and_names(self, snd_fldr):
        # Get a list of subfolders in the specified folder
        subfolders = [
            name for name in os.listdir(snd_fldr)
            if os.path.isdir(os.path.join(snd_fldr, name)) #and name != "time"
        ]
        # Get the count of subfolders
        subfolders_count = len(subfolders)
        return subfolders_count, subfolders
    #----------------------------------------------------------------------------------
    # GET AMOUNT OF MP3 FILES AND THEIR NAMES
    #----------------------------------------------------------------------------------
    def get_mp3files_count_and_names(self, act_mp3_files_path):
        # Get a list of subfolders in the specified folder
        mp3files = [name for name in os.listdir(act_mp3_files_path) if os.path.isfile(os.path.join(act_mp3_files_path, name))]
        # Get the count of subfolders
        mp3files_count = len(mp3files)
        return mp3files_count, mp3files
    #----------------------------------------------------------------------------------
    # CREATE THE SOUND MENU BUTTONS
    #----------------------------------------------------------------------------------
    def snd_menu_btns(self):
        global snd_menu_btns
        global snd_menu_btn
        global snd_menu_btn_place
        snd_menu_btn_place = subfolders_count
        snd_menu_btns = []
        x_pos_ssb_r1 = 20
        for i in range(snd_menu_btn_place):
            snd_menu_btn = tk.Button(bg=sys_clr[8], fg=sty_clr[0], font=(fonts[1], 24), text=subfolders_list[i])
            snd_menu_btn.config(command=lambda i=i: (self.get_snd_menu_btn_txt(snd_menu_btns[i]), self.load_soundfolder(), self.snd_mp3_btns(), self.app.switch_frame(7))) #todo variablen name ändern damit sich ordnername snd ändert
            snd_menu_btns.append(snd_menu_btn)
            snd_menu_btns[i].place(x=x_pos_ssb_r1, y=90, width=115, height=55)
            x_pos_ssb_r1 += +120

        slider_snd_menu_btns = tk.Scale(from_=0, to=snd_menu_btn_place-5, command=self.show_snd_menu_btns, showvalue=0, length=1245, orient='horizontal', width=30, sliderlength=50, troughcolor="#000000", highlightbackground=sys_clr[6], bg='#00ffff')
        slider_snd_menu_btns.set(1)
        slider_snd_menu_btns.place(x=15, y=90)
    #----------------------------------------------------------------------------------
    # SHOW SUBFOLDERS AS MENU BUTTONS
    #----------------------------------------------------------------------------------
    def show_snd_menu_btns(self, value):
        start_index = int(float(value))  # Convert float value to integer
        x_pos_ssb_r1 = 20
        for i in range(snd_menu_btn_place):
            if i < start_index or i >= start_index + 10:
                snd_menu_btns[i].place_forget()  # Hide the snd_menu_btns outside the range
            else:
                snd_menu_btns[i].place(x=x_pos_ssb_r1, y=130, width=115, height=55)  # Show the snd_menu_btns within the range
                x_pos_ssb_r1 += +120
    #----------------------------------------------------------------------------------
    # CREATE THE MP3 BUTTONS
    #----------------------------------------------------------------------------------
    def snd_mp3_btns(self):
        global snd_mp3_btns
        global snd_mp3_btn_place
        snd_mp3_btn_place = mp3files_count  # Number of Buttons
        snd_mp3_btns = []
        x_pos_mp3_r0 = 22
        y_pos_mp3 = 200  # Starting y-position
        num_rows = 5  # Number of rows to display
        row_length = 10  # Number of buttons per row
        rows_displayed = 0  # Variable to keep track of the number of rows displayed

        for i in range(snd_mp3_btn_place):
            snd_mp3_btn = tk.Button(bg="#000044", fg=sty_clr[0], font=("lcars", 16), text=mp3files_list[i], wraplength=100)
            snd_mp3_btn.config(command=lambda i=i: self.play_mp3(act_mp3_files_path, mp3files_list[i]))
            snd_mp3_btns.append(snd_mp3_btn)

        for i, btn in enumerate(snd_mp3_btns):
            if rows_displayed >= num_rows:
                btn.place_forget()  # Hide the buttons that exceed the desired number of rows (5)
            else:
                btn.place(x=x_pos_mp3_r0, y=y_pos_mp3, width=115, height=75)
                x_pos_mp3_r0 += 120

                if (i + 1) % row_length == 0:
                    y_pos_mp3 += 80  # Move to the next row after 'row_length' buttons
                    x_pos_mp3_r0 = 22  # Reset the x-position for the new row
                    rows_displayed += 1  # Increment the row countns

        if snd_mp3_btn_place > num_rows * row_length:
            # Add a vertical slider when there are more buttons than can be displayed
            slider_snd_mp3_btns = tk.Scale(from_=0, to=snd_mp3_btn_place - row_length, command=self.show_snd_mp3_btns,
                                            showvalue=0, length=400, orient='vertical', sliderlength=50,
                                            troughcolor="#000000", highlightbackground=sys_clr[6], bg='#00ffff')
            slider_snd_mp3_btns.set(0)
            slider_snd_mp3_btns.place(x=1220, y=200)  # Adjust the x and y positions accordingly
    def show_snd_mp3_btns(self, value):
        start_index_mp3 = int(float(value))  # Convert float value to integer
        num_rows = 4  # Number of rows to display
        row_length = 10  # Number of buttons per row

        # Show the buttons based on the new start index
        x_pos_mp3_r0 = 22
        y_pos_mp3_r0 = 200  # Set the initial y-position for the first row
        visible_buttons = []
        for i in range(start_index_mp3, min(start_index_mp3 + (num_rows * row_length), snd_mp3_btn_place)):
            btn = snd_mp3_btns[i]
            btn.place(x=x_pos_mp3_r0, y=y_pos_mp3_r0, width=115, height=75)
            x_pos_mp3_r0 += 120
            visible_buttons.append(btn)

            if (i + 1) % row_length == 0:
                y_pos_mp3_r0 += 80  # Move to the next row after 'row_length' buttons
                x_pos_mp3_r0 = 22  # Reset the x-position for the new row
    #----------------------------------------------------------------------------------
    # GET THE ACTUAL SOUNDFOLDER WITH SUBFOLDER AND KIND OF SOUND WITH INCLUDING FILES
    #----------------------------------------------------------------------------------
    def load_soundfolder(self):
        global snd_fldr, subfolders_count, subfolders_list, mp3files_count, mp3files_list, act_mp3_files_path
        #------------------------------------------------------------------------------
        # GET THE SOUNDFOLDER
        #------------------------------------------------------------------------------
        if device in [DEVICE_B_txt[1], DEVICE_B_txt[2], DEVICE_B_txt[4], DEVICE_B_txt[8]]:
            if style == STYLE_B_txt[0]:
                if theme in [THEME_B_txt[0], THEME_B_txt[1], THEME_B_txt[2], THEME_B_txt[3], THEME_B_txt[4], THEME_B_txt[5], THEME_B_txt[6], THEME_B_txt[7], THEME_B_txt[8]]:
                    soundfolder = "KARR2000"
                elif theme in [THEME_B_txt[9], THEME_B_txt[10]]:
                    soundfolder = "KARR3000"
            elif style == STYLE_B_txt[1]:
                if theme in [THEME_B_txt[0], THEME_B_txt[1], THEME_B_txt[2], THEME_B_txt[3], THEME_B_txt[4], THEME_B_txt[5], THEME_B_txt[6], THEME_B_txt[7], THEME_B_txt[8]]:
                    soundfolder = "KITT2000"
                elif theme in [THEME_B_txt[9], THEME_B_txt[10]]:
                    soundfolder = "KITT3000"
        snd_fldr = os.path.join(folder,'sound', soundfolder)

        #------------------------------------------------------------------------------
        # GET AMOUNT OF SUBFOLDERS
        #------------------------------------------------------------------------------
        subfolders_count, subfolders_list = self.get_subfolders_count_and_names(snd_fldr)
        #------------------------------------------------------------------------------
        # GET AMOUNT AND NAMES OF MP3 FILES
        #------------------------------------------------------------------------------
        act_mp3_files_path = os.path.join(snd_fldr, snd_btn_txt)
        mp3files_count, mp3files_list = self.get_mp3files_count_and_names(act_mp3_files_path)
        self._publish_state(
            snd_fldr=snd_fldr,
            subfolders_count=subfolders_count,
            subfolders_list=subfolders_list,
            mp3files_count=mp3files_count,
            mp3files_list=mp3files_list,
            act_mp3_files_path=act_mp3_files_path,
        )
    #----------------------------------------------------------------------------------
    # OPEN AND PLAY THE MP3 FILE
    #----------------------------------------------------------------------------------
    def play_mp3(self, path, file):
        full_path = os.path.join(path, file)
        try:
            pygame.mixer.music.load(full_path)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Fehler beim Abspielen von {full_path}: {e}")
    #----------------------------------------------------------------------------------
    # PLAY A SPECIFIC MP3 FILE IN A LOOP
    #----------------------------------------------------------------------------------
    def toggle_audio_loop(self, filepath, loop=True):
        filename = os.path.basename(filepath)

        if filename not in self.audio_sounds:
            try:
                self.audio_sounds[filename] = pygame.mixer.Sound(filepath)
            except Exception as e:
                print(f"[AUDIO] Fehler beim Laden: {filepath} → {e}")
                return False

        # Wenn im Loop: Toggle Start/Stop
        if loop:
            if filename in self.audio_channels and self.audio_channels[filename].get_busy():
                self.audio_channels[filename].stop()
                del self.audio_channels[filename]
                return False  # gestoppt
            else:
                channel = pygame.mixer.find_channel()
                if channel:
                    channel.play(self.audio_sounds[filename], loops=-1)
                    self.audio_channels[filename] = channel
                    return True  # gestartet
                else:
                    print("[AUDIO] Kein freier Kanal")
                    return False
        else:
            # Nur einmal abspielen
            channel = pygame.mixer.find_channel()
            if channel:
                channel.play(self.audio_sounds[filename], loops=0)
            return None  # kein Statuswechsel
        #----------------------------------------------------------------------------------
        # VOICECOMMAND LISTEN FOR ACTIVATION WORD #todo import from above
        #----------------------------------------------------------------------------------
        #def listen_for_activation_word():
    #--------------------------------------------------------------------------------------
    # DEV001 FUNCTIONS
    #--------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------
    # DEV001 HARDWARE
    #----------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    # GPS MODULE
    #------------------------------------------------------------------------------
    def gps_data(self):
        global gps_date, gps_odo_metric_cnt, gps_odo_imperial_cnt
        global odo_trip_gps_metric_old, odo_trip_gps_imperial_old
        global odo_total_gps_metric_old, odo_total_gps_imperial_old
        global gps_odo_metric_0str, gps_odo_imperial_0str
        global gps_time, gps_lat_str, gps_lat_dir, gps_long_str, gps_lon_dir
        global gps_altitude, gps_altitude_units
        global gps_kph_0, gps_mph_0, time_zone_offset
        global reset_trip

        # Lade alte Werte aus Datei
        with open(os.path.join(datadir, "btn_states.json"), encoding="utf-8") as f:
            data = json.load(f)
        odo_trip_gps_imperial_old = data["odo_config"]["odo_trip_gps_imperial"]
        odo_trip_gps_metric_old = data["odo_config"]["odo_trip_gps_metric"]
        odo_total_gps_imperial_old = data["odo_config"]["odo_total_gps_imperial"]
        odo_total_gps_metric_old = data["odo_config"]["odo_total_gps_metric"]

        last_gps_time = time.time()
        try:
            gps_raw = gps_serial.readline().decode('ascii', errors='replace')
            parsed = pynmea2.parse(gps_raw)

            if gps_raw.startswith('$GPRMC'):
                gps_date = parsed.datestamp
                if parsed.spd_over_grnd:
                    knots = parsed.spd_over_grnd
                    gps_speed_kmh = knots * 1.852
                    gps_kph_0 = f"{round(gps_speed_kmh):03d}"
                    gps_mph_0 = f"{round(knots * 1.15078):03d}"

                    # Zeitdifferenz zur letzten Messung
                    current_time = time.time()
                    delta_time = current_time - last_gps_time
                    last_gps_time = current_time

                    # Filter: unrealistische Zeit oder Geschwindigkeit < 2.0 km/h → keine Zählung
                    if delta_time <= 0 or delta_time > 2.0 or gps_speed_kmh < 2.0:
                        distance_km = 0.0
                    else:
                        distance_km = gps_speed_kmh * (delta_time / 3600.0)

                    gps_odo_metric_cnt += distance_km * 10000  # intern in "Zehntausendstel km"
                    gps_odo_imperial_cnt += distance_km * 10000 * 0.621371192

                    gps_odo_metric_0str = f"{(gps_odo_metric_cnt / 10000 + odo_trip_gps_metric_old):.2f}"
                    gps_odo_imperial_0str = f"{(gps_odo_imperial_cnt / 10000 + odo_trip_gps_imperial_old):.2f}"

                    odo_trip_gps_metric_new = round((gps_odo_metric_cnt / 10000 + odo_trip_gps_metric_old), 2)
                    odo_trip_gps_imperial_new = round((gps_odo_imperial_cnt / 10000 + odo_trip_gps_imperial_old), 2)

                    if odo_trip_gps_metric_new != odo_trip_gps_metric_old:
                        bsm.set_odo_value("odo_trip_gps_metric", odo_trip_gps_metric_new)
                        save_needed = True

                    if odo_trip_gps_imperial_new != odo_trip_gps_imperial_old:
                        bsm.set_odo_value("odo_trip_gps_imperial", odo_trip_gps_imperial_new)
                        save_needed = True

            elif gps_raw.startswith('$GPGGA'):
                gps_time_raw = parsed.timestamp

                from datetime import datetime, timedelta
                if 'time_zone_offset' in globals():
                    gps_time_adjusted = datetime.combine(datetime.today(), gps_time_raw) + timedelta(hours=int(time_zone_offset))
                else:
                    gps_time_adjusted = datetime.combine(datetime.today(), gps_time_raw)

                gps_time = gps_time_adjusted.strftime("%H:%M:%S")
                gps_lat_str = f"{parsed.latitude:.5f}"
                gps_lat_dir = parsed.lat_dir
                gps_long_str = f"{parsed.longitude:.5f}"
                gps_lon_dir = parsed.lon_dir
                if parsed.altitude is not None:
                    gps_altitude = f"{parsed.altitude:.1f}"
                    gps_altitude_units = parsed.altitude_units

        except Exception as e:
            print("no GPS data:", e)

        save_needed = False

        # Trip zurücksetzen falls gewünscht
        if reset_trip:
            bsm.set_odo_value("odo_trip_gps_metric", 0.0)
            bsm.set_odo_value("odo_trip_gps_imperial", 0.0)
            reset_trip = False
            save_needed = True
        else:
            # Final neue Werte berechnen
            odo_trip_gps_metric_new = round((gps_odo_metric_cnt / 10000) + odo_trip_gps_metric_old, 1)
            odo_trip_gps_imperial_new = round((gps_odo_imperial_cnt / 10000) + odo_trip_gps_imperial_old, 1)
            odo_total_gps_metric_new = round((gps_odo_metric_cnt / 10000) + odo_total_gps_metric_old, 1)
            odo_total_gps_imperial_new = round((gps_odo_imperial_cnt / 10000) + odo_total_gps_imperial_old, 1)

            if odo_trip_gps_metric_new != odo_trip_gps_metric_old:
                bsm.set_odo_value("odo_trip_gps_metric", odo_trip_gps_metric_new)
                save_needed = True

            if odo_trip_gps_imperial_new != odo_trip_gps_imperial_old:
                bsm.set_odo_value("odo_trip_gps_imperial", odo_trip_gps_imperial_new)
                save_needed = True

            if odo_total_gps_metric_new != odo_total_gps_metric_old:
                bsm.set_odo_value("odo_total_gps_metric", odo_total_gps_metric_new)
                save_needed = True

            if odo_total_gps_imperial_new != odo_total_gps_imperial_old:
                bsm.set_odo_value("odo_total_gps_imperial", odo_total_gps_imperial_new)
                save_needed = True

        if save_needed:
            bsm.save()
    #--------------------------------------------------------------------------------------
    # DEV002 FUNCTIONS
    #--------------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------
    # DEV002 I2C RELAIS BOARDS
    #----------------------------------------------------------------------------------
    def toggle_relay(self, relay_num):
        global relay_states_1to8, relay_states_9to16, btns_RB01, buses
        board_num = relay_num // 16
        relay_index = relay_num % 16

        if relay_index < 8:
            relay_states_1to8[board_num] ^= (1 << relay_index)
        else:
            relay_states_9to16[board_num] ^= (1 << (relay_index - 8))

        hi = relay_states_9to16[board_num]
        lo = relay_states_1to8[board_num]

        try:
            buses[board_num].write_word_data(i2c_addr_dev02rb[board_num], lo, hi)
        except Exception as e:
            print("Relaisbefehl uebersprungen – Board nicht erreichbar oder nicht definiert:", e)
        self._publish_state(
            relay_states_1to8=relay_states_1to8,
            relay_states_9to16=relay_states_9to16,
        )

    def _publish_state(self, **values):
        self.main_globals.update(values)
        globals().update(values)
        set_context(self.main_globals)
