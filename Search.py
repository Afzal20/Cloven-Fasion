import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from database import search_data


class App:
    def __init__(self, root):
        self.CODE_CHEAKBOX_CLICK = 0
        self.BRAND_CHEAKBOX_CLICK = 0
        self.PRICE_CHEAKBOX_CLICK = 0
        self.NAME_CHEAKBOX_CLICK = 0
        
        
        OK_BUTTON_BG_COLORS     = "#01aaed"

        # ----------------------------------------------------------------------------------- #
        #                                     HEADING COLOR                                   #
        HEADING_BG_COLOR = "#1e9fff"
        HEADING_FG_COLOR = "#fad400"
        
        # ----------------------------------------------------------------------------------- #
        #                                     HEADING SIZE                                    #
        HEADING_WIDTH    = 870
        HEADING_HEIGHT   = 51
        
        
        # ----------------------------------------------------------------------------------- #
        #                                   FONT SIZE AND FAMILY                              #
        FONT_SIZE        = 34
        FONT_FAMILY      = 'Times'
        HEADING_FONT     = tkFont.Font(family=FONT_FAMILY,size=FONT_SIZE)
        LABLE_FONT   = tkFont.Font(family='Times',size=16)
        BUTTON_FONT  = tkFont.Font(family='Times',size=22)


        
        # ----------------------------------------------------------------------------------- #
        #                                   DATABASE VIEW POSITION                            #
        POSITION_X       = 20
        POSITION_Y       = 180
        DATA_VIEW_WIDTH  = 831
        DATA_VIEW_HEIGHT = 300
        
        
        # ----------------------------------------------------------------------------------- #
        #                                       SCREEN SIZE                                   #
        SCREEN_WIDTH     = 871
        SCREEN_HEIGHT    = 532
        
        # ----------------------------------------------------------------------------------- #
        #                           CHEAKBOX FONT SIZE, FAMILY AND COLOR                      #
                
        # ----------------------------------------------------------------------------------- #
        #                                        VIEW HEADERS                                 #
        VIEW_HEADING    = ('SL', 'PRODUCT_CODE', 'PROCUCT_NAME', 'BRAND', 'PRICE', 'QUANTITY')
        
        CHEAKBOX_FONT_FAMILY = 'Times'
        CHEAKBOX_FONT_SIZE   = 14
        CHEAKBOX_FONT        = tkFont.Font(family= CHEAKBOX_FONT_FAMILY,size=CHEAKBOX_FONT_SIZE)
        
        
        root.title("Cloven Fashion - Search Product")
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (SCREEN_WIDTH, SCREEN_HEIGHT, (screenwidth - SCREEN_WIDTH) / 2, (screenheight - SCREEN_HEIGHT) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        TOPLABLE = tk.Label(root)
        TOPLABLE["bg"] = HEADING_BG_COLOR
        TOPLABLE["font"] = HEADING_FONT
        TOPLABLE["fg"] = HEADING_FG_COLOR
        TOPLABLE["justify"] = "center"
        TOPLABLE["text"] = "CLOVEN FASHION"
        TOPLABLE["relief"] = "ridge"
        TOPLABLE.place(x=0,y=0,width=HEADING_WIDTH,height=HEADING_HEIGHT)

        SEARCH_BY_NAME_CHEAKBOX=tk.Checkbutton(root)
        SEARCH_BY_NAME_CHEAKBOX["font"] = CHEAKBOX_FONT
        SEARCH_BY_NAME_CHEAKBOX["fg"] = "#333333"
        SEARCH_BY_NAME_CHEAKBOX["justify"] = "center"
        SEARCH_BY_NAME_CHEAKBOX["text"] = "Name"
        SEARCH_BY_NAME_CHEAKBOX["offvalue"] = "0"
        SEARCH_BY_NAME_CHEAKBOX["onvalue"] = "1"
        SEARCH_BY_NAME_CHEAKBOX.place(x=330,y=70,width=70,height=25)
        SEARCH_BY_NAME_CHEAKBOX["command"] = self.SEARCH_BY_NAME_CHEAKBOX_command

        SEARCH_BY_CODE_CHEAKBOX=tk.Checkbutton(root)
        SEARCH_BY_CODE_CHEAKBOX["font"] = CHEAKBOX_FONT
        SEARCH_BY_CODE_CHEAKBOX["fg"] = "#333333"
        SEARCH_BY_CODE_CHEAKBOX["justify"] = "center"
        SEARCH_BY_CODE_CHEAKBOX["text"] = "Code"
        SEARCH_BY_CODE_CHEAKBOX.place(x=470,y=70,width=70,height=25)
        SEARCH_BY_CODE_CHEAKBOX["offvalue"] = "0"
        SEARCH_BY_CODE_CHEAKBOX["onvalue"] = "1"
        SEARCH_BY_CODE_CHEAKBOX["command"] = self.SEARCH_BY_CODE_CHEAKBOX_command

        SEARCH_BY_BRAND_CHEAKBOX=tk.Checkbutton(root)
        SEARCH_BY_BRAND_CHEAKBOX["font"] = CHEAKBOX_FONT
        SEARCH_BY_BRAND_CHEAKBOX["fg"] = "#333333"
        SEARCH_BY_BRAND_CHEAKBOX["justify"] = "center"
        SEARCH_BY_BRAND_CHEAKBOX["text"] = "Brand"
        SEARCH_BY_BRAND_CHEAKBOX.place(x=600,y=70,width=70,height=25)
        SEARCH_BY_BRAND_CHEAKBOX["offvalue"] = "0"
        SEARCH_BY_BRAND_CHEAKBOX["onvalue"] = "1"
        SEARCH_BY_BRAND_CHEAKBOX["command"] = self.SEARCH_BY_BRAND_CHEAKBOX_command

        SEARCH_BY_PRICE_CHEAKBOX=tk.Checkbutton(root)
        SEARCH_BY_PRICE_CHEAKBOX["font"] = CHEAKBOX_FONT
        SEARCH_BY_PRICE_CHEAKBOX["fg"] = "#333333"
        SEARCH_BY_PRICE_CHEAKBOX["justify"] = "center"
        SEARCH_BY_PRICE_CHEAKBOX["text"] = "Price"
        SEARCH_BY_PRICE_CHEAKBOX.place(x=740,y=70,width=70,height=25)
        SEARCH_BY_PRICE_CHEAKBOX["offvalue"] = "0"
        SEARCH_BY_PRICE_CHEAKBOX["onvalue"] = "1"
        SEARCH_BY_PRICE_CHEAKBOX["command"] = self.SEARCH_BY_PRICE_CHEAKBOX_command

        ENTRY_TEXT=tk.Label(root)
        ENTRY_TEXT["bg"] = "#3b4155"
        ENTRY_TEXT["font"] = CHEAKBOX_FONT
        ENTRY_TEXT["fg"] = "#ffffff"
        ENTRY_TEXT["justify"] = "center"
        ENTRY_TEXT["text"] = "Search By"
        ENTRY_TEXT.place(x=20,y=70,width=271,height=30)
        
        ENTRY_TEXT=tk.Label(root)
        ENTRY_TEXT["bg"] = "#3b4155"
        ENTRY_TEXT["font"] = CHEAKBOX_FONT
        ENTRY_TEXT["fg"] = "#ffffff"
        ENTRY_TEXT["justify"] = "center"
        ENTRY_TEXT["text"] = "Enetr Texts"
        ENTRY_TEXT.place(x=20,y=120,width=271,height=30)
        
        self.NAME_ENTRY=tk.Entry(root)
        self.NAME_ENTRY["borderwidth"] = "1px"
        self.NAME_ENTRY["font"] = LABLE_FONT
        self.NAME_ENTRY["fg"] = "#333333"
        self.NAME_ENTRY["justify"] = "center"
        
        self.CODE_ENTRY=tk.Entry(root)
        self.CODE_ENTRY["borderwidth"] = "1px"
        self.CODE_ENTRY["font"] = LABLE_FONT
        self.CODE_ENTRY["fg"] = "#333333"
        self.CODE_ENTRY["justify"] = "center"
        
        self.BRAND_ENTRY=tk.Entry(root)
        self.BRAND_ENTRY["borderwidth"] = "1px"
        self.BRAND_ENTRY["font"] = LABLE_FONT
        self.BRAND_ENTRY["fg"] = "#333333"
        self.BRAND_ENTRY["justify"] = "center"
        
        self.PRICE_ENTRY=tk.Entry(root)
        self.PRICE_ENTRY["borderwidth"] = "1px"
        self.PRICE_ENTRY["font"] = LABLE_FONT
        self.PRICE_ENTRY["fg"] = "#333333"
        self.PRICE_ENTRY["justify"] = "center"
        
        self.TREE_VIEW = ttk.Treeview(root, columns=VIEW_HEADING, show='headings')
        self.TREE_VIEW.heading('SL', text='SL')
        self.TREE_VIEW.heading('PRODUCT_CODE', text='PRODUCT CODE')
        self.TREE_VIEW.heading('PROCUCT_NAME', text='PROCUCT NAME')        
        self.TREE_VIEW.heading('BRAND', text='BRAND')        
        self.TREE_VIEW.heading('PRICE', text='PRICE')        
        self.TREE_VIEW.heading('QUANTITY', text='QUANTITY') 
        self.TREE_VIEW.place(x=POSITION_X, y=POSITION_Y, width=DATA_VIEW_WIDTH, height=DATA_VIEW_HEIGHT)
    
        SCROLL_BAR_X = tk.Scrollbar(self.TREE_VIEW, orient='horizontal', command=self.TREE_VIEW.xview)
        SCROLL_BAR_X.pack(side='bottom', fill='x')
        
        SCROLL_BAR_Y = tk.Scrollbar(self.TREE_VIEW, orient='vertical', command=self.TREE_VIEW.yview)
        SCROLL_BAR_Y.pack(side='right', fill='y')
        
        FIND_BUTTON = tk.Button(root)
        FIND_BUTTON["bg"] = OK_BUTTON_BG_COLORS
        FIND_BUTTON["font"] = BUTTON_FONT
        FIND_BUTTON["fg"] = "#000000"
        FIND_BUTTON["justify"] = "center"
        FIND_BUTTON["text"] = "Find"
        FIND_BUTTON.place(x=740,y=480,width=89,height=30)
        FIND_BUTTON["command"] = self.FIND_BUTTON_command
        
    
    def SEARCH_BY_NAME_CHEAKBOX_command(self):
        self.NAME_CHEAKBOX_CLICK += 1
        if self.NAME_CHEAKBOX_CLICK % 2 == 1:
            self.NAME_ENTRY.place(x=330,y=120,width=100,height=30)
            n_cmd = "SEARCH_BY_NAME"
        elif self.NAME_CHEAKBOX_CLICK % 2 == 0:
            self.NAME_ENTRY.place(x=330, y=120, width=0,height=0)
            n_cmd = ""
        return n_cmd
        
        
    def SEARCH_BY_CODE_CHEAKBOX_command(self):
        self.CODE_CHEAKBOX_CLICK += 1
        if self.CODE_CHEAKBOX_CLICK % 2 == 1:
            self.CODE_ENTRY.place(x=470,y=120,width=100,height=30)
            c_cmd = "SEARCH_BY_CODE"
        elif self.CODE_CHEAKBOX_CLICK % 2 == 0:
            self.CODE_ENTRY.place(x=470, y=120, width=0, height=0)
            c_cmd = ""
        return c_cmd


    def SEARCH_BY_BRAND_CHEAKBOX_command(self):
        self.BRAND_CHEAKBOX_CLICK += 1
        if self.BRAND_CHEAKBOX_CLICK % 2 == 1:
            self.BRAND_ENTRY.place(x=600,y=120,width=100,height=30)
            b_cmd = "SEARCH_BY_BRAND"
        elif self.BRAND_CHEAKBOX_CLICK % 2 == 0:
            self.BRAND_ENTRY.place(x=600,y=120,width=0,height=0)
            b_cmd = ""
        return b_cmd


    def SEARCH_BY_PRICE_CHEAKBOX_command(self):
        self.PRICE_CHEAKBOX_CLICK += 1
        if self.PRICE_CHEAKBOX_CLICK % 2 == 1:
            self.PRICE_ENTRY.place(x=740,y=120,width=100,height=30)
            p_cmd = "SEARCH_BY_PRICE"
        elif self.PRICE_CHEAKBOX_CLICK % 2 == 0:
            self.PRICE_ENTRY.place(x=740,y=120,width=0,height=0)
            p_cmd = ""
        return p_cmd
        
        
    def FIND_BUTTON_command(self):
        for i in self.TREE_VIEW.get_children():
            self.TREE_VIEW.delete(i)
        self.PRODUCT_CODE = self.CODE_ENTRY.get()
        data = search_data(self.PRODUCT_CODE)
        # print(data)
        
        index = 1
        
        for row in data:
            self.productCode = row[0]
            self.productName = row[1]
            self.productBrand = row[2]
            self.productPrice = row[3]
            self.productQuantity = row[4]
            self.TREE_VIEW.insert("", tk.END, values=(index, self.productCode, self.productName, self.productBrand, self.productPrice, self.productQuantity))
            
            index += 1
            # self.TREE_VIEW.
        # self.TREE_VIEW.insert("", tk.END, values=(index, self.productCode, self.productName, self.productBrand, self.productPrice, self.productQuantity))
        
            
    
def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

# main()