import customtkinter as ctk
from tkinter import Canvas, filedialog
from PIL import Image, ImageTk
import os

def FileSelect(parent):

    # grid
    FileSelectFrame = ctk.CTkFrame(parent, fg_color = '#222222')
    FileSelectFrame.rowconfigure((0,1,2,3,4), weight = 1)
    FileSelectFrame.columnconfigure(0, weight = 2)
    FileSelectFrame.columnconfigure(1, weight = 1)

    # widgets
    Pack_exportLabel = ctk.CTkLabel(FileSelectFrame, text = 'Pack Export\nName')
    Pack_exportEntry = ctk.CTkEntry(FileSelectFrame)
    Localization_ent = ctk.CTkEntry(FileSelectFrame)
    Default_all_btn = ctk.CTkButton(FileSelectFrame, text = 'DEF all')
    Skin_SelectLabel = ctk.CTkLabel(FileSelectFrame, text = 'Select Skin')
    Skin_select_menu = ctk.CTkOptionMenu(FileSelectFrame, values = ['Select File'])
    Cape_SelectLabel = ctk.CTkLabel(FileSelectFrame, text = 'Select Cape')
    Cape_select_menu = ctk.CTkOptionMenu(FileSelectFrame, values = ['Select File'])
    
    # placement
    Pack_exportLabel.grid(row = 0, column = 1, sticky = 'w', padx = 10)
    Pack_exportEntry.grid(row = 0, column = 0, sticky = 'ew')
    Localization_ent.grid(row = 2, column = 0, sticky = 'ew')
    Default_all_btn.grid(row = 4, column = 0)
    Skin_SelectLabel.grid(row = 1, column = 1, sticky = 's')
    Skin_select_menu.grid(row = 2, column = 1, sticky = 'n')
    Cape_SelectLabel.grid(row = 3, column = 1, sticky = 's')
    Cape_select_menu.grid(row = 4, column = 1, sticky = 'n')
    FileSelectFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = .5)

def ExportControls(parent):
    
    # grid
    ExportControlsFrame = ctk.CTkFrame(parent, fg_color = '#191919')
    ExportControlsFrame.rowconfigure((0,1,2), weight = 1)
    ExportControlsFrame.columnconfigure((0,1), weight = 1)
    
    # widgets
    OutputLabel = ctk.CTkLabel(ExportControlsFrame, text = 'Output Label')
    AddButton = ctk.CTkButton(ExportControlsFrame, text = 'Add', fg_color = '#10b409', hover_color = '#077d02')
    ExportButton = ctk.CTkButton(ExportControlsFrame, text = 'Export', fg_color = '#c61d1d', hover_color = '#830d0d')
    Export_PATHEntry = ctk.CTkEntry(ExportControlsFrame)
    
    # placement
    OutputLabel.grid(row = 0, column = 0, columnspan = 2)
    AddButton.grid(row = 1, column = 0)
    ExportButton.grid(row = 1, column = 1)
    Export_PATHEntry.grid(row = 2, column = 0, columnspan = 2)
    ExportControlsFrame.place(relx = 0, rely = .5, relwidth = 1, relheight = .5)

def FileOutput(parent):

    # grid
    FileOutputFrame = ctk.CTkFrame(parent)
    FileOutputFrame.rowconfigure((0,1), weight = 1, uniform = 'a')
    FileOutputFrame.columnconfigure((0,1), weight = 1, uniform = 'a')
    
    # widgets
    Current_SkinLabel = ctk.CTkLabel(FileOutputFrame, text = 'Current\nSkin', fg_color = '#292929', text_color = 'white')
    Current_CapeLabel = ctk.CTkLabel(FileOutputFrame, text = 'Current\nCape', fg_color = '#292929', text_color = 'white')
    Skin_Folder_SelectButton = ctk.CTkButton(FileOutputFrame, text = 'Skin\nFolder\nSelect', fg_color = '#d35e0a', hover_color = '#934005')
    Cape_Folder_SelectButton = ctk.CTkButton(FileOutputFrame, text = 'Cape\nFolder\nSelect', fg_color = '#d35e0a', hover_color = '#934005')
    
    # placement
    Current_SkinLabel.grid(row = 0, column = 0, sticky = 'news', padx = 10, pady = 10)
    Current_CapeLabel.grid(row = 1, column = 0, sticky = 'news', padx = 10, pady = 10)
    Skin_Folder_SelectButton.grid(row = 0, column = 1, sticky = 'news', padx = 10, pady = 10)
    Cape_Folder_SelectButton.grid(row = 1, column = 1, sticky = 'news', padx = 10, pady = 10)
    FileOutputFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)