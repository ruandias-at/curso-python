lista = list()
par = list()
impar = list()
while True:
    n = int(input("Digite o valor a ser adicionado: "))
    lista.append(n)
    r = str(input("Você deseja adicionar outro valor? [S/N]"))
#    if n % 2 == 0:
#        par.append(n)
#    elif n % 2 != 0:
#        impar.append(n)    
    if r in "Nn":
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)        
#lista.sort()
#par.sort()
#impar.sort()
#print("Lista completa em ordem crescente:")
print("LISTA COMPLETA")
print(lista)
print("=-"*20)
#print("Lista de números pares:")
print("NÚMEROS PARES NA LISTA")
print(par)
print("=-"*20)
#print("Lista de números ímpares:")
print("NÚMEROS ÍMPARES NA LISTA")
print(impar)
print("=-"*20)
