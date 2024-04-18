from random import randint
print("-=" * 20)
print("\033[36m            ADVINHE O NÚMERO\033[m")
print("-=" * 20)
cont = 1
pc = randint(0, 10)
n = int(input("Tente advinhar o número que estou pensando de 0 a 10:"))
while n != pc:
    n = int(input("\033[31mVocê errou!\033[m Tente novamente:"))
    cont += 1
if n == pc:
    print("\033[32mParabéns você acertou!\033[m O número que eu estava pensando era \033[32m{}\033[m e você precisou de \033[33m{}\033[m tentativa(s).".format(pc, cont))
