import math

a = float(input("Digite o comprimento do cateto adjacente:"))
o = float(input("Digite o comprimento do cateto oposto:"))
h = math.hypot(a, o)

print("A hipotenusa mede {:.2f}".format(h))
