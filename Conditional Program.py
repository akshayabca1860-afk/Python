#Check Whether a number is even or odd.
print("Even or Odd")
a=int(input("Enter a number:"))
if a % 2 == 0:
    print("It is Even Number")
else:
    print("It is Odd Number")
#Check Whether a number is positive, negative, or zero.

x=int(input("Enter a value:"))
if x>0:
    print("it is Positive Number")
elif x<0:
    print("It is Negative Number")
else:
    print("It is Zero")
#Find the largest of 3 numbers.
print("\n\nFind theh largest number")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>=b and a>=c:
    print("Largest number is :",a)
elif b>=a and  b>=c:
    print("Largest number is :",b)
else:
    print("Largest number is:",c)





