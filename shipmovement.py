import pygame
import numpy
from smth import field_creation, caption_creation, mousepos, write
from graphics import Ship
from format import Cell




window_width = 1700
"""Ширина окна"""
FPS = 30
window_height = 800
"""Высота окна"""


def shiphere(cells:list, ship):
    '''
    position describes position of the ship
    '''
    mousepos(cells).state = 1
    vertical = ship.turn_flag
    i, j = mousepos(cells).i, mousepos(cells).j
    if vertical == 0:
        for k in range (i, i + 4):
            cells[k][j].state = 1
            cells[k][j].warship = ship
    if vertical == 1:
        for k in range (j, j + 4):
            cells[i][k].state = 1
            cells[i][k].warship = ship
            
def  placetheship(ship:Ship, cell:Cell, cells:list, screen):
    '''
    changes coordinates of the ship
    '''   
    i, j = cell.i, cell.j
    notfree = 0
    if ship.turn_flag == 0:
        if i > 6:
            notfree = 1
        mini = max(i-1, 0)
        maxi = min(i+5, 10)
        for a in range (mini, maxi):
            minj = max(0, j-1)
            maxj = min(10, j+2)
            for b in range (minj, maxj):
                notfree += cells[a][b].state
    if ship.turn_flag == 1:
        if j > 6:
            notfree = 1
        minj = max(j-1, 0)
        maxj = min(j+5, 10)
        for a in range (minj, maxj):
            mini = max(0, i-1)
            maxi = min(10, i+2)
            for b in range (mini, maxi):
                notfree += cells[a][b].state
    if notfree != 0:
       return 0
       #may be write smth like "not possible"
    if notfree == 0:
        x, y = cell.x, cell.y
        ship.x0 = x
        ship.y0 = y
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
        return 1
    
def whichship(ships):
    '''
    Возвращает порядковый номер корабля из списка,
    в который зафиксировано попадание
    '''
    x, y = pygame.mouse.get_pos()
    for i, ship in enumerate(ships):
        if ship.x0 <= x <= ship.x1:
            if ship.y0 <= y <= ship.y1:
                return i
    return -1
    


pygame.quit()

