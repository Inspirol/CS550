import math

# for x in range(100, -101, -10):
#     print(x)
    
# for x in range(7, 701, 7):
#     print(x)
    
# for x in range(1, 101, 1):
#     neg = math.modf(x / 2)[0] == 0.0 and -1 or 1
#     print(x * neg)
    
# val = 4
# for x in range(1, 101):
#     f = x + val
#     print(f)
#     val = f + val

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

val = 0
for x in range(1, 101):
    print(x + val)
    val = val + x