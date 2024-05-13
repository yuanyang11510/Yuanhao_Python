#抢红包
l1 = ['殷元昊','代方方','代圆圆','代华杨','李玉玲','余银娟','殷晓洪','陈露露','代东东','杨婷']
from random import*
i = 1
x = 100
l2 = []
while i < 10:
    a = randint(0,x)
    x = x-a
    l2.append(a)
    i = i+1
l2.append(round(x,2))
d = dict(zip(l1,l2))
for name,money in d.items():
    print(name,money)
