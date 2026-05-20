#Create a class Student with name,age and mark
class Student:
    def __init__(self, name, age, mark):
        self.name=name
        self.age=age
        self.mark=mark
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Mark:",self.mark)

a=input("Enter your name:")
b=int(input("Enter your age:"))
c=int(input("Enter your mark:"))
s1=Student(a,b,c)
s1.display()
