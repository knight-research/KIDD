from pages.page_context import sync_context

sync_context(globals())

#------------------------------------------------------------------------------------------
# PAGE 08: VIDEO
#------------------------------------------------------------------------------------------
class P08_VIDEO(tk.Frame):
    if debug == True:
        print (MENU_B_txt[7])
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
        # CREATE BACKGROUND GRID OVERLAYS
        #------------------------------------------------------------------------------
        #--------------------------------------------------------------------------
        # GLOBALS
        #--------------------------------------------------------------------------            
        # COORDINATES OF HORIZONTAL LINES
        coordinates = [
            (30, 15, 1245, 15),     #TITLE TOP
            (30, 75, 1245, 75),     #TITLE BOTTOM
            (30, 90, 1245, 90),     #MAIN TOP
            (30, 615, 1245, 615),   #MAIN BOTTOM
            (30, 630, 1245, 630),   #MENU TOP
            (30, 720, 1245, 720),   #MENU BOTTOM
            (1310, 15, 2340, 15),   #RIGHT TOP
            (1310, 720, 2340, 720), #RIGHT BOTTOM
        ]
        # Define colors
        colors_corner = [sys_clr[3], sys_clr[4]]
        gradient_colors = [sys_clr[5], sys_clr[6], sys_clr[7]]
        num_segments = 50                
        #--------------------------------------------------------------------------
        # CREATE TITLE CORNERS
        #--------------------------------------------------------------------------
        canvas.create_line(15, 15, 25, 15, fill=colors_corner[0], width=1)      #LT_X
        canvas.create_line(15, 15, 15, 25, fill=colors_corner[1], width=1)      #LT_Y
        canvas.create_line(1250, 15, 1260, 15, fill=colors_corner[0], width=1)  #RT_X
        canvas.create_line(1260, 15, 1260, 25, fill=colors_corner[1], width=1)  #RT_Y
        canvas.create_line(15, 75, 25, 75, fill=colors_corner[0], width=1)      #LB_X
        canvas.create_line(15, 75, 15, 65, fill=colors_corner[1], width=1)      #LB_Y            
        canvas.create_line(1250, 75, 1260, 75, fill=colors_corner[0], width=1)  #RB_X
        canvas.create_line(1260, 75, 1260, 65, fill=colors_corner[1], width=1)  #RB_Y
        #--------------------------------------------------------------------------
        # CREATE HORIZONTAL LINES
        #--------------------------------------------------------------------------
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
        # CREATE MAIN CORNERS
        #--------------------------------------------------------------------------
        canvas.create_line(15, 90, 25, 90, fill=colors_corner[0], width=1)      #LT_X
        canvas.create_line(15, 90, 15, 100, fill=colors_corner[1], width=1)     #LT_Y
        canvas.create_line(1250, 90, 1260, 90, fill=colors_corner[0], width=1)  #RT_X
        canvas.create_line(1260, 90, 1260, 100, fill=colors_corner[1], width=1) #RT_Y               
        canvas.create_line(15, 615, 25, 615, fill=colors_corner[0], width=1)    #LB_X
        canvas.create_line(15, 605, 15, 615, fill=colors_corner[1], width=1)    #LB_Y
        canvas.create_line(1250, 615, 1260, 615, fill=colors_corner[0], width=1)#RB_X
        canvas.create_line(1260, 605, 1260, 615, fill=colors_corner[1], width=1)#RB_Y
        #--------------------------------------------------------------------------
        # CREATE MENU CORNERS
        #--------------------------------------------------------------------------
        canvas.create_line(15, 630, 25, 630, fill=colors_corner[0], width=1)    #LT_X
        canvas.create_line(15, 630, 15, 640, fill=colors_corner[1], width=1)    #LT_Y
        canvas.create_line(1250, 630, 1260, 630, fill=colors_corner[0], width=1)#RT_X
        canvas.create_line(1260, 630, 1260, 640, fill=colors_corner[1], width=1)#RT_Y
        canvas.create_line(15, 720, 25, 720, fill=colors_corner[0], width=1)    #LB_X
        canvas.create_line(15, 710, 15, 720, fill=colors_corner[1], width=1)    #LB_Y
        canvas.create_line(1250, 720, 1260, 720, fill=colors_corner[0], width=1)#RB_X
        canvas.create_line(1260, 710, 1260, 720, fill=colors_corner[1], width=1)#RB_Y
        #--------------------------------------------------------------------------
        # CREATE MENU BUTTON STATUS CORNERS (10 BUTTONS)
        #--------------------------------------------------------------------------              
        x = 19
        for i in range(8):
            canvas.create_line(x, 705, x, 715, fill=colors_corner[0], width=1)             # Left line
            canvas.create_line(x, 715, x + 132, 715, fill=colors_corner[1], width=1)       # Bottom line
            canvas.create_line(x + 131, 705, x + 131, 715, fill=colors_corner[0], width=1) # Right line
            x += 145
        #--------------------------------------------------------------------------
        # RIGHT SCREEN CORNERS
        #--------------------------------------------------------------------------
        if device == DEVICE_B_txt[1]: 
            canvas.create_rectangle(1295, 15, 1750, 685, outline=sys_clr[6], width=2)
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
        canvas.create_text(20, 20, **txt_style_pagename, fill=sys_clr[9], text="VIDEO")
        #canvas.create_rectangle(15, 15, 1265, 85, outline=sys_clr[6], width=2)  #TITLEBAR
        #canvas.create_rectangle(15, 90, 1265, 605, outline=sys_clr[6], width=2) #PAGE
        #canvas.create_rectangle(15, 645, 1265, 715, outline=sys_clr[6], width=2) #MENU
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        read.buttons_menu()
        self.update_page()
    def update_page(self):
        if debug == True:
            print (MENU_B_txt[7])
        self.after(time_conf, self.update_page)
