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


def resumo(n=0, pa=0, pd=0):
    print("-" * 35)
    print("RESUMO DO VALOR".center(35))
    print("-" * 35)
    print(f"PREÇO ANALISADO: \t{moeda(n)}")
    print(f"PREÇO DOBRADO: \t\t{dobro(n, True)}")
    print(f"METADE DO PREÇO: \t{metade(n, True)}")
    print(f"DESCONTO DE {pd}%: \t{diminuir(n, pd, True)}")
    print(f"AUMENTO DE {pa}%: \t{aumentar(n, pa, True)}")
    print("-" * 35)