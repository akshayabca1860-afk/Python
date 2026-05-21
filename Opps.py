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

#Create a BankAccount class with deposit and withdraw methods.
class BankAccount:
    
    def __init__(self,balance):
        self.balance=balance
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Deposit Amount:",amount)
        print("Balance:",self.balance)

    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        
            print("Withdraw Amount:",amount)
            print("Balance:",self.balance)

        else:
            print("Insufficient Balance")


balance=1000
b1=BankAccount(balance)     


deposit_amount=int(input("Enter your amount:"))
b1.deposit(deposit_amount)
withdraw_amount=int(input("Enter your amount:"))
b1.withdraw(withdraw_amount)

#Create an Employee class and calculate salary.
class Employee:
    def __init__(self,name,salary,days):
        self.name=name
        self.salary=salary
        self.days=days
    def calculatesalary(self):
        total_salary=self.salary*self.days
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Days:",self.days)
        print("total_salary:",total_salary)

name=input("Enter the Employee name:")
salary=int(input("Enter the Salary: "))
days=int(input("Enter the days:"))
e1=Employee(name,salary,days)
e1.calculatesalary()

#Use method overriding with parent and child classes.
("\nOverriding")
class Parent:
    def show(self):
        print("This is Parent class")
class Child(Parent):
    def show(self):
        print("This is Child class")

c1=Child()
c1.show()
   



