n = (int(input("Digite um valor:")),
     int(input("Digite outro valor:")),
     int(input("Digite mais um valor:")),
     int(input("Digite o último valor:")))
print(f"Os valores digitados foram:{n}")
print(f"O número 9 apareceu {n.count(9)} vezes.")
if 3 in n:
    print(f"O número 3 apareceu pela primeira vez na {n.index(3) + 1}ª posição.")
else:
    print("O número 3 não apareceu nenhuma vez.")
print("Os números pares digitados foram:", end=" ")
for v in n:
    if v % 2 == 0:
        print(v, end="-")
