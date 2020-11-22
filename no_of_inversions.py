def merge(arr, temp, l, m, h):
    i = l
    j = m
    k = l
    count = 0
    while i <= m-1 and j <= h:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            count += m - i
            temp[k] = arr[j]
            k += 1
            j += 1

    while i <= m-1:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= h:
        temp[k] = arr[j]
        k += 1
        j += 1

    for i in range(l, h+1):
        arr[i] = temp[i]
    return count


def mergesort(arr, temp, l, h):
    count = 0
    if l < h:
        mid = int((l+h)/2)
        count += mergesort(arr, temp, l, mid)
        count += mergesort(arr, temp, mid + 1, h)
        count += merge(arr, temp, l, mid+1, h)
    return count

n = int(input("Enter size of the matrix: "))
arr = []

print("Enter array elements: ")
for i in range(0,n):
    arr.append(int(input()))

temp = [0]*len(arr)

print("Original Array: ")
for x in arr:
     print(x, end=" ")
print("\n")
print(mergesort(arr, temp, 0, len(arr) -1))
