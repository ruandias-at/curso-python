from random import randint
from time import sleep

def sorteia(lista):
    for c in range(0, 5):    
        n = randint(1, 10)
        print(f"{n}", end=' ', flush=True)
        sleep(0.3)
        lista.append(n)
    print(f"\nOs valores sorteados foram: {lista} e", end="")    
 
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f" o valor da soma dos números pares foi {soma}")            

nums = []
sorteia(nums)
somapar(nums)
