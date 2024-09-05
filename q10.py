class student:
    def __init__(self,name,m1,m2,m3):
        self.name=input("enter 1st student name:")
        self.m1=int(input("enter 1st subject marks:"))
        self.m2=int(input("enter 2nd subject marks:"))
        self.m3=int(input("enter 3rd subject marks:"))

    def aver(self):
        print("the average marks is :",(self.m1+self.m2+self.m3/3))



s1=student("name","m1","m2","m3")
print("user name",s1.name,"\nmarks of 1st sub",s1.m1,"\nmarks of 2nd sub",s1.m2,"\nmarks of 3rd sub",s1.m3)
s1.aver()
