#Store student names in using arraylist
student=[] 
n=int(input("Enter the number of students:"))
for i in range(n):
    name=input("Enter the students name:")
    student.append(name)
print("Students name:")
for name in student:
    print(name)

#Remove duplicate numbers using HashSet
("\nDuplicate")
numbers=set()
n=int(input("Enter the number of elements:"))
for i in range(n):
    num=int(input("Enter the number:"))
    numbers.add(num)
print("After removing the duplicates:")
print(numbers)
#Store employee ID and name using Dictionary
Students={}
n=int(input("Enter the number of Students:"))
for i in range(n):
    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    mark=float(input("Enter your mark:"))
    Students[name]= {
        "age":age,
        "mark":mark
}
print(Students)