"""Write a program to take distance in meter & 
convert that distance into feet, inces & cm"""
meter= float(input("Enter the distance in Meter "))
foot=meter*3.27
inches=meter*39.37
cm=meter*100
print("Distance in Foot",foot)
print("Distance in inches",inches)
print("Distance in cm",cm)

"""Employe basic salary is input from keyboard , 
his D.A is 20% of basic salary, his H.R.A is 40% of basic salary, 
Calculate his total salary"""

bs=float(input("Enter the salary "))
da=bs*0.2
hra=bs*0.4
total=bs+da+hra
print ("Total salary is", total)