import tkinter as tk


def create_voicebox_controls(page, theme, theme_names, btn_style_imgbtn, on_images):
    page.btns_DEV001VBBTN = []
    if theme in theme_names[:3] or theme in [theme_names[7]]: #0 1 2 oder 7
        x_pos_VBBTN = 1282
        x_pos_VBBTN2 = 1633
        y_pos_VBBTN_next = +130
        y_pos_VBBTN2_next = +130
        y_pos_VBBTN = 90
        y_pos_VBBTN2 = 90
        wh_btn_VBBTN = [115, 71]
        no_VBBRN = 8
    else:
        x_pos_VBBTN = 1282
        x_pos_VBBTN2 = 1640
        y_pos_VBBTN_next = +120
        y_pos_VBBTN2_next = +120
        y_pos_VBBTN = 30
        y_pos_VBBTN2 = 30
        wh_btn_VBBTN = [100, 70]
        no_VBBRN = 10
    if theme in theme_names[:9]: #0 to 8
        for i in range(no_VBBRN):
            if i < (no_VBBRN/2):
                btn_DEV001VBBTN = tk.Button(page, **btn_style_imgbtn, command=lambda i=i: [page.master.switch_frame(page.__class__)])
                btn_DEV001VBBTN.place(x=x_pos_VBBTN, y=y_pos_VBBTN, width=wh_btn_VBBTN[0], height=wh_btn_VBBTN[1])
                y_pos_VBBTN += y_pos_VBBTN_next
                page.btns_DEV001VBBTN.append(btn_DEV001VBBTN)
            else:
                btn_DEV001VBBTN = tk.Button(page, **btn_style_imgbtn, command=lambda i=i: [page.master.switch_frame(page.__class__)])
                btn_DEV001VBBTN.place(x=x_pos_VBBTN2, y=y_pos_VBBTN2, width=wh_btn_VBBTN[0], height=wh_btn_VBBTN[1])
                y_pos_VBBTN2 += y_pos_VBBTN2_next
                page.btns_DEV001VBBTN.append(btn_DEV001VBBTN)
            page.btns_DEV001VBBTN[i].config(image=on_images[i+4])

    page.btns_DEV001VBSTBTN = []
    if theme in theme_names[:3]: #0 1 2 oder 7
        x_pos_VBSTBTN = 1400
        y_pos_VBSTBTN_next = +85
        y_pos_VBSTBTN = 380
        wh_btn_VBSTBTN = [235, 82]
    else:
        x_pos_VBSTBTN = 1397
        y_pos_VBSTBTN_next = +85
        y_pos_VBSTBTN = 410
        wh_btn_VBSTBTN = [235, 80]
    if theme in theme_names[:9]: #0 to 8
        for i in range(3):
            btn_DEV001VBSTBTN = tk.Label(page, **btn_style_imgbtn)
            btn_DEV001VBSTBTN.place(x=x_pos_VBSTBTN, y=y_pos_VBSTBTN, width=wh_btn_VBSTBTN[0], height=wh_btn_VBSTBTN[1])
            y_pos_VBSTBTN += +(wh_btn_VBSTBTN[1] +5)
            page.btns_DEV001VBSTBTN.append(btn_DEV001VBSTBTN)


def create_voicebox_leds(page, theme, theme_names, btn_style_imgbtn, off_image=None):
    page.led_DEV001VBS34L01 = []
    page.led_DEV001VBS34L02 = []
    page.led_DEV001VBS34L03 = []

    if theme == theme_names[0]:
        page.ammount_VB = 1
        page.middle_index = 0
        led_gauge_U01VB34L01 = tk.Label(page, **btn_style_imgbtn)
        if off_image is not None:
            led_gauge_U01VB34L01.config(image=off_image)
        led_gauge_U01VB34L01.place(x=1400, y=10, width=233, height=279)
        page.led_DEV001VBS34L01.append(led_gauge_U01VB34L01)
        return

    if theme in theme_names[:3]: # THEME 0 1 2
        page.ammount_VB = 18
        page.middle_index = 9  # Index of the middle LED
    elif theme in theme_names[3:11]: # THEME 3 to 8
        page.ammount_VB = 20
        page.middle_index = 10  # Index of the middle LED

    if theme in theme_names[0:7]: # THEME 1 to 8
        y_pos_VBL01 = 10
        y_pos_VBL02 = 10
        y_pos_VBL03 = 10
        for i in range(0, page.ammount_VB):
            led_gauge_U01VB34L01 = tk.Label(page, **btn_style_imgbtn)
            led_gauge_U01VB34L01.place(x=1400, y=y_pos_VBL01, width=77, height=20)
            y_pos_VBL01 += +20
            page.led_DEV001VBS34L01.append(led_gauge_U01VB34L01)
        for i in range(0, page.ammount_VB):
            led_gauge_U01VB34L02 = tk.Label(page, **btn_style_imgbtn)
            led_gauge_U01VB34L02.place(x=1477, y=y_pos_VBL02, width=77, height=20)
            y_pos_VBL02 += +20
            page.led_DEV001VBS34L02.append(led_gauge_U01VB34L02)
        for i in range(0, page.ammount_VB):
            led_gauge_U01VB34L03 = tk.Label(page, **btn_style_imgbtn)
            led_gauge_U01VB34L03.place(x=1554, y=y_pos_VBL03, width=77, height=20)
            y_pos_VBL03 += +20
            page.led_DEV001VBS34L03.append(led_gauge_U01VB34L03)
    elif theme == theme_names[8]:
        y_pos_VBL01 = 10
        y_pos_VBL02 = 10
        y_pos_VBL03 = 10
        for i in range(0, page.ammount_VB):
            led_gauge_U01VB34L01 = tk.Label(page, **btn_style_imgbtn)
            led_gauge_U01VB34L01.place(x=1400, y=y_pos_VBL01, width=77, height=20)
            y_pos_VBL01 += +20
            page.led_DEV001VBS34L01.append(led_gauge_U01VB34L01)
        for i in range(0, page.ammount_VB):
            led_gauge_U01VB34L02 = tk.Label(page, **btn_style_imgbtn)
            led_gauge_U01VB34L02.place(x=1477, y=y_pos_VBL02, width=77, height=20)
            y_pos_VBL02 += +20
            page.led_DEV001VBS34L02.append(led_gauge_U01VB34L02)
        for i in range(0, page.ammount_VB):
            led_gauge_U01VB34L03 = tk.Label(page, **btn_style_imgbtn)
            led_gauge_U01VB34L03.place(x=1554, y=y_pos_VBL03, width=77, height=20)
            y_pos_VBL03 += +20
            page.led_DEV001VBS34L03.append(led_gauge_U01VB34L03)
    elif theme == theme_names[7]:
        y_pos_VBL01 = 10
        y_pos_VBL02 = 10
        for i in range(0, 8):
            led_gauge_U01VB34L01 = tk.Label(page, **btn_style_imgbtn)
            led_gauge_U01VB34L01.place(x=1410, y=y_pos_VBL01, width=95, height=35)
            y_pos_VBL01 += +45
            page.led_DEV001VBS34L01.append(led_gauge_U01VB34L01)
        for i in range(0, 8):
            led_gauge_U01VB34L02 = tk.Label(page, **btn_style_imgbtn)
            led_gauge_U01VB34L02.place(x=1530, y=y_pos_VBL02, width=95, height=35)
            y_pos_VBL02 += +45
            page.led_DEV001VBS34L02.append(led_gauge_U01VB34L02)


def update_voicebox_status(page, theme, theme_names, btn_states_FNKT, speed_int, on_images, off_images):
    if not hasattr(page, "old_vbst_images"):
        page.old_vbst_images = [None, None, None]

    if theme in theme_names[:9]:
        if btn_states_FNKT[3]:
            img0 = on_images[14] if speed_int <= 55 else off_images[14]
            if page.old_vbst_images[0] != img0:
                page.btns_DEV001VBSTBTN[0].config(image=img0)
                page.old_vbst_images[0] = img0

            img1 = on_images[15] if 55 <= speed_int <= 100 else off_images[15]
            if page.old_vbst_images[1] != img1:
                page.btns_DEV001VBSTBTN[1].config(image=img1)
                page.old_vbst_images[1] = img1

            img2 = on_images[16] if speed_int >= 100 else off_images[16]
            if page.old_vbst_images[2] != img2:
                page.btns_DEV001VBSTBTN[2].config(image=img2)
                page.old_vbst_images[2] = img2

        else:
            for i, idx in enumerate([14, 15, 16]):
                img = off_images[idx]
                if page.old_vbst_images[i] != img:
                    page.btns_DEV001VBSTBTN[i].config(image=img)
                    page.old_vbst_images[i] = img
