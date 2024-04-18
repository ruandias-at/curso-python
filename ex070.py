caros = barato = total = cont = nomebarato = 0
while True:
    produto = str(input("Digite o nome do produto:")).strip().capitalize()
    cont += 1
    preco = float(input("Digite o preço do produto:"))
    if preco >= 1000:
        caros += 1
    if cont == 1:
        nomebarato = produto
        barato = preco
    else:
        if barato > preco:
            nomebarato = produto
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Deseja adicionar outro produto? [S/N]:")).upper().strip()
    total += preco
    if resposta == "N":
        break
print(f"Total Gasto: R${total:.2f}")
print(f"Produtos acima de R$1000,00 : {caros} produto(s).")
print(f"O produto mais barato foi {nomebarato} custando R${barato:.2f}.")
