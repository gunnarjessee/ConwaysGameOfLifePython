
# Made by Gunnar Jessee, inspired by Conway's Game of Life

class Cell:
    state = 0
    nextState = 0
    def __init__(self, state):
        self.state = state

worldSize = 20
grid = {}

# Prints string on the same line
def prnt(str):
    print(str, end="")


def display_room():
    for x in range(worldSize):
        for y in range(worldSize):
            grid[x, y] = Cell(0)


def generate_room():
    for x in range(worldSize):
        for y in range(worldSize):
            grid[x, y] = Cell(0)


def update_cells():
    # fate of each cell gets decided here
    pass


def get_active_cells():
    index = 0
    for x in range(worldSize):
        for y in range(worldSize):
            if grid[x,y].state == 1 or grid[x,y].nextState == 1:
                index = index + 1
    return index


while get_active_cells() > 0:
    update_cells()