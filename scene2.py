import pygame
import numpy
from smth import field_creation, caption_creation, mousepos, Cell, event_handler
from gr1 import Ship
from shipmovement import placetheship, whichship, shiphere

def eventer(ships:list, cells:list, screen, FPS = 60):
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    clock = pygame.time.Clock()
    finished = False

#shipdefinition
    number = -1
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
            if pygame.key.get_pressed()[pygame.K_KP_ENTER]:
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                number = whichship(ships)
            if event.type == pygame.MOUSEBUTTONUP:
                cell = mousepos(cells)
                if cell != 0:
                    if placetheship(ships[number], cell, cells, screen) == 1:
                        shiphere(cells,ships[number]) 
                #ships[number].backtonormal()
                    number = -1
        if number != -1:
            ships[number].drawShadow()
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                ships[number].rotate(90)
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                ships[number].rotate(180)
