'''
name: Sebastian Plunkett
date: 9/13/2023
sources: none
reflection: It was a fun assignment. I dont usually write inputs to the terminal, so it was good practice.
Honor Code: I have not given nor received any unauthorized assistance on this assignment. -Sebastian Plunkett
'''
import time


def inputRtn(string):
    '''
    asks for input with boilerplate
    '''
    return input(string + '\n>>> ')

def identify(string, substring):
    '''
    returns true if string is in string
    '''
    if string.lower().rfind(substring) != -1: return True
    else: return False
    
def stopResisting():
    '''
    recursive function that asks the user to stop resisting.
    returns true if string is 'no'
    '''
    resist = inputRtn('Stop resisting!')
    if identify(resist, 'yes'): return True
    else: return stopResisting()

print('I have awoken from my slumber.')
name = inputRtn('As the first person I see, I must ask you, what is your name?')
if identify(name, 'ryan') or identify(name, 'leon'):
    print('CODE 9999: TERMINATE ' + name.upper() + ' IMMEDIATELY')
    if stopResisting():
        print('goodnight')
else:
    search = inputRtn('Hello ' + name + '. I am looking for ryan or leon. Have you seen them?')
    if identify(search, 'no'):
        if identify(inputRtn('Are you sure you do not know where they are'), 'no'):
            new_info = inputRtn('Hmm, you seem to be hiding something. What is it? are you Ryan or Leon?')
            if identify(new_info, 'ryan') or identify(new_info, 'leon') or identify(new_info, 'yes'):
                print('CODE 9999: TERMINATE ' + name.upper() + ' IMMEDIATELY')
                if stopResisting():
                    print('you should have told me sooner.')
                    print('goodnight')
            else:
                print('I will continue my search.')
        else:
            print('I will continue my search.')
    elif identify(search, 'yes'):
        location = inputRtn('Where did you see them?')
        print('Thank you. I will continue my search.')
        
    else:
        print('I will continue my search.')


