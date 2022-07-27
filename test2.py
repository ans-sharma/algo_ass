def QuickSort(A, start, end):
    if(start < end):
        pIndex = Partition(A, start, end)
        QuickSort(A, start, pIndex - 1)
        QuickSort(A, pIndex + 1, end)

def Partition(A, start, end):
    pivot = A[end]
    pIndex = start
    for i in range(start, end, 1):
        if A[i] <= pivot:
            A[i], A[pIndex] = A[pIndex], A[i]
            pIndex += 1
    A[pIndex], A[end] = A[end], A[pIndex]
    return pIndex

A = [1,2,3,4]
QuickSort(A, 0, len(A)-1)
print(A)