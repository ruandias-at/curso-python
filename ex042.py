a = float(input("Primeiro lado:"))
b = float(input("Segundo Lado:"))
c = float(input("Terceiro Lado:"))

if a + b > c and b + c > a and c + a > b:
    print("É possível formar um triângulo", end=" ")
    if a == b == c:
        print("EQUILÁTERO.")
    elif a != b != c:
        print("ESCALENO.")
    else:
        print("ISÓSCELES.")
else:
    print("Não é possível formar um triângulo.")
