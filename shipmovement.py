import pygame
import numpy
from smth import field_creation
from smth import caption_creation
from smth import mousepos
from smth import Cell
from gr1 import Ship




window_width = 1700
"""Ширина окна"""
FPS = 30
window_height = 800
"""Высота окна"""


def shiphere(cells:list, position):
    '''
    position describes position of the ship
    1 - 0 angle
    2 - 90 degree 
    3 - 180 degree
    4 - 270 degree
    
    '''
    mousepos(cells).state = 1
    i, j = mousepos(cells).i, mousepos(cells).j
    if position == 1:
        for k in range (i, i + 4):
            cells[k][j].state = 1
    if position ==3:
        for k in range (i, i - 4, -1):
            cells[k][j].state = 1
    if position == 4:
        for k in range (i, i + 4):
            cells[i][k].state = 1
    else:
        for k in range (i, i-4, -1):
                cells[i][k].state = 1
def  placetheship(ship:Ship):
    '''
    
    '''
    x, y = pygame.mouse.get_pos()
    ship.x0 = x
    ship.y0 = y
    ship.x1 = x + 240
    ship.y1 = y + 60
    ship.draw()
    
def whichship(ships):
    '''
    
    '''
    x, y = pygame.mouse.get_pos()
    for i, ship in enumerate(ships):
        if ship.x0 <= x <= ship.x1:
            if ship.y0 <= y <= ship.y1:
                return i
    


pygame.quit()

