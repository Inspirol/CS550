import random

class Person:
    def __init__(self):
        self.birthday = random.randint(1, 365)
        
    def get_birthday(self):
        return self.birthday
    

class Simulation:
    
    def __init__(self, birthday):
        self.birthday = birthday
        self.people = []
        self.match = False
        
    def create_people(self, number_of_people):
        for i in range(number_of_people):
            self.people.append(Person())
            
    def check_match(self):
        for i in range(len(self.people)):
            if self.people[i].get_birthday() == self.birthday:
                self.match = True
                return
            if self.match:
                return
            
    def run_simulation(self, number_of_people):
        self.create_people(number_of_people)
        self.check_match()
        
    def reset(self):
        self.people = []
        self.match = False
        
    def average_matches(self, n):
        return sum(n) / len(n) * 100
        
    def simulate(self, percentage_threshold, n):
        
        people = 365
        
        data = []
        
        limit = False
        
        while True:
            if limit or people == 0:
                break
            for j in range(n):
                self.run_simulation(people)
                data.append(self.match)
                self.match = False
            percentage = self.average_matches(data)
            if percentage >= percentage_threshold:
                people -= 1
                self.reset()
            else:
                limit = True
            
            
        percentage = self.average_matches(data) 
        print("Percentage: " + str(percentage) + "%")
        print("Percentage threshold: " + str(percentage_threshold) + "%")
        print("Number of people: " + str(people))

birthday = int(input("Birthday (in days): "))
percentage_threshold = int(input("Enter percentage threshold: "))
n = int(input("Enter number of simulations: "))
simulation = Simulation(birthday)
simulation.simulate(percentage_threshold, n)

        
        
        