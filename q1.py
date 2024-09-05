a=int(input("enter the vale of a "))

print("you enter the no is ",a)

if(a%2==0):
    print("the no is even")
else:
     print("the no is odd")


a=int(input("enter the vale of a "))
b=int(input("enter the vale of b "))
c=int(input("enter the vale of c "))

if(a>b):
    if(a>c):
        print(a,"is the greatest")
    else:
        print(c,"is greatest")    
elif(b>a):
    if(b>c):
        print(b," is the greatest")
    else:
        print(c," is the greatest")            
else:
    print(c," is greatest")    


if(a>b and a>c):
    print(a,"is greatest")
elif(b>c):
    print(b, " is the greatest")    

else:
    print(c, " is the greatest no")








a=int(input("enter the no "))

print(a)

if(a%7==0):
    print(a,"this no is multiple of 7")
else:
    print(a," is not the miultiple of 7")    