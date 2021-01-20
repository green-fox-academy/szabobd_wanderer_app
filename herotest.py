import tkinter as tk
from cell import Cell
from grid import Grid


# Create the window with the Tk class
root = tk.Tk()

# Create the canvas and make it visible with pack()
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()  # this makes it visible

# Loads and create image (put the image in the folder)


def move(event):
    """Move the sprite image with a d w and s when click them"""
    if event.char == "a":
        img = tk.PhotoImage(file="gifs/hero-left.gif")
        image = canvas.create_image(360, 360, anchor=tk.NW, image=img)
        canvas.move(image, -72, 0)
    elif event.char == "d":
        img = tk.PhotoImage(file="gifs/hero-right.gif")
        image = canvas.create_image(360, 360, anchor=tk.NW, image=img)
        canvas.move(image, 72, 0)
    elif event.char == "w":
        img = tk.PhotoImage(file="gifs/hero-up.gif")
        image = canvas.create_image(360, 360, anchor=tk.NW, image=img)
        canvas.move(image, 0, -72)
    elif event.char == "s":
        img = tk.PhotoImage(file="gifs/hero-down.gif")
        image = canvas.create_image(360, 360, anchor=tk.NW, image=img)
        canvas.move(image, 0, 72)



img = tk.PhotoImage(file="gifs/hero-down.gif")
image = canvas.create_image(360, 360, anchor=tk.NW, image=img)

# This bind window to keys so that move is called when you press a key
root.bind("<Key>", move)

# this creates the loop that makes the window stay 'active'
root.mainloop()

from cell import Cell


class Hero:
    def __init__(self, size):
        self.grid = []
        for i in range(0, size):
            row = []
            for j in range(0, size):
                self.i = 1
                self.j = 1
                cell = Cell(self.i, self.j, "hero_down")
                row.append(cell)
            self.grid.append(row)

    def draw(self, canvas, resource, image_size):
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid)):
                self.grid[self.i][self.j].draw(canvas, resource, image_size)


class Hero:
    def __init__(self):
        self.x = 4
        self.y = 4
        self.img = "hero_down"
        self.image = canvas.create_image(72, 72, anchor=NW, image=img)
        self.cell = Cell(self.x, self.y, "hero_down")

    def draw(self, canvas, resource, image_size):

    # canvas.create_image(self.x * image_size + (image_size / 2) + 2,
    #                     self.y * image_size + (image_size / 2) + 2, image=resource.get_image(self.img))

    def move(self, canvas, new_x, new_y):
        canvas.move(self.image, new_x, new_y)


img = PhotoImage(file="gifs/hero-left.gif")
image_left = canvas.create_image(72, 72, anchor=NW, image=img)
canvas.move(image_left, -72, 0)

