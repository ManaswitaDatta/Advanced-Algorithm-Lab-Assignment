def partition(arr, l, r):
    i = (l - 1)  # index of smaller element
    pivot = arr[r]

    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quick_sort(arr, l, r):
    if len(arr) == 1:
        return arr
    if l < r:
        p = partition(arr, l, r)
        quick_sort(arr, l, p - 1)
        quick_sort(arr, p + 1, r)


try:
    num = int(input("Enter a number: "))
    arr = []
    for i in range(num):
        arr.append(int(input()))
    print("Original array: ")
    print(arr)
    print("Sorted array: ")
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
except ValueError as err:
    print(err)