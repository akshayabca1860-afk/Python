#Create method for addition, subtraction, multiplication, division.
class Method:
    
    def addition(self, a,b):
        print("Addition:", a+b)

    def subtraction(self,a,b):
        print("Subtraction:",a-b)

    def multiplication(self,a,b):
        print("Multiplication:",a*b)

    def division(self,a,b):
        print("Division:", a/b)
    
m1=Method()
m1.addition(2,4)
m1.subtraction(5,2)
m1.multiplication(4,2)
m1.division(10,2)

#Create a method to check prime number
class Primenumber:
    def check_prime(self,num):
        if num<=1:
            print(num,'is not prime number')
            return
        for i in range(2,num):
            if num %2==0:
                print(num," is not prime number")
                return
            print(num, "is a prime number")

p1=Primenumber()
p1.check_prime(3)
p1.check_prime(20)     

#Create a method to check students grade
print("\nStudents Grade")
class Studentmark:
    def grade(self,mark):
        if mark>=90:
            print("Grade A")
        elif mark>=80:
            print("Grade B")
        elif mark>=50:
            print("Grade C")
        else:
            print("Grade D")
s1=Studentmark()
a=int(input("Enter your mark:"))

s1.grade(a)

#create a method to revese sting
("\nReversestring Method")
class Reversestring:
    def reverse(self, text):
        rev=text[::-1]
        print("Reverseed String:", rev)

r=Reversestring()
a=input("Enter a String:")
r.reverse(a)
#Create a method to factorial
("\n Factorial")
class Factorial:
    def find(self,num):
        fact=1
        for i in range(1,num+1):
            fact=fact*i
            print("Factorial is:",fact)
f1=Factorial()
x=int(input("Enter a number:"))
f1.find(x)