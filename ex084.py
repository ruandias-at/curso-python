#cont = 0
#lista = list()
#dados = list()
#pesado = list()
#leve = list()
#while True:
#    dados.append(str(input("Nome: ")))
#    dados.append(int(input("Peso: ")))
#    resp = str(input("Você deseja continuar? [S/N] "))
#    lista.append(dados[:])
#    dados.clear()
#    cont += 1
#    if resp in "Nn":
#        break
#for p in lista:
#    if p[1] >= 95:
#        pesado.append(p[0])
#    elif p[1] <= 70:
#        leve.append(p[0])
#print("-="*30)
#print(f"Foram adicionadas {cont} pessoas na lista.")
#print("-="*30)
#print("LISTA DE MAIS LEVES")
#print(leve)
#print("-="*30)
#print("LISTA DE MAIS PESADOS")
#print(pesado)
#print("-="*30)
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))      
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]   
        if temp[1] < men:
            men = temp[1]    
    princ.append(temp[:])
    temp.clear()
    resp = str(input("Quer continuar? [S/N]"))
    if resp in "Nn":
        break
print(f"Ao todo, você cadastrou {len(princ)} pessoas.")
print(f"O maior peso foi de {mai} Kg, pertencentes a:", end = " ")
for p in princ:
    if p[1] == mai:
        print(f"{p[0]} ---", end = " ")
print()
print(f"O menor peso foi {men} Kg, pertencentes a:", end = " ")
for p in princ:
    if p[1] == men:
        print(f"{p[0]} ---", end = " ")
