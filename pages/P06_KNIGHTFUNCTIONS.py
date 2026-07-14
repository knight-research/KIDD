from pages.page_context import sync_context

sync_context(globals())

#------------------------------------------------------------------------------------------
# PAGE 06: KNIGHT FUNCTIONS
#------------------------------------------------------------------------------------------
class P06_KNIGHTFUNCTIONS(tk.Frame):
    if debug == True:
        print (MENU_B_txt[5])
    def __init__(self, master):
        sync_context(globals())
        tk.Frame.__init__(self, master)

        # load background image
        if device == DEVICE_B_txt[1]:
            background_image = bgDEV001_img_list[3]
        elif device == DEVICE_B_txt[2]:
            background_image = bgDEV002_img_list[3]
            
        canvas = tk.Canvas(self, bg='black', highlightthickness=0)
        canvas.pack(fill='both', expand=True)
        canvas.create_image(0, 0, image=background_image, anchor='nw')
        canvas.create_text(25, 20, **txt_style_pagename, fill=sys_clr[9], text="K-FUNC")
        #----------------------------------------------------------------------------------
        # MENU BUTTONS
        #----------------------------------------------------------------------------------
        read.buttons_menu()
        self.update_page()

    def update_page(self):
        if debug == True:
            print ("K-FUNC UPDATE")

        self.after(time_conf, self.update_page)
