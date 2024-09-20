import customtkinter as ctk
from tkinter import Canvas, filedialog, ttk
from PIL import Image, ImageTk
import os

class Layout(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # layout
        self.settings_control = ctk.CTkFrame(parent)
        self.folder_output = ctk.CTkFrame(parent)

        # data/variable
        self.entries = []
        self.localization_name = ctk.StringVar(value = '')
        
        # initializers
        self.FileSelect()
        self.ExportControls()
        self.FileOutput()

        # placement
        self.settings_control.place(relx = 0, rely = 0, relwidth = .4, relheight = 1)
        self.folder_output.place(relx = .4, rely = 0, relwidth = .6, relheight = 1)

    def FileSelect(self):
        # grid
        FileSelectFrame = ctk.CTkFrame(self.settings_control, fg_color = '#222222')
        FileSelectFrame.rowconfigure((0,1,2,3,4), weight = 1)
        FileSelectFrame.columnconfigure(0, weight = 2)
        FileSelectFrame.columnconfigure(1, weight = 1)

        # widgets
        self.Pack_exportLabel = ctk.CTkLabel(FileSelectFrame, text = 'Pack Export\nName')
        self.Pack_exportEntry = ctk.CTkEntry(FileSelectFrame, placeholder_text = 'Enter Skinpack Name')
        self.LocalizationLabel = ctk.CTkLabel(FileSelectFrame, text = 'Skin Name')
        self.Localization_ent = ctk.CTkEntry(FileSelectFrame)
        self.DeleteLast_btn = ctk.CTkButton(FileSelectFrame, text = 'Del Previous', command = self.listview)
        self.Skin_SelectLabel = ctk.CTkLabel(FileSelectFrame, text = 'Select Skin')
        self.Skin_select_menu = ctk.CTkOptionMenu(FileSelectFrame, values = ['Select File'], command = lambda event: self.skinupdateview() if self.Skin_select_menu.get() != 'Select File' else print('Please select a folder with your skin file(s)'))
        self.Cape_SelectLabel = ctk.CTkLabel(FileSelectFrame, text = 'Select Cape')
        self.Cape_select_menu = ctk.CTkOptionMenu(FileSelectFrame, values = ['Select File', 'None'], command = lambda event: self.capeupdateview() if self.Cape_select_menu.get() != 'Select File' else print('Please select a folder with your cape file(s)'))

        # placement
        self.Pack_exportLabel.grid(row = 0, column = 1, sticky = 'w', padx = 10)
        self.Pack_exportEntry.grid(row = 0, column = 0, sticky = 'ew')
        self.LocalizationLabel.grid(row = 1, column = 0, sticky = 's')
        self.Localization_ent.grid(row = 2, column = 0, sticky = 'ew')
        self.DeleteLast_btn.grid(row = 4, column = 0)
        self.Skin_SelectLabel.grid(row = 1, column = 1, sticky = 's')
        self.Skin_select_menu.grid(row = 2, column = 1, sticky = 'n')
        self.Cape_SelectLabel.grid(row = 3, column = 1, sticky = 's')
        self.Cape_select_menu.grid(row = 4, column = 1, sticky = 'n')
        FileSelectFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = .5)

    def ExportControls(self):
        # grid
        ExportControlsFrame = ctk.CTkFrame(self.settings_control, fg_color = '#191919')
        ExportControlsFrame.rowconfigure((0,1,2), weight = 1)
        ExportControlsFrame.columnconfigure((0,1), weight = 1)

        # widgets
        OutputLabel = ctk.CTkLabel(ExportControlsFrame, text = 'Output Label')
        AddButton = ctk.CTkButton(ExportControlsFrame, text = 'Add', fg_color = '#10b409', hover_color = '#077d02', command = self.addskin)
        ExportButton = ctk.CTkButton(ExportControlsFrame, text = 'Export', fg_color = '#c61d1d', hover_color = '#830d0d', command = self.listview)
        Export_PATHEntry = ctk.CTkEntry(ExportControlsFrame)
        ExportPATH_SelectButton = ctk.CTkButton(ExportControlsFrame, text = 'Select EXP Path')

        # placement
        OutputLabel.grid(row = 0, column = 0, columnspan = 2)
        AddButton.grid(row = 1, column = 0)
        ExportButton.grid(row = 1, column = 1)
        Export_PATHEntry.grid(row = 2, column = 0, sticky = 'ews', pady = 15)
        ExportPATH_SelectButton.grid(row = 2, column = 1, sticky = 'ws', padx = 10, pady = 15)
        ExportControlsFrame.place(relx = 0, rely = .5, relwidth = 1, relheight = .5)

    def FileOutput(self):
        # grid
        self.FileOutputFrame = ctk.CTkFrame(self.folder_output)
        self.FileOutputFrame.rowconfigure((0,1), weight = 1, uniform = 'a')
        self.FileOutputFrame.columnconfigure((0,1), weight = 1, uniform = 'a')

        # widgets
        self.Current_Skin = ctk.CTkLabel(self.FileOutputFrame, text = 'Current\nSkin', fg_color = '#292929', text_color = 'white')
        self.Current_Cape = ctk.CTkLabel(self.FileOutputFrame, text = 'Current\nCape', fg_color = '#292929', text_color = 'white')
        Skin_Folder_SelectButton = ctk.CTkButton(self.FileOutputFrame, text = 'Skin\nFolder\nSelect', fg_color = '#d35e0a', hover_color = '#934005', command = self.SkinFileSelect)
        Cape_Folder_SelectButton = ctk.CTkButton(self.FileOutputFrame, text = 'Cape\nFolder\nSelect', fg_color = '#d35e0a', hover_color = '#934005', command = self.CapeFileSelect)

        # placement
        self.Current_Skin.grid(row = 0, column = 0, sticky = 'news', padx = 10, pady = 10)
        self.Current_Cape.grid(row = 1, column = 0, sticky = 'news', padx = 10, pady = 10)
        Skin_Folder_SelectButton.grid(row = 0, column = 1, sticky = 'news', padx = 10, pady = 10)
        Cape_Folder_SelectButton.grid(row = 1, column = 1, sticky = 'news', padx = 10, pady = 10)
        self.FileOutputFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    def SkinFileSelect(self):
        self.SkinPATH = filedialog.askdirectory()
        self.SkinRecord = [x for x in os.listdir(self.SkinPATH)]
        if self.SkinRecord:
            self.Skins = [x if len(x)<13 else x[:10] + '...' for x in os.listdir(self.SkinPATH)]
            self.Skin_select_menu.configure(values = self.Skins)
        else:
            self.Skin_select_menu.configure(values = ['Select File'])
            print('The file you selected is empty')

    def CapeFileSelect(self):
        try:
            self.CapePATH = filedialog.askdirectory()
            self.CapeRecord = [x for x in os.listdir(self.CapePATH)]
            if self.CapeRecord:
                self.Capes = ['None'] + [x if len(x)<13 else x[:10] + '...' for x in os.listdir(self.CapePATH)]
                self.Cape_select_menu.configure(values = self.Capes)
            else:
                self.Cape_select_menu.configure(values = ['Select File', 'None'])
                print('The file you selected is empty')
        except:
            self.Cape_select_menu.configure(values = ['Select File', 'None'])
            print(self.CapePATH if self.CapePATH else '[NONE SELECTED]' + ' is not a directory')

    def skinupdateview(self, *args):
        try:
            self.SkinImage = Image.open(self.SkinPATH + '/' + self.SkinRecord[self.Skins.index(self.Skin_select_menu.get())])
            self.SkinImageRatio = self.SkinImage.size[0] / self.SkinImage.size[1]
            self.SkinImageTk = ImageTk.PhotoImage(self.SkinImage)
            self.Current_Skin.grid_forget()
            self.Current_Skin = Canvas(self.FileOutputFrame, bd = 0, highlightthickness = 0, relief = 'ridge')
            self.Current_Skin.grid(row = 0, column = 0, sticky = 'news', padx = 10, pady = 10)
            self.Current_Skin.create_image(1, 1, anchor = 'nw', image = self.SkinImageTk)
            self.Current_Skin.bind('<Configure>', self.no_sliceskin)
        except:
            print('This file is not an image/minecraft-skin')
            
    def capeupdateview(self, *args):
        if self.Cape_select_menu.get() == 'None':
            self.Current_Cape.unbind('<Configure>', None)
            self.Current_Cape.grid_forget()
            self.Current_Cape = ctk.CTkLabel(self.FileOutputFrame, text = 'Selected\nNo Cape', fg_color = '#292929', text_color = 'white')
            self.Current_Cape.grid(row = 1, column = 0, sticky = 'news', padx = 10, pady = 10)
        else:
            try:
                self.CapeImage = Image.open(self.CapePATH + '/' + self.CapeRecord[self.Capes.index(self.Cape_select_menu.get()) - 1])
                self.CapeImageRatio = self.CapeImage.size[0] / self.CapeImage.size[1]
                self.CapeImageTk = ImageTk.PhotoImage(self.CapeImage)
                self.Current_Cape.grid_forget()
                self.Current_Cape = Canvas(self.FileOutputFrame, bd = 0, highlightthickness = 0, relief = 'ridge')
                self.Current_Cape.grid(row = 1, column = 0, sticky = 'news', padx = 10, pady = 10)
                self.Current_Cape.create_image(1, 1, anchor = 'nw', image = self.CapeImageTk)
                self.Current_Cape.bind('<Configure>', self.no_slicecape)
            except:
                print('This file is not an image/minecraft-cape')
        
    def no_sliceskin(self, event):
        global skinresized_tk
        canvas_ratio = event.width / event.height

        if canvas_ratio > self.SkinImageRatio:
            self.skinheight = int(event.height)
            self.skinwidth = int(self.skinheight * self.SkinImageRatio)
        else:
            self.skinwidth = int(event.width)
            self.skinheight = int(self.skinwidth / self.SkinImageRatio)
        
        self.Current_Skin.delete('all')
        resized_image = self.SkinImage.resize((self.skinwidth, self.skinheight))
        skinresized_tk = ImageTk.PhotoImage(resized_image)
        self.Current_Skin.create_image(int(event.width / 2), int(event.height / 2), anchor = 'center', image = skinresized_tk)
    
    def no_slicecape(self, event):
        global caperesized_tk
        canvas_ratio = event.width / event.height

        if canvas_ratio > self.CapeImageRatio:
            self.capeheight = int(event.height)
            self.capewidth = int(self.capeheight * self.CapeImageRatio)
        else:
            self.capewidth = int(event.width)
            self.capeheight = int(self.capewidth / self.CapeImageRatio)
        
        self.Current_Cape.delete('all')
        resized_image = self.CapeImage.resize((self.capewidth, self.capeheight))
        caperesized_tk = ImageTk.PhotoImage(resized_image)
        self.Current_Cape.create_image(int(event.width / 2), int(event.height / 2), anchor = 'center', image = caperesized_tk)
    
    def addskin(self):
        if self.Skin_select_menu.get() == 'Select File' and self.Cape_select_menu.get() == 'Select File':
            print('This program is not magic, please select your folders and choose your cape and/or skin') 
        elif self.Skin_select_menu.get() == 'Select File':
            print('Please select a skin file from a folder')
        elif self.Cape_select_menu.get() == 'Select File':
            print('Please select "None" or a cape file from a folder')
        else: 
            self.entries.append({
                'Name': self.Localization_ent.get() if self.Localization_ent.get() != '' else self.SkinRecord[self.Skins.index(self.Skin_select_menu.get())].split('.')[0] + ('None' if self.Cape_select_menu.get() == 'None' else self.CapeRecord[self.Capes.index(self.Cape_select_menu.get()) - 1].split('.')[0]),
                'Skin': self.SkinPATH + '/' + self.SkinRecord[self.Skins.index(self.Skin_select_menu.get())], 
                'Cape': (self.CapePATH + '/' + self.CapeRecord[self.Capes.index(self.Cape_select_menu.get()) - 1]) if self.Cape_select_menu.get() != 'None' else 'None'})
    
    def deleteprev(self):
        if self.entries:
            del self.entries[-1]
        else:
            print('You have added no entries into the skinpack')
    
    def listview(self):
        self.viewthing = ctk.CTk()
        self.viewthing.title('Windowthing')
        self.viewthing.resizable(False, False)
        self.viewthing.geometry('750x500')
        self.entrylist = ttk.Treeview(self.viewthing, columns = ('Skin-Name', 'Skin-img', 'Cape-img'), show = 'headings')
        self.entrylist.heading('Skin-Name', text = 'Skin-Name')
        self.entrylist.heading('Skin-img', text = 'Skin-img')
        self.entrylist.heading('Cape-img', text = 'Cape-img')
        self.entrylist.pack(fill = 'both', expand = True)

        for x in self.entries:
            self.entrylist.insert(parent = '', index = ctk.END, values = (x['Name'], x['Skin'], x['Cape']))

        self.closeandsave = ctk.CTkLabel(self.viewthing, text = "Press ESC to exit and save changes (only works if you're focused on this window)")
        self.closeandsave.pack()

        self.viewthing.bind_all('<Escape>', lambda event: self.contents())

        self.viewthing.mainloop()
    
    def contents(self):
        for x in self.entrylist.get_children():
            print(self.entrylist.item(x)['values'])
        self.viewthing.destroy()
