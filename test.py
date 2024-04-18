def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


# Programa Principal
num = int(input("Digite um valor para saber se ele é par: "))
if par(num):
    print(f"{num} é par!")
else:
    print(f"{num} é ímpar!")
        