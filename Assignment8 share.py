import random
import time 
import matplotlib.pyplot as plt

def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up: 
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up     
    return b     
              
def bucketSort(x):
    arr = []
    slot_num = 10 
    for i in range(slot_num):
        arr.append([])
          
    for j in x:
        index_b = int(slot_num * j) 
        arr[index_b].append(j)
      
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])
          
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x
  
et = []
n = []
for i in range(2, 1000, 100):
    arr = []
    for j in range(0, i):
        temp = random.uniform(0,1)
        arr.append(temp)
    start = time.perf_counter()
    bucketSort(arr)
    et.append((time.perf_counter()-start)*100000)
    n.append(i)
plt.plot(n, et, label="counting sort")
plt.plot(n, n, label="n")
plt.xlabel('array size')
plt.ylabel('execution time')
plt.title('Counting Sort')
plt.legend()
plt.show()
    