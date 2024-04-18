print("\033[34m-=\033[m" * 15)
print("    \033[35m CONVERSOR DE BASES \033[m ")
print("\033[34m-=\033[m" * 15)

num = int(input("Digite um número inteiro:"))
print("""Escolha uma das bases para conversão:
 [ 1 ] Converter para BINÁRIO
 [ 2 ] Converter para OCTAL
 [ 3 ] Converter para HEXADECIMAL """)
opcao = int(input("Digite o número de sua opção:"))

if opcao == 1:
    print("{} convertido para binário é {}.".format(num, bin(num)))
elif opcao == 2:
    print("{} convertido para octal é {}.".format(num, oct(num)))
else:
    print("{} convertido para hexadecimal é {}.".format(num, hex(num)))
print("-FIM-")