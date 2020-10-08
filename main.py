import random
a = random.randint(100,999)
print(a)

c = a/100
o = a%100
c = int(c)
c1 = o/10
c1 = int(c1)
o1 = int(o%10)

s = c+c1+o1
print(s)