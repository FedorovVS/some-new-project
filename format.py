class Cell3:
    def __init__(self, i, j,  state = 0, ship = 0, ship_orientation = 0, ship_i = -1, ship_j = -1):
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
        mouse - shows whether the mouse is on the cell
        """
        self.i = i
        self.j = j
        self.state = state
        self.ship = ship
        self.obj_type = 0
        self.ship_orientation = ship_orientation
        self.ship_i = ship_i
        self.ship_j = ship_j


    
    def change_state(self):
        '''
        функция меняет состояние клетки
        пустая - мертвая
        с кораблем - задетая
        '''
        if self.state == 0:
            self.state = 2
            return -1
        elif self.state == 1:
            self.state = 3
            return 0
        else:
            return 1
        
class Cell:
    def __init__(self, i, j, x, y, state=0, ship=0, warship=0):
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
        warship - ship that stands oh this cell
        """
        self.i = i
        self.j = j
        self.state = state
        self.ship = ship
        self.x = x
        self.y = y
        self.warship = warship

    def clear(self):
        if self.warship == 0:
            self.state = 0

def convert_Cell_to_Cell3_list(cell_list:list):
    '''
    функция конвертирует элементы исходного массива в объекты класса Cell3
    на вход подается массив
    '''
    result = []
    for i,a in enumerate(cell_list):
        result.append([])
        for b in a:
            if b.state == 1 or b.state == 3:
                check_size = min(b.warship.x1-b.warship.x0, b.warship.y1-b.warship.y0)
                result[i].append(Cell3(b.i, b.j, int(b.state), b.warship.type, b.warship.turn_flag, b.i - (b.x-b.warship.x0)//check_size, b.j - (b.y-b.warship.y0)//check_size))
            else:
                result[i].append(Cell3(b.i, b.j))

    return result
