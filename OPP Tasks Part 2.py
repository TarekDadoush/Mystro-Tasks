class Calculator:
    def __init__(self):
        print("Welcome")

    def sum(self,x,y):
        return x + y

    def mull(self,x,y):
        return x*y

    
class SciCalc(Calculator):

    def power(self,x,y):
        return x**y


sc = SciCalc()

print(sc.sum(10,20))
print(sc.mull(10,20))
print(sc.power(2,2))

print("When we inherite a class, the sub class inherites everything from the parent class")
    
