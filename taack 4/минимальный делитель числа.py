def Min(n):
    i = 1
    while i != n:
        i += 1
        if n % i == 0:
            return i
        if i >= n ** (1 / 2):
            return n
n = int(input())
print(Min(n))
