from grid import Grid

class Game:
    def __init__(self):
        self.grid = Grid()
        self.grid.print_grid()
        self.ticks = 0

    def tick(self):
        self.ticks += 1
        self.grid.update()
        self.grid.print_grid()

