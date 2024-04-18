#lista = []
#par = []
#impar = []
#for c in range(0, 7):
#    valor = int(input("Digite um valor: "))
#    if valor % 2 == 0:
#        par.append(valor)
#    elif valor % 2 == 1:
#        impar.append(valor)
#par.sort()
#lista.append(par[:])
#par.clear()
#impar.sort()
#lista.append(impar[:])
#impar.clear()
#print("-="*15)
#print(f"""\033[34mLISTA DE PARES\033[m
#{lista[0]}
#\033[34mLISTA DE ÍMPARES\033[m
#{lista[1]}""")
#print("-="*15)
lista = [[], []]
for c in range(1, 8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print("-="*15)
print(f"Os valores pares digitados foram: {lista[0]}.")
print(f"Os valores ímpares digitados foram: {lista[1]}.")
