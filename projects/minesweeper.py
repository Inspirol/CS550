import math, random

class Block:
    
    def __init__(self, x, y, is_mine):
        
        self.x = x
        self.y = y
        self.is_mine = is_mine
        self.is_flagged = False
        self.is_revealed = False
        self.adjacent_mines = 0
        
    def __str__(self):
        return str(self.is_mine) + " " + str(self.edge())
    
    def edge(self):
        return self.x == 0 or self.y == 0 or self.x == 2 or self.y == 2


list_2d = [[Block(i, j, random.randint(0,1)) for i in range(0, 3)] for j in range(0, 3)]



def pretty_list(array: list):
    return [str(i) for i in array]
    # # column lines
    # for i in range(0, len(array), 2):
    #     array.insert(i + 1, "|")
    # # row lines
    # row_gap = ''.join(['-' for i in range(0, len(array))])
    # return ''.join(str(array) for array in array) + '\n ' + row_gap

print("", *(str(pretty_list(row)) + '\n' for row in list_2d))