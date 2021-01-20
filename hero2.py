from tkinter import *

class Hero:
    def __init__(self, canvas):
        self.x = 4
        self.y = 4
        self.image = None

    def draw(self, canvas):
        img = PhotoImage(file="gifs/hero-down.gif")
        # image = canvas.create_image(10, 10, anchor=NW, image=img)
        self.image = canvas.create_image(72, 72, anchor=NW, image=img)

    def move(self, canvas, new_x, new_y):
        canvas.move(self.image, new_x, new_y)


