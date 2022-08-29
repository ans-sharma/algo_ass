from typing import Counter
import numpy as np
import time as t
import matplotlib.pyplot as plt


COUNT = 0

def bucketSort(arr):
    global COUNT
    COUNT = 0
    tempArr = []
    noOfSlots = len(arr)
    for i in range(noOfSlots):
        COUNT += 1
        tempArr.append([])
          
    for j in arr:
        # COUNT += 1
        elementIndex = int(noOfSlots * j) 
        tempArr[elementIndex].append(j)
      
    # Sorting buckets
    for i in range(noOfSlots):
        tempArr[i] = insertionSort(tempArr[i])
        
    k = 0
    for i in range(noOfSlots):
        for j in range(len(tempArr[i])):
            arr[k] = tempArr[i][j]
            k += 1
    return arr

def insertionSort(arr):
    global COUNT
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp: 
            # COUNT += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp     
    return arr 
  
START = 2
END = 1000
STEPS = 100

# n = []
# n_n = []
# et = []
# for i in range(START, END, STEPS):
#     arr = np.random.uniform(low=0, high=1, size=i)
#     n.append(i)
#     n_n.append(i*0.00001)
#     start = t.perf_counter()
#     bucketSort(arr)
#     end = t.perf_counter()
#     executionTime = end - start
#     et.append(executionTime)
    
# plt.plot(n, et, label="bucket sort")
# plt.plot(n, n_n, label="n")
# plt.xlabel('array size')
# plt.ylabel('execution time(s)')
# plt.title('Bucket Sort')
# plt.legend()
# plt.show()

n = []
n_n = []
count = []

for i in range(START, END, START):
    arr = np.random.uniform(low=0, high=1, size=i)
    n.append(i)
    n_n.append(i*0.00001)
    bucketSort(arr)
    count.append(COUNT)
plt.plot(n, count, label="bucket sort")
plt.plot(n, n, label="n")
plt.xlabel('array size')
plt.ylabel('execution time(s)')
plt.title('Bucket Sort')
plt.legend()
plt.show()