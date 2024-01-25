import random, math

def simulate(percentage, n_times):
    
    days_in_year = 365
    
    birthday = random.randint(1, days_in_year)
    
    final_percentage = 0
    
    while True:
        num_people = 1
        total_percentage = []
        for i in range(n_times):
            percentages = []
            birthdays = [random.randint(1, days_in_year) for i in range(num_people)]
            
            for birth in birthdays:
                if birth == birthday:
                    percentages.append(1)
                else:
                    percentages.append(0)
                    
            total_percentage.append(sum(percentages) / num_people * 100)
            
        final_percentage = sum(total_percentage) / n_times
        
        if final_percentage >= percentage:
            break
        
        num_people += 1
        
    print(f'For {percentage}% probability, you need {num_people} people')
    
    
    
simulate(25, 100)

simulate(50, 100)

simulate(75, 100)
