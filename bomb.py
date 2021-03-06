#!/usr/bin/env python

from random import randint
from Tkinter import *
import PIL.ImageTk, PIL.Image, Tkinter, tkMessageBox, os.path, pip, sys, os

class Field:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.isMine = randint(0, 1)
        self.button = Tkinter.Button(master = Menu.top, image = fieldImage, command = self.callback, height = 50, width = 50).grid(row=i, column=j)

    def callback(self):
        if self.isMine == 1:
            self.button = Tkinter.Button(master = Menu.top, image = bombImage, command = self.callback, height = 50, width = 50).grid(row=self.x, column=self.y)
            tkMessageBox.showinfo("BombSekker", "Game Over")

            exit()

        else:
            self.button = Tkinter.Button(master = Menu.top, image = crossImage, command = self.callback, height = 50, width = 50).grid(row=self.x, column=self.y)

class Menu:
    script_dir = os.path.dirname(os.path.abspath(__file__))

    top = Tkinter.Tk()
    top.wm_title("Bomb Seeker")
    top.withdraw()              #hide this window

    @staticmethod
    def initImage(image):
        image = PIL.Image.open(os.path.join(Menu.script_dir, image))
        image = image.resize((50,50), PIL.Image.ANTIALIAS)
        image = PIL.ImageTk.PhotoImage(image)
        return image

    def __init__(self):
        self.window = Tkinter.Tk()
        self.window.wm_title("Bomb Seeker")

        self.label0 = Label(self.window, text = "Select the dimensions (x,y)").grid(row = 1, column = 1, columnspan = 2)

        self.label1 = Label(self.window, text = "Insert the number of columns:").grid(row = 2, column = 1)
        self.form1 = Entry(self.window)
        self.form1.grid(row = 2, column = 2)

        self.label2 = Label(self.window, text = "Insert the number of rows:").grid(row = 3, column = 1)
        self.form2 = Entry(self.window)
        self.form2.grid(row = 3, column = 2)

        self.button = Button(self.window, text = "Go!", command = self.callbackButton).grid(row = 4, column = 1, columnspan = 2)

        self.window.mainloop()

    def callbackButton(self):
        self.cols = int(self.form1.get())
        self.rows = int(self.form2.get())

        self.window.destroy()

        for i in range(self.cols):
            for j in range(self.rows):
                self.field = Field(i,j)

        Menu.top.deiconify()

#################################
######## Executive block ########
#################################

fieldImage = Menu.initImage("field.jpg")        #images for the fields
bombImage = Menu.initImage("bomb.png")
crossImage = Menu.initImage("red-cross-md.png")

if not 'PIL' in sys.modules:
    print "installing pillow..."
    pip.main(['install', "pillow"])

menu = Menu()
