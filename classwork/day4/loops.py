'''
Why loops?
to repeat things
'''
import time
import random

looping = True

while looping:
    print('Hello, world!')
    time.sleep(1)
    if random.random() < 0.1:
        looping = False
    
for x in range(10):
    print(x)
    time.sleep(1)
    
for x in range(5, 10 ,5):
    print(x)
    time.sleep(1)
    
for counter in range(7):
    print('Hello, world!')
    time.sleep(1)
    
for _ in range(7):
    print('Hello, world!')
    time.sleep(1)

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for item in mylist:
    print(item)
    time.sleep(1)