#Usando WHILE
num = int(input("Digite um número:"))
cont = num
f = 1
print("{}! = ".format(num), end="")
while cont > 0:
    print("{}".format(cont), end="")
    print(" x " if cont > 1 else " = ", end="")
    f *= cont
    cont -= 1
print("{}.".format(f))

#Usando MATH
"""from math import factorial
n = int(input("Digite um número:"))
f = factorial(n)
print("{}! = {}.".format(n, f))
"""
#Usando FOR
"""n = int(input("Digite um número:"))
f = 1
for c in range(n, 1, -1):
    f *= c
print("{}! = {}.".format(n, f))
"""
