class Student:
    # name="sujeet"
    college_name="IGC"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print(self)
        print("self call")

    def welcome(self):
        print("welcome student")

s1=Student("sujeet",89)
print(s1.name,s1.marks)
print(s1.college_name)
print(Student.college_name)

s1.welcome()