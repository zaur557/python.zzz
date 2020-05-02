n = int(input())
n1 = n // 1000
n2 = n % 1000 // 100
n3 = n % 100 // 10
n4 = n % 10
p1 = n1 - n4
p2 = n2 - n3
print(p1 * 7 + p2 * 9 + 1)
