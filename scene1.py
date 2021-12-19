import pygame
from graphics import Text

def pure_screen(screen, text: str):
    '''
    функция рисует заставку
     screen - экран, на котором рисуется заставка
     text - текст, который пишется, начиная с координаты (50, 50)
     выход из состояния заставки происходит по нажатии мышки
    '''
    clock = pygame.time.Clock()
    finished = False
    while not finished:
        pygame.display.update()
        clock.tick(30)
        screen.fill((242, 221, 198))
        Text(50, 50, 1000, 1000, 1, screen, text, (14, 41, 74)).draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                finished = True