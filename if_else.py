#basic program
from functools import total_ordering


age=int(input("Enter your age "))
if age>=18:
    print("you can vote")
else:
    print("you can not vote")

#basic program
x=int(input("enter number "))
#y=x%2
if x%2==0:
    print("even")
else:
    print("odd")

"""Write a program to take 2 number into A&B variable and
Print which is maximum number"""
a=int(input("Enter num1 "))
b=int(input("Enter num2 "))
if a>b:
    print("a is max")
else:
    print("B is max")

"""Write a program to take 3 digit number from the user and check 
the number is armstronge aur not"""
a=int(input("Enter 3 digit number "))
b=a//100
c=a%100
d=c//10
e=c%10
f=b**3+d**3+e**3
if f==a:
    print("Armstrongee number")
else:
    print("not Armstronge number")

"""Write a program to take input angle of the trangle 
and check that wheather it is valid or not"""
a1=int(input("Enter Angle 1"))
a2=int(input("Enter Angle 2"))
a3=int(input("Enter Angle 3"))
total=a1+a2+a3
if total==180:
    print("Valid Trangle ")
else:
    print("Invaild ")