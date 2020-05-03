def ch(a, n):
    def even(n):
        if n % 2 == 0:
            return 1
        return 0
    if n == 0:
        return 1
    if even(n):
        return ch(a, n / 2) ** 2
    return a * ch(a, n - 1)
a = float(input())
n = float(input())
print(ch(a, n))
