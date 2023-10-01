import tkinter as tk
import tkinter.font as tkFont
from database import remove_data
class App:
    def __init__(self, root):
        # ----------------------------------------------------------------------------------- #
        #                               BUTTON FONT SIZE AND FAMILY                           #
        FONT_SIZE    = 24
        FONT_FAMILY  = 'Times'
        HEADING_FONT = tkFont.Font(family=FONT_FAMILY,size=FONT_SIZE+10)
        LABLE_FONT   = tkFont.Font(family='Times',size=16)
        BUTTON_FONT  = tkFont.Font(family='Times',size=22)
        
        
        # ----------------------------------------------------------------------------------- #
        #                                              COLORS                                 #
        LABLE_BG_COLORS         = "#393d49"
        OK_BUTTON_BG_COLORS     = "#01aaed"
        CANCLE_BUTTON_BG_COLORS = "#cc0000"
        LABLE_FONT_COLOR        = "#ffffff" 
        BUTTON_FG_COLOR         = "#000000"
        TOPLABLE_BG_COLOR       = "#1e9fff"
        TOPLABLE_FG_COLOR       = "#fad400"
        
        
        # ----------------------------------------------------------------------------------- #
        #                                 Window Title and SIze                               #
        root.title("Cloven Fashion - delete Product")
        width=561
        height=332
        
        self.window = root
        
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        TOPLABLE=tk.Label(root)
        TOPLABLE["bg"] = TOPLABLE_BG_COLOR
        TOPLABLE["font"] = HEADING_FONT
        TOPLABLE["fg"] = TOPLABLE_FG_COLOR
        TOPLABLE["justify"] = "center"
        TOPLABLE["text"] = "CLOVEN FASHION"
        TOPLABLE.place(x=0,y=0,width=562,height=55)

        ENTER_NAME_LABLE=tk.Label(root)
        ENTER_NAME_LABLE["bg"] = LABLE_BG_COLORS
        ENTER_NAME_LABLE["font"] = LABLE_FONT
        ENTER_NAME_LABLE["fg"] = LABLE_FONT_COLOR
        ENTER_NAME_LABLE["justify"] = "center"
        ENTER_NAME_LABLE["text"] = "Enter Product Code"
        ENTER_NAME_LABLE.place(x=0,y=60,width=245,height=38)

        self.NAME_ENTRY=tk.Entry(root)
        self.NAME_ENTRY["borderwidth"] = "1px"
        self.NAME_ENTRY["font"] = LABLE_FONT
        self.NAME_ENTRY["fg"] = "#333333"
        self.NAME_ENTRY["justify"] = "center"
        self.NAME_ENTRY["text"] = "Entry"
        self.NAME_ENTRY.place(x=250,y=60,width=302,height=39)

        SEARCH_BUTTON=tk.Button(root)
        SEARCH_BUTTON["bg"] = OK_BUTTON_BG_COLORS
        SEARCH_BUTTON["font"] = BUTTON_FONT
        SEARCH_BUTTON["fg"] = BUTTON_FG_COLOR
        SEARCH_BUTTON["justify"] = "center"
        SEARCH_BUTTON["text"] = "Delete"
        SEARCH_BUTTON.place(x=450,y=280,width=93,height=36)
        SEARCH_BUTTON["command"] = self.DELETE_BUTTON_command

        CANCLE_BUTTON=tk.Button(root)
        CANCLE_BUTTON["bg"] = CANCLE_BUTTON_BG_COLORS
        CANCLE_BUTTON["font"] = BUTTON_FONT
        CANCLE_BUTTON["fg"] = BUTTON_FG_COLOR
        CANCLE_BUTTON["justify"] = "center"
        CANCLE_BUTTON["text"] = "Cancel "
        CANCLE_BUTTON.place(x=320,y=280,width=109,height=36)
        CANCLE_BUTTON["command"] = self.CANCLE_BUTTON_command

    def DELETE_BUTTON_command(self):
        PRODUCT_CODE = self.NAME_ENTRY.get()
        remove_data(PRODUCT_CODE)
        self.window.destroy()
        

    def CANCLE_BUTTON_command(self):
        self.window.destroy()
        
        
def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

# main()