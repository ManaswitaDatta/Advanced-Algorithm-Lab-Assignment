def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


try:
    num = int(input("Enter a number: "))
    arr = []
    for i in range(num):
        arr.append(int(input()))
    print("Original array: ")
    print(arr)
    print("Sorted array: ")
    print(insertion_sort(arr))
except ValueError as err:
    print(err)