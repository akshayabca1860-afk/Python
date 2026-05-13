#Calculator Program
while True:
    num1=int(input("Enter a number:"))
    operator=input("Enter a operator(+,-,*,/):")
    num2=int(input("Enter a number:"))
    if operator=="+":
        result=num1+num2
        print("Answer:",result)

    elif operator=="-":
        result=num1-num2
        print("Answer:",result)
    elif operator =="*":
        result=num1*num2
        print("Answe",result)
    elif operator=="/":
        if  num2==0:
           print("Cannot divide by zero")
        else:
            result==num1/num2
            print("Answer:",result)
    else:
        print("Invalid result")

    choice=input("Do you want to continue? (yes or no):")
    if choice=="no":
        print("Calaultor colsed")
        break
    
