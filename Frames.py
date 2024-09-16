import customtkinter as ctk
from tkinter import Canvas, filedialog
from PIL import Image, ImageTk

class FileSelect(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = '#2c2c2c')
        
        # grid
        self.rowconfigure((0,1,2,3,4), weight = 1)
        self.columnconfigure(0, weight = 2)
        self.columnconfigure(1, weight = 1)

        # widgets
        Pack_exportLabel = ctk.CTkLabel(self, text = 'Pack Export\nName')
        Pack_exportEntry = ctk.CTkEntry(self)
        Localization_ent = ctk.CTkEntry(self)
        Default_all_btn = ctk.CTkButton(self, text = 'DEF all')
        Skin_SelectLabel = ctk.CTkLabel(self, text = 'Select Skin')
        Skin_select_menu = ctk.CTkOptionMenu(self, values = ['This', 'is', 'a', 'test'])
        Cape_SelectLabel = ctk.CTkLabel(self, text = 'Select Cape')
        Cape_select_menu = ctk.CTkOptionMenu(self, values = ['More', 'or', 'less', 'know'])
        
        # placement
        Pack_exportLabel.grid(row = 0, column = 1, sticky = 'w', padx = 10)
        Pack_exportEntry.grid(row = 0, column = 0, sticky = 'ew')
        Localization_ent.grid(row = 2, column = 0, sticky = 'ew')
        Default_all_btn.grid(row = 4, column = 0)
        Skin_SelectLabel.grid(row = 1, column = 1, sticky = 's')
        Skin_select_menu.grid(row = 2, column = 1, sticky = 'n')
        Cape_SelectLabel.grid(row = 3, column = 1, sticky = 's')
        Cape_select_menu.grid(row = 4, column = 1, sticky = 'n')

class ExportControls(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = '#191919')

        # grid
        self.rowconfigure((0,1,2), weight = 1)
        self.columnconfigure((0,1), weight = 1)

        # widgets
        OutputLabel = ctk.CTkLabel(self, text = 'Output Label')
        AddButton = ctk.CTkButton(self, text = 'Add', fg_color = '#10b409', hover_color = '#077d02')
        ExportButton = ctk.CTkButton(self, text = 'Export', fg_color = '#c61d1d', hover_color = '#830d0d')
        Export_PATHEntry = ctk.CTkEntry(self)

        # placement
        OutputLabel.grid(row = 0, column = 0, columnspan = 2)
        AddButton.grid(row = 1, column = 0)
        ExportButton.grid(row = 1, column = 1)
        Export_PATHEntry.grid(row = 2, column = 0, columnspan = 2)

class FileOutput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # grid
        self.rowconfigure((0,1), weight = 1, uniform = 'a')
        self.columnconfigure((0,1), weight = 1, uniform = 'a')

        # widgets
        Current_SkinLabel = ctk.CTkLabel(self, text = 'Current\nSkin', fg_color = '#292929', text_color = 'white')
        Current_CapeLabel = ctk.CTkLabel(self, text = 'Current\nCape', fg_color = '#292929', text_color = 'white')
        Skin_Folder_SelectButton = ctk.CTkButton(self, text = 'Skin\nFolder\nSelect', fg_color = '#d35e0a', hover_color = '#934005')
        Cape_Folder_SelectButton = ctk.CTkButton(self, text = 'Cape\nFolder\nSelect', fg_color = '#d35e0a', hover_color = '#934005')

        # placement
        Current_SkinLabel.grid(row = 0, column = 0, sticky = 'news', padx = 10, pady = 10)
        Current_CapeLabel.grid(row = 1, column = 0, sticky = 'news', padx = 10, pady = 10)
        Skin_Folder_SelectButton.grid(row = 0, column = 1, sticky = 'news', padx = 10, pady = 10)
        Cape_Folder_SelectButton.grid(row = 1, column = 1, sticky = 'news', padx = 10, pady = 10)