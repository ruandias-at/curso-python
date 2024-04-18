from utilidadesCeV import moeda
from utilidadesCeV import dados

valor = dados.leiaDinheiro("Digite o preço: R$")
moeda.resumo(valor, 12 , 3)
