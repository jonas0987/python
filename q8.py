#   1:-------------


def summ(n):
    if(n==0):
        return 0
    
    return summ(n-1)+n

print(summ(8))    


#   2:-------------

l1=[1,2,3,4,5]

def pr(a,i):
    if(i==len(l1)):
        return
    print(l1[i])
    pr(a,i+1)

pr(l1,0)