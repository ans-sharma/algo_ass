import random
import time 
import matplotlib.pyplot as plt

def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
  
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
        
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
  
#  Radix Sort
def radixSort(arr):
  
    # maximum number
    max1 = max(arr)
    exp = 1
    while max1 / exp > 1:
        countingSort(arr, exp)
        exp *= 10

et = []
n = []
for i in range(2, 1000, 100):
    arr = []
    for j in range(0, i):
        temp = random.randint(0, 99999)
        arr.append(temp)
    start = time.perf_counter()
    radixSort(arr)
    et.append((time.perf_counter()-start)*100000)
    n.append(i)
plt.plot(n, et, label="counting sort")
plt.plot(n, n, label="n")
plt.xlabel('array size')
plt.ylabel('execution time')
plt.title('Counting Sort')
plt.legend()
plt.show()
    