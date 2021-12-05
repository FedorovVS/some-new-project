import pygame
import numpy
from smth.py import field_creation
from smth.py import caption_creation
from smth.py import mousepos







window_width = 1700
"""Ширина окна"""

window_height = 800
"""Высота окна"""

pygame.init()

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
            cells.[k][j].state = 1
    if position ==3:
        for k in range (i, i - 4, -1):
            cells.[k][j].state = 1
    if position == 4:
        for k in range (i, i + 4):
            cells.[i][k].state = 1
    else:
        for k in range (i, i-4, -1):
                cells.[i][k].state = 1
            
    
    
    
    

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    pygame.display.update()
    clock.tick(FPS)
    field_creation(300, 100, 900, 700)
    field_creation(1000, 100, 1600, 700)
    caption_creation(300, 100, 900, 700)
    caption_creation(1000, 100, 1600, 700)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

