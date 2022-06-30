from random import randint
from math import log2
import timeit
import matplotlib.pyplot as plt


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0	 # Initial index of first subarray
    j = 0	 # Initial index of second subarray
    k = l	 # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


arr = []
x = []
y = []
n = []
for i in range(1, 3000, 100):
    for j in range(i):
        temp = randint(0, i)
        arr.append(temp)
    x.append(i)
    start = timeit.default_timer()
    mergeSort(arr, 0, i-1)
    end = timeit.default_timer()
    y.append(end - start)
    n.append(i*log2(i)*0.00000029)

plt.plot(x, y, label='merge sort')
plt.plot(x, n, label='nlogn')
plt.legend()
plt.xlabel('array size ')
plt.ylabel('execution time (s)')
plt.title('Merge Sort')
plt.show()
