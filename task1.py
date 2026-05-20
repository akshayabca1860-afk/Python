a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("Addition:",a+b)
print("Subraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Floor division:",a//b)
print("Modulus:",a%b)

#using method 
print("\nUsing Method")
class Calculator():
    def add(self,a,b):
        print("Addition:",a+b)
    def sub(self,a,b):
        print("Subtraction:",a-b)
    def multiply(self,a,b):
        print("Multiplication:",a*b)
    def div(self,a,b):
        print("Division:",a/b)
c=Calculator()
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c.add(a,b)
c.sub(a,b)
c.multiple(a,b)
c.div(a,b)
    
print("\nPassword Calculation")
correct_password="12345"
for attempt in range(3):
    password =input("Enter your password:")
    if password==correct_password:
        print("Your password in correct")
    
        
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")
        choice=input("Enter your choice:")
        if choice=="5":
            print("The Calculation is closed")
            break
        elif choice in["1","2","3","4"]:
            num1=int(input("Enter your first number:"))
            num2=int(input("Enter you second number:"))
            if choice=="1":
                print("result",num1+num2)
            elif choice=="2":
                print("result",num1-num2)
            elif choice=="3":
                print("result",num1*num2)
            elif choice=="4":
                if num2==0:
                    print("Cannot divided by zero")
                else:
                    print("result",num1/num2)
            break
    else:
       
       print("Your password is incorrect")
       print("Remaining attempts:",2-attempt)
else:
    print("Your limit is over")

            

   








