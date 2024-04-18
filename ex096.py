def área(l, c):
    a = l * c
    print("--" * 20)
    print(f"A área do terreno de {l} m x {c} m é de {a} m²")
    print("--" * 20)


#Programa Principal
print("CONTROLE DE TERRENOS")
print("--" * 20)
l = float(input("Digite a largura do terreno em metros: "))
c = float(input("Digite o comprimento do terreno em metros: "))    
área(l, c)
