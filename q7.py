
#   1:----------

a=[1,2,3,4,5,6]


def ln(a):
    return len(a)

print(ln(a))

# 2:-------------

l1=[1,4,9,16,25,36]

def ele():
    for a in l1:
        print(a,end=" ")
   

ele()   


# 3:----------

n=int(input("enter n for fact :-"))

def cal_fact(n):
    fact=1
    while n !=0:
        fact=fact*n
        n=n-1
    print(fact)    

cal_fact(n)


# 4:------------

a=int(input("enter amount in dollar $:-"))

def calrs(a):
    return a*83

print("your amount in inr is :",calrs(a))


#5:----------

num=int(input("enter the no:-"))

def check(num):
    if(num%2==0):
        print("EVEN")
    else:
        print("ODD")    

check(num)
