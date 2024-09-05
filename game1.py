import random

target=random.randint(1,100)

while True:
   userchoice=int(input("enter your number "))
   if(userchoice==target):
      print("congtratulation")
      break
    
   elif(userchoice < target):
        print("your no is smaller think small no ")
        
   else:
        print("your no is bigger think big no ")
        
 
print("-------GAME OVER-------")
