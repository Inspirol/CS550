
import matplotlib.pyplot as plt
import random, math

data = [random.gauss(0, 1) for i in range(1000000)]

plt.plot(data)
# plt.bar([1,2,3], data)
plt.hist(data, bins=100)

plt.show()
