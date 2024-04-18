extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete",
           "oito", "nove", "dez", "onze", "doze", "treze", "quatorze",
           "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    n = int(input("Digite um valor de 0 à 20:"))
    if 0 <= n <= 20:
        break
    print("Tente novamente.", end=" ")
print(f"Você digitou o número \033[33m{extenso[n]}\033[m.")
