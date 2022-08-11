
print("1- Base class = parent class = main class are the classes that sub classes = derived classes inherite from")

print("1.6- instance is the constructor, we can define it by __init__")

input("Press any key to continue...")

print("2- when we have the same classes with the same methods and they do the same function but we can't inherite them, because the code inside is differnt")

class A:
    def do(self):
        print("in A")

class B(A):
    pass
        

class C:
     def do(self):
        print("in C")

class D(B,C):
    pass
        


d = D()

d.do()

input("Press any key to continue...")

print("3 - 4 yes we can, it will inherite the first class that has the function that is needed to finish the process")
