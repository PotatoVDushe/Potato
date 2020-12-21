import math
def h(A,B,C):
    D = 0
    D = B * B - 4 * A * C
    if D < 0:
        return 0
    elif D == 0:
        return 1
    else:
        return 2
for i in range(0,3):
    print('Введите  A: ');
    A=float(input())
    print('Введите  B: ');
    B=float(input())
    print('Введите  C: ');
    C=float(input())
    print(' ')
    print(' = ',h(A,B,C))
    print(' ')
