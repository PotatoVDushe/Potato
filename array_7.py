import random
n = int(input('Введите число n '))
a=[]
print('Число из N списка ')
for i in range(n):
    a.append(random.randint(0, 100))
    print(a[i], end = " ")
print(' ')
for i in range(n):
    print(a[n-1-i], end =" ")
