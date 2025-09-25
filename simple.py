i = 1 
while i<=5:
    print(i)
    i = i+1

i = 1
while i<=10:
    print(i)
    i = i+2

i = 2
while i<=10:
    print(i)
    i =i+2

    
i = 5
while i>=1:
    print(i)
    i = i-1


i = 1
while i<=5:
    print("5 * ", i, " =" , 5 * i)
    i = i+1

i = 1
total=0
while i<=10:
    total+=i
    i=i+1
print("Sum" , total)
total + i 



times = 0
while times < 5:
    print("Hi")
    times = times + 1

print("Bye")

i = 5
while i>=1:
    print(i)
    i = i-1



# countdown function and sum

def countdown(number):
    total = 0
    while number >= 0:
        print(number)
        total += number
        number -= 1
    return total
def main():
    num = int(input("Enter a number: "))
    result + countdown(num)
    print("The sum is:", result)

main()

def countup(number):
    total = 0
    i = 1
    while i <= number:
        print(i)
        total += i
        i += 1