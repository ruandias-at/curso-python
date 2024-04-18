from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
pc = randint(0,2)
print("\033[36m-=\033[m" * 13)
print("\033[31m         JOKENPÔ \033[m")
print("\033[36m-=\033[m" * 13)
opcao = int(input("""          OPÇÃO
 [ 0 ] Pedra
 [ 1 ] Papel
 [ 2 ] Tesoura
       Digite o dígito de sua opção:"""))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!")
print("-=" * 12)
print("Computador jogou {}.".format(itens[pc]))
print("Você jogou {}.".format(itens[opcao]))
print("-=" * 12)
if pc == 0:
    if opcao == 0:
        print("EMPATE!")
    elif opcao == 1:
        print("JOGADOR VENCE!")
    else:
        print("COMPUTADOR VENCE!")
elif pc == 1:
    if opcao == 0:
        print("COMPUTADOR VENCE!")
    elif opcao == 1:
        print("EMPATE!")
    else:
        print("JOGADOR VENCE!")
elif pc == 2:
    if opcao == 0:
        print("JOGADOR VENCE!")
    elif opcao == 1:
        print("COMPUTADOR VENCE!")
    else:
        print ("EMPATE")
