def combi(arr, i, v, path):
    # target reached
    if v == 0 and i == len(arr):
        print(path)
        return 1
    if i >= len(arr):
        return 0
    val = str(arr[i])
    if arr[i] < 0:
        val = "(" + str(arr[i]) + ")"
    if path == "":
        path1 = val
        path2 = "-" + val
    else:
        path1 = path + "+" + val
        path2 = path + "-" + val
    return combi(arr, i+1, v, path) + combi(arr, i+1, v - arr[i], path1) + combi(arr, i+1, v + arr[i], path2)


n = int(input("Enter size of the array: "))
arr = []

print("Enter array elements: ")
for i in range(0, n):
    arr.append(int(input()))
v = int(input("Enter v: "))
print(combi(arr, 0, v, ""))
