"""primeiro = cont = int(input("Digite o primeiro termo:"))
razao = int(input("Digite a razão:"))
decimo = primeiro + (10 - 1) * razao
while cont <= decimo:
    print("{}".format(cont), end="")
    print("->" if cont != decimo else "", end="")
    cont += razao
"""
num = int(input("Digite o primeiro termo:"))
razao = int(input("Digite a razão da PA:"))
termo = num
cont = 1
while cont <= 10:
    print("{}".format(termo), end="->")
    termo += razao
    cont += 1
print("FIM")
