soma = maior = menor = opcao = cont = 0
while opcao != "N":
    n = int(input("Digite o {}º número:".format(cont + 1)))
    opcao = str(input("Quer digitar outro valor?[S/N]")).strip().upper()[0]
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
print("O maior valor informado foi {} e o menor foi {}".format(maior, menor))
print("A média dos {} valores informados foi {:.2f}.".format(cont, soma / cont))
