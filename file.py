#  read mode:-------

f=open("dem.txt","r")
data=f.read()

print(data)

f.close()



#  write mode:---------

f=open("dem.txt","w")
data=f.write("my name is sujeet")

f.close()

# append:----


f=open("dem.txt","a")
data=f.write(" hlooo")
f.close()

# with syntax:-----

with open("dem.txt","r") as f:
 
    data=f.read()
    print(data)
f.close()



# delete a file :---


import os
os.remove("new.txt")