import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        # ----------------------------------------------------------------------------------- #
        #                                              COLORS                                 #
        LABLE_BG_COLORS         = "#393d49"
        OK_BUTTON_BG_COLORS     = "#01aaed"
        CANCLE_BUTTON_BG_COLORS = "#cc0000"
        LABLE_FONT_COLOR        = "#ffffff" 
        
        # ----------------------------------------------------------------------------------- #
        #                               BUTTON FONT SIZE AND FAMILY                           #
        FONT_SIZE    = 24
        FONT_FAMILY  = 'Times'
        HEADING_FONT = tkFont.Font(family=FONT_FAMILY,size=FONT_SIZE+10)
        LABLE_FONT   = tkFont.Font(family='Times',size=16)
        BUTTON_FONT  = tkFont.Font(family='Times',size=22)
         
        # ----------------------------------------------------------------------------------- #
        #                                       Window Size                                   #
        width=561
        height=332
        
        # ----------------------------------------------------------------------------------- #
        #                                        WINDOE TITLE                                 #
        root.title("Cloven Fashion - Edit Product ")
        
        
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        TOPLABLE=tk.Label(root)
        TOPLABLE["bg"] = "#1e9fff"
        TOPLABLE["font"] = HEADING_FONT
        TOPLABLE["fg"] = "#fad400"
        TOPLABLE["justify"] = "center"
        TOPLABLE["text"] = "CLOVEN FASHION"
        TOPLABLE.place(x=0,y=0,width=562,height=55)
        
        CODE_LABLE=tk.Label(root)
        CODE_LABLE["bg"] = LABLE_BG_COLORS
        CODE_LABLE["font"] = LABLE_FONT
        CODE_LABLE["fg"] = LABLE_FONT_COLOR
        CODE_LABLE["justify"] = "center"
        CODE_LABLE["text"] = "Product Code"
        CODE_LABLE.place(x=10,y=60,width=158,height=32)

        self.GET_CODE_ENTRY=tk.Entry(root)
        self.GET_CODE_ENTRY["borderwidth"] = "1px"
        self.GET_CODE_ENTRY["font"] = LABLE_FONT
        self.GET_CODE_ENTRY["fg"] = "#333333"
        self.GET_CODE_ENTRY["justify"] = "center"
        self.GET_CODE_ENTRY.place(x=180,y=60,width=259,height=32)

        FINT_BUTTON=tk.Button(root)
        FINT_BUTTON["bg"] = OK_BUTTON_BG_COLORS
        FINT_BUTTON["font"] = BUTTON_FONT
        FINT_BUTTON["fg"] = "#000000"
        FINT_BUTTON["justify"] = "center"
        FINT_BUTTON["text"] = "Find"
        FINT_BUTTON.place(x=450,y=60,width=89,height=30)
        FINT_BUTTON["command"] = self.FINT_BUTTON_command

    def FINT_BUTTON_command(self):
        CODE = self.GET_CODE_ENTRY.get()
        print(CODE)

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    
# main()