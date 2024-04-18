geral = []
pessoa = {}
totalp = totali = 0
while True:
    pessoa.clear()
    pessoa["Nome"] = str(input("Digite o nome: ")).title()
    totalp += 1
    while True: 
        pessoa["Sexo"] = str(input("Digite o sexo: [M/F]")).upper()[0]
        if pessoa["Sexo"] in "MF":
            break
        print("ERRO! DIGITE APENAS M OU F!")
    pessoa["Idade"] = int(input("Digite a idade: "))
    totali += pessoa["Idade"]
    geral.append(pessoa.copy())
    while True:
        resp = str(input("Deseja cadastrar outra pessoa? [S/N]")).upper()[0]
        if resp in "SN":
            break
        print("ERRO! DIGITE APENAS S OU N!")
    if resp == "N":
        break
media = (totali / totalp)    
print("-=" * 20)   
print(f"Foram cadastradas {totalp} pessoas.")
print(f"A média de idade foi de {media} anos.")
print(f"A lista de mulheres cadastradas foi: ", end =" ")
for p in geral: 
    if p["Sexo"] in "Ff":
        print(f"{p['Nome']}", end=" ")
print( )        
print(f"Lista de pessoas acima da média de idade: ")
for p in geral:
    if p["Idade"] >= media:
        print("    ")
        for k, v in p.items():
            print(f"{k} ---> {v}", end=" ")
print( )        
print("-=" * 20)
