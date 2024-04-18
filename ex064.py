c = n = s = 0
while n != 999:
    n = int(input("Digite um valor, \033[33m[999] para encerrar\033[m:"))
    c += 1
    s += n
print("Você digitou {} valor(es) e a soma dele(s) foi {}.".format(c - 1, s - 999))
