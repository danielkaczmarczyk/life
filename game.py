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

DEBUG = False

class Cell:
    def __init__(self, alive):
        self.alive = alive

    def __repr__(self):
        if self.alive:
            return "\u265E"
        else:
            return ' '

    def __str__(self):
        if self.alive:
            return "\u25A9"
        else:
            return ' '

class Grid:
    def __init__(self, w=30, h=50):
        self.w = w
        self.h = h
        self.grid = self.generate_grid(self.w, self.h)

    def get_random_cell(self):
        import random
        if random.random() < .5:
            return Cell(True)
        else:
            return Cell(False)

    def generate_grid(self, w, h):
        grid = [[self.get_random_cell() for n in range(self.h) ] for n in range(self.w)]
        return grid

    def print_grid(self):
        grid = self.grid
        print("-" * (len(grid) + 2))
        for row in grid:
            print("|", end='')
            for item in row:
                print(item, end='')
            print("|", end='')
            print()
        print("-" * (len(grid) + 2))

    def get_cell(self, row, column):
        if row < 0 or column < 0:
            return None
        try:
            return self.grid[row][column]
        except IndexError:
            return None

    def check_neighbors(self, row, column):
        n = 0
        g = self.grid
        # look at all neighbors and count
        # a neighbor is a cell that is alive
        # implement returning true/false based on the rules
        # try getting a value for every direction
        offsets = []

        nums = [-1, 0, 1]
        nums_idx = 0

        for i in range(9):
            if nums_idx == 3:
                nums_idx = 0
            if i < 3:
                offsets.append([1, nums[nums_idx]])
                nums_idx += 1
            if i >= 3 and i < 6:
                offsets.append([0, nums[nums_idx]])
                nums_idx += 1
            if i >= 6:
                offsets.append([-1, nums[nums_idx]])
                nums_idx += 1
        
        # calculate actual offsets

        offsets.remove([0,0])
        for offset in offsets:
            offset[0] += row
            offset[1] += column

        # check for presence of cells
        for offset in offsets:
            cell = self.get_cell(offset[0], offset[1])
            if cell:
                if cell.alive:
                    n += 1

        return n

    def update(self):
        # get a copy of the grid
        new_grid = self.generate_grid(self.w, self.h)
        # go over every cell in the grid
        # count neighbors
        for row, row_array in enumerate(self.grid):
            for column, cell in enumerate(row_array):
                cell = self.grid[row][column]
                n = self.check_neighbors(row, column)
                message = f"cell {row}:{column} has n of {n}"
                if cell.alive:
                    message += " it was found alive"
                    if n < 2:
                        message += " and dies of underpopulation"
                        new_grid[row][column] = Cell(False)
                        #cell.alive = False
                    elif n >= 2 and n <= 3:
                        message += " and stays stable"
                        #cell.alive = True
                        new_grid[row][column] = Cell(True)
                    elif n > 3:
                        message += " and dies of overpopulation"
                        new_grid[row][column] = Cell(False)
                        #cell.alive = False
                else:
                    message += " it was found dead"
                    if n == 3:
                        message += " and will be born due to reproduction"
                        #cell.alive = True
                        new_grid[row][column] = Cell(True)
                    else:
                        new_grid[row][column] = Cell(False)
                if DEBUG:
                    print(message)

        # return updated copy of the grid
        self.grid = new_grid

class Game:
    def __init__(self):
        self.grid = Grid()
        self.grid.print_grid()
        self.ticks = 0

    def tick(self):
        print()
        self.ticks += 1
        self.grid.update()
        self.grid.print_grid()

if __name__ == '__main__':
    import time
    from os import system
    game = Game()

    while True:
        system('clear')
        game.tick()
        time.sleep(0.5)

