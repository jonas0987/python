
# 1:-----

a=1
while a<=100:
    print(a)
    a+=1

    #  2:----

a=100
while a>=1:
    print(a)
    a-=1


#  3:----

n=int(input("enter no that you want to print the table:-"))
a=1
while a<=10:
    print(n,"x",a,"=",n*a)
    a+=1
    

#  4:------

a=1
while a<=10:
    print(a**2)
    a+=1

#  5:----

s=(1,4,9,16,25,36,49,64,81,100)
 
key=int(input("enter the search element:-"))

i=0
while i<len(s):
   if(s[i]==key):
        print("found at index",i)
        break
   else:
       print("finding.....")
           
   i+=1


# -------for loop-----------
l1=[1,4,9,16,25,36,49,64,81,100]
for val in l1:
    print(val)


tuple=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
for a in tuple:
    if(x==a):
        print("found",i)
    i+=1    