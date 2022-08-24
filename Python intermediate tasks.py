numbers = [5,7,9,20,11,12]
nn = []
for n in numbers:
    new_n = n*n
    nn.append(new_n)
print(nn)
input("Press any key to continue to the second solution")
nn1 = [n*n for n in numbers]
print(nn1)
input("Press any key to continue to the third solution")
def power(n):
    return n*n
nn2 = list(map(power,numbers))
print(nn2)

names = ['tarek','ahmad','ayham','ammar']

new_names = []
for n in names:
    upper = n.upper()
    new_names.append(upper)
print(new_names)
input("Press any key to continue to the second solution")
new_names1 = [n.upper() for n in names]
print(new_names1)
input("Press any key to continue to the third solution")
def modtext(n):
    return n.upper()
new_names2 = list(map(modtext,names))
print(new_names)

numbers1 = list(range(1,101))
even_numbers = []

for n in numbers1:
    if n%2 == 0:
        even_numbers.append(n)
print(even_numbers)

input("Press any key to continue to the second solution")

even_numbers1 = [n for n in numbers1 if n%2 == 0]
print(even_numbers1)

input("Press any key to continue to the third solution")
def myfunc(n):
    if n%2 == 0:
        return True

numbers = list(range(1,101))

even_numbers2 = list(filter(myfunc,numbers))
print(even_numbers2)

prod = {'IPhone':1000, 'Samsung':800, 'Gaming PC':2000}
prod_with_tax = {}

for k,v in prod.items():
    prod_with_tax[k] = v+(v*(19/100))
print(prod_with_tax)

input("Press any key to continue to the second solution")

prod_with_tax1 = {k:v+(v*(19/100)) for k,v in prod.items()}
print(prod_with_tax1)

input("Press any key to continue to the third solution")
def withtax(n):
    return n+(n*(19/100))

prodwithtax = list(map(withtax,prod.values()))
print(prodwithtax)