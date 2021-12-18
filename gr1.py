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
        self.origin = pygame.Surface((self.x1-self.x0, self.y1-self.y0))

    def draw (self):
        pass

class Ship (GraphObject):
    '''
    корбаль
    '''

    def __init__(self, x0, y0, x1, y1, obj_type, screen, filename, turn_flag):
        '''
        инициализация корабля
        Args:
        x0 y0 - координаты левого верхнего угла
        x1 y1 - координаты правого нижнего угла
        obj_type - тип объекта
        screen
        filename - имя файла со скином
        turn_flag - поворот (вертикальная ориентация)
        '''
        super().__init__(x0, y0, x1, y1, obj_type, screen)

        self.img = pygame.image.load(filename).convert_alpha()
        if turn_flag:
            self.img = pygame.transform.rotate(self.img, 90)
        self.img = pygame.transform.scale(self.img, (self.x1-self.x0, self.y1-self.y0))
        self.img.set_colorkey('#00FF00')

    def draw(self):
        '''
        Функция рисования объекта
        '''
        super().draw()
        self.screen.blit(self.img, (self.x0, self.y0))

    def drawShadow(self):
        '''
        Функция рисования тени корабля
        '''
        self.img.set_alpha(100)
        position = pygame.mouse.get_pos()
        self.screen.blit(self.img, (position[0]-(self.x1-self.x0)/2 ,position[1]-(self.y1-self.y0)/2))


class Water (GraphObject):
    '''
    Водяной фон с переодичным размытием
    '''

    def draw(self):
        '''
        Функция рисования объекта
        '''
        super().draw()

        COLORS = [(0,204,255), (0,89,255), (0,255,216), (0,12,216)]

        Nx = 20
        Ny = 30
        W = self.x1 - self.x0
        H = self.y1 - self.y0

        time_difference = time.time() - self.time0
        frec = 3
        time_difference /= 3

        if time_difference > frec:

            for i in range(Nx):
                for j in range(Ny):
                    rect(self.origin, choice(COLORS), (i*W/Nx, j*H/Ny, W/Nx, H/Ny))
            self.time0 = time.time()

        

        if 5**(1+3*(time_difference-frec/2)**2) < 50 :
            self.originX = pygame.transform.smoothscale(self.origin, (int(W/5**(1+3*(time_difference-frec/2)**2)), (int(H/5**(1+3*(time_difference-frec/2)**2)))))
        else:
            self.originX = pygame.transform.smoothscale(self.origin, (int(W/50), (int(H/50))))
        self.originX = pygame.transform.smoothscale(self.originX,(W,H))
        self.screen.blit(self.originX, (self.x0, self.y0))


class Stressing (GraphObject):
    '''
    Выделение заданным цветом
    '''
    def draw(self):
        '''
        Функция рисования объекта
        '''
        super().draw()

        additional_surface = pygame.Surface((self.x1-self.x0, self.y1-self.y0))
        additional_surface.set_alpha(150)  # прозрачность
        additional_surface.fill('#7FFFD4')  # цвет выделения
        self.screen.blit(additional_surface, (self.x0, self.y0))

class EmptyCheck (GraphObject):
    '''
    Специальное выделение
    '''
    def draw(self):
        '''
        Функция рисования объекта
        '''
        super().draw()

        additional_surface = pygame.Surface((self.x1-self.x0, self.y1-self.y0))
        additional_surface.set_alpha(150)
        additional_surface.fill('#FF0000')
        self.screen.blit(additional_surface, (self.x0, self.y0))

class Smoke (GraphObject):
    '''
    Дымы
    '''
    def __init__(self, x0, y0, x1, y1, obj_type, screen):
        '''
        Инициализация объекта класса Smoke
        '''
        super().__init__(x0, y0, x1, y1, obj_type, screen)

        self.N = 5
        self.begin_scale = 5
        self.end_scale = min((x1-x0), (y1-y0))
        self.speed = 0.5
        self.COLORS = ['#999999']
        self.frec = 0.1

        self.position_x = []
        self.position_y = []
        self.stain_size = []
        self.stain_color = []
        self.surfaces = []

    def draw(self):
        '''
        Функция рисования объекта
        '''
        super().draw()

        time_difference = time.time() - self.time0
        if time_difference > self.frec:
            if len(self.stain_size):
                if self.stain_size[0] >= self.end_scale/4:
                    self.position_x.pop(0)
                    self.position_y.pop(0)
                    self.stain_size.pop(0)
                    self.surfaces.pop(0)
                    self.stain_color.pop(0)
            self.time0 = time.time()

            self.position_x.append(randint(int(-self.end_scale/4), int(self.end_scale/4)))
            self.position_y.append(randint(int(-self.end_scale/4), int(self.end_scale/4)))
            self.stain_size.append(self.begin_scale)
            self.surfaces.append(pygame.Surface((self.end_scale,self.end_scale)))
            self.stain_color.append(choice(self.COLORS))

        self.stain_size = [stain + self.speed for stain in self.stain_size]
        for num in range(len(self.stain_size)):
            self.surfaces[num].set_alpha(200-200*self.stain_size[num]/self.end_scale*4)
            self.surfaces[num].fill('#000000')
            circle(self.surfaces[num], self.stain_color[num], (int(self.end_scale/2), int(self.end_scale/2)), self.stain_size[num])
            self.surfaces[num].set_colorkey('#000000')
            self.screen.blit(self.surfaces[num], (self.x0+self.position_x[num], self.y0+self.position_y[num]))


class Fire (Smoke):
    def __init__(self, x0, y0, x1, y1, obj_type, screen):
        '''
        Инициализация объекта класса Fire
        '''
        super().__init__(x0, y0, x1, y1, obj_type, screen)

        self.COLORS = ['#f7943c', '#ffcf48', '#ee9086', '#99958c', '#778899', '#FFFFFF']
        self.frec = 0.5

class WaterBlock (GraphObject):
    def __init__(self, x0, y0, x1, y1, obj_type, screen):
        super().__init__(x0, y0, x1, y1, obj_type, screen)

        self.N = 5
        self.begin_scale = 5
        self.end_scale = min((x1-x0), (y1-y0))
        self.speed = 1.5
        self.COLORS = [(0,204,255), (0,89,255), (0,255,216), (0,12,216)]
        self.frec = 1

        self.position_x = []
        self.position_y = []
        self.stain_size = []
        self.stain_color = []
        self.surfaces = []

    def draw(self):
        super().draw()

        time_difference = time.time() - self.time0
        if time_difference > self.frec:
            if len(self.stain_size):
                if self.stain_size[0] >= self.end_scale:
                    self.position_x.pop(0)
                    self.position_y.pop(0)
                    self.stain_size.pop(0)
                    self.surfaces.pop(0)
                    self.stain_color.pop(0)
            self.time0 = time.time()

            self.position_x.append(randint(int(-self.end_scale/2), int(self.end_scale/2)))
            self.position_y.append(randint(int(-self.end_scale/2), int(self.end_scale/2)))
            self.stain_size.append(self.begin_scale)
            self.surfaces.append(pygame.Surface((self.end_scale,self.end_scale)))
            self.stain_color.append(choice(self.COLORS))

        self.stain_size = [stain + self.speed for stain in self.stain_size]
        for num in range(len(self.stain_size)):
            self.surfaces[num].set_alpha(200-200*self.stain_size[num]/self.end_scale)
            self.surfaces[num].fill('#000000')
            rect(self.surfaces[num], self.stain_color[num], (0, 0, int(self.stain_size[num]), int(self.stain_size[num])))
            self.surfaces[num].set_colorkey('#000000')
            self.screen.blit(self.surfaces[num], (self.x1/2+self.x0/2+self.position_x[num]-self.stain_size[num]/2, self.y1/2+self.y0/2+self.position_y[num]-self.stain_size[num]/2))

class Button (GraphObject):

    def __init__(self, x0, y0, x1, y1, obj_type, screen, text):
        super().__init__(x0, y0, x1, y1, obj_type, screen)

        self.text = text
        self.border = 3

    def draw(self):
        rect(self.screen, '#000080', (self.x0, self.y0, self.x1-self.x0, self.y1-self.y0))

        font = pygame.font.SysFont('ComicSansMs', 30)
        self.screen.blit(font.render(self.text, 0, '#9932cc'), (self.x0+self.border, self.y0+self.border))

class Text (GraphObject):
    def __init__(self, x0, y0, x1, y1, obj_type, screen, text, color='#9932cc'):
        super().__init__(x0, y0, x1, y1, obj_type, screen)

        self.text = text
        self.color = color

    def draw(self):

        font = pygame.font.SysFont('ComicSansMs', 30)
        self.screen.blit(font.render(self.text, 0, self.color), (self.x0, self.y0))
