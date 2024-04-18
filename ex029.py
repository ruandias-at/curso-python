velocidade = int(input("Escreva sua velocidade em km/h:"))
multa = 7 * (velocidade - 80)
if velocidade > 80:
    print("Você foi multado! Deverá pagar uma multa no valor de R${:.2f}".format(multa))
else:
    print("Você não foi multado.")
