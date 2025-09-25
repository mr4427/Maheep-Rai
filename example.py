name = "Maheep"
print(name)
print(len(name))
print(name[0])
print(name[3])
print(name[-1])

name = "Maheep"
print(name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name)
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])

name = "Joda"
print(name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name)
print(name[::-1])

name = "aya"
rname = name[::-1]
if name == name[::-1]:
    print("It is palindrome")


word = input("Enter a word")
print(word)
print(word[::-1])
if word == word[::-1]:
    print("Palindrome")
else:
    print("It is not a palindrome")


count = 0
while True:
    count = count + 1
    if count % 5 == 0:
        continue
    elif count >= 1000:
        break
    print(count)

print("Done!")
def sum_of_odd():
    total = 0
    while True:
        num = int(input("Enter a number (0 to stop): "))
        if num == 0:
            break
        if num % 2 == 0:
            continue
        total += num
    print("Sum of odd numbers:", total)
sum_of_odd()


def hello_you(name='Leia'):
    print('Hello,', name)

hello_you('Luke')
hello_you()

r1_5 = range(1, 5)
print(r1_5)

r2_10 = range(2, 10)
print(r2_10)


def print_range(a_range):
    for num in a_range:
        print(num, end=" ")
print_range(range(0, 11))
print_range(range(0, 21, 2))
print_range(range(5, 16, 2))
print_range(range(10, -1, -1))




