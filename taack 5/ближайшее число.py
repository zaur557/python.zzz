n = int(input())
s = list(map(int, input().split(" ")))
x = int(input())
zzz = []
for i in range(n):
    s[i] = int(s[i])
    zzz.append(abs(s[i] - x))
n = zzz.index(min(zzz))
print(s[n])
