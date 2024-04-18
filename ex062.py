num = int(input("Digite o primeiro termo:"))
razao = int(input("Digite a razão:"))
termo = num
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print("{}".format(termo), end="->")
        termo += razao
        cont += 1
    mais = int(input("\nQuantos termos você ainda quer ver?"))
print("Progressão finalizado com {} termos utilizados.".format(total))
print("Fim")
