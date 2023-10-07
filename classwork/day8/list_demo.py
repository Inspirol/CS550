# make a lit from 0 to 100
# print
# remove all multiples of 5
# print

the_list = [i for i in range(0, 101)]

print(the_list)

print([*enumerate(the_list)][2]) # enumerate returns a list of tuples (index, value)

the_list = filter(lambda x: x == 0 or x % 5 != 0, the_list)

print([*the_list]) 




basic_2d_list = [[x for x in range(0, 3)] for y in range(0,3)]

print(*(str(row) + '\n' for row in basic_2d_list))
