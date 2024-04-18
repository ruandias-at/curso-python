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


# Programa Principal
print("-" * 35)
n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}.")
print("-" * 35)