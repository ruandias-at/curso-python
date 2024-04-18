listanum = []
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f"Digite o número da posição {c}:")))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print("=" * 50)
print(f"Você digitou os valores: {listanum}")
print("=" * 50)
print(f"O menor valor digitado foi {menor} e ele está na(s) posição(ões): ", end = " ")
for i, v in enumerate(listanum):
    if v == menor:
        print(f"{i} ", end = " ")
print(f"\nO maior valor digitado foi {maior} e ele está na(s) posição(ões): ", end = " ")
for i, v in enumerate(listanum):
    if v == maior:
        print(f"{i} ", end = " ")
