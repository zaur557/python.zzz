a = list(map(int, input().split(" ")))
b = []
for i in range(len(a)):
    if i % 2 == 0:
        b.append(a[i])
print(' '.join(map(str, b)))
