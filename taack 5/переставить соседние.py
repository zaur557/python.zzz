s = list(map(int, input().split(" ")))
zzz = []
ggg = []
for i in range(len(s)):
    while i < len(s) - 1 and len(zzz) < len(s):
        zzz.append(s[i + 1])
        zzz.append(s[i])
        i += 2
    if len(s) % 2 != 0:
        ggg.append(s.pop())
        r = ggg[0]
        zzz.append(r)
print(*zzz)
