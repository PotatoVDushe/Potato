x=int(input('Введите год '))
if x%4 == 0:
	if x%100 == 0 and x%400 != 0:
		print('Дней в году 365')
	else:
		print('Дней в году 366')
else:
	print('Дней в году 365')
