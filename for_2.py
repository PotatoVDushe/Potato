a = int(input('Введите число A '))
b = int(input('Введите число B '))
while a > b:
	b = int(input('Введите число b (B>A) '))
n=b-a
for i in range(n+1):
	print(a)
	a=a+1
