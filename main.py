import pygame
import numpy
from smth import field_creation
from smth import caption_creation
from smth import mousepos
from smth import Cell

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
#myship = Ship(0, 0, 240, 60, 1, screen, '1.png')
#shipdefinition
#shippositioning:
clock = pygame.time.Clock()
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




