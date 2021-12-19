import pygame
import numpy
from smth import field_creation, caption_creation, mousepos, event_handler
from gr1 import Ship, Text
from shipmovement import placetheship, whichship, shiphere
from scene2 import eventer
from scene3 import Window
from format import Cell, Cell3, convert_Cell_to_Cell3_list

def pure_screen(screen, text):
    clock = pygame.time.Clock()
    finished = False
    while not finished:
        pygame.display.update()
        clock.tick(30)
        screen.fill('#80daeb')
        Text(50, 50, 1000, 1000, 1, screen, text).draw()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                finished = True



window_width = 1700
"""Ширина окна"""

window_height = 800
"""Высота окна"""

pygame.init()

screen = pygame.display.set_mode((window_width, window_height))

pure_screen(screen, 'Для начала нажмите на экран')

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

pure_screen(screen, 'Теперь следующий игрок')

ENEMYships = []
for i in range (0, 5):
    k = i + 1
    if i == 4:
        k = 1
    ENEMYships.append(Ship(0, i*60, 240, (i+1) * 60, 1, screen, '{name}.png'.format(name=str(k)), 0))
eventer(ENEMYships, enemycells, screen)
for a in range (10):
    for b in range(10):
        print(cells[a][b].state, cells[a][b].warship.x0 if cells[a][b].state else 0)


cells = convert_Cell_to_Cell3_list(cells)
enemycells = convert_Cell_to_Cell3_list(enemycells)

player1_window = Window(screen, cells, enemycells)
player2_window = Window(screen, enemycells, cells)

while 1:
    pure_screen(screen, 'Теперь следующий')
    player1_window.main_loop()
    if player1_window.score == 5:
        pure_screen(screen, 'Победил игрок 1, с чем мы его и поздравляем')
        pygame.quit()
    pure_screen(screen, 'И снова меняемся')
    player2_window.main_loop()
    if player2_window.score == 5:
        pure_screen(screen, 'Победил игрок 2, с чем мы его и поздравляем')
        pygame.quit()
        
pygame.quit()
