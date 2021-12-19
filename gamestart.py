import pygame

window_width = 1700
"""Ширина окна"""

window_height = 800
"""Высота окна"""

pygame.init()

FPS = 30
screen = pygame.display.set_mode((window_width, window_height))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


def field_creation(x1, y1, x2, y2, screen, color = white):
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
    caption_creation(x1, y1, x2, y2, screen)
    
    
def caption_creation(x1, y1, x2, y2, screen, window_width = 1000, window_height = 800):
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
        write(screen, str(i+1), x, y1)
        write(screen, s[i], x1, y)
        x += h
        y += h

def event_handler(cells:list):
    '''
    changes the state of a cell, if one has been pressed on
    or must write that one had been killed already
    '''
    if mousepos(cells) != 0:      
        one = mousepos(cells)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if mousepos(cells) != 0:      
            one = mousepos(cells)
            if one.state > 1:
                write(screen, 'It had been', 30, 100)
                write(screen, 'already pressed on', 30, 130)
            else:
                mousepos(cells).nowdead()
                x, y = one.x,one.y
                #supposed to be fire, may be a marker
                pygame.draw.line(screen, (255, 0, 0), (x, y), (x+60, y+60))
                pygame.draw.line(screen, (255,0,0), (x, y+60), (x+60, y))

def write(screen, signature:str, x, y, color = (255, 255, 255)):
    '''
    writes what you want
    signature is ur text
    x, y define the position of the very first letter,
    color is the color of text( white automatically)
    '''
    f1 = pygame.font.Font(None, 30)
    pygame.font.SysFont('arial', 72)
    text1 = f1.render(signature, 1, color)
    screen.blit(text1, (x, y))  
    
def mousepos(cells:list):
    (x, y) = pygame.mouse.get_pos()
    if 99 < y < 701:
        xmin = cells[0][0].x
        xmax = cells[len(cells)-1][0].x
        if xmin - 1 < x < xmax + 61:
            i = (x - 1 - xmin) // 60
            j = (y - 100) //60
            return cells[i][j]
        else:
            return 0    
    else:
        return 0

