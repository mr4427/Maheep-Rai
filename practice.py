
a = int(input("First side"))
b = int(input("second side"))
c = int(input("third side"))
if a==b and b==c and c==a:
    print("yes")
else:
    print("no")

def volume_of_cuboid(length,breadth,height):
    return length*breadth*height

def main():
    volume = volume_of_cuboid(10,10,10)
    print("Volume of cuboid: ", volume)

main()

