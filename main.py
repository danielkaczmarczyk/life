if __name__ == '__main__':
    import time
    from os import system
    from game import Game
    game = Game()

    while True:
        system('clear')
        game.tick()
        time.sleep(0.5)

