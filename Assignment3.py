# 3. Write a program to perform heapsort on an n-length array. 
# You should first construct the heap from the array and then perform heapsort 
# and print the correct sorted sequence of the input array. 
# Also analyze the time complexity of the algorithm by plotting the graph of 
# running time of the algorithm for different values of n and comparing it with nlogn.
# Give your comments.

# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap

import math
import time
import random
import timeit
import matplotlib.pyplot as plt
START = 1
MAXSIZE = 10000
STEPS = 1000

# heapify
def heapify(arr, n, i):
   largest = i # largest value
   l = 2 * i + 1 # left
   r = 2 * i + 2 # right
   # if left child exists
   if l < n and arr[i] < arr[l]:
      largest = l
   # if right child exits
   if r < n and arr[largest] < arr[r]:
      largest = r
   # root
   if largest != i:
      arr[i],arr[largest] = arr[largest],arr[i] # swap
      # root.
      heapify(arr, n, largest)
# sort
def heapSort(arr):
   n = len(arr)
   # maxheap
   for i in range(n, -1, -1):
      heapify(arr, n, i)
   # element extraction
   for i in range(n-1, 0, -1):
      arr[i], arr[0] = arr[0], arr[i] # swap
      heapify(arr, i, 0)

# Driver code
# arr = [12, 11, 13, 5, 6, 7]
# heapSort(arr)
# n = len(arr)
# print("Sorted array is")
# for i in range(n):
# 	print("%d" % arr[i],end=" ")

def returnRandomInt():
    return random.randint(1,MAXSIZE)



# Driver code to test above code
arr = []
no = []
et = []
logy_n = []
for i in range(START,MAXSIZE+1, STEPS):
    for j in range(1,i):
        temp = random.randint(0, i)
        arr.append(temp)
    no.append(i)
    start = timeit.default_timer()
    heapSort(arr)
    end = timeit.default_timer()
    executionTime = (end-start)
    et.append(executionTime)
    logy_n.append((i*math.log10(i))*0.000005)

print(logy_n)
print(et)

plt.plot(no, et, label="heap-sort")
plt.plot(no,logy_n, label="nlogn")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('HeapSort')
plt.legend()
plt.show()