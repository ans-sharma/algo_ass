import numpy as np
import time as t
import matplotlib.pyplot as plt

def countingSort(arr, maxRange):
    countArr = np.zeros(maxRange+1,dtype=int)
    for element in arr:
        countArr[element] += 1

    for i in range(1, len(countArr)):
        countArr[i] = countArr[i-1] + countArr[i]

    for i in range(len(countArr)-1, 0, -1):
        countArr[i] = countArr[i-1]
    countArr[0] = 0
    tempArr = np.zeros(len(arr), dtype=int) #creating a secondary array to store the sorted elements
    for element in arr:
        tempArr[countArr[element]] = element
        countArr[element] += 1
    arr = tempArr

START = 2
END = 100000
STEPS = 10000
K = 10
n = []
n_n =[]
et = []
for i in range(START, END, STEPS):
    arr = np.random.randint(0, K, i, dtype=int)
    n.append(i)
    n_n.append(i*0.00001)
    start = t.perf_counter()
    countingSort(arr, K)
    end = t.perf_counter()
    executionTime = end - start
    et.append(executionTime)
    
plt.plot(n, et, label="counting sort")
plt.plot(n, n_n, label="n")
plt.xlabel('array size')
plt.ylabel('execution time(s)')
plt.title('Counting Sort')
plt.legend()
plt.show()
    