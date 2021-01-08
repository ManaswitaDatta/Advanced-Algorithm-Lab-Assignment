import sys


def merge(arr, temp, l, m, h, b):
    i = l
    j = m
    k = l
    count = 0
    while i <= m-1 and j <= h:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        elif arr[j] < arr[i] <= b*arr[j]:
            temp[k] = arr[j]
            k += 1
            j += 1
        else:
            count += m - i
            temp[k] = arr[j]
            k += 1
            j += 1
    if i <= m-1 and arr[i] > b * arr[h]:
        temp[k] = arr[i]
        k += 1
        i += 1
    while i <= m-1:
        if arr[i] > b*arr[h]:
            count += 1
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


def countBinversions(arr, temp, l, h, b):
    count = 0
    if l < h:
        mid = int((l+h)/2)
        count += countBinversions(arr, temp, l, mid, b)
        count += countBinversions(arr, temp, mid + 1, h, b)
        count += merge(arr, temp, l, mid+1, h, b)
    return count


def main():
    if len(sys.argv) != 2:
        return

    fname = sys.argv[1]
    file = open(fname, 'r')

    line = file.readline()  # Read in the numbers in the sequence
    arr = []
    # Print the numbers in the sequence one by one.
    for w in line.split(' '):
        arr.append(int(w))
        print(w, end=' ')


    b = int(file.readline())  # The number b
    print(b)
    temp = [0] * len(arr)
    print(countBinversions(arr, temp, 0, len(arr) -1, b))

    file.close()


if __name__ == '__main__':
    main()