print("=" * 26)
print("\033[4;32m AVALIADOR DE EMPRÉSTIMOS \033[m   ")
print("=" * 26)
casa = float(input("Qual o valor do imóvel desejado?"))
salario = float(input("Qual o seu salário atual?"))
anos = int(input("Em quantos anos você deseja pagar?"))
prestacao = casa / (anos * 12)

if prestacao > salario * 0.3:
    print("Infelizmente você não pode realizar esse empréstimo.")
else:
    print("Parabéns você pode realizar o empréstimo pagando prestações mensais de R${:.2f}.".format(prestacao))
