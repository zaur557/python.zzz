zzz, n = map(int, input().split())
volume = sorted([int(input()) for _ in range(n)])
amount = sum(volume)
while amount > zzz and n:
    amount -= volume.pop()
    n -= 1
print(n)
