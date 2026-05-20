def load_style_symbols(device, style, system, device_names, style_names, system_names):
    # SETUP DISPLAY RESOULUTIONS AND BACKGROUND GRIDS
    # left, width_display1, width_display2, top, height
    grid_spacing = 15
    if device == device_names[1]:
        dual_disp_style = "LR"
        bggrid = [0, 1280, 1280, 0, 768, 0]
    elif device == device_names[2]:
        dual_disp_style = "LR"
        bggrid = [0, 1280, 1280, 0, 768, 0]
    elif device == device_names[3]:
        dual_disp_style = "LR"
        bggrid = [0, 1280, 1280, 0, 768, 0]
    elif device == device_names[4]:
        dual_disp_style = "NONE"
        bggrid = [0, 1920, 0, 0, 1200, 0]
    elif device == device_names[8]:
        dual_disp_style = "UD"
        bggrid = [0, 320, 0, 0, 1480, 0]
    else:
        dual_disp_style = "NONE"
        bggrid = [0, 1280, 0, 0, 768, 0]

    kidd_left = "%s" % bggrid[0]
    kidd_top = "%s" % bggrid[3]
    kidd_width = "%s" % (bggrid[1] + bggrid[2])
    kidd_height = "%s" % bggrid[4]

    frm00_YPOS = 15
    frm01_YPOS = frm00_YPOS + 75
    frm02_YPOS = frm01_YPOS + 105
    frm03_YPOS = frm02_YPOS + 105
    frm04_YPOS = frm03_YPOS + 105
    frm05_YPOS = bggrid[4] - 138

    #        00            01                 02          03                    04                05       06           07             08              09
    fonts = ["BankGothic", "Bebas Neue Bold", "ccar7seg", "DSEG7 Classic Mini", "DSEG14 Classic", "lcars", "LCDDot TR", "led16sgmnt2", "Penn Station", "NostromoOutline-Black"]

    #             00_GRD-BG  01_GRD-X   02_GRD-Y   03_CRNR-X  04_CRNR-Y  05_GRAD_1  06_GRAD_2  07_GRAD_3  08_BG_BTN  09_TXT_BTN 10_ON      11_OFF
    sys_clr_OR = ["#151000", "#251500", "#201500", "#FF7700", "#FFBB00", "#551100", "#FF5500", "#AA5500", "#301000", "#FFF862", "#44FF44", "#FF4444"]
    sys_clr_GN = ["#001500", "#003010", "#103010", "#55FF55", "#BBFFBB", "#005500", "#00FF00", "#449944", "#002000", "#88FF88", "#44FF44", "#FF4444"]
    sys_clr_BU = ["#000515", "#001530", "#001030", "#0099FF", "#BBFFFF", "#005555", "#00FFFF", "#009999", "#002020", "#33AAFF", "#44FF44", "#FF4444"]
    sys_clr_WH = ["#000000", "#101010", "#151515", "#AAAAAA", "#BBBBBB", "#555555", "#FFFFFF", "#999999", "#202020", "#FFFFFF", "#44FF44", "#FF4444"]
    sys_clr_CP = ["#000000", "#110000", "#050000", "#EDC64D", "#EDC64D", "#FF0000", "#F8403E", "#F8403E", "#100000", "#76DAEB", "#44FF44", "#FF4444"]

    #             00_TXT_LBL 01_TXT_SYS 02_TXT_SYS 03_LBL_BG  04_BG_INF  05_TXT_INF 06_BLACK
    sty_clr_ka = ["#FFFFFF", "#FFFFDD", "#FFBB00", "#222200", "#142827", "#00FFFF", "#000000"]
    sty_clr_ki = ["#FFFFFF", "#FFDDDD", "#FF0000", "#250000", "#142827", "#00FFFF", "#000000"]

    sys_palettes = {
        system_names[0]: sys_clr_OR,
        system_names[1]: sys_clr_GN,
        system_names[2]: sys_clr_BU,
        system_names[3]: sys_clr_WH,
        system_names[4]: sys_clr_CP,
    }
    style_palettes = {
        style_names[0]: sty_clr_ka,
        style_names[1]: sty_clr_ki,
    }
    sys_clr = sys_palettes.get(system, sys_clr_OR)
    sty_clr = style_palettes.get(style, sty_clr_ka)

    return {
        "grid_spacing": grid_spacing,
        "dual_disp_style": dual_disp_style,
        "bggrid": bggrid,
        "kidd_left": kidd_left,
        "kidd_top": kidd_top,
        "kidd_width": kidd_width,
        "kidd_height": kidd_height,
        "frm00_YPOS": frm00_YPOS,
        "frm01_YPOS": frm01_YPOS,
        "frm02_YPOS": frm02_YPOS,
        "frm03_YPOS": frm03_YPOS,
        "frm04_YPOS": frm04_YPOS,
        "frm05_YPOS": frm05_YPOS,
        "fonts": fonts,
        "sys_clr": sys_clr,
        "sty_clr": sty_clr,
        "sys_clr_OR": sys_clr_OR,
        "sys_clr_GN": sys_clr_GN,
        "sys_clr_BU": sys_clr_BU,
        "sys_clr_WH": sys_clr_WH,
        "sys_clr_CP": sys_clr_CP,
        "sty_clr_ka": sty_clr_ka,
        "sty_clr_ki": sty_clr_ki,
        "btn_style_imgbtn": {'borderwidth': 0, 'highlightthickness': 0},
        "btn_style_imgbtn_lcars": {'borderwidth': 0, 'highlightthickness': 0, 'width': '181', 'height': '87'},
        "lbl_style_setup_btns": {'font': (fonts[6], 26), 'anchor': 'c'},
        "lbl_style_setup_btns_small": {'font': (fonts[6], 18), 'anchor': 'c', 'width': '11', 'height': '1'},
        "lbl_style_7SEG01_S12": {'font': (fonts[7], 75), 'anchor': 'nw', 'borderwidth': 0, 'highlightthickness': 0},
        "lbl_style_7SEG01_S34": {'font': (fonts[3], 60, "bold"), 'anchor': 'nw', 'borderwidth': 0, 'highlightthickness': 0},
        "lbl_style_7SEG03_S34": {'font': (fonts[2], 165), 'anchor': 'nw', 'borderwidth': 0, 'highlightthickness': 0},
        "lbl_style_SETUP": {'font': (fonts[6], 40), 'anchor': 'c'},
        "lbl_style_SETUP2": {'font': (fonts[6], 25), 'anchor': 'c'},
        "keypad_style": {'font': (fonts[0], 18), 'anchor': 'c', 'width': 4, 'height': 2},
        "txt_style_pagename": {'font': (fonts[8], 25), 'anchor': 'nw'},
        "txt_style_pageinfo": {'font': (fonts[5], 16), 'anchor': 'nw'},
        "lbl_style_sysinfo": {'font': (fonts[6], 36), 'anchor': 'nw'},
        "lbl_style_voicecmd": {'font': (fonts[6], 24), 'anchor': 'nw'},
        "txt_style_sysinfo": {'font': (fonts[6], 36), 'anchor': 'nw'},
        "txt_style_S34c": {'fill': sty_clr[0], 'font': (fonts[5], 24), 'anchor': 'c'},
        "txt_style_S34e": {'fill': sty_clr[0], 'font': (fonts[5], 24), 'anchor': 'e'},
    }