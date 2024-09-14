import customtkinter as ctk

class Frame(ctk.CTkFrame):
    def __init__(self, parent, x, y, width, height, color = 'transparent'):
        super().__init__(parent, fg_color = color)
        self.place(relx = x, rely = y, relwidth = width, relheight = height)

class Label(ctk.CTkLabel):
    def __init__(self, parent, text, rw, col, color = 'white', tcolor = 'black', sticky = True):
        super().__init__(parent, text = text, fg_color = color, text_color = tcolor)
        self.grid(row = rw, column = col, sticky = 'news' if sticky else '', padx = 10, pady = 10)

class Entry(ctk.CTkEntry):
    def __init__(self, parent, rw, col):
        super().__init__(parent)
        self.grid(row = rw, column = col, sticky = 'ew', pady = 20)

class DropMenu(ctk.CTkOptionMenu):
    def __init__(self, parent, rw, col, list):
        super().__init__(parent, values = list)
        self.grid(row = rw, column = col)

class Button(ctk.CTkButton):
    def __init__(self, parent, rw, col, text):
        super().__init__(parent, text = text)
        self.grid(row = rw, column = col)