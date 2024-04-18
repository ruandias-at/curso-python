import random
sorte = random.randint(0, 5)
num = int(input("Tente advinhar o número inteiro entre 0 e 5:"))

if num == sorte:
    print("Você acertou! O número sorteado era mesmo {}!".format(num))
else:
    print("Tente novamente! O número correto era {}!".format(sorte))
