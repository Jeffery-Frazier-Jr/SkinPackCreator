import customtkinter as ctk
from tkinter import Canvas, filedialog, ttk
from PIL import Image, ImageTk
import os
import shutil
import uuid

class Layout(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # layout
        self.settings_control = ctk.CTkFrame(parent)
        self.folder_output = ctk.CTkFrame(parent)

        # data/variables
        self.Added_Skins = []
        self.Skin_Name = ctk.StringVar(value = '')
        self.exportPATH = ctk.StringVar(value = os.getcwd().replace('\\', '/'))
        
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
        self.Pack_NameLabel = ctk.CTkLabel(FileSelectFrame, text = 'Pack Export\nName')
        self.Pack_NameEntry = ctk.CTkEntry(FileSelectFrame, placeholder_text = 'Enter Skinpack Name')
        self.Skin_NameLabel = ctk.CTkLabel(FileSelectFrame, text = 'Skin Name')
        self.Skin_NameEntry = ctk.CTkEntry(FileSelectFrame, textvariable = self.Skin_Name)
        self.DeleteButton = ctk.CTkButton(FileSelectFrame, text = 'Delete Skins', command = self.skinpackview)
        self.Skin_SelectLabel = ctk.CTkLabel(FileSelectFrame, text = 'Select Skin')
        self.Skin_SelectDropdownMenu = ctk.CTkOptionMenu(FileSelectFrame, values = ['Select File'], command = lambda event: self.skinupdateview() if self.Skin_SelectDropdownMenu.get() != 'Select File' else print('Please select a folder with your skin file(s)'))
        self.Cape_SelectLabel = ctk.CTkLabel(FileSelectFrame, text = 'Select Cape')
        self.Cape_SelectDropdownMenu = ctk.CTkOptionMenu(FileSelectFrame, values = ['Select File', 'None'], command = lambda event: self.capeupdateview() if self.Cape_SelectDropdownMenu.get() != 'Select File' else print('Please select a folder with your cape file(s)'))

        # placement
        self.Pack_NameLabel.grid(row = 0, column = 1, sticky = 'w', padx = 10)
        self.Pack_NameEntry.grid(row = 0, column = 0, sticky = 'ew')
        self.Skin_NameLabel.grid(row = 1, column = 0, sticky = 's')
        self.Skin_NameEntry.grid(row = 2, column = 0, sticky = 'ew')
        self.DeleteButton.grid(row = 4, column = 0)
        self.Skin_SelectLabel.grid(row = 1, column = 1, sticky = 's')
        self.Skin_SelectDropdownMenu.grid(row = 2, column = 1, sticky = 'n')
        self.Cape_SelectLabel.grid(row = 3, column = 1, sticky = 's')
        self.Cape_SelectDropdownMenu.grid(row = 4, column = 1, sticky = 'n')
        FileSelectFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = .5)

    def ExportControls(self):
        # grid
        ExportControlsFrame = ctk.CTkFrame(self.settings_control, fg_color = '#191919')
        ExportControlsFrame.rowconfigure((0,1,2), weight = 1)
        ExportControlsFrame.columnconfigure((0,1), weight = 1)

        # widgets
        self.OutputLabel = ctk.CTkLabel(ExportControlsFrame, text = 'Welcome!')
        Add_SkinButton = ctk.CTkButton(ExportControlsFrame, text = 'Add', fg_color = '#10b409', hover_color = '#077d02', command = self.addskin)
        ExportButton = ctk.CTkButton(ExportControlsFrame, text = 'Export', fg_color = '#c61d1d', hover_color = '#830d0d', command = self.Export)
        Export_PATHEntry = ctk.CTkEntry(ExportControlsFrame, textvariable = self.exportPATH)
        Export_PATH_SelectButton = ctk.CTkButton(ExportControlsFrame, text = 'Select EXP Path', command = lambda: self.exportPATH.set(filedialog.askdirectory()))

        # placement
        self.OutputLabel.grid(row = 0, column = 0, columnspan = 2)
        Add_SkinButton.grid(row = 1, column = 0)
        ExportButton.grid(row = 1, column = 1)
        Export_PATHEntry.grid(row = 2, column = 0, sticky = 'ews', pady = 15)
        Export_PATH_SelectButton.grid(row = 2, column = 1, sticky = 'ws', padx = 10, pady = 15)
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
        try: # File selected successfully
            self.SkinPATH = filedialog.askdirectory()
            self.SkinRecord = [x for x in os.listdir(self.SkinPATH)]
            if self.SkinRecord:
                self.Skins = [x if len(x)<13 else x[:10] + '...' for x in os.listdir(self.SkinPATH)]
                self.Skin_SelectDropdownMenu.configure(values = self.Skins)
                self.OutputLabel.configure(text = 'File selected')
            else: # Selected file is empty
                self.Skin_SelectDropdownMenu.configure(values = ['Select File'])
                self.OutputLabel.configure(text = 'The file you selected is empty')
                print('The file you selected is empty')
        except: # Selected path does not exist
            self.Skin_SelectDropdownMenu.configure(values = ['Select File'])
            self.OutputLabel.configure(text = "The file you selected doesn't exist")
            print(self.CapePATH if self.CapePATH else '[NONE SELECTED]' + ' is not a directory')


    def CapeFileSelect(self):
        try: # File selected successfully
            self.CapePATH = filedialog.askdirectory()
            self.CapeRecord = [x for x in os.listdir(self.CapePATH)]
            if self.CapeRecord:
                self.Capes = ['None'] + [x if len(x)<13 else x[:10] + '...' for x in os.listdir(self.CapePATH)]
                self.Cape_SelectDropdownMenu.configure(values = self.Capes)
                self.OutputLabel.configure(text = 'File selected')
            else: # Selected file is empty
                self.Cape_SelectDropdownMenu.configure(values = ['Select File', 'None'])
                self.OutputLabel.configure(text = 'The file you selected is empty')
                print('The file you selected is empty')
        except: # Selected path does not exist
            self.Cape_SelectDropdownMenu.configure(values = ['Select File', 'None'])
            self.OutputLabel.configure(text = "The file you selected doesn't exist")
            print(self.CapePATH if self.CapePATH else '[NONE SELECTED]' + ' is not a directory')

    def skinupdateview(self, *args):
        try: # Image successfully selected and can be displayed
            self.SkinImage = Image.open(self.SkinPATH + '/' + self.SkinRecord[self.Skins.index(self.Skin_SelectDropdownMenu.get())])
            self.SkinImageRatio = self.SkinImage.size[0] / self.SkinImage.size[1]
            self.SkinImageTk = ImageTk.PhotoImage(self.SkinImage)
            self.Current_Skin.grid_forget()
            self.Current_Skin = Canvas(self.FileOutputFrame, bd = 0, highlightthickness = 0, relief = 'ridge')
            self.Current_Skin.grid(row = 0, column = 0, sticky = 'news', padx = 10, pady = 10)
            self.Current_Skin.create_image(1, 1, anchor = 'nw', image = self.SkinImageTk)
            self.Current_Skin.bind('<Configure>', self.no_sliceskin)
        except: # File was selected but is either not an image or an unknown image filetype
            self.OutputLabel.configure(text = 'This file is not an image/minecraft-skin')
            print('This file is not an image/minecraft-skin')
            
    def capeupdateview(self, *args):
        if self.Cape_SelectDropdownMenu.get() == 'None': # Selected no cape
            self.Current_Cape.unbind('<Configure>', None)
            self.Current_Cape.grid_forget()
            self.Current_Cape = ctk.CTkLabel(self.FileOutputFrame, text = 'Selected\nNo Cape', fg_color = '#292929', text_color = 'white')
            self.Current_Cape.grid(row = 1, column = 0, sticky = 'news', padx = 10, pady = 10)
        else: # Cape was selected
            try: # Image successfully selected and can be displayed
                self.CapeImage = Image.open(self.CapePATH + '/' + self.CapeRecord[self.Capes.index(self.Cape_SelectDropdownMenu.get()) - 1])
                self.CapeImageRatio = self.CapeImage.size[0] / self.CapeImage.size[1]
                self.CapeImageTk = ImageTk.PhotoImage(self.CapeImage)
                self.Current_Cape.grid_forget()
                self.Current_Cape = Canvas(self.FileOutputFrame, bd = 0, highlightthickness = 0, relief = 'ridge')
                self.Current_Cape.grid(row = 1, column = 0, sticky = 'news', padx = 10, pady = 10)
                self.Current_Cape.create_image(1, 1, anchor = 'nw', image = self.CapeImageTk)
                self.Current_Cape.bind('<Configure>', self.no_slicecape)
            except: # File was selected but is either not an image or an unknown image filetype
                self.OutputLabel.configure(text = 'This file is not an image/minecraft-cape')
                print('This file is not an image/minecraft-cape')
        
    def no_sliceskin(self, event):
        global skinresized_tk
        canvas_ratio = event.width / event.height

        if canvas_ratio > self.SkinImageRatio: # canvas is wider than the image
            self.skinheight = int(event.height)
            self.skinwidth = int(self.skinheight * self.SkinImageRatio)
        else: # canvas is narrower than the image
            self.skinwidth = int(event.width)
            self.skinheight = int(self.skinwidth / self.SkinImageRatio)
        
        # Deletes previous image and places a resized image to fit the window
        self.Current_Skin.delete('all')
        resized_image = self.SkinImage.resize((self.skinwidth, self.skinheight))
        skinresized_tk = ImageTk.PhotoImage(resized_image)
        self.Current_Skin.create_image(int(event.width / 2), int(event.height / 2), anchor = 'center', image = skinresized_tk)
    
    def no_slicecape(self, event):
        global caperesized_tk
        canvas_ratio = event.width / event.height

        if canvas_ratio > self.CapeImageRatio: # canvas is wider than the image
            self.capeheight = int(event.height)
            self.capewidth = int(self.capeheight * self.CapeImageRatio)
        else: # canvas is narrower than the image
            self.capewidth = int(event.width)
            self.capeheight = int(self.capewidth / self.CapeImageRatio)
        
        # Deletes previous image and places a resized image to fit the window
        self.Current_Cape.delete('all')
        resized_image = self.CapeImage.resize((self.capewidth, self.capeheight))
        caperesized_tk = ImageTk.PhotoImage(resized_image)
        self.Current_Cape.create_image(int(event.width / 2), int(event.height / 2), anchor = 'center', image = caperesized_tk)
    
    def addskin(self):
        if self.Skin_SelectDropdownMenu.get() == 'Select File' and self.Cape_SelectDropdownMenu.get() == 'Select File': # Both the skin and cape options have not been chose
            self.OutputLabel.configure(text = 'This program is not magic, please select your folders and choose your skin and/or cape')
            print('This program is not magic, please select your folders and choose your skin and/or cape') 
        elif self.Skin_SelectDropdownMenu.get() == 'Select File': # Skin has not been slected
            self.OutputLabel.configure(text = 'Please select a skin file from a folder')
            print('Please select a skin file from a folder')
        elif self.Cape_SelectDropdownMenu.get() == 'Select File': # Cape has not been selected (and the "None" option was not selected)
            self.OutputLabel.configure(text = 'Please select "None" or a cape file from a folder')
            print('Please select "None" or a cape file from a folder')
        else: # All selections meet requirements to add a skin to the skinpack
            self.Added_Skins.append({
                'Name': self.Skin_NameEntry.get() if self.Skin_NameEntry.get() != '' else self.SkinRecord[self.Skins.index(self.Skin_SelectDropdownMenu.get())].split('.')[0] + ('None' if self.Cape_SelectDropdownMenu.get() == 'None' else self.CapeRecord[self.Capes.index(self.Cape_SelectDropdownMenu.get()) - 1].split('.')[0]),
                'Skin': self.SkinPATH + '/' + self.SkinRecord[self.Skins.index(self.Skin_SelectDropdownMenu.get())], 
                'Cape': (self.CapePATH + '/' + self.CapeRecord[self.Capes.index(self.Cape_SelectDropdownMenu.get()) - 1]) if self.Cape_SelectDropdownMenu.get() != 'None' else 'None'})
            self.OutputLabel.configure(text = str(self.Skin_NameEntry.get() if self.Skin_NameEntry.get() != '' else self.SkinRecord[self.Skins.index(self.Skin_SelectDropdownMenu.get())].split('.')[0] + ('None' if self.Cape_SelectDropdownMenu.get() == 'None' else self.CapeRecord[self.Capes.index(self.Cape_SelectDropdownMenu.get()) - 1].split('.')[0])) + ' has been added')
            self.Skin_Name.set('')
    
    def skinpackview(self):
        # setup
        self.Deletion_Window = ctk.CTk()
        self.Deletion_Window.title('Skinpack view and skin deletion')
        self.Deletion_Window.resizable(False, False)
        self.Deletion_Window.geometry('750x500')

        # widgets
        self.Skinpack_ListTreeview = ttk.Treeview(self.Deletion_Window, columns = ('Skin-Name', 'Skin-img', 'Cape-img'), show = 'headings')
        self.closeandsave = ctk.CTkLabel(self.Deletion_Window, text = "Press ESC to exit and save changes (only works if you're focused on this window)")
        
        # treeview configurations
        self.Skinpack_ListTreeview.heading('Skin-Name', text = 'Skin-Name')
        self.Skinpack_ListTreeview.heading('Skin-img', text = 'Skin-img')
        self.Skinpack_ListTreeview.heading('Cape-img', text = 'Cape-img')
        for x in self.Added_Skins:
            self.Skinpack_ListTreeview.insert(parent = '', index = ctk.END, values = (x['Name'], x['Skin'], x['Cape']))

        # placement
        self.Skinpack_ListTreeview.pack(fill = 'both', expand = True)
        self.closeandsave.pack()

        # event bindings
        self.Deletion_Window.bind_all('<Escape>', lambda event: self.grabcontents())
        self.Skinpack_ListTreeview.bind('<Delete>', self.delete)

        # run
        self.Deletion_Window.mainloop()
    
    def grabcontents(self):
        # ESC has been pressed on the window and the deletions have been saved
        self.Added_Skins = [{'Name': self.Skinpack_ListTreeview.item(x)['values'][0], 'Skin': self.Skinpack_ListTreeview.item(x)['values'][1], 'Cape': self.Skinpack_ListTreeview.item(x)['values'][2]} for x in self.Skinpack_ListTreeview.get_children()]
        self.OutputLabel.configure(text = 'Skins updated')
        self.Deletion_Window.destroy()
    
    def delete(self, event):
        # Items in the skinpack have been removed but deletions are not final
        self.OutputLabel.configure(text = f'{len([x for x in self.Skinpack_ListTreeview.selection()])} {'skin' + ('s' if len([x for x in self.Skinpack_ListTreeview.selection()]) > 1 else '')} removed from pack (press ESC to save list)')
        for item in self.Skinpack_ListTreeview.selection():
            self.Skinpack_ListTreeview.delete(item)
    
    def Export(self):
        if self.Pack_NameEntry.get(): # Skinpack name was added
            if self.Added_Skins: # Skins have been added

                # Creates the skinpack file folder (PATH)
                os.mkdir(f'{self.exportPATH.get().replace('/', '\\')}\\{self.Pack_NameEntry.get()}_SkinpackFile')

                # Creates the skins.json file
                with open(f'{self.exportPATH.get().replace('/', '\\')}\\{self.Pack_NameEntry.get()}_SkinpackFile/skins.json', 'w') as fp:
                    fp.write('{"skins": [' + ', '.join('{"localization_name": ' + f'"{x["Name"]}", "geometry": "geometry.humanoid.customSlim", "texture": "{x["Skin"].split("/")[-1]}", ' + (f'"cape": "{x["Cape"].split("/")[-1]}", ' if x["Cape"] != 'None' else '') + '"type": "free"}' for x in self.Added_Skins) + f'], "serialize_name": "{self.Pack_NameEntry.get()}", "localization_name": "{self.Pack_NameEntry.get()}"' + '}')
                
                # Creates the texts folder (PATH) inside the skinpack folder
                os.mkdir(f'{self.exportPATH.get().replace('/', '\\')}\\{self.Pack_NameEntry.get()}_SkinpackFile\\texts')

                # Creates the en_US.lang file
                with open(f'{self.exportPATH.get().replace('/', '\\')}\\{self.Pack_NameEntry.get()}_SkinpackFile\\texts\\en_US.lang', 'w') as fp:
                    fp.write(f'skinpack.{self.Pack_NameEntry.get()}={self.Pack_NameEntry.get()}\n' + '\n'.join(f'skin.{self.Pack_NameEntry.get()}.{x['Name']}={x['Name']}' for x in self.Added_Skins))
                
                # Creates the manifest.json file
                with open(f'{self.exportPATH.get().replace('/', '\\')}\\{self.Pack_NameEntry.get()}_SkinpackFile\\manifest.json', 'w') as fp:
                    fp.write('{\n  "header": {\n    "version": [\n      1,\n      0,\n      0\n    ],\n    "description": '+f'"{self.Pack_NameEntry.get()}",\n    "name": "{self.Pack_NameEntry.get()}",\n    "uuid": "{uuid.uuid4()}"'+'\n  },\n  "modules": [\n    {\n      "version": [\n        1,\n        0,\n        0\n      ],\n      "type": "skin_pack",\n      "uuid": '+f'"{uuid.uuid4()}"'+'\n    }\n  ],\n  "format_version": 1\n}')
                
                # Copies skins into skinpack
                for x in set([x['Skin'] for x in self.Added_Skins]):
                    shutil.copy(x, f'{self.exportPATH.get().replace('/', '\\')}\\{self.Pack_NameEntry.get()}_SkinpackFile')
                
                # Copies capes into skinpack
                for x in set([x['Cape'] for x in self.Added_Skins if x['Cape'] != 'None']):
                    shutil.copy(x, f'{self.exportPATH.get().replace('/', '\\')}\\{self.Pack_NameEntry.get()}_SkinpackFile')

                # Copies the geometry.json file into skinpack
                shutil.copy(f'{os.getcwd()}\\geometry.json', f'{self.exportPATH.get().replace('/', '\\')}\\{self.Pack_NameEntry.get()}_SkinpackFile')
                self.OutputLabel.configure(text = f'Pack exported into {self.exportPATH.get().replace('/', '\\')}\\{self.Pack_NameEntry.get()}_SkinpackFile')
            else: # Skins have not been added
                self.OutputLabel.configure(text = 'No added skins')
                print('No added skins')
        else: # Skinpack name has not been added
            self.OutputLabel.configure(text = 'Needs a pack name')
            print('Needs a pack name')