# Assignment 1
# Write a program to implement Merge Sort algorithm. 
# Also plot the graph of the time complexity for different values of array size ‘n’. 
# Compare this with the plot of  and give your comments in 2-3 lines.

from cmath import log
from math import log2
import time
import random
import matplotlib.pyplot as plt
MAXSIZE = 3000
STEPS = 100


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

def returnRandomInt():
    return random.randint(1,MAXSIZE)
 
# Driver code to test above
arr = []
no = []
et = []
x_n = []
y_n=[]
logx_n = []
logy_n = []

for i in range(100,MAXSIZE+1, STEPS):
    for j in range(1,i):
        arr.append(returnRandomInt())
    n = len(arr) 
    # z = i*0.0001
    x_n.append(i)
    y_n.append((i*i)*30)
    logx_n.append(i)
    logy_n.append((i*log2(i))*30)
    start = time.time_ns()
    mergeSort(arr, 0, n-1)
    executionTime = time.time_ns()-start
    # executionTime = executionTime *1000
    et.append(round(executionTime,10))
    no.append(i)

# print("n^2",y_n)
# print("mergesort",et)
print("nlogx", logx_n)
print("nlogy", logy_n)

plt.plot(x_n,y_n, label="n^2")
plt.plot(logx_n,logy_n, label="nlogn")
plt.plot(no, et, label="merge-sort")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('MergeSort')
plt.legend()
plt.show();