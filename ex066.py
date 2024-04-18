cont = soma = n = 0
while n != 999:
    n = int(input(f"Digite o {cont + 1}º valor [999 para parar]:"))
    if n == 999:
        break
    soma += n
    cont += 1
print(f"Você digitou {cont} valores e a soma deles foi {soma}.")
