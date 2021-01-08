import sys


def distribute(arr, n):
    left = 0
    right = 0
    if n == 0:
        print(str(0) + " " + str(0))
        return
    if n == 1:
        print(str(0) + " " + str(arr[0]))
        return
    for i in range(n-1, -1, -2):
        if right > left:
            right += arr[i-1]
            left += arr[i]
        else:
            right += arr[i]
            left += arr[i-1]
        if i-3 < 0:
            break
    if n % 2 == 1:
        if right > left:
            left += arr[0]
        else:
            right += arr[0]
    if right > left:
        print(str(left) + " " + str(right))
    else:
        print(str(right) + " " + str(left))
    return


def main():
    if len(sys.argv) != 2:
        return

    fname = sys.argv[1]
    file = open(fname, 'r')
    n = int(file.readline())  # total no of packets
    arr = []
    for i in range(n):
        arr.append(int(file.readline()))
    arr.sort()
    distribute(arr, n)
    file.close()


if __name__ == '__main__':
    main()
