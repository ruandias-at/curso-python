def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f"\033[31mERRO! \"{entrada}\" NÃO É UM PREÇO VÁLIDO!\033[m")
        else:
            valido = True
            return float(entrada)
        

def leiaInt(msg):
    ok = False
    v = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            ok = True
            v = n
        else:
            print("\033[31mERRO!!! DIGITE UM NÚMERO VÁLIDO\033[m")    
        if ok:
            break
    return v

