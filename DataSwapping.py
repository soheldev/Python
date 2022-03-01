"""Write a program to take two number from the user into a and b veriable 
and swap the contain of this two verb."""

a=int(input("Enter num1 "))
b=int(input("Enter num2 "))
c=a
b=a
b=c
print(a, b)

#Write a program to square the contain of two variable without using third variable.

a=int(input("Enter num1 "))
b=int(input("Enter num2 "))
a=a+b
b=a-b
a=a-b
print(a,b)

'''write a program to take two digit from user and seprate it digit and perfrom 
addition of its digit'''

a=int(input("Enter any 2 digit Number "))
b=a//10
c=a%10
print(b+c)

'''write a program to take three digit from user and seprate it digit and perfrom 
addition of its digit'''

a=int(input("Enter any 3 digit Number "))
b=a//100
c=a%100
d=c//10
e=c%10
print(b+d+e)

'''write a program to take two digit from user and seprate it digit and perfrom 
reverse of its digit'''

a=int(input("Enter any 2 digit Number"))
b=a//10
c=a%10
d=b+c*10
print(d)

'''write a program to take three digit from user and seprate it digit and perfrom 
reverse of its digit'''

a=int(input("Enter any 2 digit Number"))
b=a//100
c=a%100
d=c//10
e=c%10
f=d*10+e*100+b
print(d)