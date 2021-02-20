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

if __name__ == '__main__':
    import time
    from os import system
    from game import Game
    game = Game()

    while True:
        system('clear')
        game.tick()
        time.sleep(0.5)

