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

