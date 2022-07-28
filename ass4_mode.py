# 4.  Write a program to implement a priority queue (using Max_Heap). The program should contain the following functions:
# a.  Maximum(S)
# b.  Extract_Max(S)
# c.  Increase_key(S, i, key)
# d.  Insert (A, key)
# Show that each of the above methods takes logn time for running, where n is the problem size.

import matplotlib.pyplot as plt
import numpy as np
import time 
import random

#Heapify
def Heapify(Arr,i,Arr_len2):
    left_child = 2 * i + 1  #leftChild child
    right_child = 2 * i + 2 #rightChild child
    if left_child < Arr_len2 and Arr[left_child] > Arr[i]:
        largest = left_child
    else:
        largest = i
    if right_child < Arr_len2 and Arr[right_child] >=Arr[largest]:
        largest = right_child
    if largest != i:
        Arr[i], Arr[largest] = Arr[largest], Arr[i]
        Heapify(Arr, largest,Arr_len2)

#Build heap
def BuildHeap(Arr):
    for i in range(int((len(Arr)/2)-1), -1, -1):
        Heapify(Arr,i,len(Arr))

#finding Maximum Element
def FindingMax(arr):
    return arr[0]

#Extracting max element
def extMax(Arr):
    len_Arr=len(Arr)
    if len_Arr<1:
        return -1
    elif len_Arr==1:
        return Arr[0]
    else:
        max_element=Arr[0]
        Arr[0]=Arr[len(Arr)-1]
        lst=np.delete(Arr,len(Arr)-1)
        Heapify(Arr,0,len(Arr))
        return max_element

#Incerase Key
def increaseKey(Arr,i,key):
    if Arr[i]>key:
        return -1
    Arr[i]=key
    while (i>0 and Arr[(i)//2]<Arr[i]):
        Arr[i],Arr[(i)//2]=Arr[(i)//2],Arr[i]
        idx=i//2

#Insert A value
def insert(Arr,key):
    Arr=np.insert(Arr,-1,len(Arr)+1)
    increaseKey(Arr,len(Arr)-1,key)

arr = np.random.randint(0, 1000, 10)
BuildHeap(arr)
print("Array: ", arr)
print("Maximum: " + str(FindingMax(arr)))
print("Extract Max: " + str(extMax(arr)))
temp = np.random.randint(1000, 1500)
print("Random no. generated: " + str(temp))
increaseKey(arr, 1, temp)
print("Increased Key at index 1 key "+ str(temp))
print("Array: ", arr)
temp = np.random.randint(1000, 1500)
print("Random no. generated: " + str(temp))
insert(arr, temp)
print("Insert key " + str(temp))
print("Array: ", arr)

    
# code for the graph    
# etExtractMax=[]
# etIncMax=[]
# etIncKey=[]
# etFindMax=[]
# n=[]
# for i in range(1,50):
#     randarr=np.random.randint(1,20,i*2000)
#     n.append(len(randarr))
#     BuildHeap(randarr)
#     st_timer1=time.perf_counter()
#     largest=FindingMax(randarr)
#     etFindMax.append((time.perf_counter()-st_timer1))
    
#     st_timer2=time.perf_counter()
#     extMax(randarr)
#     etExtractMax.append(((time.perf_counter()-st_timer2)))
    
#     st_timer3=time.perf_counter()
#     increaseKey(randarr,random.randint(10,20),random.randint(40,50))
#     etIncMax.append((time.perf_counter()-st_timer3))
#     st_timer4=time.perf_counter()
#     insert(randarr,random.randint(40,60))
#     etIncKey.append((time.perf_counter()-st_timer4))
    
# logn=[(np.log2(i)/10**5.3) for i in n] #logn
# # print(lst_len2)
# # print(logn)
# plt.plot(n,logn,label="logn")
# plt.plot(n,etExtractMax,label="Extract Max")
# plt.plot(n,etIncMax,label="Increase Key")
# plt.plot(n,etIncKey,label="Insert Key")
# plt.plot(n,etFindMax,label="Finding max")
# plt.title("All heap operations")
# plt.xlabel("No. of inputs")
# plt.ylabel("execution time (ns)")
# plt.legend()
# plt.show()