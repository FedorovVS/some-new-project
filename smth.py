import pygame
import numpy



window_width = 1700
"""Ширина окна"""

window_height = 800
"""Высота окна"""

pygame.init()

FPS = 30
screen = pygame.display.set_mode((window_width, window_height))
white = (255, 255, 255)
red = (255, 0, 0)


def field_creation(x1, y1, x2, y2, color = white, surface = screen):
    '''
    creates window 10 x 10
    '''
    N = 10
    pygame.draw.rect(screen, color, (x1, y1, x2 - x1, y2 - y1), 2)
    h = (x2 - x1) // (N)
    x = x1 + h
    y = y1 + h 
    for i in range(N-1):
        pygame.draw.line(screen, color, (x, y1), (x, y2))
        pygame.draw.line(screen, color, (x1, y), (x2, y))
        x += h
        y += h
    
    
def caption_creation(x1, y1, x2, y2, surface = screen, window_width = 1000, window_height = 800):
    '''
    writes numbers and letters on the left and top side of the field
    '''
    x1 = x1 - 30
    y1 = y1 - 30
    WHITE = (255, 255, 255)
    s = 'abcdefghijklmnopqrstuvwxyz'
    N = 10
    h = (x2 - x1 + 20) // (N+1)
    x = x1 + h
    y = y1 + h 
    for i in range(N):
        write(str(i+1), x, y1)
        write(s[i], x1, y)
        x += h
        y += h
    
def event_handler(cells:list):
    '''
    changes the state of a cell, if one has been pressed on
    or must write that one had been killed already
    
    
    '''
    
    if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            minx = cells[0][0].x
            maxx = cells[len(cells)-1][0].x 
            if minx-1 < x < maxx + 61 and 99 < y < 701:
                i = (x - minx) // 60
                j = (y - 100) //60
                if (cells[i][j]).state > 1 :
                    write('It had been', 30, 100)
                    write('already pressed on', 30, 130)
                else:
                    Cell.nowdead(cells[i][j])
                    x, y = (cells[i][j]).x,(cells[i][j]).y
                    #supposed to be fire, may be a marker
                    pygame.draw.line(screen, (255, 0, 0), (x, y), (x+60, y+60))
                    pygame.draw.line(screen, (255,0,0), (x, y+60), (x+60, y))

def write(signature:str, x, y, color = (255, 255, 255)):
    f1 = pygame.font.Font(None, 30)
    pygame.font.SysFont('arial', 72)
    text1 = f1.render(signature, 1, color)
    screen.blit(text1, (x, y))  
    
def mousepos(cells:list, enemycells = []):
    (x, y) = pygame.mouse.get_pos()
    xmin = cells[0][0]
    xmax = cells[len(cells)-1][0]
    if xmin - 1 < x < xmax + 1  and 99 < y < 701:
        i = (x - 300) // 60
        j = (y - 100) //60
        return cells[i][j]
    xmin = enemycells[0][0]
    xmax = cells[len(cells)-1][0]
    elif xmin - 1 < x < xmax + 1  and 99 < y < 701:
        i = (x - 300) // 60
        j = (y - 100) //60
        return enemycells[i][j]
    else:
        return 0
        
     
class Cell:
    def __init__(self, i, j, x, y, state = 0, ship = 0):
        """ Конструктор класса Cell
        Args:
        i - first number of the cell in array
        j - second number of the cell in array
        state describes if the cell contains ship, whether it's dead etc.:
        0 - empty and has not been shot
        1 - has ship in it and is alive
        2 - empty, now dead
        3 - had ship in it, now dead
        parameter 'ship' describes what type of ship lies in the cell
        x, y - position of the top left corner 
        """
        self.i = i
        self.j = j
        self.state = state
        self.ship = ship
        self.x = x
        self.y = y
    
    def nowdead(self):
        self.state += 2
        
        
        
        
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
    
     
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    pygame.display.update()
    clock.tick(FPS)
    field_creation(300, 100, 900, 700)
    field_creation(1000, 100, 1600, 700)
    caption_creation(300, 100, 900, 700)
    caption_creation(1000, 100, 1600, 700)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        event_handler(cells)
        event_handler(enemycells)

pygame.quit()

