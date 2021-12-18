import pygame
import numpy
from smth import field_creation, caption_creation, mousepos, Cell, event_handler
from gr1 import Ship
from shipmovement import placetheship, whichship, shiphere
from scene2 import eventer

window_width = 1700
"""Ширина окна"""

window_height = 800
"""Высота окна"""

pygame.init()

screen = pygame.display.set_mode((window_width, window_height))

pygame.display.update()
screen.fill((0, 0, 0))
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

#fielddefinition
cells = []
for  a in range (10):
    cells.append([])
    for b in range (10):
        cells[a].append(Cell(a, b, 300 + 60 * a, 100 + 60 * b))
enemycells = []
for  a in range (10):
    enemycells.append([])
    for b in range (10):
        enemycells[a].append(Cell(a, b, 1000 + 60 * a, 100 + 60 * b))

#shippositioning:
eventer(ships, cells, screen)
            
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
