import pygame
import numpy
from smth import field_creation, caption_creation, mousepos, Cell
from gr1 import Ship
from shipmovement import placetheship, whichship

window_width = 1700
"""Ширина окна"""

window_height = 800
"""Высота окна"""

pygame.init()

FPS = 10
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.update()
screen.fill(black)
clock = pygame.time.Clock()
finished = False
#shipdefinition
number = -1
ships = []
for i in range (0, 5):
    k = i + 1
    if i == 4:
        k = 1
    ships.append(Ship(0, i*60, 240, (i+1) * 60, 1, screen, '{name}.png'.format(name=str(k)), 0))
#shippositioning:
while not finished: 
    pygame.display.update()
    clock.tick(FPS)
    screen.fill(black)
    for i, ship in enumerate(ships):
        ship.draw()
    field_creation(300, 100, 900, 700, screen)
    field_creation(1000, 100, 1600, 700, screen)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            number = whichship(ships)
        if event.type == pygame.MOUSEBUTTONUP:
            placetheship(ships[number])
            number = -1
    if number != -1:
        ships[number].drawShadow()
        if pygame.key.get_pressed()[pygame.K_LEFT] == 1:
            ships[number].rotate(90)
        if pygame.key.get_pressed()[pygame.K_RIGHT] == 1:
            ships[number].rotate(180)
            
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
