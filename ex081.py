lista = list()
cont = 0
while True:
    lista.append(int(input("Digite o valor a ser adicionado: ")))
    r = str(input("Você deseja continuar digitando valores? [S/N] "))
    cont += 1
    if r in "Nn":
        break
print(f"Foram adicionados {cont} valores à lista.")      
print(f"A lista organizada de forma decrescente ficou: ")
#lista.sort()
#lista.reverse()
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print("O valor 5 apareceu na lista.")
else:
    print("O valor 5 não apareceu na lista.")    
