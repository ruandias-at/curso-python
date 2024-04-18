opcao = 4
while opcao == 4:
    a = int(input("Digite um valor:"))
    b = int(input("Digite outro valor:"))
    opcao = int(input("""-----------------OPERAÇÕES-----------------
     [ 1 ] SOMAR
     [ 2 ] MULTIPLICAR
     [ 3 ] MAIOR
     [ 4 ] NOVOS NÚMEROS
     [ 5 ] SAIR DO PROGRAMA
     DIGITE O NÚMERO DA OPÇÃO:"""))
    if opcao == 5:
        print("FIM!")
    elif opcao == 1:
        print("A soma entre {} e {} resulta em {}.".format(a, b, a + b))
    elif opcao == 2:
        print("A multiplicação entre {} e {} resulta em {}.".format(a, b, a * b))
    elif opcao == 3:
        if a > b:
            print("{} é maior do que {}.".format(a, b))
        elif b > a:
            print("{} é maior do que {}.".format(b, a))
        else:
            print("Ambos tem o mesmo valor.")
    elif opcao != 4:
        print("---------------\033[31mCÓDIGO INVÁLIDO\033[m---------------")
