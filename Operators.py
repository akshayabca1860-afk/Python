#Operators are symbols used to perform operations on variables and values.
#Arithmetic Operators
#It is used for mathematical calculations
a=4
b=7
print("Arithmetic Operators")
print("Addition:",a+b)
print("Subraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Floor Division:",a//b)
print("Modulus:",a%b)
#Comparison Operators
#It is used to compare two values
print("\nComparison Operators")
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
#Logical Operatoor
#It is used to combine condition
print("\nLogical Operator")
print(a>5 and b<10)
print(a>20 or b<10)
print(not(a>b))
#Assignment Operators
#It is used to assign the values
print("\nAssignment Operator")
x=5
x+=2
print(x)
x-=3
print(x)
x*=7
print(x)
x/=5
print(x)
#Identity Operators
#it is used to compare memory locations
print("\nIdentity Operators")
c=[8,5,6]
d=c
e=[8,5,6]
print(c is d)
print(c is e)
print(c is not e)
#Membership Operators
#It is used to check value inside sequence.
print("\nMembership Operatots")
s=[2,3,4,5,7]
print(4 in s)
print(9 in s)
print(1 not in s)
#Bitwise Operators
#It is used to perform bit-level operations
print("\nBitwise Operators")
print(a&b)
print(a|b)
print(a^b)
print(-a)
print(a<<1)
print(a>>1)