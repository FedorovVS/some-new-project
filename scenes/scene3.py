import pygame
from pygame.draw import rect
from lib.graphics import WaterBlock, Ship, Text, Smoke, EmptyCheck, Fire


class Window():
    '''
    Класс окна приложения
    '''

    def __init__(self, screen, friendly_cells, enemy_cells):
        '''
        Инициализация объекта класса Window
        '''
        self.scale = 500
        '''
        Условный масштаб
        '''
        self.H = self.scale
        '''
        Высота окна
        '''
        self.W = 3 * self.scale
        '''
        Длина окна
        '''
        self.FPS = 30
        '''
        FPS
        '''
        self.screen = screen
        '''
        pygame.screen
        '''
        self.check_size = int(self.scale * 0.08)
        '''
        Размер клетки поля
        '''
        self.base_color = '#000000'
        '''
        Основной цвет
        '''
        self.special_messages = [['hello!', 60, '#FFFFFF'], [
            'buddy', 70, '#FFFFFF'], ['shall we play?', 80, '#FFFFFF']]
        '''
        Список сообщений, подлежащих отображению

        Каждое сообщение представляет из себя упорядоченный список с несколькими параметрами [message, time, color]

        message : str - сообщение
        time : int - временные отсчеты до удаления
        color : str - цвет сообщения
        '''
        self.graphic_objects = [WaterBlock(int(
            i * self.W / 3), 0, int((i + 1) * self.W / 3), self.H, 1, self.screen) for i in range(3)]
        '''
        Список графических сущностей
        '''

        self.friendly_cells = friendly_cells
        self.enemy_cells = enemy_cells
        self.score = 0

    def GR_draw_caption(self, x0, y0):
        '''
        GR рисование подписей к полю 10х10

        x0, y0 - координаты левой верхней точки поля
        '''
        x0 -= int(self.check_size * 3 / 4)
        y0 -= int(self.check_size * 3 / 4)
        x = x0 + self.check_size
        y = y0 + self.check_size
        for i in range(10):
            Text(x, y0, 1000, 1000, 1, self.screen,
                 str(i + 1), self.base_color).draw()
            Text(x0, y, 1000, 1000, 1, self.screen, chr(
                ord('a') + i), self.base_color).draw()
            x += self.check_size
            y += self.check_size

    def GR_draw_checks(self, x0, y0):
        '''
        GR рисование сетки поля 10х10

        x0, y0 - координаты левой верхней точки поля
        '''
        x1 = x0 + self.check_size * 10
        y1 = y0 + self.check_size * 10
        rect(self.screen, self.base_color, (x0, y0, x1 - x0, y1 - y0), 2)
        x = x0 + self.check_size
        y = y0 + self.check_size
        for i in range(9):
            pygame.draw.line(self.screen, self.base_color, (x, y0), (x, y1))
            pygame.draw.line(self.screen, self.base_color, (x0, y), (x1, y))
            x += self.check_size
            y += self.check_size

    def MG_message_manager(self, x0, y0):
        '''
        Менеджер сообщений игроку

        x0, y0 : int - координаты левой верхней точки области для сообщений
        '''

        for message in self.special_messages:
            Text(x0, y0, 2000, 2000, 1, self.screen,
                 message[0], message[2]).draw()
            if message[1] > 0:
                message[1] -= 1
            else:
                self.special_messages.remove(message)
            y0 += self.check_size

    def MG_graphics_manager(self):
        '''
        Менеджер графических объектов
        '''
        self.screen.fill('#80daeb')

        self.control_friendly_objects(self.friendly_cells, 30, 30)

        for object in self.graphic_objects:
            object.draw()

        self.GR_draw_caption(30, 30)
        self.GR_draw_checks(30, 30)

        self.GR_draw_caption(530, 30)
        self.GR_draw_checks(530, 30)

        self.MG_message_manager(1030, 0)

    def mouse_position(self, cells: list, x0, y0):
        '''
        Текущая позиция мыши в терминах дескретного игрового поля

        sells : list - список объектов клеток
        x0, y0 : int - координаты левой верхней точки поля
        '''
        (x, y) = pygame.mouse.get_pos()
        if x0 < x < x0 + 10 * self.check_size and y0 < y < y0 + 10 * self.check_size:
            i = (x - x0) // self.check_size
            j = (y - y0) // self.check_size
            return cells[i][j]
        else:
            return 0

    def control_graphic_objects(self, x0, y0, cells: list, active_cell):
        '''
        Контроль списка графических обектов

        x0, y0 : int - верхняя левая точка игрового поля
        cells : list - список клеток поля
        active_cell : Cell - координаты активированной клетки в терминах дескретного поля
        '''

        def check_cell(cells, i, j, i_prev=-1, j_prev=-1):
            cnt = 0
            if cells[i][j].state == 3:
                cnt += 1
                if i != 0 and (i - 1 != i_prev or j != j_prev):
                    cnt += check_cell(cells, i - 1, j, i, j)
                if i + 1 != 10 and (i + 1 != i_prev or j != j_prev):
                    cnt += check_cell(cells, i + 1, j, i, j)
                if j != 0 and (i != i_prev or j - 1 != j_prev):
                    cnt += check_cell(cells, i, j - 1, i, j)
                if j + 1 != 10 and (i != i_prev or j + 1 != j_prev):
                    cnt += check_cell(cells, i, j + 1, i, j)
            return cnt

        def fire_cell(self, x0, y0, cells, i, j, i_prev=-1, j_prev=-1):

            if cells[i][j].state == 3:
                X = x0 + i * self.check_size
                Y = y0 + j * self.check_size

                for obj in self.graphic_objects:
                    if (obj.x0, obj.y0) == (X, Y):
                        self.graphic_objects.remove(obj)
                        self.graphic_objects.append(
                            Fire(
                                X,
                                Y,
                                X +
                                self.check_size,
                                Y +
                                self.check_size,
                                1,
                                self.screen))

                if i != 0 and (i - 1 != i_prev or j != j_prev):
                    fire_cell(self, x0, y0, cells, i - 1, j, i, j)
                if i + 1 != 10 and (i + 1 != i_prev or j != j_prev):
                    fire_cell(self, x0, y0, cells, i + 1, j, i, j)
                if j != 0 and (i != i_prev or j - 1 != j_prev):
                    fire_cell(self, x0, y0, cells, i, j - 1, i, j)
                if j + 1 != 10 and (i != i_prev or j + 1 != j_prev):
                    fire_cell(self, x0, y0, cells, i, j + 1, i, j)

        # просто пролистайте дальше, оно вам не надо

        if active_cell.state == 2:
            self.graphic_objects.append(EmptyCheck(x0 +
                                                   active_cell.i *
                                                   self.check_size, y0 +
                                                   active_cell.j *
                                                   self.check_size, x0 +
                                                   (active_cell.i +
                                                    1) *
                                                   self.check_size, y0 +
                                                   (active_cell.j +
                                                    1) *
                                                   self.check_size, 1, self.screen))
        elif active_cell.state == 3:
            self.graphic_objects.append(Smoke(x0 +
                                              active_cell.i *
                                              self.check_size, y0 +
                                              active_cell.j *
                                              self.check_size, x0 +
                                              (active_cell.i +
                                               1) *
                                              self.check_size, y0 +
                                              (active_cell.j +
                                               1) *
                                              self.check_size, 1, self.screen))

            if check_cell(cells, active_cell.i, active_cell.j) == 4:
                # если вы уже здесь, то я завидую вашей стойкости.
                # Чтобы удовлетворить любопытство и развеять сомнение:
                # создаем объекты графических элементов, координаты, к
                # сожалению, записываются в не очень хорошем виде
                self.graphic_objects.append(Ship(x0 +
                                                 active_cell.ship_i *
                                                 self.check_size, y0 +
                                                 active_cell.ship_j *
                                                 self.check_size, (x0 +
                                                                   (active_cell.ship_i +
                                                                    4) *
                                                                   self.check_size) if not active_cell.ship_orientation else (x0 +
                                                                                                                              (active_cell.ship_i +
                                                                                                                               1) *
                                                                                                                              self.check_size), (y0 +
                                                                                                                                                 (active_cell.ship_j +
                                                                                                                                                  4) *
                                                                                                                                                 self.check_size) if active_cell.ship_orientation else (y0 +
                                                                                                                                                                                                        (active_cell.ship_j +
                                                                                                                                                                                                         1) *
                                                                                                                                                                                                        self.check_size), 1, self.screen, str(active_cell.ship) +
                                                 '.png', active_cell.ship_orientation))
                fire_cell(self, x0, y0, cells, active_cell.i, active_cell.j)
                self.score += 1

        # отсюда можно безопасно продолжить

    def MG_event_manager(self, cells: list, event):
        '''
        Менеджер событий

        cells : list - список объектов клеток
        event : pygame.event - событие
        '''
        click_result = -3

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked_cell = self.mouse_position(cells, 530, 30)
            if clicked_cell:
                click_result = clicked_cell.change_state()
                if click_result == 1:
                    self.special_messages.append(
                        ['Выберите другую клетку', 40, '#FF00FF'])
                else:
                    self.control_graphic_objects(530, 30, cells, clicked_cell)
        if click_result == -1:
            return 1
        else:
            return 0

    def control_friendly_objects(self, cells, X0, Y0):

        def check_object_list_for_coords(self, x0, y0, x1, y1):
            for obj in self.graphic_objects:
                if obj.x0 == x0 and obj.y0 == y0 and obj.x1 == x1 and obj.y1 == y1:
                    return 1

            return 0

        for i in range(10):
            for j in range(10):
                if cells[i][j].state == 2:
                    if not check_object_list_for_coords(self,
                                                        X0 + i * self.check_size,
                                                        Y0 + j * self.check_size,
                                                        X0 + (i + 1) * self.check_size,
                                                        Y0 + (j + 1) * self.check_size):
                        self.graphic_objects.append(EmptyCheck(X0 +
                                                               i *
                                                               self.check_size, Y0 +
                                                               j *
                                                               self.check_size, X0 +
                                                               (i +
                                                                1) *
                                                               self.check_size, Y0 +
                                                               (j +
                                                                   1) *
                                                               self.check_size, 1, self.screen))
                elif cells[i][j].state == 1 or cells[i][j].state == 3:
                    x0 = X0 + cells[i][j].ship_i * self.check_size
                    y0 = Y0 + cells[i][j].ship_j * self.check_size
                    x1 = X0 + (cells[i][j].ship_i + 4) * self.check_size if not cells[i][j].ship_orientation else X0 + (
                        cells[i][j].ship_i + 1) * self.check_size
                    y1 = Y0 + (cells[i][j].ship_j + 4) * self.check_size if cells[i][j].ship_orientation else Y0 + (
                        cells[i][j].ship_j + 1) * self.check_size
                    if not check_object_list_for_coords(self, x0, y0, x1, y1):
                        self.graphic_objects.append(
                            Ship(
                                x0, y0, x1, y1, 1, self.screen, str(
                                    cells[i][j].ship) + '.png', cells[i][j].ship_orientation))
                    if cells[i][j].state == 3:
                        if not check_object_list_for_coords(self,
                                                            X0 + i * self.check_size,
                                                            Y0 + j * self.check_size,
                                                            X0 + (i + 1) * self.check_size,
                                                            Y0 + (j + 1) * self.check_size):
                            self.graphic_objects.append(Smoke(X0 +
                                                              i *
                                                              self.check_size, Y0 +
                                                              j *
                                                              self.check_size, X0 +
                                                              (i +
                                                               1) *
                                                              self.check_size, Y0 +
                                                              (j +
                                                                  1) *
                                                              self.check_size, 1, self.screen))

    def main_loop(self):

        clock = pygame.time.Clock()
        finished = 0

        while not finished:
            self.MG_graphics_manager()
            pygame.display.update()

            clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                else:
                    finished = self.MG_event_manager(self.enemy_cells, event)

        time = 30

        while time:
            time -= 1
            self.MG_graphics_manager()
            pygame.display.update()
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
