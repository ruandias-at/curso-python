def aumentar(n=0, p=0, form=False):
    aumento = n * (p * 0.01)
    finala = n + aumento
    if form:
        return moeda(finala)
    else:
        return finala

def diminuir(n=0, p=0, form=False):
    desconto = n * (p * 0.01)
    finald = n - desconto
    if form:
        return moeda(finald)
    else:
        return finald


def dobro(n=0, form=False):
    d = n * 2
    if form:
        return moeda(d)
    else:
        return d


def metade(n=0, form=False):         
    m = n / 2
    if form:
        return moeda(m)
    else:
        return m   


def moeda(n):
    return f"R${n:.2f}".replace(".", ",")

