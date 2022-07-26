# Write a program to implement the Counting sort algorithm. 
# Verify that it runs in O(n) time for inputs in the range of n.

import numpy as np;
def countingSort(arr, maxRange):
    countArr = np.zeros(maxRange+1,dtype=int)
    # print(countArr)
    # counting the no of elements
    for element in arr:
        countArr[element] += 1
    # print(countArr)
    for i in range(1, len(countArr)):
        countArr[i] = countArr[i-1] + countArr[i]
    # print(countArr)
    # calculating indexes
    for i in range(len(countArr)-1, 0, -1):
        countArr[i] = countArr[i-1]
    countArr[0] = 0
    tempArr = np.zeros(len(arr), dtype=int) #creating a secondary array to store the sorted elements
    for element in arr:
        tempArr[countArr[element]] = element
        countArr[element] += 1
    # print(tempArr) 
    # print(countArr)
    return(tempArr)

print(countingSort(np.random.randint(0,3,200), 4))