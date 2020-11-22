from random import randint


def inPlaceQuickSort(A, start, end):
    if start < end:
        pivot = randint(start, end)
        temp = A[end]
        A[end] = A[pivot]
        A[pivot] = temp

        p = inPlacePartition(A, start, end)
        inPlaceQuickSort(A, start, p - 1)
        inPlaceQuickSort(A, p + 1, end)


def inPlacePartition(A, start, end):
    pivot = randint(start, end)
    A[end], A[pivot] = A[pivot], A[end]
    i = start - 1  # new pivot index
    for index in range(start, end):
        if A[index] < A[end]:  # check if current val is less than pivot value
            i = i + 1
            temp = A[i]
            A[i] = A[index]
            A[index] = temp
    temp = A[i + 1]
    A[i + 1] = A[end]
    A[end] = temp
    return i + 1


# n = int(input("Enter size of the matrix: "))
arr = [4, 5, 7, 4, 3, 6, 0, 4, 22, 45, 82]
'''
print("Enter array elements: ")
for i in range(0, n):
    arr.append(int(input()))
'''
inPlaceQuickSort(arr, 0, len(arr) - 1)

print("After sort: ")
for x in arr:
    print(x, end=" ")