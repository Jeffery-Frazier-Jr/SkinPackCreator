import customtkinter as ctk
class Frame(ctk.CTkFrame):
    def __init__(self, parent, x, y, width, height, color):
        super().__init__(parent, fg_color = color)
        self.place(relx = x, rely = y, relwidth = width, relheight = height)