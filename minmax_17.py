import random
n = int(input('Введите число n (1,10) '))
a=[]
max=n
p=0
for i in range(n):
    a.append(random.randint(0, 10))
    print('Число из N спмска ',a[i])
    if a[i] > max:
        max=a[i]
        p=0
    else:
         p=p+1
print('Количество элементов',p)
