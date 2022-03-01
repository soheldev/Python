#Program 01
a=int(input("Enter the Number_1 "))
b=int(input("Enter the Number_2 "))
c=int(input("Enter the Number_3 "))
if a>=b and a>c:
    print("A is Max")
elif b>a and b>=c:
    print("B is Max")
else:
    print("C is Max")

"""Write a program to take Character from the user and 
check that is capital case, Small case and Digit"""

a1=ord(input("Enter Char "))
if a1>=65 and a1<=90:
    print("Capital")
elif a1>=97 and a1<=122:
    print("Small")
elif a1>=48 and a1<=57:
    print("Digit")
else :
    print("IDK")

"""Write a program to input marks of five subject
Physic, Chemistry, Bio, Math & computer"""

s1=int(input("Enter Subject Marks_1"))
s2=int(input("Enter Subject Marks_2"))
s3=int(input("Enter Subject Marks_3"))
s4=int(input("Enter Subject Marks_4"))
s5=int(input("Enter Subject Marks_5"))
total=s1+s2+s3+s4+s5
per=total*0.2
if per>=90:
    print("Grade A")
elif per>=80:
    print("Grade B")
elif per>=70:
    print("Grade C")
elif per>=60:
    print("Grade D")
elif per>=40:
    print("Grade E")
else:
    print("Grade F")
print("END")

"""Write a program to input any alphabet and 
check whether it is Vowel or Consonant"""

a2=chr(input("Enter Alphabet"))
if a2=='a' or a2=='e' or a2=='i' or a2=='o' or a2=='u':
    print("It is a Vowel")
else:
    print("It is Consonant")