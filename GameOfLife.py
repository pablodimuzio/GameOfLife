import tkinter
import numpy as np
from time import *

root = tkinter.Tk()

GRID_X_SIZE = 150 #number of cells on the x component
GRID_Y_SIZE = 150 #number of cells on the y component
SCALING_FACTOR = 7 #side length of a cell
GAME_SPEED = 1 #milliseconds

myCanvas = tkinter.Canvas(root, bg="black", height=GRID_Y_SIZE*SCALING_FACTOR, width=GRID_X_SIZE*SCALING_FACTOR)
grid = np.zeros((GRID_Y_SIZE, GRID_X_SIZE), dtype=int)


def setPixelToAlive(event):
    gridMouseX = event.x//SCALING_FACTOR
    gridMouseY = event.y//SCALING_FACTOR

    grid[gridMouseX][gridMouseY] = 1

    update(gridMouseX, gridMouseY)

def countAliveNeigbors(x, y):
    if (x != 0 and x != GRID_X_SIZE-1) and (y != 0 and y != GRID_Y_SIZE-1):
        return grid[x-1][y-1]+grid[x-1][y]+grid[x-1][y+1]+grid[x][y-1]+grid[x][y+1]+grid[x+1][y-1]+grid[x+1][y]+grid[x+1][y+1]

    if (x == 0) and (y != 0 and y != GRID_Y_SIZE-1):
        return grid[x][y-1]+grid[x][y+1]+grid[x+1][y-1]+grid[x+1][y]+grid[x+1][y+1]

    if (x == GRID_X_SIZE-1) and (y != 0 and y != GRID_Y_SIZE-1):
        return grid[x-1][y-1]+grid[x-1][y]+grid[x-1][y+1]+grid[x][y-1]+grid[x][y+1]

    if (x != 0 and x != GRID_X_SIZE-1) and (y == 0):
        return grid[x-1][y]+grid[x-1][y+1]+grid[x][y+1]+grid[x+1][y]+grid[x+1][y+1]

    if (x != 0 and x != GRID_X_SIZE-1) and (y == GRID_Y_SIZE-1):
        return grid[x-1][y-1]+grid[x-1][y]+grid[x][y-1]+grid[x+1][y-1]+grid[x+1][y]

    if (x == 0) and (y == 0):
        return grid[x][y+1]+grid[x+1][y]+grid[x+1][y+1]

    if (x == 0) and (y == GRID_Y_SIZE-1):
        return grid[x][y-1]+grid[x+1][y-1]+grid[x+1][y]
    
    if (y == GRID_Y_SIZE-1):
        return grid[x-1][y-1]+grid[x-1][y]+grid[x][y-1]
    
    return grid[x-1][y]+grid[x-1][y+1]+grid[x][y+1]



def update(x, y):
    if grid[x][y] == 1:
        myCanvas.create_rectangle(x*SCALING_FACTOR,y*SCALING_FACTOR, (x+1)*SCALING_FACTOR, (y+1)*SCALING_FACTOR, fill="white")
    else:
        myCanvas.create_rectangle(x*SCALING_FACTOR,y*SCALING_FACTOR, (x+1)*SCALING_FACTOR, (y+1)*SCALING_FACTOR, fill="black")

#Rules: 
# A dead cell becomes alive if they have 3 neighbors alive
# An alive cell stays alive if it has 2-3 neighbors alive
# Cells outside canvas are all dead
# Cell = 0 = Dead
# Cell = 1 = Alive
def cellLife(event):
    cellLife.event = event
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            aliveNeighbors = countAliveNeigbors(x, y)
            isCellAlive = bool(grid[x][y])
            if aliveNeighbors == 0:
                continue
            if isCellAlive:
                if aliveNeighbors !=3 and aliveNeighbors !=2:
                    grid[x][y] = 0
                    update(x, y)
                    continue
            if aliveNeighbors == 3:
                grid[x][y] = 1
                update(x, y)

def life(event):
    myCanvas.event = event
    cellLife(event)
    if True:
        myCanvas.after(GAME_SPEED, life, event)

    

myCanvas.pack()
myCanvas.bind('<Button-3>', life)
myCanvas.bind('<Button-1>', setPixelToAlive)
root.mainloop()