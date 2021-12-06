import pygame 
from pygame.draw import ellipse, circle, polygon, rect, line
from random import randint, choice
import time

class GraphObject:

    def __init__ (self, x0, y0, x1, y1, obj_type, screen):
        '''
        инициализация графического объекта

        Args:
        x0 y0 - координаты левого верхнего угла
        x1 y1 - координаты правого нижнего угла
        obj_type - тип объекта
        screen
        '''
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.obj_type = obj_type
        self.screen = screen
        self.time0 = time.time()
        self.origin = pygame.Surface(x1-x0, y1-y0)

    def draw (self):
        pass

class Ship (GraphObject):
    '''
    корбаль

    '''

    def __init__(self, x0, y0, x1, y1, obj_type, screen, filename):
        '''
        инициализаци корабля

        Args:
        x0 y0 - координаты левого верхнего угла
        x1 y1 - координаты правого нижнего угла
        obj_type - тип объекта
        screen
        filename - имя файла со скином
        '''
        super().__init__(x0, y0, x1, y1, obj_type, screen)

        self.img = pygame.image.load(filename).convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.x1-self.x0, self.y1-self.y0))
        self.img.set_colorkey('#00FF00')

    def draw(self):
        super().draw()
        self.screen.blit(self.img, (self.x0, self.y0))

class Water (GraphObject):

    def draw(self):
        super().draw()

        COLORS = [(0,204,255), (0,89,255), (0,255,216), (0,12,216)]

        Nx = 20
        Ny = 30

        W = self.x1 - self.x0
        H = self.y1 - self.y0

        time_difference = time.time() - self.time0

        if time_difference > 0.5:

            for i in range(Nx):
                for j in range(Ny):
                    rect(self.origin, choice(COLORS), (i*W/Nx, j*H/Ny, W/Nx, H/Ny))
            self.time0 = time.time()
        self.screen.blit(self.origin, self.x0, self.y0)

class Stressing (GraphObject):

    def draw(self):
        super().draw()

        additional_surface = pygame.Surface((self.x1-self.x0, self.y1-self.y0))
        additional_surface.set_alpha(100)
        additional_surface.fill('#7FFFD4')
        self.screen.blit(additional_surface, self.x0, self.y0)

class EmptyCheck (GraphObject):
    def draw(self):
        super().draw()

        additional_surface = pygame.Surface((self.x1-self.x0, self.y1-self.y0))
        additional_surface.set_alpha(100)
        additional_surface.fill('#FF0000')
        self.screen.blit(additional_surface, self.x0, self.y0)

class Smoke (GraphObject):
    def draw(self):
        super().draw()
    pass

class Fire (GraphObject):
    def draw(self):
        super().draw()
    pass

class Button (GraphObject):
    def draw(self):
        super().draw()
    pass

class Text (GraphObject):
    def draw(self):
        super().draw()
    pass