class Point:
    x: int = 0
    y: int = 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({},{})".format(self.x, self.y)
    
    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        else:
            return Point(self.x * other, self.y * other)
        
    @x.setter
    def x(self, value):
        if isinstance(value, int):
            self.x = value
        else:
            raise TypeError("x must be an int")
        
    @y.setter
    def y(self, value):
        if isinstance(value, int):
            self.y = value
        else:
            raise TypeError("y must be an int")
        
    @property
    def x(self):
        return self.x
    
    @property
    def y(self):
        return self.y

            
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
a = Point(1, 2)

print(a.x)