import moeda

valor = float(input("Digite o valor: "))
print(f"O dobro de {valor} é {moeda.dobro(valor)}.")
print(f"A metade de {valor} é {moeda.metade(valor)}.")
print(f"Adicionando 15% a mais em {valor} totaliza {moeda.aumentar(valor, 15)}.")
print(f"Excluindo 24% de {valor} resulta em {moeda.diminuir(valor, 24)}.")
