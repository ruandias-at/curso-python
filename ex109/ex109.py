import moeda

valor = float(input("Digite o preço: R$"))
print(f"O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}.")
print(f"A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}.")
print(f"Adicionando 15% a mais em {moeda.moeda(valor)} totaliza {moeda.aumentar(valor, 15, True)}.")
print(f"Excluindo 24% de {moeda.moeda(valor)} resulta em {moeda.diminuir(valor, 24, True)}.")
