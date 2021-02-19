"""
    rules:

    1. any live cell with fewer than two live neighbours dies
    2. any live cell with two or three neighbours lives
    3. any live cell withm more than three live neighbours dies
    4. any dead cell with exactly three live neighbours becomes a live cell

    therefore:

    1. any live cell with two or three live neighbours survives
    2. any dead cell with three live neighbours becomes a live cell
    3. all other live cells die in the next generation. similarly, all other dead cells stay dead.

"""

# prototype of a game of life script
# build a grid
# place some cells
# iterate over grid, calculate next generation
# display generations at an interval

class Cell:
    DEAD = 'x'
    ALIVE = 'o'

    def __init__(self, status=False):
        if status == True:
            self.status = self.ALIVE
        elif status == False:
            self.status = self.DEAD

    def __repr__(self):
        return self.status

class Grid:
    def __init__(self, w=3, h=3):
        self.w = w
        self.h = h
        self.grid = self.generate_grid(self.w, self.h)

    def generate_grid(self, w, h):
        grid = [ [Cell() for n in range(self.h) ] for n in range(self.w)]
        return grid

    def print_grid(self):
        grid = self.grid
        for row in grid:
            for item in row:
                print(item, end='')
            print()

    def check_neighbors(self, row, column):
        n = 0
        # look at all neighbors and count
        # a neighbor is a cell that is alive
        # implement returning true/false based on the rules
        print(f"neighbor count for {row}:{column}: {n}") 
        pass

    def update(self):
        # get a copy of the grid
        # go over every cell in the grid
        # count neighbors
        for row, row_array in enumerate(self.grid):
            for column, cell in enumerate(row_array):
                print(f"{row=}, {column=}")
                verdict = self.check_neighbors(row, column)
                # change cell status
                cell.status = verdict
        # return updated copy of the grid
        pass

class Game:
    def __init__(self):
        self.grid = Grid()

    def tick(self):
        self.grid.update()

if __name__ == '__main__':
    game = Game()
    game.tick()

