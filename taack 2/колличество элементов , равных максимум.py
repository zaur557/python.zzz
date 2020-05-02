a = int(input())
max = a
k = 1
while a != 0:
    a = int(input())
    if max == a:
        k = k + 1
    else:
        if max < a:
            max = a
            k = 1
        else:
            continue
print(k)
