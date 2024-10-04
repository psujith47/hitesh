""""01.Write a Python program to convert temperature in
degree Celsius to degree Fahrenheit. If water boils
at 100 degree C and freezes as 0 degree C, use the
program to find out what is the boiling point and
freezing point of water on the Fahrenheit scale.
(Hint: T(°F) = T(°C) × 9/5 + 32)"""

print('Hello,Do wanna convert Celsius to Fahrenheit?')
response=input("Type Yes or No: ")
if response.lower() == "yes":
    print("Okay, Lets go\nEnter the temperature in Celsius:")
    C = float(input())
    F = C * 9/5 + 32
    print("So the temperature in Fahrenheit is: ", F,'F')

else :
    print("Okay, Have a nice day!")



"""02.Write a program to asks the user name and age. Print a message addressed to the user that tells the user 
the year in which they will turn 100 years old."""

name=str(input("Hi there, May I have your name?"))
print("Okay",name,"Let me know how old are you:")
age=int(input())
print("So,",name,"I am sorry to say that you will be turning 100 years old in",2024-age+100)


""" 03.A dartboard of radius 10 units and the wall it is hanging on are represented using a two-dimensional 
coordinate system, with the board’s center at coordinate (0,0). Variables x and y store the 
x-coordinate and the y-coordinate of a dart that hits the dartboard. Write a Python expression using 
variables x and y that evaluates to True if the dart hits (is within) the dartboard, and then evaluate the 
expression for these dart coordinates:
 a) (0,0)
 b) (10,10)
 c) (6, 6) 
d) (7,8)"""

print("Let's see if you have hit the dartboard or not!")
x=int(input("Mention your x-coordinate: "))
y=int(input("Mention your y-coordinate: "))


area=float(3.14*x*y)
if area < 314 and x!=0 or y!=0:
    print("You have hit the dartboard!")

if area > 314:
    print("You missed the dartboard!")

if x==0 and y==0:
    print("You have hit the bulls eye,let's go!!")

"""04.write a program to create a simple calculator to perform basic arithmetic operations on two numbers. 
The program should do the following:
 • Accept two numbers from the user.
 • Ask user to input any of the operator (+, -, *, /). 
   An error message is displayed if the user enters 
anything else.
 • Display only positive difference in case of the 
operator "-".
 • Display a message “Please enter a value other 
than 0” if the user enters the second number as 
0 and operator ‘/’ is entered"""

import math
print("Hi this is a basic calculator to perform basic arithmetic operations on two numbers\n")
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
prf=str.lower((input("What do you wanna do?\n+, -, *, / or modulus,sqrt: ")))

if prf == "+":
    print(a+b)

elif prf == "-":
    print(a-b)

elif prf == "*":
    print(a*b)

elif prf == "/":
    if b == 0:
        print("Please enter a value other than 0")
    else:
        print(a/b)


if  prf == "modulus" :
    print(a//b)
if prf == "sqrt":
    ch=str.lower(input("Of which number? " ))

    if ch == "first number":
        print(math.sqrt(a))
    if ch == "second number":
        print(math.sqrt(b))

#05.

k=int(input("enter any number:"))
for i in range(1,k+1):
    if k%i==0:
        print(i)


#06.
# Initialize the sum to 0

total_sum=0
while True:
    # Ask the user for input
    num = int(input("Enter a number (negative number to stop): "))

    # If the number is negative, break the loop
    if num < 0:
        break

    # Add the positive number to the total sum
    total_sum += num

# Display the result
print(f"The sum of all positive numbers is: {total_sum}")


#07.


num3=int(input("Enter the number: "))
for rg in range(1,num3):
    print(rg)
for i,rg in enumerate(range(1,num3)):
    if i==0:
        print(i)






