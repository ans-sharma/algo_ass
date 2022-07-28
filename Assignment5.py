import matplotlib.pyplot as plt
import numpy as np
import time 

# sorting
def quickSort(arr, start, end):
    if(start < end):
        ptrIndex = partition(arr, start, end)
        quickSort(arr, start, ptrIndex - 1)
        quickSort(arr, ptrIndex + 1, end)

# partition for quicksort
def partition(arr, start, end): 
    pivot = arr[end]
    ptrIndex = start
    for i in range(start, end, 1):
        if arr[i] <= pivot:
            arr[i], arr[ptrIndex] = arr[ptrIndex], arr[i]
            ptrIndex += 1
    arr[ptrIndex], arr[end] = arr[end], arr[ptrIndex]
    return ptrIndex


START = 1
END = 20000
STEPS = 1000


et = []
n = []
nlogn = []

for i in range(START, END, STEPS):
    arr = np.random.randint(0,i**2,size=i)
    lenArr = len(arr)
    n.append(lenArr)
    start = time.perf_counter()
    quickSort(arr, 0, lenArr-1)
    end = time.perf_counter()
    et.append(end-start)
    nlogn.append((lenArr*np.log2(lenArr))*0.000001)


print(et)
print(n)
print(nlogn)


plt.plot(n, et, label='quick sort')
plt.plot(n, nlogn, label='nlogn')
plt.legend()
plt.xlabel('array size (n)')
plt.ylabel('execution time (s)')
plt.title('Quick Sort')
plt.show()