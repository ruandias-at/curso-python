peso = float(input("Informe seu peso em quilogramas:"))
alt = float(input("Informe sua altura em metros:"))
imc = peso / (alt ** 2)
if imc < 18.5:
    print("Abaixo do peso, com IMC de {:.2f}.".format(imc))
elif 25 > imc >= 18.5:
    print("Você está no peso ideal, com IMC de {:.2f}.".format(imc))
elif 30 > imc >= 25:
    print("Você está com SOBREPESO, com IMC de {:.2f}.".format(imc))
elif 40 > imc >= 30:
    print("Você está com OBESIDADE, com IMC de {:.2f}.".format(imc))
else:
    print("Você está com OBESIDADE MÓRBIDA, com IMC de {:.2f}.".format(imc))
