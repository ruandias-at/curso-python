print("-=" * 20)
print("Analisador de Aproveitamento do Atleta")
print("-=" * 20)
todos = list()
jogador = dict()
totalg = 0
partidas = list()
while True:
    jogador.clear()
    jogador["Nome"] = str(input("Digite o nome do jogador: ")).title()
    totalp = int(input(f"Quantas partidas {jogador['Nome']} jogou: "))
    jogador["Gols"] = list()
    partidas.clear()
    for c in range(totalp):
        gols = int(input(f"Quantos gols ele marcou na {c + 1}ª partida: "))
        jogador["Gols"].append(gols)
        totalg += gols    
    jogador["Total"] = totalg
    todos.append(jogador.copy())
    while True:
        resp = str(input("Deseja cadastrar outro jogador? [S/N]")).upper()[0]
        if resp in "SN":
            break
        print("ERRO! DIGITE APENAS S OU N!")
    if resp == "N":
        break
print("-=" * 20)    
print("Cód", end=" ")  
for i in jogador.keys():
    print(f"{i:<15}", end=" ")  
print( )
print("-=" * 20)
for k, v in enumerate(todos):
    print(f"{k:>4}", end=" ")
    for d in v.values():
        print(f"{str(d):<15}", end=" ")
    print( )    
print("-=" * 20)
while True:
    busca = int(input("Digite o código do jogador para mais informações: [999 para finalizar] "))
    if busca == 999:
        break
    if busca >= len(todos):
        print("ERRO! NÃO EXISTE JOGADOR COM ESSE CÓDIGO!")
    else:
        print(f"Levantamento do jogador {todos[busca]['Nome']}: ")
        for i, g in enumerate(todos[busca]["Gols"]):
            print(f"{i + 1}ª partida ---> {g} gols.")      
print("-=" * 20)
print("<<<PROGRAMA FINALIZADO>>>")
print("-=" * 20)