import math


def prime(num):
    if num < 2:
        return False
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True


try:
    num = int(input("Enter a number: "))
    print(prime(num))
except ValueError:
    print("Invalid Number")