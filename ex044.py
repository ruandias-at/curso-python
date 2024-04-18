preco = float(input("Digite o valor do produto:"))
opcao = int(input("""Qual será a forma de pagamento?
 [ 1 ] À vista no dinheiro/cheque\033[32m(10% de desconto)\033[m.
 [ 2 ] Á vista no cartão\033[32m(5% de desconto)\033[m.
 [ 3 ] 2 vezes no cartão\033[32m(Sem juros)\033[m.
 [ 4 ] 3 vezes ou mais no cartão\033[33m(20% de juros)\033[m.
       Digite o número da opção de pagamento:"""))
if opcao == 1:
    print("O produto vai custar R${:.2f}.".format(preco - preco * 0.1))
elif opcao ==2:
    print("O produto vai custar R${:.2f}.".format(preco - preco * 0.05))
elif opcao ==3:
    print("O produto vai continuar custando R${:.2f}.".format(preco))
else:
    print("O produto vai custar R${:.2f}.".format(preco + preco * 0.2))
