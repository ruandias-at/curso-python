d = int(input("Escreva a distância de sua viagem:"))
c = 0.5 * d
l = 0.45 * d

if d <= 200:
    print("O preço da sua passagem será de R${:.2f}, pois será cobrado R$0.50 por quilômetro.".format(c))
else:
    print("O preço da sua passagem será de R${:.2f}, pois será cobrado R$0.45 por quilômetro.".format(l))
