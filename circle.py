def circle_area(radius):
    return 3.14*radius**2

def main():
    area = circle_area(10)
    print("Area of Circle: ",area)

main()

def triangle_area(base,height):
    return 1/2 * base * height

def main():
    area = triangle_area(10,20)
    print("Area of triangle: ",area)

main()
def square_area(side):
    return side*side

def main():
    area = square_area(10)
    print("Area of sqyare: ",area)

main()

def rectangle_area(length,breadth):
    return length*breadth

def main():
    area = rectangle_area(10,20)
    print("Area of rectangle: ",area)

main()

def circumference(radius):
    return 2 * 3.14 *radius
def main():
    circum = circumference(10)
    print("Circumference of circle: ",circum)

main()

import math
def area(radius):
    return math.pi * radius * radius
def main():
    r = float(input("Enter the radius of the circle: "))
    print("Area of the circle: ", area(r))

main()

def add(x,y):
    return x + y

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("Addition: ",add(num1,num2))

main()

def subtraction(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("subtraction: ",subtraction(num1,num2))
    print("Multiplication: ",multiply(num1,num2))
    print("Division: ",divide(num1,num2))

main()



    




