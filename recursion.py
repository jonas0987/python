def show(a):
    if(a==0):
        return
    print(a)
    show(a-1)


show(10)    


def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return fact(n-1)*n

print(fact(8)) 