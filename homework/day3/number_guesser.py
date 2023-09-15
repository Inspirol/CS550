'''
name: Sebastian Plunkett
date: 9/15/2023
sources: none
reflection: This was also a fun project. I never really get to use recursive functions a lot so I enjoyed that. I took inspirations from Erics pauses in his prints, so I tried that here. 
Honor Code: I have not given nor received any unauthorized assistance on this assignment. -Sebastian Plunkett
'''
import random
import time

def generateNumber(base, to):
    '''
    generates a random number between the parameter base and two
    @param base: the minimum value of the random number
    @param to: the maximum value of the random number
    @returns the random number
    '''
    random.seed()
    return random.randint(base, to)

def inputRtn(string):
    '''
    asks for input with boilerplate
    @param string: the string to ask for input with
    @returns the input
    '''
    return input(string + '\n>>> ')

def identify(string, substring):
    '''
    returns true if string is in string
    @param string: the string to search
    @param substring: the substring to search for
    @returns true if the substring is in the string
    '''
    if string.lower().rfind(substring) != -1: return True
    else: return False
    
def printSequence(sequence: list, delay: float):
    '''
    prints a list of strings
    @param sequence: the list of strings to print
    @param delay: the delay between each print
    
    shout-out to eric for the idea of pauses in the print
    '''
    for i in sequence:
        print(i)
        time.sleep(delay)
        
def guessNumber(number, tries):
    '''
    asks the user to guess the input, then compares it to the original number (recursive function)
    @param number: the number to compare to
    @param tries: the number of tries the user has left
    @returns true if the user guessed the number
    '''
    
    spelling = tries == 1 and 'try' or 'tries'
    
    guess = inputRtn('Guess my number!')
    if identify(guess, str(number)):
        print('You guessed my number!')
        return True
    elif tries <= 1:
        print('Sorry, you have guessed wrong again.')
        print(f'My number was {number}.')
        print('You have no more tries left.')
        return False
    else:
        print('Sorry, you have guessed wrong.')
        number_difference = int(number) < int(guess) and 'lower' or 'higher'
        print(f'My number is {number_difference} than your guess.')
        print(f'You have {str(tries - 1)} {spelling} left.')
        return guessNumber(number, tries - 1)
    
def main():
    
    # variables
    from_num = 1
    to_num = 100
    selected_number = generateNumber(from_num, to_num)
    tries = 3
    
    # intro
    printSequence(['Welcome to the number guesser.', f'You will have to guess my number from {from_num} to {to_num}', f'Think of a number between {from_num} and {to_num}.'], 1)
    
    confirm = inputRtn('Have you thought of a number? (YES/no)')
    if identify(confirm, 'no'):
        printSequence(['I guess you dont want to play then :(', 'I am sad.', 'Goodbye'], .6)
        return
    
    # confirming that you want to play
    printSequence(['Good!', 'Now, try to guess my number.', 'I will tell you if you are wrong.', f'you have {tries} tries. Good luck!'], .5)
    
    # start of recursive function
    if(guessNumber(selected_number, tries) == False):
        # guess number returns false (user failed to guess number)
        printSequence(['You have failed to guess my number. :(', 'Low-key thought you were smarter than that.', 'Goodbye'], 1)
        return
    
    # guess number returns true (user guessed number)
    printSequence(['You have guessed my number!', 'Good job', 'Goodbye'], 1)
    
if __name__ == '__main__':
    main()



