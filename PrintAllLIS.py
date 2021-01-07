class Pair:

    def __init__(self, length, index, value, path):
        self.length = length
        self.index = index
        self.value = value
        self.path = path

def lis(arr):
    n = len(arr)
    dp = [0 for i in range(n)]
    omax = 0
    omaxindex = 0
    for i in range(n):
        max = 0
        for j in range(i):
            # not strictly increasing
            if arr[j] <= arr[i]:
                if dp[j] > max:
                    max = dp[j]
        dp[i] = max+1
        if dp[i] > max:
            omax = dp[i]
            omaxindex = i
    deque = []
    deque.append(Pair(omax, omaxindex, arr[omaxindex], str(arr[omaxindex]) +" "))
    print("Max length", omax)
    while deque:
        rem = deque.pop()
        if rem.length == 1:
            print(rem.path)
        for j in range(rem.index-1, -1, -1):
            if dp[j] == rem.length-1 and arr[j] <= rem.value:
                deque.append(Pair(dp[j], j, arr[j], str(arr[j]) + " " + rem.path))


# Driver program to test above function
'''
num = int(input("Enter a number: "))
arr = []
for i in range(num):
    arr.append(int(input()))
'''
arr = [5, 2, 8, 6, 3, 6, 9, 7]
ans = lis(arr)
