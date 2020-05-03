a = input().split()
max = int(a[0])
zzz = 0
for i in range(len(a)):
    if int(a[i]) >= max:
        max = int(a[i])
        zzz = i
print(max, zzz)
