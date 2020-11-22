def factorial_rec(num):
    if num <= 1:
        return 1
    return num*factorial_rec(num-1)


def factorial_iterative(num):
    res = 1
    for i in range(1, num+1):
        res = res*i
    return res


try:
    num = int(input("Enter a number: "))
    print(factorial_rec(num))
    print(factorial_iterative(num))
except ValueError:
    print("Invalid Number")