def fatorial(num=1, show=False):
    """
A função permite calcular o fatorial de um número qualquer e mostrar o processo por meio do parâmetro "show"
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(" x ", end='')
            else:
                print(" = ", end='')
        f *= c
    return f


# Programa Principal
print(fatorial(7, True))
