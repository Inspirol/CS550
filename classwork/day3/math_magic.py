'''
name: Sebastian Plunkett
date: 9/13/2023
sources: none

'''
num = 5
print('Welcome to the math magic machine!')
print('For my first trick, please select a number, any number!')
got_it = input('Got it? (y/n)\n>>> ')
if got_it.lower() == 'n':
    print('Well, I guess I will just have to guess then.')
    import random
    num = random.randint(1, 100)
    correct = input('Is your number ' + str(num) + '?')
    print('well I am a computer, so I am always right.')

print('Now, I will multiply your number by 2.')
print('subtract by 15')
print('divide by 20')
print('raise to the power of 3')
print('add 5')
print('subtract your original number')
print('divide by 2')
print('subtract 2')
print('and finally, add 1')
print('I am left with the number 1.')
print('I am a computer, so I am always right.')
print('This is your number new number I dont care: ' + str(num))
num *= 2
print('Now, I will multiply your number by 2.')
input(num)
num -= 15
print('subtract by 15')
input(num)
num /= 20
print('divide by 20')
input(num)
num **= 3
print('raise to the power of 3')
input(num)
num += 5
print('add 5')
input(num)
num -= num
print('subtract your original number')
input(num)
num /= 2
input(num)
num -= 2
input(num)
num += 1
print('the answer is:',num)
print('I am left with the number 1.')
print('I am a computer, so I am always right.')
print('Goodbye.')