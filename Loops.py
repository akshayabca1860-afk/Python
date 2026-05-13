#Print numbers from 1 to 10
for i in range(11):
    print(i)

#Print numbers from 10 to 1
print("\nLoops")
for i in range (10,0,-1):
    print(i)

#Print even numbers from 1 to 20
print("\nEven Numbers")
for i in range(2,20,2):
    print(i)

#print odd numbers from 1 to 20
print("\nOdd Numbers")
for i in range(1,20,2):
    print(i)

#print multiplictiontble of a number Gind the sum of numbers from 1 to 100
print("\nMulitiplication")
num=7
for i in range(1,11):
    print(num,'x',i,'=',num*i)
# Find the sum of numbers
print("\nFind sum of Number")
value=0
for i in range(1,99):
    value=value+i
    print(value)
#Find the factorial numbers
print("\nFactorial numbers")
num=6
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)
#Count how many number divisiblel by 5 from 1 to 50
count=0
for i in range(1,51):
   if i % 5==0:
       count=count+1
print(count)
#Print each character in a word
word="Akshu"
for letter in word:
    print(letter) 

#Count vowels in a string
print("\nFind Vowels")
word="Messageyourself"
count=0
for letter in word:
    if letter in "aeiou":
        count = count + 1
print(count)

