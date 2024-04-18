from time import sleep
c = ('\033[m',          # 0 - Sem cor
     '\033[0;30;41m',   # 1 - Vermelho
     '\033[0;30;42m',   # 2 - Verde
     '\033[0;30;43m',   # 3 - Amarelo
     '\033[0;30;44m',   # 4 - Azul
     '\033[0;30;45m',   # 5 - Roxo
     '\033[7;30m'       # 6 - Branco
    )


def ajuda(funcao):
    title(f'Acessando o manual do comando \'{funcao}\'', 4)
    print(c[6], end='')
    help(funcao)
    print(c[0], end='')
    sleep(2)


def title(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    title("SISTEMA DE AJUDA RUAN.PY", 2)
    comando = str(input("Função ou biblioteca >>> "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)    
title("FIM DO PROGRAMA!", 1)
