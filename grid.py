from cell import Cell


class Grid:

    def __init__(self, size):
        self.grid = []
        self.floors = []
        for i in range(0, size):
            row = []
            for j in range(0, size):
                if 1 < i < 5 and j == 2 or 0 < j < 6 and i == 1 or i == 2 and j == 4:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif 4 < j < 10 and i == 6 or 3 < i < 7 and j == 5:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif 5 < i < 9 and j == 1 or 1 < j < 6 and i == 8:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif 0 < i < 5 and 6 < j < 8 or j == 8 and 5 < i < 9 or i == 2 and j == 8 or i == 4 and j == 9:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif i == 6 and 1 < j < 4 or i == 4 and j == 3 or i == 3 and j == 0 or i == 0 and j == 7:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                else:
                    cell = Cell(i, j, "floor")
                    row.append(cell)
                    self.floors.append([i, j])
            self.grid.append(row)

    def draw(self, canvas, resource, image_size):
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid)):
                self.grid[i][j].draw(canvas, resource, image_size)
