from random import randint
resultado = 0
print("-=" * 15)
print("Vamos jogar par ou ímpar!")
print("-=" * 15)
while True:
    opcao = str(input("PAR ou ÍMPAR[P/I]")).strip().upper()[0]
    jogador = int(input("Digite um valor:"))
    pc = randint(0, 10)
    if (jogador + pc) % 2 == 0 and opcao == "P":
        print(f"O computador jogou {pc} e você jogou {jogador}.")
        print("Você Venceu! Vamos jogar novamente!")
        resultado = "V"
    elif (jogador + pc) % 2 != 0 and opcao == "I":
        print(f"O computador jogou {pc} e você jogou {jogador}.")
        print("Você Venceu! Vamos jogar novamente!")
        resultado = "V"
    elif (jogador + pc) % 2 == 0 and opcao == "I":
        print(f"O computador jogou {pc} e você jogou {jogador}.")
        print("Você Perdeu!")
        resultado = "D"
    elif (jogador + pc) % 2 != 0 and opcao == "P":
        print(f"O computador jogou {pc} e você jogou {jogador}.")
        print("Você Perdeu!")
        resultado = "D"
    if resultado == "D":
        break
print("GAME OVER!")
