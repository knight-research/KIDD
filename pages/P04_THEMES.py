from pages.page_context import sync_context

sync_context(globals())

#------------------------------------------------------------------------------------------
# PAGE 04: THEMES
#------------------------------------------------------------------------------------------
class P04_THEMES(tk.Frame):
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
            [frm00_YPOS, frm00_YPOS+60], #0 TITLE FRAME
            [frm01_YPOS, frm01_YPOS+90], #1 DEV FRAME
            [frm02_YPOS, frm02_YPOS+90], #2 STYLE FRAME
            [frm03_YPOS, frm03_YPOS+90], #3 THEME FRAME
            [frm04_YPOS, frm04_YPOS+90], #4 SYSTEM FRAME
            [frm05_YPOS, frm05_YPOS+90], #5 MENU FRAME
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
        #--------------------------------------------------------------------------
        # CREATE FRAME 01 CORNERS LEFT/TOP DISPLAY
        #--------------------------------------------------------------------------
        coordinates = [
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][0]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[1][0]), 0, 1),        # LT_X
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][0]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][0]+xy_width), 1, 1),        # LT_Y
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][0]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[1][0]), 0, 0),  # RT_X
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][0]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][0]+xy_width), 1, 0),  # RT_Y
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][1]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[1][1]), 0, 1),        # LB_X
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][1]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[1][1]-xy_width), 1, 1),        # LB_Y
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][1]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[1][1]), 0, 0),  # RB_X
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][1]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[1][1]-xy_width), 1, 0),  # RB_Y
        ]
        for x1, y1, x2, y2, is_vertical, is_top in coordinates:
            line_color = colors_corner[is_vertical]
            line_width = 1
            canvas.create_line(x1, y1, x2, y2, fill=line_color, width=line_width)
        #--------------------------------------------------------------------------
        # CREATE FRAME 02 CORNERS LEFT/TOP DISPLAY
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
        # CREATE FRAME 03 CORNERS LEFT/TOP DISPLAY
        #--------------------------------------------------------------------------
        coordinates = [
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[3][0]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[3][0]), 0, 1),        # LT_X
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[3][0]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[3][0]+xy_width), 1, 1),        # LT_Y
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[3][0]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[3][0]), 0, 0),  # RT_X
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[3][0]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[3][0]+xy_width), 1, 0),  # RT_Y
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[3][1]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[3][1]), 0, 1),        # LB_X
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[3][1]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[3][1]-xy_width), 1, 1),        # LB_Y
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[3][1]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[3][1]), 0, 0),  # RB_X
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[3][1]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[3][1]-xy_width), 1, 0),  # RB_Y
        ]
        for x1, y1, x2, y2, is_vertical, is_top in coordinates:
            line_color = colors_corner[is_vertical]
            line_width = 1
            canvas.create_line(x1, y1, x2, y2, fill=line_color, width=line_width)
        #--------------------------------------------------------------------------
        # CREATE FRAME 04 CORNERS LEFT/TOP DISPLAY
        #--------------------------------------------------------------------------
        coordinates = [
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[4][0]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[4][0]), 0, 1),        # LT_X
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[4][0]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[4][0]+xy_width), 1, 1),        # LT_Y
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[4][0]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[4][0]), 0, 0),  # RT_X
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[4][0]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[4][0]+xy_width), 1, 0),  # RT_Y
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[4][1]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[4][1]), 0, 1),        # LB_X
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[4][1]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[4][1]-xy_width), 1, 1),        # LB_Y
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[4][1]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[4][1]), 0, 0),  # RB_X
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[4][1]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[4][1]-xy_width), 1, 0),  # RB_Y
        ]
        for x1, y1, x2, y2, is_vertical, is_top in coordinates:
            line_color = colors_corner[is_vertical]
            line_width = 1
            canvas.create_line(x1, y1, x2, y2, fill=line_color, width=line_width)
        #--------------------------------------------------------------------------
        # CREATE FRAME 02 (MENU) CORNERS LEFT/TOP DISPLAY
        #--------------------------------------------------------------------------
        coordinates = [
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[5][0]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[5][0]), 0, 1),        # LT_X
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[5][0]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[5][0]+xy_width), 1, 1),        # LT_Y
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[5][0]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[5][0]), 0, 0),  # RT_X
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[5][0]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[5][0]+xy_width), 1, 0),  # RT_Y
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[5][1]), (bggrid[0]+xcrnrborder+xy_width), (bggrid[3]+frames[5][1]), 0, 1),        # LB_X
            ((bggrid[0]+xcrnrborder), (bggrid[3]+frames[5][1]), (bggrid[0]+xcrnrborder), (bggrid[3]+frames[5][1]-xy_width), 1, 1),        # LB_Y
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[5][1]), (bggrid[1]-xcrnrborder_ri-xy_width), (bggrid[3]+frames[5][1]), 0, 0),  # RB_X
            ((bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[5][1]), (bggrid[1]-xcrnrborder_ri), (bggrid[3]+frames[5][1]-xy_width), 1, 0),  # RB_Y
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
        # STATIC TEXT
        #----------------------------------------------------------------------------------
        canvas.create_text(20, frm00_YPOS+4, **txt_style_pagename, fill=sys_clr[9], text="THEMES")
        canvas.create_text(20, frm01_YPOS+4, **txt_style_pagename, fill=sys_clr[9], text="DEVICE")
        canvas.create_text(20, frm02_YPOS+4, **txt_style_pagename, fill=sys_clr[9], text="STYLE")
        canvas.create_text(20, frm03_YPOS+4, **txt_style_pagename, fill=sys_clr[9], text="THEME")
        canvas.create_text(20, frm04_YPOS+4, **txt_style_pagename, fill=sys_clr[9], text="SYS")
        canvas.create_text(20, frm05_YPOS+4, **txt_style_pagename, fill=sys_clr[9], text="MENU")
        #----------------------------------------------------------------------------------
        # INFORMATION TEXT
        #----------------------------------------------------------------------------------
        canvas.create_text(1320, frm00_YPOS+20, **txt_style_pagename, fill=sys_clr[9], text="DEV000: WIFI ROUTER")
        canvas.create_text(1320, frm00_YPOS+50, **txt_style_pagename, fill=sys_clr[9], text="DEV001: SPEEDOMETER AND VOICEBOX")
        canvas.create_text(1320, frm00_YPOS+80, **txt_style_pagename, fill=sys_clr[9], text="DEV002: TACHOMETER AND POWERBOARD")
        canvas.create_text(1320, frm00_YPOS+110, **txt_style_pagename, fill=sys_clr[9], text="DEV003: 2TV DASH MONITORS")
        canvas.create_text(1320, frm00_YPOS+140, **txt_style_pagename, fill=sys_clr[9], text="DEV004: 1TV DASH MONITOR")
        canvas.create_text(1320, frm00_YPOS+170, **txt_style_pagename, fill=sys_clr[9], text="DEV005: LOWER CONSOLE")
        canvas.create_text(1320, frm00_YPOS+200, **txt_style_pagename, fill=sys_clr[9], text="DEV006: SWITCHPOD LEFT")
        canvas.create_text(1320, frm00_YPOS+230, **txt_style_pagename, fill=sys_clr[9], text="DEV007: SWITCHPOD RIGHT")
        canvas.create_text(1320, frm00_YPOS+260, **txt_style_pagename, fill=sys_clr[9], text="DEV008: OHC")
        canvas.create_text(1320, frm00_YPOS+290, **txt_style_pagename, fill=sys_clr[9], text="DEV009: MIRROR LEFT")
        canvas.create_text(1320, frm00_YPOS+320, **txt_style_pagename, fill=sys_clr[9], text="DEV010: MIRROR CENTER")
        canvas.create_text(1320, frm00_YPOS+350, **txt_style_pagename, fill=sys_clr[9], text="DEV011: MIRROR RIGHT")
        canvas.create_text(1320, frm00_YPOS+380, **txt_style_pagename, fill=sys_clr[9], text="DEV012: RADIO")
        canvas.create_text(1320, frm00_YPOS+410, **txt_style_pagename, fill=sys_clr[9], text="DEV013: HUD")
        canvas.create_text(1320, frm00_YPOS+440, **txt_style_pagename, fill=sys_clr[9], text="DEV014: RES")
        canvas.create_text(1320, frm00_YPOS+470, **txt_style_pagename, fill=sys_clr[9], text="DEV015: WIFI RELAIS BOARD")
            
        canvas.create_text(1320, frm00_YPOS+530, **txt_style_pagename, fill=sys_clr[9], text="DEV030: KNIGHT3000 HUD")
        canvas.create_text(1320, frm00_YPOS+560, **txt_style_pagename, fill=sys_clr[9], text="DEV032: KNIGHT3000 RADIO")
        canvas.create_text(1320, frm00_YPOS+590, **txt_style_pagename, fill=sys_clr[9], text="DEV033: KNIGHT3000 MIRROR")
        #----------------------------------------------------------------------------------
        # DEVICE BUTTONS
        #----------------------------------------------------------------------------------
        read.buttons_device()
        #----------------------------------------------------------------------------------
        # STYLE BUTTONS
        #----------------------------------------------------------------------------------   
        read.buttons_style()
        #----------------------------------------------------------------------------------
        # THEME BUTTONS
        #----------------------------------------------------------------------------------   
        read.buttons_theme()
        #----------------------------------------------------------------------------------
        # SYSTEM STYLE BUTTONS
        #----------------------------------------------------------------------------------   
        read.buttons_sys()
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        read.buttons_menu()
        #----------------------------------------------------------------------------------
        # END INIT
        #----------------------------------------------------------------------------------
        self.update_page()
    def update_page(self):
        if debug == True:
            print (MENU_B_txt[3])
        self.after(time_conf, self.update_page)
