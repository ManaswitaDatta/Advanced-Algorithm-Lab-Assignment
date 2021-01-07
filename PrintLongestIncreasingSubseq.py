'''
As you have pointed out, the indices of the LIS need to be stored as well.

This can be done by introducing an additional array prev. In the original code, lis(n) represents the length of the
LIS ending at n, and we have prev(n) representing the index number immediately before n in the LIS ending at n
(i.e. the second last index number of the LIS), if the LIS ending at n is of length 1, we simply define
prev(n) = n.

Whenever you update the value of lis(n), prev(n) also needs to be updated accordingly.
'''
# lis returns length of the longest increasing subsequence
# in arr of size n
def lis(arr):
    n = len(arr)

    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    lis = [1]*n

    prev = [0]*n
    for i in range(0, n):
        prev[i] = i

    # Compute optimized LIS values in bottom up manner
    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1:
                lis[i] = lis[j]+1
                prev[i] = j

    # Initialize maximum to 0 to get the maximum of all
    # LIS
    maximum = 0
    idx = 0

    # Pick maximum of all LIS values
    for i in range(n):
        if maximum < lis[i]:
            maximum = lis[i]
            idx = i

    seq = [arr[idx]]
    while idx != prev[idx]:
        idx = prev[idx]
        seq.append(arr[idx])

    return (maximum, reversed(seq))
# end of lis function

# Driver program to test above function
'''
num = int(input("Enter a number: "))
arr = []
for i in range(num):
    arr.append(int(input()))
'''
arr = [5, 2, 8, 6, 3, 6, 9, 7]
ans = lis(arr)
print("Length of lis is ", ans[0])
print("The longest sequence is ", ", ".join(str(x) for x in ans[1]))
