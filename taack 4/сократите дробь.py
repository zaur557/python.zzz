def дробь(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b
a = int(input())
b = int(input())
print(a // дробь(a, b), b // дробь(a, b))
