import random

a1 = str(input("Escreva o nome do primeiro aluno:"))
a2 = str(input("Escreva o nome do segundo:"))
a3 = str(input("Escreva o nome do terceiro:"))
a4 = str(input("Escreva o nome do quarto:"))
lista = [a1, a2, a3, a4]
e = random.choice(lista)

print("O aluno escolhido foi o {}!".format(e))