#begin 23
a = int (input ('Введите число А, А = '))
b = int (input ('Введите число B, B = '))
c = int (input ('Введите число C, C = '))
d = a
a = b
b = c
c = d
print('A -> B Новое A = ',a)
print('B -> C Новое B = ',b)
print('C -> A Новое C = ',c)