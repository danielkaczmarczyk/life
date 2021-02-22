from cell import Cell
import os

class Grid:
    def __init__(self):
        size = os.get_terminal_size() 
        self.w = size.columns
        self.h = size.lines
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
        for row in grid:
            for item in row:
                print(item, end='')
            print()

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
        
        offsets.remove([0,0])
        for offset in offsets:
            offset[0] += row
            offset[1] += column

        for offset in offsets:
            cell = self.get_cell(offset[0], offset[1])
            if cell:
                if cell.alive:
                    n += 1

        return n

    def update(self):
        new_grid = self.generate_grid(self.w, self.h)
        for row, row_array in enumerate(self.grid):
            for column, cell in enumerate(row_array):
                cell = self.grid[row][column]
                n = self.check_neighbors(row, column)
                if cell.alive:
                    if n < 2:
                        new_grid[row][column] = Cell(False)
                    elif n >= 2 and n <= 3:
                        new_grid[row][column] = Cell(True)
                    elif n > 3:
                        new_grid[row][column] = Cell(False)
                else:
                    if n == 3:
                        new_grid[row][column] = Cell(True)
                    else:
                        new_grid[row][column] = Cell(False)

        self.grid = new_grid

