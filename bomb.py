from random import randint
from Tkinter import *
import PIL.ImageTk, PIL.Image, Tkinter, tkMessageBox, os.path, pip, sys

script_dir = os.path.dirname(os.path.abspath(__file__))


class Game:
    def __init__(self):
        self.top = Tkinter.Tk()          #we will hide this window
        self.top.withdraw()

    def initImage(image):
        image = PIL.Image.open(os.path.join(script_dir, image))
        image = image.resize((50,50), PIL.Image.ANTIALIAS)
        image = PIL.ImageTk.PhotoImage(image)
        return image

fieldImage = game.initImage("field.jpg")        #images for the fields
bombImage = game.initImage("bomb.png")
crossImage = game.initImage("red-cross-md.png")

class Field:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.isMine = randint(0, 1)
        self.button = Tkinter.Button(game.top, image = fieldImage, command = self.callback, height = 50, width = 50).grid(row=i, column=j)

    def callback(self):
        if(self.isMine == 1):
            self.button = Tkinter.Button(game.top, image = bombImage, command = self.callback, height = 50, width = 50).grid(row=self.x, column=self.y)
            tkMessageBox.showinfo("BombSekker", "Game Over")

	    for i in range(menu.rows):
		for j in range(menu.cols):
		    menu.field = None
		           
	    game.top.withdraw()
	    menu = Menu()
        else:
            self.button = Tkinter.Button(game.top, image = crossImage, command = self.callback, height = 50, width = 50).grid(row=self.x, column=self.y)

class Menu:
    def __init__(self):
        self.topForm = Tkinter.Tk()

        self.label1 = Label(self.topForm, text = "Insert the number of columns:")
        self.form1 = Entry(self.topForm)
        self.label1.grid(row = 1, column = 1)
        self.form1.grid(row = 1, column = 2)    #frist part of the form

        self.label2 = Label(self.topForm, text = "Insert the number of rows:")
        self.form2 = Entry(self.topForm)
        self.label2.grid(row = 2, column = 1)
        self.form2.grid(row = 2, column = 2)    #second one...

        self.button = Button(self.topForm, text = "Go!", command = self.callbackButton)
        self.button.grid(row = 3, column = 2)

        self.topForm.mainloop()

    def callbackButton(self):
        self.cols = int(self.form1.get())
        self.rows = int(self.form2.get())

        self.topForm.destroy()

        for i in range(self.cols):
            for j in range(self.rows):
                self.field = Field(i,j)

        top.deiconify()

def main():                #main function
    if 'PIL' in sys.modules:
        pass
    else:
        print "installing pillow..."
        pip.main(['install', "pillow"])
    
    game = Game()
    menu = Menu()

if __name__ == "__main__":
    main()
