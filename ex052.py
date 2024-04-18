tot = 0
n = int(input("Digite o número para saber se é um número primo:"))
for c in range(1, n + 1):
    if n % c == 0:
        print("\033[33m", end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(c), end=" ")
print("\n\033[m{} foi dividido {} vezes".format(n, tot))
if tot > 2:
    print("{} não é um número primo.".format(n))
else:
    print("{} é um número primo.".format(n))
