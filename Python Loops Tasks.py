print("1- printing numbers from 0 to 10 using while...")
x = 0
while x < 11:
    print(x)
    x +=1

input("Press any key to continue...")

print("2- Printing numbers from 0 to 10 using for...")

for x in range(11):
    print(x)

input("Press any key to continue...")

print("3- Stopping the loop if the number = 5")

for x in range(10):
    if x>=5:
        break
    print(x)

input("Press any key to continue...")

print("4- Skipping the 5 iteration from print")

for x in range(10):
    if x==5:
        continue
    print(x)

input("Press any key to continue...")

print("5- Printing multiplication table from 1 to 5")
num = [1,2,3,4,5]

for numbers in num:
    for y in range(1,11):
        print(*num, "x", y, "=", y*numbers)

input("Press any key to continue...")

print("6- Getting numbers from 10 to 20 using range")

for x in range(10,21):
    print(x)

input("Press any key to continue...")

print("7- Getting numbers from 10 to 100 with 3 at each step using range")

for x in range(10,101,3):
    print(x)

input("Press any key to continue...")

print("8 & 10")

for num in range(0,101,2):
        print(num)

input("Press any key to continue...")

print("9- Getting a list of even numbers from 1 to 100 using while...")

x=0

while x != 100:
    x+=2
    print(x)






