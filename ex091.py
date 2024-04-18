from time import sleep
from random import randint
from operator import itemgetter
resultados = {"Jogador 1": randint(1, 6),
              "Jogador 2": randint(1, 6),             
              "Jogador 3": randint(1, 6),  
              "Jogador 4": randint(1, 6)}
print("-=" * 20)
print("VALORES SORTEADOS")
print("-=" * 20)
for k, v in resultados.items():
    sleep(1)
    print(f"O {k} sortou {v}.")
print("-=" * 20)
rank = []
rank = sorted(resultados.items(), key=itemgetter(1), reverse=True)    
for i, v in enumerate(rank):
    sleep(1)
    print(f"{i + 1}º Lugar ===> {v}.")
print("-=" * 20)    
