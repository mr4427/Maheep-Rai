#Maheep Kaur Rai id-751000235
def triangle_type_checker():
    """
    Function will take 3 sides from user and show which triangle it is
    """
    side1 = int(input("Enter you first side"))
    side2 = int(input("Enter your second side"))
    side3 = int(input("Enter your third side"))
    if side1==side2 and side2==side3:
        print("It is an equilateral triangle")
    elif side1==side2 or side2==side3 or side1==side3:
        print("It is an isosceles triangle")
    else:
        print("It is a scalene triangle")
    
def main():
    """
    The function will call the previous function
    """
    triangle_type_checker()

main()