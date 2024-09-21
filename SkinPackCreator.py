import customtkinter as ctk
from Frames import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # setup
        self.geometry('1500x800')
        self.minsize(750,400)
        self.title('SkinPackCreator')
        ctk.set_appearance_mode('dark')

        # programs
        Layout(self)

        # run
        self.mainloop()

App()