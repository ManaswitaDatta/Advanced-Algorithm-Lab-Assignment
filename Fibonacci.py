def fibonacci_rec(num):
    if num <= 1:
        return num
    return fibonacci_rec(num - 1) + fibonacci_iterative(num - 2)


def fibonacci_iterative(num):
    if num < 2:
        return num
    f1 = 0
    f2 = 1
    for i in range(2, num+1):
        f1, f2 = f2, f1 + f2
    return f2


try:
    num = int(input("Enter a number: "))
    print(fibonacci_rec(num))
    print(fibonacci_iterative(num))
except ValueError:
    print("Invalid Number")