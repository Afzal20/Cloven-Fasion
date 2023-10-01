import tkinter as tk
import tkinter.font as tkFont
from database import insert_data

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
        self.window = root
        self.window.title("Cloven Fashion - Add Product  ")

        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)
        self.window.resizable(width=False, height=False)

        TOPLABLE=tk.Label(self.window)
        TOPLABLE["bg"] = "#1e9fff"
        TOPLABLE["font"] = HEADING_FONT
        TOPLABLE["fg"] = "#fad400"
        TOPLABLE["justify"] = "center"
        TOPLABLE["text"] = "CLOVEN FASHION"
        TOPLABLE.place(x=0,y=0,width=562,height=55)

        PRODUCT_CODE_LABLE=tk.Label(self.window)
        PRODUCT_CODE_LABLE["bg"] = LABLE_BG_COLORS
        PRODUCT_CODE_LABLE["font"] = LABLE_FONT
        PRODUCT_CODE_LABLE["fg"] = LABLE_FONT_COLOR
        PRODUCT_CODE_LABLE["justify"] = "center"
        PRODUCT_CODE_LABLE["text"] = "Product code"
        PRODUCT_CODE_LABLE.place(x=20,y=70,width=164,height=30)

        NAME_LABLE=tk.Label(root)
        NAME_LABLE["bg"] = LABLE_BG_COLORS
        NAME_LABLE["font"] = LABLE_FONT
        NAME_LABLE["fg"] = LABLE_FONT_COLOR
        NAME_LABLE["justify"] = "center"
        NAME_LABLE["text"] = "NAME"
        NAME_LABLE.place(x=20,y=110,width=163,height=30)

        BRAND_LABLE=tk.Label(root)
        BRAND_LABLE["bg"] = LABLE_BG_COLORS
        
        BRAND_LABLE["font"] = LABLE_FONT
        BRAND_LABLE["fg"] = LABLE_FONT_COLOR
        BRAND_LABLE["justify"] = "center"
        BRAND_LABLE["text"] = "Brand"
        BRAND_LABLE.place(x=20,y=150,width=164,height=30)

        PRICE_LABLE=tk.Label(root)
        PRICE_LABLE["bg"] = LABLE_BG_COLORS
        
        PRICE_LABLE["font"] = LABLE_FONT
        PRICE_LABLE["fg"] = LABLE_FONT_COLOR
        PRICE_LABLE["justify"] = "center"
        PRICE_LABLE["text"] = "Price "
        PRICE_LABLE.place(x=20,y=190,width=163,height=30)

        QUANTITY_LABLE=tk.Label(root)
        QUANTITY_LABLE["bg"] = LABLE_BG_COLORS
        
        QUANTITY_LABLE["font"] = LABLE_FONT
        QUANTITY_LABLE["fg"] = LABLE_FONT_COLOR
        QUANTITY_LABLE["justify"] = "center"
        QUANTITY_LABLE["text"] = "Quantity "
        QUANTITY_LABLE.place(x=20,y=230,width=164,height=30)

        self.CODE_ENTRY=tk.Entry(root)
        self.CODE_ENTRY["borderwidth"] = "1px"
        self.CODE_ENTRY["font"] = LABLE_FONT
        self.CODE_ENTRY["fg"] = "#333333"
        self.CODE_ENTRY["justify"] = "center"
        self.CODE_ENTRY.place(x=210,y=70,width=277,height=30)

        self.Name_ENTRY=tk.Entry(root)
        self.Name_ENTRY["borderwidth"] = "1px"
        self.Name_ENTRY["font"] = LABLE_FONT
        self.Name_ENTRY["fg"] = "#333333"
        self.Name_ENTRY["justify"] = "center"
        self.Name_ENTRY.place(x=210,y=110,width=276,height=30)

        self.BRAND_ENTRY=tk.Entry(root)
        self.BRAND_ENTRY["borderwidth"] = "1px"
        self.BRAND_ENTRY["font"] = LABLE_FONT
        self.BRAND_ENTRY["fg"] = "#333333"
        self.BRAND_ENTRY["justify"] = "center"
        self.BRAND_ENTRY["text"] = ""
        self.BRAND_ENTRY.place(x=210,y=150,width=278,height=30)

        self.PRICE_ENTRY=tk.Entry(root)
        self.PRICE_ENTRY["borderwidth"] = "1px"
        self.PRICE_ENTRY["font"] = LABLE_FONT
        self.PRICE_ENTRY["fg"] = "#333333"
        self.PRICE_ENTRY["justify"] = "center"
        self.PRICE_ENTRY["text"] = ""
        self.PRICE_ENTRY.place(x=210,y=190,width=278,height=30)

        self.QUANTITY_ENTRY=tk.Entry(root)
        self.QUANTITY_ENTRY["borderwidth"] = "1px"
        self.QUANTITY_ENTRY["font"] = LABLE_FONT
        self.QUANTITY_ENTRY["fg"] = "#333333"
        self.QUANTITY_ENTRY["justify"] = "center"
        self.QUANTITY_ENTRY["text"] = ""
        self.QUANTITY_ENTRY.place(x=210,y=230,width=279,height=30)

        OK_BUTTON=tk.Button(root)
        OK_BUTTON["bg"] = OK_BUTTON_BG_COLORS
        OK_BUTTON["font"] = BUTTON_FONT
        OK_BUTTON["fg"] = "#000000"
        OK_BUTTON["justify"] = "center"
        OK_BUTTON["text"] = "OK"
        OK_BUTTON.place(x=470,y=280,width=74,height=37)
        OK_BUTTON["command"] = self.OK_BUTTON_command

        CANCEL_BUTTON=tk.Button(root)
        CANCEL_BUTTON["bg"] = CANCLE_BUTTON_BG_COLORS
        CANCEL_BUTTON["font"] = BUTTON_FONT
        CANCEL_BUTTON["fg"] = "#000000"
        CANCEL_BUTTON["justify"] = "center"
        CANCEL_BUTTON["text"] = "CANCEL"
        CANCEL_BUTTON.place(x=330,y=280,width=130,height=36)
        CANCEL_BUTTON["command"] = self.CANCEL_BUTTON_command

    def OK_BUTTON_command(self):
        PRODUCT_CODE = self.CODE_ENTRY.get()
        PRODUCT_NAME = self.Name_ENTRY.get()
        BRAND        = self.BRAND_ENTRY.get()
        PRICE        = self.PRICE_ENTRY.get()
        QUANTITY     = self.QUANTITY_ENTRY.get()
        
        insert_data(PRODUCT_CODE, PRODUCT_NAME, BRAND, PRICE, QUANTITY)
        self.window.destroy()

    def CANCEL_BUTTON_command(self):
        self.window.destroy()
        

def main():
# if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

# main()