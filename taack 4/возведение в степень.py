def число(a, n):
    if n == 0:
        return 1
    return a * число(a, n - 1)
a = float(input())
n = float(input())
print(число(a, n))
