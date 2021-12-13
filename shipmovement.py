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
        for k in range (j, j + 4):
            cells[i][k].state = 1
    else:
        for k in range (i, j-4, -1):
                cells[i][k].state = 1
def  placetheship(ship:Ship, x, y):
    '''
    
    '''    
    ship.x0 = x
    ship.y0 = y
    #100 - left border of the field
    if ship.turn_flag == 0:
        ship.x1 = x  + 240
        #4 cells
        ship.y1 = y  + 60
        #1 cell 
    if ship.turn_flag == 1:
        ship.y1 = y  + 240
        #4 cells
        ship.x1 = x + 60
        #1 cell 
    
def whichship(ships):
    '''
    
    '''
    x, y = pygame.mouse.get_pos()
    for i, ship in enumerate(ships):
        if ship.x0 <= x <= ship.x1:
            if ship.y0 <= y <= ship.y1:
                return i
    return -1
    


pygame.quit()

