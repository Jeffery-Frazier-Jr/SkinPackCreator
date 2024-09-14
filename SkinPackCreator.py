import customtkinter as ctk
from Widgets import *
from Frames import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1500x800')
        self.minsize(750,400)
        self.title('SkinPackCreator')

        # main layout
        settings_control = Frame(self, 0, 0, .4, 1)
        folder_output = Frame(self, .4, 0, .6, 1)

        # settings layout
        # file_selection = Frame(settings_control, 0, 0, 1, .5, 'white')       # panels
        FileSelect(settings_control).place(relx = 0, rely = 0, relwidth = 1, relheight = .5)
        # export_controls = Frame(settings_control, 0, .5, 1, .5, 'pink')
        ExportControls(settings_control).place(relx = 0, rely = .5, relwidth = 1, relheight = .5)
        
        # export_controls.rowconfigure((0,1,2), weight = 1, uniform = 'b')
        # export_controls.columnconfigure((0,1), weight = 1, uniform = 'b')

        # Entry(file_selection, 0, 0)
        # Label(file_selection, 'PackExpName', 0, 1)
        # Entry(file_selection, 1, 0)
        # DropMenu(file_selection, 1 , 1, ['This', 'is', 'a', 'test'])
        # Button(file_selection, 2, 0, 'DEF all')
        # DropMenu(file_selection, 2, 1, ['More', 'or', 'less', 'know'])

        # File view & Folder select frame
        folder_output.rowconfigure((0,1), weight = 1, uniform = 'a')         # grid
        folder_output.columnconfigure((0,1), weight = 1, uniform = 'a')
        
        Label(folder_output, 'Current\nSkin', 0, 0, 'white', 'black')        # widgets
        Label(folder_output, 'Skin\nFolder\nSelect', 0, 1, 'red', 'black')
        Label(folder_output, 'Current\nCape', 1, 0, 'yellow', 'black')
        Label(folder_output, 'Cape\nFolder\nSelect', 1, 1, 'blue', 'black')

        # run
        self.mainloop()

App()