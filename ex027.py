nome = str(input("Escreva seu nome completo:")).strip().split()
print("Muito prazer em te conhecer")
print("O seu primeiro nome é {}.".format(nome[0].capitalize()))
print("E o seu último nome é {}.".format(nome[len(nome) - 1].capitalize()))
