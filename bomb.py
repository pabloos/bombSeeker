from random import randint
from Tkinter import *
import PIL.ImageTk, PIL.Image, Tkinter, tkMessageBox, os.path, pip, sys

script_dir = os.path.dirname(os.path.abspath(__file__))

top = Tkinter.Tk()
top.withdraw()

def initImage(image):
    image = PIL.Image.open(os.path.join(script_dir, image))
    image = image.resize((50,50), PIL.Image.ANTIALIAS)
    image = PIL.ImageTk.PhotoImage(image)
    return image

img = initImage("field.jpg")
img2 = initImage("bomb.png")
img3 = initImage("red-cross-md.png")

class Field:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.isMine = randint(0, 1)
        self.button = Tkinter.Button(top, image = img, command = self.callback, height = 50, width = 50).grid(row=i, column=j)

    def callback(self):
        if(self.isMine == 1):
            self.button = Tkinter.Button(top, image = img2, command = self.callback, height = 50, width = 50).grid(row=self.x, column=self.y)
            tkMessageBox.showinfo("BombSekker", "Game Over")
            exit()
        else:
            self.button = Tkinter.Button(top, image = img3, command = self.callback, height = 50, width = 50).grid(row=self.x, column=self.y)

class Menu:
    def __init__(self):
        self.topForm = Tkinter.Tk()

        self.label1 = Label(self.topForm, text = "Insert the number of columns:")
        self.form1 = Entry(self.topForm)
        self.label1.grid(row = 1, column = 1)
        self.form1.grid(row = 1, column = 2)

        self.label2 = Label(self.topForm, text = "Insert the number of rows:")
        self.form2 = Entry(self.topForm)
        self.label2.grid(row = 2, column = 1)
        self.form2.grid(row = 2, column = 2)

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

def main():
    if 'PIL' in sys.modules:
        pass
    else:
        print "installing pillow..."
        pip.main(['install', "pillow"])

    menu = Menu()

if __name__ == "__main__":
    main()
