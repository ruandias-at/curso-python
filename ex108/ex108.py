import moeda

valor = float(input("Digite o valor: "))
print(f"O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}")
print(f"A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}")
print(f"Adicionando 15% a mais em {moeda.moeda(valor)} totaliza {moeda.moeda(moeda.aumentar(valor, 15))}")
print(f"Excluindo 24% de {moeda.moeda(valor)} resulta em {moeda.moeda(moeda.diminuir(valor, 24))}")
