from lib.interface import *
from lib.arquivo import *
from time import sleep

#Cria arquivo de texto para armazenar dados
arq = "cursoemvideotxt"
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    if resp == 1:
        #Opção para mostrar os cadastrados
        lerArquivo(arq)
    elif resp == 2:
        #Opção para cadastrar novas pessoas
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")  
        cadastrar(arq, nome, idade)
    elif resp == 3:
        #Opção para sair do sistema
        cabeçalho("SAINDO DO SISTEMA... ATÉ LOGO!")
        break
    else:
        #Digitou uma opção inexistente
        print("\033[31mERRO! DIGITE UMA OPÇÃO EXISTENTE!")
    sleep(1.5)    