nomedovei = 0
velho = 0
bocetas = 0
mediaidade = 0
soma = 0
for p in range(1, 5):
    print("-----------------{}ª PESSOA-----------------".format(p))
    nome = str(input("Digite o nome da {}ª pessoa:".format(p))).strip()
    idade = int(input("Digite a idade da {}ª pessoa:".format(p)))
    sexo = int(input("""Gênero
[1] Masculino
[2] Feminino
Digite o número referente ao sexo da {}ª pessoa:""".format(p)))
    soma += idade
    if p == 1 and sexo == 1:
        velho = idade
        nomedovei = nome
    if idade > velho and sexo == 1:
        velho = idade
        nomedovei = nome
    if idade < 20 and sexo == 2:
        bocetas += 1

mediaidade = soma / 4
print("A média de idade do grupo é de {} anos.".format(mediaidade))
print("Tem o total de {} boceta(s) nova(s)".format(bocetas))
if velho != 0:
    print("O nome do mais velho é {}.".format(nomedovei))
