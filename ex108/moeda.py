def aumentar(n=0, p=0):
    aumento = n * (p * 0.01)
    finala = n + aumento
    return finala


def diminuir(n=0, p=0):
    desconto = n * (p * 0.01)
    finald = n - desconto
    return finald


def dobro(n=0):
    d = n * 2
    return d


def metade(n=0):         
    m = n / 2
    return m   


def moeda(n):
    formatado = str(f"R${n:.2f}".replace(".", ","))
    return formatado

