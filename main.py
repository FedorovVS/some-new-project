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
number = -1
'''
ship1 = Ship(0, 0, 240, 60, 1, screen, '1.png', 0)
ship2 = Ship(0, 60, 240, 120, 1, screen, '2.png', 0)
ship3= Ship(0, 120, 240, 180, 1, screen, '3.png', 0)
ship4 = Ship(0, 180, 240, 240, 1, screen, '4.png', 0)
ship5 = Ship(0, 180, 240, 240, 1, screen, '4.png', 0)
ships = [ship1, ship2, ship3, ship4, ship5]
'''
ships = []
for i in range (0, 5):
    ships.append(Ship(0, i*60, 240, (i+1) * 60, 1, screen, str(i+1) +'.png', 0))
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
        if event.type == pygame.MOUSEBUTTONDOWN:
                placetheship(ships[number])
    if number != -1:
        ships[number].drawShadow()
            
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
