import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from database import fech_data

class App:
    def __init__(self, root):
        # ----------------------------------------------------------------------------------- #
        #                                     HEADING COLOR                                   #
        HEADING_BG_COLOR = "#1e9fff"
        HEADING_FG_COLOR = "#fad400"
        
        # ----------------------------------------------------------------------------------- #
        #                                     HEADING SIZE                                    #
        HEADING_WIDTH    = 1170
        HEADING_HEIGHT   = 51
        
        
        # ----------------------------------------------------------------------------------- #
        #                                   FONT SIZE AND FAMILY                              #
        FONT_SIZE        = 34
        FONT_FAMILY      = 'Times'
        HEADING_FONT     = tkFont.Font(family=FONT_FAMILY,size=FONT_SIZE)
        
        # ----------------------------------------------------------------------------------- #
        #                                   DATABASE VIEW POSITION                            #
        POSITION_X       = 10
        POSITION_Y       = 60
        DATA_VIEW_WIDTH  = 1148
        DATA_VIEW_HEIGHT = 460
        
        
        # ----------------------------------------------------------------------------------- #
        #                                       SCREEN SIZE 0                                  #
        SCREEN_WIDTH     = 1171
        SCREEN_HEIGHT    = 532
        
        # ----------------------------------------------------------------------------------- #
        #                                        VIEW HEADERS                                 #
        VIEW_HEADING    = ('SL', 'PRODUCT_CODE', 'PROCUCT_NAME', 'BRAND', 'PRICE', 'QUANTITY')
        
        root.title("Cloven Fashion - View Product")
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
                
        TREE_VIEW = ttk.Treeview(root, columns=VIEW_HEADING, show='headings')
        TREE_VIEW.heading('SL', text='SL')
        TREE_VIEW.heading('PRODUCT_CODE', text='PRODUCT CODE')
        TREE_VIEW.heading('PROCUCT_NAME', text='PROCUCT NAME')        
        TREE_VIEW.heading('BRAND', text='BRAND')        
        TREE_VIEW.heading('PRICE', text='PRICE')        
        TREE_VIEW.heading('QUANTITY', text='QUANTITY') 
        TREE_VIEW.place(x=POSITION_X, y=POSITION_Y, width=DATA_VIEW_WIDTH, height=DATA_VIEW_HEIGHT)
    
        SCROLL_BAR_X = tk.Scrollbar(TREE_VIEW, orient='horizontal', command=TREE_VIEW.xview)
        SCROLL_BAR_X.pack(side='bottom', fill='x')
        
        index = 1
        
        data = fech_data()
        for row in data:
            self.productCode = row[0]
            self.productName = row[1]
            self.productBrand = row[2]
            self.productPrice = row[3]
            self.productQuantity = row[4]
            TREE_VIEW.insert("", tk.END, values=(index, self.productCode, self.productName, self.productBrand, self.productPrice, self.productQuantity))
            
            index += 1
        
        SCROLL_BAR_Y = tk.Scrollbar(TREE_VIEW, orient='vertical', command=TREE_VIEW.yview)
        SCROLL_BAR_Y.pack(side='right', fill='y')
        

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

# main()