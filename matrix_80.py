def h1(l):
    s = 0
    i = 0
    while i < n:
        s += l[i][i]
        i += 1
    return s
import numpy as np
import random
a=[]
n = int(input('Количество столбцов/строк '))
a = np.random.randint(0, 5, size=(n,n))
sum = h1(a)
print(a)
print('Сумма ',sum)
