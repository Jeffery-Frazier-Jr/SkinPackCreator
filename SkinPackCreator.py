import customtkinter as ctk
from Widgets import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1500x800')
        self.title('SkinPackCreator')

        # layout
        setttings_control = Frame(self, 0, 0, .6, 1, 'red')
        folder_output = Frame(self, .6, 0, .4, 1, 'green')

        # run
        self.mainloop()

App()