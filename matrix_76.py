import numpy as np
import random
a=[]
a = int(input('Количество столбцов '))
b = int(input('Количество строк '))
a = np.random.randint(0, 5, size=(a, b))
a = np.sort(a, axis = 1)
print(a)
