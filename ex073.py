classificacao = ("Botafogo", "Grêmio", "Palmeiras", "Flamengo", "Red Bull", "Athletico", "Fluminense",
                 "Cuiabá", "São Paulo", "Atlético", "Fortaleza", "Cruzeiro", "Corinthians",
                 "Internacional", "Goiás", "Bahia", "Santos", "Vasco", "Coritiba", "América")
print("-=" * 20)
print("CLASSIFICAÇÃO ATUAL")
print("-=" * 20)
print(classificacao)
print("-=" * 20)
print(f"Os 5 primeiros são: {classificacao[0:5]}")
print("-=" * 20)
print(f"Os 4 últimos colocados são: {classificacao[-4:]}")
print("-=" * 20)
print("TIMES EM ORDEM ALFÁBETICA")
print("-=" * 20)
print(sorted(classificacao))
print("-=" * 20)
print(f"O Botafogo está na {classificacao.index("Botafogo")+1}ª posição.")
print("-=" * 20)
print("Fim do Programa")
