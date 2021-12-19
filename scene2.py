import pygame
import numpy
from smth import field_creation, caption_creation, mousepos, event_handler
from gr1 import Ship, WaterBlock
from shipmovement import placetheship, whichship, shiphere

def eventer(ships:list, cells:list, screen, FPS = 60):
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (7, 11, 18)
    clock = pygame.time.Clock()
    finished = False
#shipdefinition
    number = -1
    water1 = WaterBlock(420, 220, 780, 580, 1, screen)
    water2 = WaterBlock(1120, 220, 1480, 580, 1, screen)
    while not finished:         
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
                ships[number].turn_flag = not(ships[number].turn_flag)
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                ships[number].rotate(180)
        if pygame.key.get_pressed()[pygame.K_RETURN]:
                finished = True
