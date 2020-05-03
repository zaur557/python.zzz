def summa():
    global s
    n = int(input())
    if n != 0:
        s += n
        summa()
    if n == 0:
        print(s)
s = 0
summa()
