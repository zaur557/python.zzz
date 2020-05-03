a = int(input())
b = int(input())
if a < b:
    for d in range(a, b + 1):
        print(d, end=' ')
if a > b:
    for d in range(a, b - 1, -1):
        print(d, end=' ')
if b == a:
    print(a)
