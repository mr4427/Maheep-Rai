"""
i = 1
while i<=5:
    print(i)
    i = i+1

for i in range(1,6):
    print(i)

for i in range(0,11,2):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(1,10,2):
    print(i,end=" ")



word = "apple"
for i in word:
    print(i)

for i in "apple":
    print(i)



for i in range(10,0,-1):
    print(i)


for i in range(0,10):
    print(i*i)

for i in range(1,6):
    print(i*i*i)

for i in range(1,6):
    print("*"*i)



total=0
for i in range(1,11):
    total += i
    print("Sum =", total)



for x in range(6):
    print(x)

for x in range(2,6):
    print(x)


for x in range(2,30,3):
    print(x)

for x in range(0,11):
    print(x,end=" ")

def print_range(a_range):
    for num in a_range:
        print(num, end =" ")

print_range(range(0,11))
print_range(range(0,21,2))
print_range(range(0,16,2))
print_range(range(0,-1,-1))

def print_reverse(text):
    print("Original string: ", text)
    for i in range(-1,-len(text)-1,-1):
        print(text[i])
print_reverse("Dubaqi")

str="Dubai"
print(str[::-1])

"""



    
