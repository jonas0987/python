class student:
    def __init__(self,name,marks):
        self.name=input("enter your name:-")
        

    @staticmethod
    def aas():
      print("hello")

s1=student("name","marks")
print("the name of first student is",s1.name)

s1.aas()