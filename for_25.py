x = float(input('Введите число |x| (<1) '))
n = int(input('Введите число n (>0) '))
b=0
a=0
for i in range(1,n):
    b=a+b
    a=((-1)**i-1)*(x**i)/i
print(b)
