from time import sleep
from datetime import datetime
pessoa = dict()
print("-=" * 20)
print("Calculador de Aposentadoria")
print("-=" * 20)
pessoa["Nome"] = str(input("Digite seu nome: "))
anonasc = int(input("Digite seu ano de nascimento: "))
pessoa["Idade"] = datetime.now().year - anonasc
pessoa["Carteira de Trabalho"] = int(input("Digite sua Carteira de Trabalho: [Caso não tenha digite 0]"))
if pessoa["Carteira de Trabalho"] != 0:
    pessoa["Ano de Contratação"] = int(input("Digite o ano de contratação: "))
    pessoa["Salário"] = float(input("Digite o seu salário atual: "))
    pessoa["Aposentadoria"] = (pessoa["Ano de Contratação"] + 35) - anonasc
for k, v in pessoa.items():
    print(f"{k} ---> {v}.")
    sleep(1)
print("-=" * 20)
