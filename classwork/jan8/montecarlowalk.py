import random


class walker:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.history = [(self.x, self.y)]
        
    def move(self):
        # you can move north, south, east, or west
        
        # pick a random direction
        
        random_direction = random.choice(['north', 'south', 'east', 'west'])
        
        # move in that direction
        
        if random_direction == 'north':
            self.y += 1
        elif random_direction == 'south':
            self.y -= 1
        elif random_direction == 'east':
            self.x += 1
        elif random_direction == 'west':
            self.x -= 1
            
        # add the new position to the history
        
        self.update_history()
        
    def update_history(self):
        self.history.append((self.x, self.y))
        
    def blocks_from_home(self):
        blocks_x = sum([x for x, y in self.history])
        blocks_y = sum([y for x, y in self.history])
        
        
        return abs(blocks_x) + abs(blocks_y)
    
    def past_limit(self, limit):
        return self.blocks_from_home() > limit
    
    
    

class simulation:
    
    block_limits = int
    
    def __init__(self, num_walkers, block_limits):
        self.walkers = [walker() for i in range(num_walkers)]
        self.block_limits = block_limits
        self.past_limits = []
        
    def run(self, r: int):
        for walker in self.walkers:
            for i in range(r):
                walker.move()
            if walker.past_limit(self.block_limits):
                self.past_limits.append(walker)
                
    def simulate(self, length):
        self.run(length)
        if self.results() < 0.5:
            self.clear()
            return self.simulate(length + 1)
        else:
            return length
        
    def run_simulation(self):
        return self.simulate(self.block_limits + 1)
        
        
    def results(self):
        print(len(self.past_limits) / len(self.walkers))
        return len(self.past_limits) / len(self.walkers)
    
    def clear(self):
        self.past_limits = []
    

if __name__ == "__main__":
    sim = simulation(100, 4)
    print(sim.run_simulation())

