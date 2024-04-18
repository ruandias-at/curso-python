numeros = list()
print("Crie sua lista de números.")
print("-="*18)
while True:
    n = int(input("Digite um valor > "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso.")
    r = str(input("Você deseja continuar? [S/N] "))
    if r in "Nn":
        break
print("             LISTA FINAL")
print("-="*18)
numeros.sort()
print(numeros)
print("-="*18)
