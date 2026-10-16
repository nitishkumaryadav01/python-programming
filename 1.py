""" a=int(input("enter a no : "))
b=int(input("enter a no :"))
def add(a,b):
    return a+b
print(add(a,b)) """

""" a=int(input("enter a no :"))
b=int(input("enter a no :"))
def multiplication(a,b):
    return a*b
print(multiplication(a,b)) """

#compare that product against 1000 to decide whether to return the product or the sum.
a=int(input("enter a no : "))
b=int(input("enter a no :"))
def add(a,b):
    return a+b
def multiplication(a,b):
    return a*b
print(multiplication(a,b))
if multiplication(a,b)>1000:
    print(add(a,b))
else:
    print(multiplication(a,b))
