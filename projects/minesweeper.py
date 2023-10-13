import math, random
from typing import Any


minesweeper_size = (12, 12)

class Block:
    '''
    the individual blocks that make up the grid
    '''
    def __init__(self, x, y, is_mine):
        
        self.x = x
        self.y = y
        self.is_mine = is_mine
        self.is_mine_selected = False
        self.is_flagged = False
        self.is_revealed = False
        self.adjacent_mines = 0
        
    def __str__(self):
        '''
        returns the string representation of the block'''
        # return str(self.adjacent_mines)
        if self.is_mine_selected:
            return '*'
        if self.is_revealed:
            return str(self.adjacent_mines)
        elif self.is_flagged:
            return 'F'
        else:
            return 'X'
    
    def edge(self):
        '''
        returns true if the block is on the edge of the grid
        '''
        return self.x == 0 or self.y == 0 or self.x == 2 or self.y == 2
    
class Grid:
    '''
    the grid that the game is played on'''
    def __init__(self):
        self.size: tuple[float, float]
        self.grid: list[list[Block]]
        self.mine_num: int = 0
        

    def __str__(self):
        '''
        returns the string representation of the grid
        '''
        def pretty_list(array: list):    
            return [str(i) for i in array]
        print("", *(str(pretty_list(row)) + '\n' for row in grid.get()))
    
    def get(self):
        '''
        returns the grid
        '''
        return self.grid
    
    def get_block(self, x, y):
        '''
        returns the block at the given coordinates
        '''
        return self.grid[x][y]
    
    def get_adjacent_blocks(self, x_pos, y_pos):
        '''
        returns a list of the blocks adjacent to the given coordinates
        '''
        return [self.grid[x][y] for x in range(x_pos-1, x_pos+2) for y in range(y_pos-1, y_pos+2) if x >= 0 and y >= 0 and x < self.size[0] and y < self.size[1]]
    
    def get_adjacent_mines(self, x, y):
        '''
        returns the number of mines adjacent to the given coordinates
        '''
        return sum([block.is_mine for block in self.get_adjacent_blocks(x, y)])
    
    def get_input(self, flag = False):
        '''
        gets the user input
        '''
        if flag:
            try:
                res = input("Enter a coordinate (x, y) to flag or unflag a block: ")
                x, y = res.split(',')
                x = int(x) - 1
                y = int(y) - 1
                if x > self.size[0] or y > self.size[1] or x < 0 or y < 0:
                    print('Please enter a valid coordinate')
                    return self.get_input()
                return int(x), int(y)
            except ValueError:
                print('please input a number like such (0,0)') 
                return self.get_input()
        try:
            res = input("Enter a coordinate (x, y), or type f to flag a block (r to show board, q to quit): ")
            
            if res == 'q':
                print('Goodbye!')
                exit()
            if res == 'r':
                self.__str__()
                return self.get_input()
            if res == 'f':
                y, x = self.get_input(flag=True)
                if self.get_block(x, y).is_flagged:
                    self.get_block(x, y).is_flagged = False
                else: self.get_block(x, y).is_flagged = True
                self.__str__()
                return self.get_input()
            else:
                x, y = res.split(',')
                x = int(x) - 1
                y = int(y) - 1
                if x > self.size[0] or y > self.size[1] or x < 0 or y < 0:
                    print('Please enter a valid coordinate')
                    return self.get_input()
                return int(x), int(y)
        except ValueError:
            print('please input a number like such (0,0)') 
            return self.get_input()
        
    
        
    def generate_grid(self):
        '''
        generates the grid
        '''
        if not self.size: return print('Please set a size for the grid.')
        self.grid = [[Block(i, j, 0) for i in range(self.size[0])] for j in range(self.size[1])]
        self.set_mines()
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                self.grid[x][y].adjacent_mines = self.get_adjacent_mines(x, y)
                
    def set_size(self):
        '''
        sets the size of the grid
        '''
        x = 0
        y = 0
        while x < 3 or x > 100:
            try:
                x = int(input('Enter a length greater than 3 and less than 100: '))
                if x < 3 or x > 100:
                    raise ValueError
            except ValueError:
                print('Please enter a valid number')
        while y < 3 or y > 100:
            try:
                y = int(input('Enter a height greater than 3 and less than 100: '))
                if y < 3 or y > 100:
                    raise ValueError
                
            except ValueError:
                print('Please enter a valid number')
        print(f'Generating a {x}x{y} grid...')
        self.size = (x, y)
        # self.generate_grid()
        
    def set_mines(self):
        for i in range(self.mines_num):
            x = random.randint(0, self.size[0] - 1)
            y = random.randint(0, self.size[1] - 1)
            print('mine at', x + 1, y + 1)
            self.grid[x][y].is_mine = True
        
        
    def ask_mines(self):
        '''
        sets the mines on the grid
        '''
        try:
            res = input('Would you like to set the number of mines manually? (y/n): ')
            if res == 'y':
                while True:
                    try:
                        x = int(input('how many mines would you like on the grid? '))
                        if x > self.size[0] * self.size[1]:
                            raise ValueError
                        else:
                            self.mines_num = x
                        break
                    except ValueError:
                        print('Please enter a valid number within the size of the grid')
                    if res == 'n':
                        break
            elif res == 'n':
                self.mines_num = math.floor(self.size[0] * self.size[1] * .1)
            else:
                raise ValueError
        except ValueError:
            print('Please enter a valid response')
            return self.ask_mines()
    
    def start(self):
        '''
        starts the game
        '''
        print('Welcome to Minesweeper!')
        self.set_size()
        self.ask_mines()
        self.generate_grid()
        self.__str__()
        while True:
            y, x = self.get_input()
            block = self.get_block(x, y)
            if block.is_mine:
                block.is_mine_selected = True
                self.__str__()
                print('You hit a mine!')
                print('Game over!')
                break
            else:
                block.is_revealed = True
                if block.adjacent_mines == 0:
                    for block in self.get_adjacent_blocks(x, y):
                        block.is_revealed = True
                self.__str__()
    



grid = Grid()

grid.start()