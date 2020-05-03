def sum(i):
    global gh
    if i != 0:
        i -= 1
        gh += 1
        sum(i)
    return gh
a = int(input())
b = int(input())
gh = 0
sum(a)
sum(b)
print(gh)
