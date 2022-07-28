import numpy as np
import time as t
import matplotlib.pyplot as plt

def countingSort(array, place):
    arrLen = len(array)
    tempArr = [0] * arrLen
    countArr = [0] * 10

    for i in range(0, arrLen):
        index = array[i] // place
        countArr[index % 10] += 1

    for i in range(1, 10):
        countArr[i] = countArr[i - 1] + countArr[i]

    i = arrLen - 1
    while i >= 0:
        index = array[i] // place
        tempArr[countArr[index % 10] - 1] = array[i]
        countArr[index % 10] -= 1
        i -= 1

    for i in range(0, arrLen):
        array[i] = tempArr[i]

def radixSort(array):
    # Get maximum element
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

START = 2
END = 100000
STEPS = 10000
n = []
n_n = []
et = []
for i in range(START, END, STEPS):
    arr = np.random.randint(0, i, i, dtype=int)
    n.append(i)
    n_n.append(i*0.00001)
    start = t.perf_counter()
    radixSort(arr)
    end = t.perf_counter()
    executionTime = end - start
    et.append(executionTime)
    
plt.plot(n, et, label="radix sort")
plt.plot(n, n_n, label="n")
plt.xlabel('array size')
plt.ylabel('execution time(s)')
plt.title('Radix Sort')
plt.legend()
plt.show()
    