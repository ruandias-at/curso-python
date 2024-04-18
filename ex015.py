km = float(input("Quantos quilômetros foram percorridos com o carro alugado?"))
d = int(input("Quantos dias foi alugado?"))
p = (km * 0.15) + (d * 60)

print("Deverá ser pago R${:.2f} pelo aluguel do carro." .format(p))
