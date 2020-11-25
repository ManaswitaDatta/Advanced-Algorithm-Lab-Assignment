def majority_element_rec(arr, lo, hi):
    # base case; the only element in an array of size 1 is the majority
    # element.
    if lo == hi:
        return arr[lo]

    # recurse on left and right halves of this slice.
    mid = (hi - lo) // 2 + lo
    left = majority_element_rec(arr, lo, mid)
    right = majority_element_rec(arr, mid + 1, hi)

    # if the two halves agree on the majority element, return it.
    if left == right:
        return left

    # otherwise, count each element and return the "winner".
    left_count = sum(1 for i in range(lo, hi + 1) if arr[i] == left)
    right_count = sum(1 for i in range(lo, hi + 1) if arr[i] == right)
    return left if left_count > right_count else right

try:
    num = int(input("Enter a number: "))
    arr = []
    for i in range(num):
        arr.append(int(input()))
    print("Original array: ")
    print(arr)
    print("Maximum element: ")
    print(majority_element_rec(arr, 0, len(arr) - 1))
except ValueError as err:
    print(err)