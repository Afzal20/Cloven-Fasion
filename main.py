import tkinter as tk
import tkinter.font as tkFont
import Add, delete, view, Edit, Search

class App:
    def __init__(self, root):
        
        # ----------------------------------------------------------------------------------- #
        #                                   BACKGTOUND COLORS                                 #
        ADD_BUTTON_BG_COLOR    =  "#5fb878"
        DELETE_BUTTON_BG_COLOR =  "#ff5722"
        SEARCH_BUTTON_BG_COLOR =  "#00ced1"
        EDIT_BUTTON_BG_COLOR   =  "#999999"
        VIEW_BUTTON_BG_COLOR   =  "#ffd700"

        # ----------------------------------------------------------------------------------- #
        #                               BUTTON FONT SIZE AND FAMILY                           #
        FONT_SIZE    = 24
        FONT_FAMILY  = 'Times'
        BUTTON_FONT  = tkFont.Font(family=FONT_FAMILY, size=FONT_SIZE)
        HEADING_FONT = tkFont.Font(family=FONT_FAMILY,size=FONT_SIZE+10)

        # ----------------------------------------------------------------------------------- #
        #                                WINDOE TITLE AND SIZE 
        root.title("Cloven Fashion ")
        width=561
        height=332
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


        AddButton=tk.Button(root)
        AddButton["bg"] = ADD_BUTTON_BG_COLOR
        AddButton["font"] = BUTTON_FONT
        AddButton["fg"] = "#393d49"
        AddButton["justify"] = "center"
        AddButton["text"] = "Add Product"
        AddButton.place(x=110,y=60,width=345,height=41)
        AddButton["command"] = self.AddButton_command

        DeleteButton=tk.Button(root)
        DeleteButton["bg"] = DELETE_BUTTON_BG_COLOR
        DeleteButton["font"] = BUTTON_FONT
        DeleteButton["fg"] = "#393d49"
        DeleteButton["justify"] = "center"
        DeleteButton["text"] = "Delete Product"
        DeleteButton.place(x=110,y=110,width=345,height=40)
        DeleteButton["command"] = self.DeleteButton_command

        SearchButton=tk.Button(root)
        SearchButton["bg"] = SEARCH_BUTTON_BG_COLOR
        SearchButton["font"] = BUTTON_FONT
        SearchButton["fg"] = "#393d49"
        SearchButton["justify"] = "center"
        SearchButton["text"] = "Search Product"
        SearchButton.place(x=110,y=160,width=346,height=40)
        SearchButton["command"] = self.SearchButton_command

        EditButton=tk.Button(root)
        EditButton["bg"] = EDIT_BUTTON_BG_COLOR
        EditButton["font"] = BUTTON_FONT
        EditButton["fg"] = "#000000"
        EditButton["justify"] = "center"
        EditButton["text"] = "Edit Product"
        EditButton.place(x=110,y=210,width=347,height=40)
        EditButton["command"] = self.EditButton_command

        ViewButton=tk.Button(root)
        ViewButton["bg"] = VIEW_BUTTON_BG_COLOR
        ViewButton["font"] = BUTTON_FONT
        ViewButton["fg"] = "#393d49"
        ViewButton["justify"] = "center"
        ViewButton["text"] = "View Product"
        ViewButton.place(x=110,y=260,width=349,height=40)
        ViewButton["command"] = self.ViewButton_command

    def AddButton_command(self):
        Add.main()


    def DeleteButton_command(self):
        delete.main()


    def SearchButton_command(self):
        Search.main()


    def EditButton_command(self):
        Edit.main()


    def ViewButton_command(self):
        view.main()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()