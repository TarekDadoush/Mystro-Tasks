print("1- taking 2 numbers and printing their values...")

def do():
    f = 10
    ff = 20
    print(f,ff)
    
do()

input("Press any key to continue...")

print("For the tasks: 2 & 3 & 4")

def num2(x=0,y=0):
    result = x + y
    return result

z = num2()
print(z)

input("Press any key to continue...")

print("5- Creating sum function...")

def mysum(x,y):
    result = x + y
    return f"The result {result} is bigger than 10" if result > 10 else print("The result is smaller than 10")

z = mysum(10,5)
print (z)

input("Press any key to continue...")

print("5 & 6- Creating lambda with sum function...")

z = (lambda x,y: x+y)(10,5)
print(z)

input("Press any key to continue...")

print("Local variable can be seen only inside the function, global variable will remain visible for the whole coding sheet")
