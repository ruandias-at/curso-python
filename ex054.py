maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input("Data de nascimento:"))
    if ano >= 2006:
        menor += 1
    else:
        maior += 1
print("{} pessoa(s) são maiores de idade e {} são menores.".format(maior, menor))
