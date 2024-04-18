def ficha(nome="<desconhecido>", gols="0"):
    return f"O jogador {nome} marcou {gols} gol(s) no campeonato."


# Programa Principal
n = str(input("Nome do jogador: "))
g = str(input("Número de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    print(ficha(gols=g))
else:
    print(ficha(n, g)) 
