"""
a = int(input("Enter your first number"))
b = int(input("Enter your second number"))
if a > b:
    print("a is greater")
elif a < b:
    print("b is greater")
else:
    print("a and b are equal")

age = int(input("Enetr your age"))
if age <= 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

age = int(input("Enetr your age"))
if age < 2:
    print("infant")
elif age < 4:
    print("Toddlers")
elif age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age > 60:
    print("Senior")
else:
    print("Adult")


a = int(input("Enter your first number"))
b = int(input("Enter your second number"))
c = int(input("Enter your third number"))

if a>=b and a>=c:
    print("a is greater")
elif b>=a and b>=c:
    print("b is greater")
else:
    print("c is greater")

grade = int(input("Enter your marks"))
if grade>90:
    print("A")
elif grade>75:
    print("B")
elif grade>65:
    print("C")
elif grade>55:
    print("D")
else:
    print("Fail")
"""

a = int(input("Enter first side"))
b = int(input("Enter second side"))
c = int(input("Enter third side"))
if a==b and b==c:
    print("It is a equilateral triangle")
elif a==b or b==c or a==c:
    print("Its is an issoceles triangle")
else:
    print("It is a scalene triangle")











