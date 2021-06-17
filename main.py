
# Made by Gunnar Jessee, inspired by Conway's Game of Life

from os import system
from time import sleep


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
            cell = grid[x, y]
            if cell.state == 0:
                prnt('0')
            if cell.state == 1:
                prnt('1')
        print("")


def generate_room():
    for x in range(worldSize):
        for y in range(worldSize):
            grid[x, y] = Cell(0)


def amount_neighbors(neighbors):
    count = 0
    for neighbor in neighbors:
        if neighbor.state == 1:
            count = count + 1
    return count


def update_cells():
    for x in range(worldSize):
        for y in range(worldSize):
            if 0 < x < worldSize - 1 and 0 < y < worldSize - 1:
                cell = grid[x, y]

                n = grid[x, y + 1]
                nw = grid[x - 1, y - 1]
                s = grid[x, y - 1]
                sw = grid[x - 1, y + 1]
                se = grid[x + 1, y + 1]
                ne = grid[x + 1, y - 1]
                w = grid[x - 1, y]
                e = grid[x + 1, y]

                neighbors = [n, s, nw, sw, ne, se, e, w]
                if 2 < amount_neighbors(neighbors) < 4:
                    cell.nextState = 1
                else:
                    cell.nextState = 0

    for x in range(worldSize):
        for y in range(worldSize):
            grid[x, y].state = grid[x, y].nextState

def get_active_cells():
    index = 0
    for x in range(worldSize):
        for y in range(worldSize):
            if grid[x,y].state == 1 or grid[x,y].nextState == 1:
                index = index + 1
    return index


generate_room()
grid[10, 10].state = 1
grid[10, 11].state = 1
grid[10, 12].state = 1

while get_active_cells() > 0:
    system('cls')
    display_room()
    update_cells()
    sleep(.5)