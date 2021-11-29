import pygame
import numpy



window_width = 1000
"""Ширина окна"""

window_height = 800
"""Высота окна"""

pygame.init()

FPS = 30
screen = pygame.display.set_mode((window_width, window_height))
color = (255, 255, 255)

def field_creation(surface = screen, window_width = 1000, window_height = 800, color = color):
    '''
    creates window 10 x 10
    '''
    x1 = 300
    y1 = 100
    x2 = 900
    y2 = 700
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
    
def caption_creation(surface = screen, window_width = 1000, window_height = 800):
    '''
    writes numbers and letters on the left and top side of the field
    '''
    x1 = 300 - 30
    y1 = 100 - 30
    WHITE = (255, 255, 255)
    s = 'abcdefghijklmnop'
    x2 = 900
    y2 = 700
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
            i = (x - 300) // 60
            j = (y - 100) //60
            if 299 < x < 901 and 99 < y < 701:
                i = (x - 300) // 60
                j = (y - 100) //60
                if (cells[i][j]).state > 1 :
                    write('It had been already pressed on', 30, 100)
                else:
                    Cell.nowdead(cells[i][j])

def write(signature:str, x, y, color = (255, 255, 255)):
    f1 = pygame.font.Font(None, 30)
    pygame.font.SysFont('arial', 72)
    text1 = f1.render(signature, 1, color)
    screen.blit(text1, (x, y))  
    
     
class Cell:
    def __init__(self, i, j, state = 0):
        """ Конструктор класса Cell
        Args:
        i - first number of the cell in array
        j - second number of the cell in array
        state describes if the cell contains ship, whether it's dead etc.
        0 - empty
        1 - has ship in it and is alive
        2 - empty, now dead
        3 - had ship in it, now dead
        x, y - position of the top left corner 
        """
        self.i = i
        self.j = j
        self.state = state
        self.x = 300 + 60 * i
        self.y = 100 + 60 * i
    
    def nowdead(self):
        self.state += 2
        
cells = []
for  a in range (10):
    cells.append([])
    for b in range (10):
        cells[a].append(Cell(a, b, 0))  

    
     
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    pygame.display.update()
    clock.tick(FPS)
    field_creation()
    caption_creation()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        event_handler(cells)
        

pygame.quit()

