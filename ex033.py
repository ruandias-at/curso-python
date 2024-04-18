n1 = int(input("Primeiro número:"))
n2 = int(input("Segundo número:"))
n3 = int(input("Terceiro número:"))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3
print("O maior número é {}.".format(maior))

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3
print("E o menor número é {}.".format(menor))
