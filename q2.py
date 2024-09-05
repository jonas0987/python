
movie=[]

m1=input("enter your 1st movie name:-")
m2=input("enter your 2nd movie name:-")
m3=input("enter your 3rd movie name:-")

movie.append(m1)
movie.append(m2)
movie.append(m3)


print(movie)






# check for palindrome--------------

l1=['m','a','a','m']

l2=l1.copy()

l2.reverse()


if(l1==l2):
    print("this is palindrome")
else:
    print("no palindrome")    
