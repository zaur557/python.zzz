h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
hh1 = (h1 % 24) * 60 * 60
mm1 = (m1 % 60) * 60
ss1 = s1 % 60
hh2 = (h2 % 60) * 60 * 60
mm2 = (m2 % 60) * 60
ss2 = s2 % 60
print((hh2 + mm2 + ss2) - (hh1 + mm1 + ss1))
