n=int(input("enter n:-"))
sum=0

while n!=0:
    sum=sum+n
    n-=1

print(sum)


#  2:------

a=int(input("enter n for factorial :-"))
fact=1
while a!=0:
    fact=fact*a
    a-=1
print(fact)    


for i in range(1,a+1):
    fact*=i
    
print(fact)
