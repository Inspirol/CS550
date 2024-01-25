import random

def simulation(move: bool, n_times: float):
    
    got_prize = 0
    
    for i in range(n_times):
        # create 3 doors
        doors = [1, 2, 3]
        # put prize behind one door
        prize = random.choice(doors)
        # choose one door
        choice = random.choice(doors)
        # remove one door
        new_doors = doors.copy()
        new_doors.remove(choice)
        # if choice is not prize and choice is not removed door, remove choice
        if prize in new_doors:
            new_doors.remove(prize)
            
        doors.remove(random.choice(new_doors))
        
        # if move is True, change choice
        if move:
            choice = random.choice(doors)
       
        if choice == prize:
            got_prize += 1
        
    return got_prize / n_times * 100

def main():
    
    change = simulation(True, 10000)
    
    print(f'Change Decision: {change}%')
    
    keep = simulation(False, 10000)
    
    print(f'Keep Decision: {keep}%')
    
    if change > keep:
        print('Change Decision is better')
    elif keep > change:
        print('Keep Decision is better')
    

if __name__ == '__main__':
    main()
    
    
    # because the probability of getting the prize is 1/3, and the probability of getting the prize after changing the choice is 2/3, the change decision is better
    
    # since you move the choice after the initial guess, which is 1/3, and after they removed the door, its better to change.