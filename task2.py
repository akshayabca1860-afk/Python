def add(a,b):
        return a+b
def sub(a,b):
        return a-b
def multiply(a,b):
        return a*b
def divided(a,b):
        return(a/b)
def Calculate():
    
        
        
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")

    
        choice=input("Enter your choice:")
        if choice=="5":
            print("The Calculation is closed")
          
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

        continue_choice=input("Do you want to continue? (yes/no):")
        if continue_choice=="no":
         print("Thank you")
                    
                    
                    
       
          
correct_password="12345"
for attempt in range(3):
    password =input("Enter your password:")
    if password==correct_password:
        print("Your password is correct")
        Calculate()
        break
    else:
       
       print("Your password is incorrect")
       print("Remaining attempts:",2-attempt)
      
else:
    print("Your limit is over")
