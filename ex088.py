from random import randint
from time import sleep
jogo = list()
todos = list()
print("-" * 40)
print("      GERADOR DE JOGOS MEGA-SENA")
print("-" * 40)
quant = int(input("Quantos jogos você quer que eu sorteie? "))
print("-=" * 5 , " GERANDO JOGOS...", "-=" * 5)
tot = 1
while tot <= quant:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
            cont += 1
        if cont >= 6:
            break   
    jogo.sort()    
    todos.append(jogo[:])
    jogo.clear()
    tot += 1
for i, l in enumerate(todos):
    sleep(1)
    print(f"Jogo {i + 1} ---> {l}")
print("-" * 40)
