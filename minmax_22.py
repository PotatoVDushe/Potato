import random
n = int(input('Введите число n (2,10) '))
a=[]
min=n
s=n
for i in range(n):
    a.append(random.randint(0, 10))
    print('Число из N спмска ',a[i])
    if a[i] < min:
        min=a[i]
    if a[i] > min and a[i] < s:
        s=a[i]
print ('2 минимальных элиментов в порядке возрастания ',min,s)
