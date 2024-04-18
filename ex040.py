print("\033[36m-=\033[m" * 20)
print("\033[34m         ANALISADOR DE MÉDIAS \033[m")
print("\033[36m-=\033[m" * 20)

n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
media = (n1 + n2) / 2

if media < 5:
    print("Você foi \033[31mREPROVADO\033[m! Sua média foi de {:.1f}.".format(media))
elif 7 > media >= 5:
    print("Você está de \033[33mRECUPERAÇÃO\033[m! Sua média foi de {:.1f}.".format(media))
else:
    print("Você foi \033[32mAPROVADO\033[m! Sua média foi de {:.1f}.".format(media))
