s = input()
z = 'f'
a = s.find(z)
sNext = s [a + 1 :: 1]
b = sNext.find(z)
if a != -1:
    if b != -1:
        print(b + a + 1)
    elif b == -1:
        print('-1')
elif a == -1:
    print('-2')
        
