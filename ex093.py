print("-=" * 20)
print("Analisador de Aproveitamento do Atleta")
print("-=" * 20)
jogador = dict()
totalg = 0
jogador["Nome"] = str(input("Digite o nome do jogador: "))
totalp = int(input(f"Quantas partidas {jogador['Nome']} jogou: "))
jogador["Gols por partida"] = list()
for c in range(totalp):
    gols = int(input(f"Quantos gols ele marcou na {c + 1}ª partida: "))
    jogador["Gols por partida"].append(gols)
    totalg += gols    
jogador["Total de Gols"] = totalg
print("-=" * 20)
print(jogador)
print("-=" * 20)
for k, v in jogador.items():
    print(f"{k} ---> {v}")
print("-=" * 20)        
print(f"O jogador {jogador['Nome']} jogou {totalp} partida(s).")
for i, v in enumerate(jogador["Gols por partida"]):
    print(f"Na {i + 1}ª partida marcou {v} gol(s).")
print(f"Foi um total de {totalg} gol(s).")
print("-=" * 20)
