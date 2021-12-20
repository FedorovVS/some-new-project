import pygame
from lib.graphics import Ship, Text
from scenes.scene1 import pure_screen
from scenes.scene2 import eventer
from scenes.scene3 import Window
from lib.format import Cell, Cell3, convert_Cell_to_Cell3_list


window_width = 1700
"""Ширина окна"""

window_height = 800
"""Высота окна"""

pygame.init()

screen = pygame.display.set_mode((window_width, window_height))

pure_screen(screen, 'Чтобы начать расставлять корабли, нажмите на экран')

pygame.display.update()
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
finished = False

# shipdefinition
number = -1
ships = []
for i in range(0, 5):
    k = i + 1
    if i == 4:
        k = 1
    ships.append(Ship(0, i * 60, 240, (i + 1) * 60, 1, screen,
                 '{name}.png'.format(name=str(k)), 0))

# fielddefinition
cells = []
for a in range(10):
    cells.append([])
    for b in range(10):
        cells[a].append(Cell(a, b, 300 + 60 * a, 100 + 60 * b))
enemycells = []
for a in range(10):
    enemycells.append([])
    for b in range(10):
        enemycells[a].append(Cell(a, b, 1000 + 60 * a, 100 + 60 * b))

# shippositioningfirstplayer:
eventer(ships, cells, screen)

# shippositioningsecondplayerini
pure_screen(screen, 'Теперь следующий игрок расставляет корабли')

ENEMYships = []
for i in range(0, 5):
    k = i + 1
    if i == 4:
        k = 1
    ENEMYships.append(Ship(0, i * 60, 240, (i + 1) * 60, 1,
                      screen, '{name}.png'.format(name=str(k)), 0))
eventer(ENEMYships, enemycells, screen)
cells = convert_Cell_to_Cell3_list(cells)
enemycells = convert_Cell_to_Cell3_list(enemycells)

player1_window = Window(screen, cells, enemycells)
player2_window = Window(screen, enemycells, cells)
pure_screen(
    screen,
    'Начинается основной этап игры. Чтобы было веселее играть, сделаем фон менее мрачным.')
while True:
    player1_window.main_loop()
    if player1_window.score == 5:
        pure_screen(screen, 'Победил игрок 1, с чем мы его и поздравляем : D ')
        pygame.quit()
    pure_screen(screen, 'И снова меняемся')
    player2_window.main_loop()
    if player2_window.score == 5:
        pure_screen(screen, 'Победил игрок 2, с чем мы его и поздравляем :*) ')
        pygame.quit()
    pure_screen(screen, 'Теперь следующий игрок делает выстрел (:\\/) ')

pygame.quit()
