import timeit
import random
import matplotlib.pyplot as plt

MAXSIZE = 10000
STEP = 1000
START = 1

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

def buildHeap(Arr):
    for i in range(int((len(Arr)/2)-1), -1, -1):
        heapify(Arr,i,len(Arr))

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

def returnRandomInt():
    return random.randint(1,MAXSIZE)
arr = []
arr1 = []
noOfElements = [] # no of elements
et_mergeSort = [] # merge sort execution time
et_heapSort = [] # heap sort execution time

for i in range(START, MAXSIZE, STEP):
    for j in range(i):
        temp = random.randint(0, i)
        arr.append(temp)
    n = len(arr)
    noOfElements.append(n)
    arr1 = arr # making a copy for sorting
    start_et_mergeSort = timeit.default_timer()
    mergeSort(arr, 0 , i-1)
    end_et_mergeSort = timeit.default_timer()
    et_mergeSort.append(end_et_mergeSort-start_et_mergeSort) #storing the execution time of merge sort
    #building the heap
    # buildHeap(arr1)
    start_et_heapSort = timeit.default_timer()
    heapSort(arr1)
    end_et_heapSort = timeit.default_timer()
    # et_heapSort.append((end_et_heapSort-start_et_heapSort)*0.2) #storing the execution time of heap sort
    et_heapSort.append(end_et_heapSort-start_et_heapSort)

plt.plot(noOfElements, et_mergeSort, label = 'merge sort')
plt.plot(noOfElements, et_heapSort, label = 'heap sort')
plt.legend()
plt.xlabel('array size ')
plt.ylabel('execution time (s)')
plt.title('Merge Sort VS Heap Sort')
plt.show()
