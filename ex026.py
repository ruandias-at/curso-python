frase = str(input("Escreva uma frase:")).lower().strip()
print("Sua frase tem {} letra(s) A.".format(frase.count("a")))
print("A letra A aparece pela primeira vez na posição {}.".format(frase.find("a") + 1))
print("A letra A aparece pela última vez na posição {}.".format(frase.rfind("a") + 1))

