N = int(input())
K = int(input())
if K % N > 0:
    print(K // N + 1)
else:
    print(K // N)
