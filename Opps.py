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


