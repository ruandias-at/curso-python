sal = float(input("Qual o salário atual?"))
dez = sal + sal * 0.1
qui = sal + sal * 0.15

if sal > 1250:
    print("O novo salário será de R${:.2f}.".format(dez))
else:
    print("O novo salário será de R${:.2f}.".format(qui))
