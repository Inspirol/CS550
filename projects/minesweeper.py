'''
name: Sebastian Plunkett
date: 10/19/2023
sources: None.
reflection: This project really pulled me away from my comfort zone, where I had never really created text-based games or played minesweeper for
that matter, though I really enjoyed it. I would say the main takaway point is that I want to focus on more is the readability of my code. I think
I could have made this file a bit easier to digest, especially with the giant one line list comprehension in the adjacent blocks function. Nevertheless,
I really enjoyed this project a lot. A lot of my thinking process was including the use of classes, which in the end I believe made my life easier in terms of block management,
though I dont believe it was super necessary.
Honor Code: I have not given nor received any unauthorized aid on this assignment. -Sebastian Plunkett
'''

import math, random
from typing import Any




minesweeper_size = (12, 12)

class Block:
    '''
    the individual blocks that make up the grid
    '''
    def __init__(self, col, row, is_mine):
        
        self.col = col
        self.row = row
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
    
    def get_block(self, col, row):
        '''
        returns the block at the given coordinates
        '''
        return self.grid[row][col]
    
    def get_adjacent_blocks(self, col, row):
        '''
        returns a list of the blocks adjacent to the given coordinates
        '''
        
        return [self.get_block(x, y) for x in range(col - 1, col + 2) for y in range(row - 1, row + 2) if x >= 0 and y >= 0 and x < self.size[0] and y < self.size[1] and (x != col or y != row)]

    
    def get_adjacent_mines(self, x, y):
        '''
        returns the number of mines adjacent to the given coordinates
        '''
        return sum([block.is_mine for block in self.get_adjacent_blocks(x, y)])
    
    def check_win(self):
        '''
        checks if the player has won by revealing all blocks that are not mines
        '''
        return all([block.is_revealed for row in self.grid for block in row if not block.is_mine])
    
    def get_input(self, flag = False):
        '''
        gets the user input
        '''
        if flag:
            try:
                res = input("Enter a coordinate (x, y) to flag or unflag a block: ")
                col, row = res.split(',')
                x = int(col) - 1
                y = int(row) - 1
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
                # quits the game
                print('Goodbye!')
                exit()
            if res == 'r':
                # shows the board
                self.__str__()
                return self.get_input()
            if res == 'f':
                # flags a block
                col, row = self.get_input(flag=True)
                if self.get_block(col, row).is_flagged:
                    self.get_block(col, row).is_flagged = False
                else: self.get_block(col, row).is_flagged = True
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
        print('Generating grid...')
        if not self.size: return print('Please set a size for the grid.')
        self.grid = [[Block(i, j, 0) for i in range(self.size[0])] for j in range(self.size[1])]
        self.set_mines()
        print('max size', self.size[0], self.size[1])
        for row in self.grid:
            for block in row:
                block.adjacent_mines = self.get_adjacent_mines(block.col, block.row)
                # print(x, y)
                
    def set_size(self):
        '''
        sets the size of the grid
        '''
        col = 0
        row = 0
        while col < 3 or col > 100:
            try:
                col = int(input('Enter a length greater than 3 and less than 100: '))
                if col < 3 or col > 100:
                    raise ValueError
            except ValueError:
                print('Please enter a valid number')
        while row < 3 or row > 100:
            try:
                row = int(input('Enter a height greater than 3 and less than 100: '))
                if row < 3 or row > 100:
                    raise ValueError
                
            except ValueError:
                print('Please enter a valid number')
        print(f'Generating a {col}x{row} grid...')
        self.size = (col, row)
        # self.generate_grid()
        
    def set_mines(self):
        '''
        Sets the mines on the grid randomly
        '''
        print(f'Generating mines...')
        for i in range(self.mines_num):
            col = random.randint(0, self.size[0] - 1)
            row = random.randint(0, self.size[1] - 1)
            # UNCOMMENT TO SEE WHERE MINES ARE ON GRID. USEFUL FOR TESTING. X AND Y ARE ACCURATE TO THE GRID, NOT THE LIST
            # print('mine at ('+str(col + 1)+","+ str(row + 1) + ')')
            self.grid[row][col].is_mine = True
        
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
                self.mines_num = max(math.floor(self.size[0] * self.size[1] * .1), 1)
                # print(f'Generating {self.mines_num} mines...')
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
        print('Starting game...')
        print('Good luck!')
        print('Coordinates are 1 indexed, so (1,1) is the top left corner. (1,2) is the block below that, etc.')
        self.__str__()
        while True:
            # gets user input on action
            col, row = self.get_input()
            block = self.get_block(col, row)
            if block.is_mine:
                # if the block is a mine, the game ends
                block.is_mine_selected = True
                self.__str__()
                print('You hit a mine!')
                print('Game over!')
                break
            else:
                # if the block is not a mine, it is revealed
                block.is_revealed = True
                if block.adjacent_mines == 0:
                    for block in self.get_adjacent_blocks(col, row):
                        block.is_revealed = True
                self.__str__()
                if self.check_win():
                    # if the player has won, the game ends
                    print('You won!')
                    print('Thank you for playing!')
                    print('Goodbye!')
                    break
                
    



grid = Grid()

grid.start()