nome = str(input("Escreva seu nome completo:")).strip()
print("Seu nome em maiúsculo é {}.".format(nome.upper()))
print("Seu nome em minúsculo é {}.".format(nome.lower()))
print("Seu nome ao todo tem {} letras.".format(len(nome) - nome.count(" ")))

sep = nome.split()
print("Seu primeiro nome é {}.".format(sep[0]))
