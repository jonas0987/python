with open("practise.txt","+w") as f:
    f.write("hi everyone\nwe are learnning FILE I/O\nusing java \n I like programing in java")

with open("practise.txt","r") as f:
 a=f.read()
print(a)



# 2:-----

with open("practise.txt","r") as f:
    d=f.read()
e=d.replace("java","python")
print(e)    


# 3----

with open("practise.txt","r") as f:
    data=f.read()

    if(data.find("learnning") !=-1):
        print("found")
    else:
        print("not found")     


def check():

 line=1
 with open("practise.txt","r") as f:

    while True:
      data=f.readline()
      if("java"in data):
        print(line)
        return
      line+=1
 return -1
 
check()

