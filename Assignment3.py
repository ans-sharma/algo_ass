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
MAXSIZE = 50000
STEPS = 5000

# heapify   
def heapify(arr, n, i):   
   # Find largest among root and children
   largest = i    
   l = 2 * i + 1     
   r = 2 * i + 2

   if l < n and arr[i] < arr[l]:
      largest = l

   if r < n and arr[largest] < arr[r]:
      largest = r

      # If root is not largest, swap with largest and continue heapifying
   if largest != i:
       arr[i], arr[largest] = arr[largest], arr[i]
       heapify(arr, n, largest)


def heapSort(arr):
   n = len(arr)
  
   # Build max heap
   # for i in range(n//2, -1, -1):
   #    heapify(arr, n, i)
  
   for i in range(n-1, 0, -1):
      # Swap
      arr[i], arr[0] = arr[0], arr[i]
  
      # Heapify root element
      heapify(arr, i, 0)

def buildHeap(Arr):
    for i in range(int((len(Arr)/2)-1), -1, -1):
        heapify(Arr,i,len(Arr))
      
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
    buildHeap(arr)
    no.append(i)
    start = timeit.default_timer()
    heapSort(arr)
    end = timeit.default_timer()
    executionTime = (end-start)
    et.append(executionTime)
    logy_n.append((i*math.log2(i))*0.0000001)

print(logy_n)
print(et)

plt.plot(no, et, label="heap-sort")
plt.plot(no,logy_n, label="nlogn")
plt.xlabel('array size ')
plt.ylabel('execution time (microsec)')
plt.title('HeapSort')
plt.legend()
plt.show()