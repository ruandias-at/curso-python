maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Peso da {}ª pessoa:".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print("O maior peso é {}Kg.".format(maior))
print("O menor peso é {}Kg.".format(menor))