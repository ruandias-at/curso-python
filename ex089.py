ficha = list()
while True:
    nome = str(input("Nome do aluno: "))
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media][:])
    resp = str(input("Você deseja continuar? [S/N] "))
    if resp in "Nn":
        break
print("-="*20)    
print(f"{"Nº":<4}{"Nome":<10}{"Média":>8}")
print("-="*20)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
print("-="*20)
while True:
    opc = int(input("Você quer ver a nota de qual aluno? [999 para finalizar]"))
    print("-="*20)
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f"Notas de {ficha[opc][0]}: Nota 1 --> {ficha[opc][1][0]} Nota 2 --> {ficha[opc][1][1]}")
        print("-="*20)
    else:
        print("\033[31mAluno não encontrado. Tente Novamente!\033[m")
        print("-="*20)
print("    PROGRAMA FINALIZADO!")
print("-="*20)
