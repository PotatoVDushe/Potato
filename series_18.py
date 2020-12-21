import pandas as pd
from itertools import groupby
import random
a=[]
n = int(input('Введите число n '))
print('Число из N списка ')
for i in range(n):
    a.append(random.randint(0, 5))
    print(a[i], end=" ")
print(' ')
a.sort()
a2 = [el for el, _ in groupby(a)]
a2 = pd.Series(a2)
print(a2)
