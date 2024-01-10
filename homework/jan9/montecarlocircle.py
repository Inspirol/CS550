import random, math

class square: 
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        
        return self.width * self.height
    

class circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        
        return math.pi * self.radius ** 2
    
    def circumference(self):
            
            return 2 * math.pi * self.radius
        
class grid:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.square = square(width, height)
        self.circle = circle(width / 2)
        self.center = (width / 2, height / 2)
        
    def random_point(self):
        x = random.uniform(0, self.width)
        y = random.uniform(0, self.height)
        
        return (x, y)
    
    def distance_from_center(self, point):
        x, y = point
        x0, y0 = self.center
        
        return math.sqrt((x - x0) ** 2 + (y - y0) ** 2)
    
    def in_circle(self, point):
        return self.distance_from_center(point) <= self.circle.radius
    
    
class simulation:
    
    def __init__(self, width, height, num_trials):
        self.grid = grid(width, height)
        self.num_trials = num_trials
        self.num_in_circle = 0
        
    def run(self):
        for i in range(self.num_trials):
            point = self.grid.random_point()
            if self.grid.in_circle(point):
                self.num_in_circle += 1
                
    def results(self):
        return (self.num_in_circle / self.num_trials) * 4
    
    def clear(self):
        self.num_in_circle = 0
        
        
def average(values):
    return sum(values) / len(values)

def run_simulations(width, height, num_trials, num_simulations):
    sim = simulation(width, height, num_trials)
    results = []
    for i in range(num_simulations):
        sim.run()
        results.append(sim.results())
        sim.clear()
        
    print(average(results))
        
if __name__ == "__main__":
    print('running simulations')
    print('100')
    run_simulations(1, 1, 100, 10)
    print('1000')
    run_simulations(1, 1, 1000, 10)
    print('10000')
    run_simulations(1, 1, 10000, 10)
    print('100000')
    run_simulations(1, 1, 100000, 10)
    print('1000000')
    run_simulations(1, 1, 1000000, 10)
    
    print('this looks like it is approaching pi')
    
    print('horizontal asymptote')
    
    print('i think this works because the more trials you run, the more accurate the simulation is')
    
    print('when each trial is random between 0 and 1, and the circle limit is pi, most of the time the simulation will be under pi')