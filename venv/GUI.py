import arcade
from tkinter import *
from World.World import GWorld

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class GGUI:
    def __init__(self, master):
        self.master = master
        master.title("Virtual World")

        self.label = Label(master, text="Choose world size:")
        self.label.pack()

        self.greet_button = Button(master, text="Start", command=self.greet)
        self.greet_button.pack()

        self.scale = Scale(master, from_=0, to=30, orient=HORIZONTAL, resolution=1)
        self.scale.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        game = GWorld(self.scale.get())
        arcade.run()