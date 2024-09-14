import customtkinter as ctk

class FileSelect(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = '#2c2c2c')
        
        # grid
        self.rowconfigure((0,1,2), weight = 1)
        self.columnconfigure(0, weight = 2)
        self.columnconfigure(1, weight = 1)

        # widgets
        Pack_exportLabel = ctk.CTkLabel(self, text = 'Pack Export\nName')
        Pack_exportEntry = ctk.CTkEntry(self)
        Localization_ent = ctk.CTkEntry(self)
        Default_all_btn = ctk.CTkButton(self, text = 'DEF all')
        Skin_select_menu = ctk.CTkOptionMenu(self, values = ['This', 'is', 'a', 'test'])
        Cape_select_menu = ctk.CTkOptionMenu(self, values = ['More', 'or', 'less', 'know'])
        
        # placement
        Pack_exportLabel.grid(row = 0, column = 1)
        Pack_exportEntry.grid(row = 0, column = 0, sticky = 'ew')
        Localization_ent.grid(row = 1, column = 0, sticky = 'ew')
        Default_all_btn.grid(row = 2, column = 0)
        Skin_select_menu.grid(row = 1, column = 1)
        Cape_select_menu.grid(row = 2, column = 1)

class ExportControls(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = '#191919')

        # grid
        self.rowconfigure((0,1,2), weight = 1)
        self.columnconfigure((0,1), weight = 1)

        # widgets
        OutputLabel = ctk.CTkLabel(self, text = 'Output Label')
        AddButton = ctk.CTkButton(self, text = 'Add')
        ExportButton = ctk.CTkButton(self, text = 'Export')
        Export_PATHEntry = ctk.CTkEntry(self)

        # placement
        OutputLabel.grid(row = 0, column = 0, columnspan = 2)
        AddButton.grid(row = 1, column = 0)
        ExportButton.grid(row = 1, column = 1)
        Export_PATHEntry.grid(row = 2, column = 0, columnspan = 2)