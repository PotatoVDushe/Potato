import random
n = int(input('Введите число n '))
a=[]
b=[]
c=[]
d=[]
for i in range(n):
    a.append(random.randint(0, 100))
    b.append(random.randint(0, 100))
    c.append(random.randint(0, 100))
for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print('Массив a ',a)
for i in range(n-1):
    for j in range(n-i-1):
        if b[j] > b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]
print('Массив b ',b)
for i in range(n-1):
    for j in range(n-i-1):
        if c[j] > c[j+1]:
            c[j], c[j+1] = c[j+1], c[j]
print('Массив c ',c)
d = a+b+c
n=n*3
for i in range(n-1):
    for j in range(n-i-1):
        if d[j] > d[j+1]:
            d[j], d[j+1] = d[j+1], d[j]
print('Массив d ',d)
