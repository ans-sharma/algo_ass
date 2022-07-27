# Write a program to implement the Counting sort algorithm. 
# Verify that it runs in O(n) time for inputs in the range of n.

import numpy as np
import time as t
import matplotlib.pyplot as plt
def countingSort(arr, maxRange):
    countArr = np.zeros(maxRange+1,dtype=int)
    # print(countArr)
    # counting the no of elements
    for element in arr:
        countArr[element] += 1
    # print(countArr)
    for i in range(1, len(countArr)):
        countArr[i] = countArr[i-1] + countArr[i]
    # print(countArr)
    # calculating indexes
    for i in range(len(countArr)-1, 0, -1):
        countArr[i] = countArr[i-1]
    countArr[0] = 0
    tempArr = np.zeros(len(arr), dtype=int) #creating a secondary array to store the sorted elements
    for element in arr:
        tempArr[countArr[element]] = element
        countArr[element] += 1
    # print(tempArr) 
    # print(countArr)
    arr = tempArr

print(countingSort(np.random.randint(0,3,200), 4))

START = 2
END = 100
STEPS = 10
K = 10
n = []
et = []
for i in range(START, END, STEPS):
    arr = np.random.randint(0, K, i, dtype=int)
    n.append(i)
    start = t.perf_counter()
    countingSort(arr, K)
    end = t.perf_counter()
    executionTime = end - start
    et.append(executionTime*100000)
    
plt.plot(n, et, label="counting sort")
plt.plot(n, n, label="n")
plt.xlabel('array size')
plt.ylabel('execution time')
plt.title('Counting Sort')
plt.legend()
plt.show()
    