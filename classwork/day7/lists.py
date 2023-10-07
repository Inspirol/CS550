import random
import math

list = [random.randint(0, 10) for i in range(100)]
print(list)

list0 = [0 for i in range(1000)]

print(list0)

list7 = [random.randrange(77, 777, 7) for i in range(10)]

print(list7)

list77 = [77 + 7*i for i in range(101)]

print(list77)

listEven = [random.randrange(2, 100, 2) for i in range(25)]

print(listEven)