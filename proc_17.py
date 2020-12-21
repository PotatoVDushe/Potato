def D(x,n):
    if n==1:
        D=x%10
    else:
        if x<10:
            D=-1
        else:
            D=D(x//10 ,n-1)
