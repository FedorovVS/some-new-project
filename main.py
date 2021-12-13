import pygame
import numpy
from smth import field_creation
from smth import caption_creation
from smth import mousepos
from smth import Cell
from gr1 import Ship
from shipmovement import placetheship

window_width = 1700
"""Ширина окна"""

window_height = 800
"""Высота окна"""

pygame.init()

FPS = 30
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.update()
screen.fill(black)
clock = pygame.time.Clock()
finished = False
#shipdefinition
ship1 = Ship(0, 0, 240, 60, 1, screen, '1.png', 0)
ship2 = Ship(0, 60, 240, 120, 1, screen, '2.png', 0)
ship3= Ship(0, 120, 240, 180, 1, screen, '3.png', 0)
ship4 = Ship(0, 180, 240, 240, 1, screen, '4.png', 0)
ship5 = Ship(0, 180, 240, 240, 1, screen, '4.png', 0)
ships = [ship1, ship2, ship3, ship4, ship5]
#shippositioning:
while not finished:
    pygame.display.update()
    clock.tick(FPS)
    screen.fill(black)
    field_creation(300, 100, 900, 700)
    field_creation(1000, 100, 1600, 700)
    for ship in ships:
        ship.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            number = whichship(ships)
            ships[number].drawShadow()
            if event.type == pygame.MOUSEBUTTONDOWN:
                placetheship(ships[number])
            
'''            
finished = False
while not finished:
    pygame.display.update()
    clock.tick(FPS)
    screen.fill(black)
    field_creation(300, 100, 900, 700)
    field_creation(1000, 100, 1600, 700)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        
        event_handler(cells)
        event_handler(enemycells)


'''
pygame.quit()
