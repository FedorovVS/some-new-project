import pygame
from gamestart import field_creation, mousepos
from graphics import Ship, WaterBlock
from shipmovement import placetheship, whichship, shiphere


def clearall(cells: list):
    '''
    функция проверяет лежит ли в клетке корабль
    если нет, то присваивает атрибуту ее состояния значение 0
    '''
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            cells[i][j].clear()


def eventer(ships: list, cells: list, screen, FPS=30):
    blue = (0, 49, 83)
    clock = pygame.time.Clock()
    finished = False
    number = -1
    water1 = WaterBlock(420, 220, 780, 580, 1, screen)
    water2 = WaterBlock(1120, 220, 1480, 580, 1, screen)
    while not finished:
        clearall(cells)
        check(ships, cells)
        pygame.display.update()
        clock.tick(FPS)
        screen.fill(blue)
        water1.draw()
        water2.draw()
        for ship in ships:
            ship.draw()
        field_creation(300, 100, 900, 700, screen)
        field_creation(1000, 100, 1600, 700, screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[
                    0] == 1:
                number = whichship(ships)
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pressed()[
                    0] == 0:
                cell = mousepos(cells)
                if cell != 0:
                    if placetheship(ships[number], cell, cells, screen) == 1:
                        shiphere(cells, ships[number])
                    number = 10
        if number != 10:
            ships[number].drawShadow()
            if pygame.mouse.get_pressed()[2] == 1:
                ships[number].rotate(90)
                ships[number].turn_flag = not(ships[number].turn_flag)
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            finished = True
