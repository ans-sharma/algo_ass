import random
import time
from matplotlib import pyplot as plt 

def countingSort(array):
    size = len(array)
    output = [0] * size
    count = [0] * 1001
    for i in range(0, size):
        count[array[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
    for i in range(0, size):
        array[i] = output[i]

et = []
n = []
for i in range(2, 1000, 100):
    arr = []
    for j in range(0, i):
        temp = random.randint(0, 1000)
        arr.append(temp)
    start = time.perf_counter()
    countingSort(arr)
    et.append((time.perf_counter()-start)*1000000)
    n.append(i)
plt.plot(n, et, label="counting sort")
plt.plot(n, n, label="n")
plt.xlabel('array size')
plt.ylabel('execution time')
plt.title('Counting Sort')
plt.legend()
plt.show()
    
    
        